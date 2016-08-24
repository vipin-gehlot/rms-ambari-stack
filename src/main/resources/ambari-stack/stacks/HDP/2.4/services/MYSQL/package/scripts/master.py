import sys
from resource_management import *
from resource_management.libraries.script.script import Script


class Master(Script):
    def install(self, env):
        self.install_packages(env)
        config = Script.get_config()
        self.configure(env)

    def configure(self, env):
        config = Script.get_config()
        File('/etc/my.cnf', content=InlineTemplate(
            format(config['configurations']['my.cnf']['my.cnf_content'])), mode=0644)

        File('/home/mysql_user_creation.sql', content=InlineTemplate(
            format(config['configurations']['mysql-env']['mysql_user_creation'])), mode=0644)

        File('/home/mysql_db_creation.sql', content=InlineTemplate(
            format(config['configurations']['mysql-env']['mysql_db_creation'])), mode=0644)

    def start(self, env):
        self.configure(env)
        Execute('service mysql start')
        self.createUser()
        self.createDB()

    def stop(self, env):
        Execute('service mysql stop')

    def status(self, env):
        Execute('service mysql status')

    def createUser(self):
        try:
            Execute('mysql -u root < /home/mysql_user_creation.sql')
        except Exception as e:
            print("User already exists :"+str(e))

    def createDB(self):
        try:
            Execute('mysql -u drs --password=drs < /home/mysql_db_creation.sql')
        except Exception as e:
            print(str(e))

if __name__ == "__main__":
    Master().execute()
