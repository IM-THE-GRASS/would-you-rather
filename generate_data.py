
import random
import json
dict = {}
f = open("choices.json")
filedata = f.read()
f.close()
filedata = json.loads(filedata)
for choices in filedata:
    index = filedata.index(choices)
    dict[str(index)] = {
        "option1":random.randrange(0,5),
        "option2":random.randrange(0,5)
    }
f = open("stats.json", "w")
f.write(json.dumps(dict, indent=4))
#print(filedata)
