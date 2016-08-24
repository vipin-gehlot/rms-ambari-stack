import sys
from resource_management import *


class Master(Script):
    def install(self, env):
        self.install_packages(env)
        print 'WARNING: DRS does not support HTTPD post INSTALL configuration yet! Please do it manually.'
        self.configure(env)

    def configure(self, env):
        import params
        env.set_params(params)
        Logger.info("Allowing Jenkins/All user to write permission on /var/www/html/repo ")
        Directory('/var/www/html/repo', mode=0777)

        for t in params.configuration_template:
            File(format('/var/www/html/{t.to}'), content=Template(format("{t.from}")),
                 mode=0644, owner='root', group='root')

        for t in params.httpd_configuration_template:
            File(format('/etc/httpd/conf/{t.to}'), content=Template(format("{t.from}")),
                 mode=0644, owner='root', group='root')

    def start(self, env):
        self.configure(env)
        Execute('service httpd start')

    def stop(self, env):
        Execute('service httpd stop')

    def status(self, env):
        Execute('service httpd status')

    def get_artifacts_from_external_repository(self, env):
        import params
        env.set_params(params)

        app_packages_list=format("{external_repository_packages}").split(",")
        for app_package_bundle in app_packages_list:
            File("/var/www/html/repo/"+app_package_bundle,
                 content=DownloadSource(format("{external_repository_url}/")+app_package_bundle,
                                        redownload_files=True),mode=0644)

if __name__ == "__main__":
    Master().execute()
