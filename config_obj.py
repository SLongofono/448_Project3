## @file config_obj.py
# @brief Defines a simple container for user and authentication details, as populated from a configuration file
#
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('.rektconfig.txt')
user = {'username':config.get('user', 'username'),
	'client_id':config.get('user', 'client_id'),
	'client_secret':config.get('user', 'client_secret'),
	'redirect_uri':config.get('user', 'redirect_uri')
	}

def get_user():
	return user

def get_db():
	return config.get('database', 'filename')
