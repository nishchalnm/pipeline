import mycsv
data,header=mycsv.readcsv(mycsv.getdata())
op='{\n'

#adding the headers to the json, pointer is at the new line

op=op+'  "headers":['
#looping to add "values", 
for i in header:
    op=op+'"'+i+'", '
#removing the last ", "
size = len(op)
op = op[:size - 2]
#adding the  '],' at the end
op=op+'],\n'

#adding the data to the json, pointer at the new line

op=op+'  "data":[\n'
#looping to add "values",
for record in data:
    op=op+'    {\n      '
    for i in range(0,len(record)):
        head=header[i]
        dat=record[i]
        op=op+'"'+head+'":"'+dat+'", '
    #removing the last ', ' at the end
    size = len(op)
    op = op[:size - 2]
    op=op+'\n    },\n'
    
#closing all the braces, final touches

#removing the ',' at the end
size = len(op)
op = op[:size - 2] #now the pointer is not at the new line but at the end of the } of the last entry

op=op+'\n  ]\n}'
print(op)
