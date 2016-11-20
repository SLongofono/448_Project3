import os

def prompt_and_verify(prompt):
	while True:
		value = raw_input(prompt)
		response = raw_input("You entered: " + str(value) + "\nIs this correct? (y/n): ")
		if (response == 'y'):
			break
	return value
def go():
	print "\n[ Setting up configuration file... ]\n"
	username      = prompt_and_verify("\nEnter your Spotify username: ")
	client_id     = prompt_and_verify("\nEnter your spotify client ID: ")
	client_secret = prompt_and_verify("\nEnter your Spotify client secret: ")
	redirect_uri  = prompt_and_verify("\nEnter your redirect uri (if you are unsure, use 'http://localhost:8888/callback/'): ")

	print("\nWriting configuration as such:\n\tUsername:\t%s\n\tClient ID:\t%s\n\tClient secret:\t%s\n\tRedirect URI:\t%s\n") % (username, client_id, client_secret, redirect_uri)
	output = open('.rektconfig.txt', 'w')
	output.write('[user]\n')
	output.write('username = ' + username + '\n')
	output.write('client_id = ' + client_id + '\n')
	output.write('client_secret = ' + client_secret + '\n')
	output.write('redirect_uri = ' + redirect_uri + '\n')
	output.close()

go()
print "\n[ SUCCESS ]\n"
