# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

# If this file is changed in development, the development server will
# have to be manually restarted because changes will not be noticed
# immediately.

DEBUG = False

# Make these unique, and don't share it with anybody.
SECRET_KEY = "6@!6yreauz&k4)(4(((jq@17w@_mcr9bzu49%7%=vuze_!3f8!"
NEVERCACHE_KEY = "-&outap0_#5%035lkznw1rd5okape@jnup2!b*ezpu$g%v(#dv"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

###################
# DEPLOY SETTINGS #
###################

# Domains for public site
#ALLOWED_HOSTS = ["dev.westgate-estate.co.uk"] ##DEV##
ALLOWED_HOSTS = ["www.westgate-estate.co.uk", "westgate-estate.co.uk"] ##LIVE##
# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

FABRIC = {
    "DEPLOY_TOOL": "git",  # Deploy with "git", "hg", or "rsync"
    #"SSH_USER": "root",  # VPS SSH username ##DEV##
    #"SSH_PASS":  '1d&JiL4v|v1qGh6:r^?0ZNaqMqom\E[,9PIILzgvc~V(4*PVj"T@h^B6~=K~v1A', # SSH password (consider key-based  authentication) ##DEV##
    "SSH_USER": "waff",  # VPS SSH username ##LIVE##
    "SSH_PASS":  'n7F@btdun$xV9%YCXD%K', # SSH password (consider key-based authentication) ##LIVE##
    #"VIRTUALENV_HOME":  "/home/root/do", # Absolute remote path for virtualenvs ##DEV##
    "VIRTUALENV_HOME":  "/home/waff/do", # Absolute remote path for virtualenvs ##LIVE##
    #"PROJECT_NAME": "westgate_estates", # Unique identifier for project ##DEV##
    "PROJECT_NAME": "live_westgate_estates", # Unique identifier for project ##LIVE##
    #"GUNICORN_PORT": 8000, # Port gunicorn will listen on ##DEV##
    "GUNICORN_PORT": 8010, # Port gunicorn will listen on ##LIVE##
    "REPO_URL": "https://jason5001001@bitbucket.org/jason5001001/westgate-estates.git", # Git or Mercurial remote repo URL for the project
    "HOSTS": ["139.162.200.178"],  # The IP address of your VPS
    "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
    "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
    "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
    "DB_PASS": "westgate@123",  # Live database password
    "ADMIN_PASS": "westgate@123",  # Live admin user password
    "SECRET_KEY": SECRET_KEY,
    "NEVERCACHE_KEY": NEVERCACHE_KEY,
}
