import csv
from time import ctime
from pprint import pprint

entry_data  = open('data')
reader      = csv.reader(entry_data)
data        = list(reader)

output_data = open('newData.csv', 'w', newline='')
csv_writer  = csv.writer(output_data, lineterminator='\n')

on  = {}
off = {}

# Save unix epoch for all sensors when on and off.
for row in data:
    sensor_name = row[0]
    sensor_temp = int(row[1])
    timestamp   = row[len(row) - 1]

    on.setdefault(sensor_name, [])
    off.setdefault(sensor_name, [])

    if sensor_temp >= 5000:
        on[sensor_name].append(int(timestamp))
    else:
        off[sensor_name].append(int(timestamp))

for sensor in on.items():
    name        = sensor[0]
    temps       = sensor[1]
    offs        = off[name]

    if not temps:
        csv_writer.writerow([name, 'NONE', offs[0]])
        continue
    else:
        pass

output_data.close()
