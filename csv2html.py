
import mycsv
data,header=mycsv.readcsv(mycsv.getdata())
op= "<html>\n<body>\n<table>\n"

op=op+"<tr><th>"
for i in header:
    op=op+i+"</th><th>"
size = len(op)
op = op[:size - 4]
op=op+"</tr>\n"

for j in range(len(data)):
    op=op+"<tr><td>"
    for i in data[j]:
        op=op+i+"</td><td>"
    size = len(op)
    op = op[:size - 4]
    op=op+"</tr>\n"

op= op+"</table>\n</body>\n</html>"
print (op)