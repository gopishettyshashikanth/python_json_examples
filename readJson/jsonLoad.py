import json
items = []
with open('state.json') as json_data:
	json_data = json.load(json_data)
	for data in json_data['states']:
		datas =  data['id']
		datas =  data['name']
		datas = data['country_id']
		print datas