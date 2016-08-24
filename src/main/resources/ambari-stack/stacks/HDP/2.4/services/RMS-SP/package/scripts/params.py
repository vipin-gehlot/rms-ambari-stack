from resource_management.libraries.script.script import Script

config = Script.get_config()

java_home = config['hostLevelParams']['java_home']

app_repository_url = config['configurations']['rms-sp-env']['app_repository_url']
app_configuration_templates = [{'from': "rms-sp.conf.j2", 'to': 'rms-sp.conf'}]
