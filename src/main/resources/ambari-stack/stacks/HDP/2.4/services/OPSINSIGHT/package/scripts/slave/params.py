from resource_management import *
from resource_management.libraries.script.script import Script

config = Script.get_config()

java_home = config['hostLevelParams']['java_home']

zookeeper_hosts = ",".join(config['clusterHostInfo']['zookeeper_hosts'])

hostname = None
if config.has_key('hostname'):
    hostname = config['hostname']

filebeat_app_config = config['configurations']['filebeat-env']

filebeat_app_name = filebeat_app_config["app_name"]
filebeat_app_user = filebeat_app_config["app_user"]
filebeat_app_group = filebeat_app_config["app_group"]

filebeat_app_repository_url = filebeat_app_config['app_repository_url']
filebeat_app_package = filebeat_app_config["app_package"]
filebeat_app_package_bundle_extension = filebeat_app_config["app_package_bundle_extension"]
filebeat_app_package_bundle = filebeat_app_package + filebeat_app_package_bundle_extension

#======================================================================================================================
