import json
import sys

if len(sys.argv)==1: # if no file given, read from stdin
    data = sys.stdin.read()
else:
    f = open(sys.argv[1], "r")
    data = f.read()
    f.close()

data=json.loads(data)

headers=data['headers']

rows=[[] for i in range(len(data['data']))]

for i in range(len(data['data'])):
    for j in range(len(headers)):
        rows[i].append(data['data'][i][headers[j]])

        
op=','.join(headers)
op=op+'\n'
for row in rows:
    op=op+','.join(row)
    op=op+'\n'

size = len(op)
op = op[:size - 1]
print(op)