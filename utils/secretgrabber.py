import json

def getSecret():
	with open('config.json') as secret_json_data_file:
		data = json.load(secret_json_data_file)
		secret = data['secret']
		return secret
