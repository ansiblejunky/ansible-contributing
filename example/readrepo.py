import ConfigParser, os

repo = "CentOS-Vault.repo"
config = ConfigParser.ConfigParser()
config.read(['/etc/yum.repos.d/' + repo])
print "Loaded repo file ... " + repo
print config.sections()
