from resource_management import *
from master import *

class Slave(Master):
    def configure(self, env, action=None):
        import params
        env.set_params(params)
        File(format('/etc/ntp.conf'), content=InlineTemplate(format(format("{ntp_slave_conf_template}"))))

        for t in params.app_configuration_templates:
            File(format('/etc/{t.to}'), content=Template(format("{t.from}")),
                 mode=0644)


if __name__ == "__main__":
    Slave().execute()
