from resource_management import *
from resource_management.core import shell
import httplib
import time
import json
import re
import os


class Master(Script):
    def install(self, env):
        self.install_packages(env)
        self.configure(env)

    def configure(self, env, action=None):
        import params
        env.set_params(params)
        File(format('/etc/ntp.conf'), content=InlineTemplate(format("{ntp_master_conf_template}")))

        for t in params.app_configuration_templates:
            File(format('/etc/{t.to}'), content=Template(format("{t.from}")),
                 mode=0644)

    def stop(self, env):
        Execute('service ntpd stop', logoutput=True)

    def start(self, env):
        import params
        env.set_params(params)
        self.configure(env)
        Execute('service ntpd restart', logoutput=True)
        Execute('ntpq -nc peers', logoutput=True)

    def status(self, env):
        metric_collector_properties_file = '/etc/ntpd_metrics.properties'
        return_code, output = shell.call('ntpstat')
        match_output = re.search(" time correct to within (\d+.?\d*) ms\n", output)
        if match_output:
            if os.path.isfile(metric_collector_properties_file):
                try:
                    prop = dict(line.strip().split('=') for line in open(metric_collector_properties_file))
                    collector_host = prop.get('METRIC_COLLECTOR_HOST')
                    collector_port = prop.get('METRIC_COLLECTOR_PORT')
                    hostname = prop.get('HOSTNAME')

                    metricValue = match_output.group(1)
                    AMS_METRICS_POST_URL = "/ws/v1/timeline/metrics/"
                    headers = {"Content-type": "application/json"}
                    current_time = int(time.time()) * 1000

                    metric_json = {
                        "metrics": [
                            {
                                "metricname": "ntpd.clock.skew",
                                "appid": "ntpd",
                                "hostname": hostname,
                                "timestamp": current_time,
                                "starttime": current_time,
                                "metrics": {
                                    str(current_time): metricValue
                                }
                            }
                        ]
                    }
                    try:
                        print("Connecting (POST) to %s:%s%s" % (collector_host,
                                                                collector_port,
                                                                AMS_METRICS_POST_URL))
                        conn = httplib.HTTPConnection(collector_host, int(collector_port))
                        conn.request("POST", AMS_METRICS_POST_URL, json.dumps(metric_json), headers)
                        response = conn.getresponse()
                        print("Http response: %s %s" % (response.status, response.reason))
                        conn.close()
                    except Exception as e:
                        print("Connection failed. " + str(e))

                except IOError as e:
                    print("Cannot read metric collector properties " + str(e))

            else:
                print(metric_collector_properties_file + " not found")

        else:
            print("Metric not available")

        Execute("ntpstat")

    def check_clock_skew(self, env):
        import params
        env.set_params(params)
        Execute('ntpq -nc peers', logoutput=True)
        Execute('ntpstat', logoutput=True)


if __name__ == "__main__":
    Master().execute()
