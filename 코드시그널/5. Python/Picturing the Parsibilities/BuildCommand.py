import json
from collections import OrderedDict

def buildCommand(jsonFile):
    return json.dumps(clean(json.loads(jsonFile, object_pairs_hook=OrderedDict)))

def clean(x):
    print('...',x)
    print()
    if type(x) is int or type(x) is float:
        return 0
    elif type(x) is str :
        return ""
    elif type(x) is list:
        return []
    elif type(x) is OrderedDict:
        print('this order dict')
        res = OrderedDict()
        for i, j in x.items():
            #처음 x가 들어오면, {}기준으로 짤라서 res가되어 clean함수로 재귀된다.
            res[i] = clean(j)
        return res

jsonFile= "{\"version\": \"0.1.0\",\"command\": \"c:python\",\"args\": [\"app.py\"],\"problemMatcher\": {\"fileLocation\": [\"relative\", \"${workspaceRoot}\"],\"pattern\": {\"regexp\": \"^(.*)+s$\", \"message\": 1}}}"

print(buildCommand(jsonFile))
#여기서는 dump의 개념과, loads()의 개념을 잡을 수 있다. 