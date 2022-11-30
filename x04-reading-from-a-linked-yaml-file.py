import yaml
import requests

d = requests.get('https://raw.githubusercontent.com/mycourseresource/datastore/master/bank-holidays-ie.yaml')

# uncomment below line to see the content of the file that we downloaded with get()
#print(d.content)

parsed_yaml=yaml.safe_load(d.content)
# uncomment below line to see the parsed file content as a Python dictionary
#print(parsed_yaml)

# below line will print the Irish bank holiday's for 2023
print(parsed_yaml['BH']['dates']['2023'])