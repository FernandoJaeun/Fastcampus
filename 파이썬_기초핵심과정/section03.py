import simplejson as json


test_dict = {'1': 95, '2': 100}

print(json.dumps(test_dict, sort_keys = True, indent = 2 *' '))