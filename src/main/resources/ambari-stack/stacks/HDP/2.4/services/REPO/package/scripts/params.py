from resource_management.libraries.script.script import Script

config = Script.get_config()

external_repository_url = config['configurations']['repo-env']['external_repository_url']
external_repository_packages=config['configurations']['repo-env']['external_repository_packages']
configuration_template = [{'from': "index.html.j2", 'to': 'index.html'}]
httpd_configuration_template = [{'from': "httpd.conf.j2", 'to': 'httpd.conf'}]

#======================================================================================================================

