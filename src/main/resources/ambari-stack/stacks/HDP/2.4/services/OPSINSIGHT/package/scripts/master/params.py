from resource_management import *
from resource_management.libraries.script.script import Script

config = Script.get_config()

java_home = config['hostLevelParams']['java_home']

zookeeper_hosts = ",".join(config['clusterHostInfo']['zookeeper_hosts'])

hostname = None
if config.has_key('hostname'):
    hostname = config['hostname']

elasticsearch_app_configuration_templates = [{'from': "elasticsearch.j2", 'to': 'elasticsearch'}]

elasticsearch_app_config = config['configurations']['elasticsearch-env']

elasticsearch_app_name = elasticsearch_app_config["app_name"]
elasticsearch_app_user = elasticsearch_app_config["app_user"]
elasticsearch_app_group = elasticsearch_app_config["app_group"]

elasticsearch_app_repository_url = elasticsearch_app_config['app_repository_url']
elasticsearch_app_package = elasticsearch_app_config["app_package"]
elasticsearch_app_package_bundle_extension = elasticsearch_app_config["app_package_bundle_extension"]
elasticsearch_app_package_bundle = elasticsearch_app_package + elasticsearch_app_package_bundle_extension
elasticsearch_app_plugins = elasticsearch_app_config['app_plugins']

java_opts = elasticsearch_app_config['java_opts']

kibana_app_config = config['configurations']['kibana-env']

kibana_app_name = kibana_app_config["app_name"]
kibana_app_user = kibana_app_config["app_user"]
kibana_app_group = kibana_app_config["app_group"]

kibana_app_repository_url = kibana_app_config['app_repository_url']
kibana_app_package = kibana_app_config["app_package"]
kibana_app_package_bundle_extension = kibana_app_config["app_package_bundle_extension"]
kibana_app_package_bundle = kibana_app_package + kibana_app_package_bundle_extension
kibana_app_plugins = kibana_app_config['app_plugins']


#======================================================================================================================

