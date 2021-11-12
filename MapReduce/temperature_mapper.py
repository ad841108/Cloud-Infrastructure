import sys

valid_quality = {0, 1, 4, 5, 9}
for line in sys.stdin:
    yearMonthDay = int(line[15:23])
    if(line[87] == '-'):
        temperature = int(line[88:92]) * -1
    else:
        temperature = int(line[88:92])
    if(temperature == 9999):
        continue
    quality = int(line[92])
    if (quality in valid_quality):
        print('%s\t%d' % (yearMonthDay, temperature))