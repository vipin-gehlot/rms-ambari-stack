from resource_management import *
from resource_management.libraries.script.script import Script

# server configurations
config = Script.get_config()

print("************************** Status Param ****************************************")
print(config["configurations"]["rms-api-env"]["app_package"])
print("************************************************************************************")


app_name = config["configurations"]["rms-api-env"]["app_name"]
app_user = config["configurations"]["rms-api-env"]["app_user"]
app_group = config["configurations"]["rms-api-env"]["app_group"]

app_package = config["configurations"]["repo-env"]["app_package"]
app_package_bundle_extension = config["configurations"]["rms-api-env"]["app_package_bundle_extension"]
app_package_bundle = app_package + app_package_bundle_extension
