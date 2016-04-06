#!/usr/bin/python
import re

f = open("./WG1.BLM", "r");
output = open("./procfile", "w");
file_contents = f.read();
buffer = re.split('#[A-Z]+#', file_contents);
header = buffer[2].strip();
data = buffer[3].strip();
mergedparts = header + data;
rows = re.split('~', mergedparts);

dwellings = []
for i in rows:
    fields = re.split('^', i);
    dwellings.append(fields)
    


print repr(dwellings[6])

query = 'INSERT dwellings[1],  INTO "firstcolumn", "secondcolumn"'

f.close();

output.close();



