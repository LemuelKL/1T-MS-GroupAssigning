import json
from pprint import pprint

with open('data/studentChoies.json', 'r') as dataIn:
    studentChoices = json.load(dataIn)

pprint(studentChoices)

jsonString = '[ {"pyccode":"001", "choie1": "society", "choie2": "finanace"}, {"pyccode": "002", "choie1": "math", "choie2": "it"}, {"pyccode":"003", "choie1": "phy", "choie2": "engine"} ]'

def parseObjs2Str(objs):
    return pp.pformat(objs)
    

parsed = json.loads(jsonString)
with open('data/studentChoiesTest.json', 'w') as outfile:
    json.dump(parsed, outfile, indent = 4, sort_keys = False)
