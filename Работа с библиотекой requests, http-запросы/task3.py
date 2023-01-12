import requests
from pprint import pprint

resp_stack = requests.get('https://api.stackexchange.com/2.3/questions?fromdate=1673308800&todate=1673395200&order=desc&sort=activity&site=stackoverflow')
data_stack = resp_stack.json()['items']

for list_stack in data_stack:
    for python_tags in list_stack['tags']:
        if python_tags == 'python':
            pprint(list_stack)
