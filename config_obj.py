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