import untangle
import sys

if len(sys.argv)==1: # if no file given, read from stdin
    data = sys.stdin.read()
else:
    f = open(sys.argv[1], "r")
    data = f.read()
    f.close()

xml=untangle.parse(data)

for header in xml.file.headers:
    headers=header.cdata.split(',')
    
headers=[i.replace('_',' ') for i in headers] #to restore the _ back to spaces in headers
    
len_records=len(xml.file.data.record)

data=[[] for i in range(len_records)] #list of lists to store the records

for i in range(len_records):
    for j in range(0,len(headers)):
        data[i].append(xml.file.data.record[i].children[j].cdata)
        
#loop i runs throuh number of records, loop j runs through every value in a record
op=','.join(headers)
op=op+'\n'
for row in data:
    op=op+','.join(row)
    op=op+'\n'
    
size = len(op)
op = op[:size - 1]
print(op)