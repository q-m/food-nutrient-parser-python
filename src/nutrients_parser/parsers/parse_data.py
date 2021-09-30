import json
from jsonpath_ng import jsonpath, parse

def parse_data(data):
    data = json.loads(data)
    # TODO