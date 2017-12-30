import json
items = []
with open('state.json') as json_data:
	json_data = json.load(json_data)
	for data in json_data['states']:
		del data['country_id']
	
with open('new_states.json','w') as f:
	new_string = json.dump(json_data, f,indent=2)
	