from resource_management import *
import os
import glob
import time


class Master(Script):
    def install(self, env):
        self.install_packages(env)
        # TODO Cleanup before fresh install
        self.configure(env)

    def start(self, env):
        print 'Start Ambari Extensions Provider Master'
        self.configure(env)

    def stop(self, env):
        print 'Stop Ambari Extensions Provider Master'

    def status(self, env):
        print 'Ambari Extensions Provider Master'

    def configure(self, env):
        print 'Configure Ambari Extensions Provider Master'

    def reinstall_ambari_extensions(self, env):
        import params
        env.set_params(params)

        app_package_bundle = params.config['configurations']['ambari-extensions-provider-env']['stack_package']
        File("/" + app_package_bundle, content=DownloadSource(format("{external_repository_url}/") + app_package_bundle,
                                                              redownload_files=True), mode=0644)

        Execute(format('tar -xvf /' + app_package_bundle + ' -C /'))

    def restart_ambari_server(self, env):
        #This operation would be marked timed out due to sync restart of ambari-server which is fine.Async restart has pid related issues.
        #TODO Fix async restart issues.
        Execute(format('ambari-server restart'))
        print("Scheduled to restart ambari-server")

    def backup_mysql(self,env):
        now = int(time.time()) * 1000
        backupfilename = str(now) + '.rms.mysql.backup.sql'
        print('Start------------------------------------------------')
        print("......performing back up of PostgreSQL database for Ambari ")
        try:
            Execute("mysqldump --add-drop-database --add-drop-table --complete-insert --create-options --debug-check --dump-date --events --extended-insert --flush-privileges --lock-all-tables --databases rms > "+backupfilename,user='mysql', logoutput=True)
            print("......finished backing up RMS Mysql database ")
            print("......moving backup file to repo")
            Execute("cp /home/mysql/" + backupfilename + " /var/www/html/repo/" + backupfilename, logoutput=True)
        except Exception as e:
            print(str(e))

    def backup_postgresql(self,env):
        now = int(time.time()) * 1000
        backupfilename = str(now) + '.ambari.postgresql.backup'
        print('Start------------------------------------------------')
        print("......performing back up of PostgreSQL database for Ambari ")
        Execute("pg_dump ambari > " + backupfilename, user='postgres', logoutput=True)
        print("......finished backing up Ambari PostgreSQL database ")
        print("......moving backup file to repo")
        Execute("cp /var/lib/pgsql/" + backupfilename + " /var/www/html/repo/" + backupfilename, logoutput=True)

if __name__ == "__main__":
    Master().execute()
