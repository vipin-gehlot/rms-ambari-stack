from resource_management import *


class JenkinsMaster(Script):
    def install(self, env):
        self.install_packages(env)
        self.configure(env)

    def configure(self, env):
        import params
        env.set_params(params)

        # Jenkins don't use JAVA_HOME , so need explicit link
        Directory('/usr/lib/jvm/', action='create', mode=0755, recursive=False)
        Execute(format('ln -sf {java_home} /usr/lib/jvm/jre-1.8.0'))
        File('/etc/sysconfig/jenkins', content=InlineTemplate(
            format(params.config['configurations']['jenkins']['etc.sysconfig.jenkins'])), mode=0644)

    def start(self, env):
        self.configure(env)
        Execute('service jenkins start')

    def stop(self, env):
        Execute('service jenkins stop')

    def status(self, env):
        Execute('service jenkins status')


if __name__ == "__main__":
    JenkinsMaster().execute()
