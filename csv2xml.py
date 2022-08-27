import mycsv
data,header=mycsv.readcsv(mycsv.getdata())
header2=header.copy() #copying to fill in original values without '_'
header=[i.replace(' ','_') for i in header]
op='<?xml version="1.0"?>\n<file>\n'

#adding header to xml
op=op+'  <headers>'
for i in header2:
    op=op+i+','
#removing  ',' at the end
size = len(op)
op = op[:size - 1]
op=op+'</headers>\n'

op=op+'  <data>\n'

for record in data:          #this loop will iterate through every row
    op=op+'    <record>\n      '          #record starts with spaces for next line added to ease the loop function for each entry in the row
    for i in range(0,len(record)):      #this loop adds every entry in the row 
        head=header[i]
        dat=record[i]
        op=op+'<'+head+'>'+dat+'</'+head+'>'         
    op=op+'\n    </record>\n'
    
#after the entries are filled, the pointer is at the new line
op=op+'  </data>\n'
op=op+'</file>'
print (op)