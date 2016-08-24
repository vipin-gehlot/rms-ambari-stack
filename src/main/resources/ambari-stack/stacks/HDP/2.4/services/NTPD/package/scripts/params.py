from resource_management import *
from resource_management.libraries.script.script import Script
from resource_management.libraries.functions.default import default

# config object that holds the configurations declared in the config xml file
config = Script.get_config()

ntp_master_conf_template = config['configurations']['ntpd-leader-config']['ntp.conf']
ntp_slave_conf_template = config['configurations']['ntpd-follower-config']['ntp.conf']
app_configuration_templates = [{'from': "ntpd_metrics.properties.j2", 'to': 'ntpd_metrics.properties'}]

hostname = None
if config.has_key('hostname'):
    hostname = config['hostname']

metric_collector_host = ""
metric_collector_port = ""

ams_collector_hosts = default("/clusterHostInfo/metrics_collector_hosts", [])
has_metric_collector = not len(ams_collector_hosts) == 0

if has_metric_collector:
    if 'cluster-env' in config['configurations'] and \
                    'metrics_collector_vip_host' in config['configurations']['cluster-env']:
        metric_collector_host = config['configurations']['cluster-env']['metrics_collector_vip_host']
    else:
        metric_collector_host = ams_collector_hosts[0]
    if 'cluster-env' in config['configurations'] and \
                    'metrics_collector_vip_port' in config['configurations']['cluster-env']:
        metric_collector_port = config['configurations']['cluster-env']['metrics_collector_vip_port']
    else:
        metric_collector_web_address = default("/configurations/ams-site/timeline.metrics.service.webapp.address", "0.0.0.0:6188")
        if metric_collector_web_address.find(':') != -1:
            metric_collector_port = metric_collector_web_address.split(':')[1]
        else:
            metric_collector_port = '6188'
    pass
