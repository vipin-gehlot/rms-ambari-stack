################################
# Elasticsearch
################################

# Elasticsearch home directory
#ES_HOME=/usr/share/elasticsearch

# Elasticsearch Java path
JAVA_HOME={{java_home}}

# Elasticsearch configuration directory
#CONF_DIR=/etc/elasticsearch

# Elasticsearch data directory
#DATA_DIR=/var/lib/elasticsearch

# Elasticsearch logs directory
#LOG_DIR=/var/log/elasticsearch

# Elasticsearch PID directory
#PID_DIR=/var/run/elasticsearch

# Additional Java OPTS
ES_JAVA_OPTS="{{java_opts}}"

# Configure restart on package upgrade (true, every other setting will lead to not restarting)
#ES_RESTART_ON_UPGRADE=true

################################
# Elasticsearch service
################################

# SysV init.d
#
# When executing the init script, this user will be used to run the elasticsearch service.
# The default value is 'elasticsearch' and is declared in the init.d file.
# Note that this setting is only used by the init script. If changed, make sure that
# the configured user can read and write into the data, work, plugins and log directories.
# For systemd service, the user is usually configured in file /usr/lib/systemd/system/elasticsearch.service
ES_USER=elasticsearch
ES_GROUP=elasticsearch

# The number of seconds to wait before checking if Elasticsearch started successfully as a daemon process
ES_STARTUP_SLEEP_TIME=5

################################
# System properties
################################

# Specifies the maximum file descriptor number that can be opened by this process
# When using Systemd, this setting is ignored and the LimitNOFILE defined in
# /usr/lib/systemd/system/elasticsearch.service takes precedence
#MAX_OPEN_FILES=65536

# The maximum number of bytes of memory that may be locked into RAM
# Set to "unlimited" if you use the 'bootstrap.memory_lock: true' option
# in elasticsearch.yml.
# When using Systemd, the LimitMEMLOCK property must be set
# in /usr/lib/systemd/system/elasticsearch.service
#MAX_LOCKED_MEMORY=unlimited

# Maximum number of VMA (Virtual Memory Areas) a process can own
# When using Systemd, this setting is ignored and the 'vm.max_map_count'
# property is set at boot time in /usr/lib/sysctl.d/elasticsearch.conf
#MAX_MAP_COUNT=262144
