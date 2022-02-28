import json
a = open("/home/rishabharidas/Desktop/train/day_2/test.txt","r")
contacts = json.loads(a.read())

print(contacts)