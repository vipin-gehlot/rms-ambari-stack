import sys
from resource_management import *
from resource_management.core.exceptions import ComponentIsNotRunning
from resource_management.libraries.resources.properties_file import PropertiesFile
import glob

class Master(Script):
    def install(self, env):
        # RMS-API installation is @TODO self.install_packages(env)
        print 'RMS-API installation started'
        self.configure(env)

    def start(self, env):
        self.configure(env)
        self.do_app_service_operation(env, 'start')
        self.status(env)

    def stop(self, env):
        self.do_app_service_operation(env, 'stop')

    def restart(self, env):
        self.configure(env)
        self.do_app_service_operation(env, 'restart')

    def status(self, env):
		if self.do_app_service_operation(env, 'status') != 0:
			raise ComponentIsNotRunning()

    def configure(self, env):
        import params, status_params
        env.set_params(params)
	env.set_params(status_params)
		
        File(format("/home/{app_user}/{app_package_bundle}"),
             content=DownloadSource(format(format("{app_repository_url}/{app_package_bundle}")),
                                    redownload_files=("SNAPSHOT" in format("{app_package_bundle}"))),
             mode=0644, owner=format('{app_user}'))

        Execute(format('tar -xvf /home/{app_user}/{app_package_bundle}'), user=format('{app_user}'))

        Execute(format('ln -sfv /home/{app_user}/{app_name}/{app_name}.jar /etc/init.d/{app_name}'))

        for t in params.app_configuration_templates:
            File(format('/home/{app_user}/{app_name}/{t.to}'), content=Template(format("{t.from}")),
                 mode=0644, owner=format('{app_user}'), group=format('{app_group}'))

        properties={}
        for k,v in params.config['configurations'][format('{app_name}')].items():
            properties[k]=format(v)

        PropertiesFile(format('application.properties'),
                       dir=format('/home/{app_user}/{app_name}/'),
                       properties=properties,
                       owner=format('{app_user}'), group=format('{app_group}')
                       )
			
    def do_app_service_operation(self, env, service_operation):
        import status_params
	env.set_params(status_params)

        Directory([format('/var/run/{app_name}'), format('/var/log/{app_name}')],
                  owner=format('{app_user}'), group=format('{app_group}'), recursive=True)

        File(format('/var/log/{app_name}/{app_name}.log'), mode=0644, owner=format('{app_user}'),
             group=format('{app_group}'), content='')

        Execute(format('chmod +x /home/{app_user}/{app_name}/{app_name}.jar'), user=format('{app_user}'))

        cmd = format('/etc/init.d/{app_name} {service_operation}')
        code, output = shell.call(cmd, user=format('{app_user}'), timeout=20)
        return code
			
if __name__ == "__main__":
    Master().execute()
