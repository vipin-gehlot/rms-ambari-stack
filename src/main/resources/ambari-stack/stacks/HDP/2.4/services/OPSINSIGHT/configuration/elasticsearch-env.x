<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<configuration>
    <property>
        <name>app_user</name>
        <value>elasticsearch</value>
        <property-type>USER</property-type>
        <description>Operating Systems user name to run this service as</description>
    </property>
    <property>
        <name>app_group</name>
        <value>elasticsearch</value>
        <property-type>GROUP</property-type>
        <description>Operating Systems userGroup name to run this service as</description>
    </property>
    <property>
        <name>app_name</name>
        <value>elasticsearch</value>
        <description>Application Name</description>
    </property>
    <property>
        <name>app_repository_url</name>
        <value>http://{config.clusterHostInfo.ambari_server_host[0]}:{config.configurations.repo-env.repository_port}/repo/</value>
        <description>Application Repository URL</description>
    </property>
    <property>
        <name>app_package</name>
        <value>elasticsearch-5.0.0-alpha5</value>
        <description>Application Packaged Directory Name</description>
    </property>
    <property>
        <name>app_package_bundle_extension</name>
        <value>.rpm</value>
        <description>Application Packaged bundle e.g. '.tar.gz'</description>
    </property>
    <property>
        <name>app_plugins</name>
        <value>x-pack-5.0.0-alpha5.zip</value>
        <description>Comma separated Application Plugins names</description>
    </property>
    <property>
        <name>java_opts</name>
        <value>-Xms2g -Xmx2g</value>
        <description>Java Opts</description>
    </property>
</configuration>
