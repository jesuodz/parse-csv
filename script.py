import csv

entry_data  = open('data')
reader      = csv.reader(entry_data)
data        = list(reader)

output_data = open('newData.csv', 'w', newline='')
csv_writer  = csv.writer(output_data, lineterminator='\n')

on  = {}
off = {}

# Save unix epoch sorted by sensor when on and off.
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

# Save sensor times
for sensor in on.items():
    name    = sensor[0]
    ons     = sensor[1]
    offs    = off[name]

    if not ons:     # Save time of last status update
        csv_writer.writerow([name, 'NONE', offs[-1]])
        continue
    else:
        """
            Sensor has at least one activation.

            last_off: last off time
            curr_on:  current time in ons
            time_off: current time in offs
        """
        last_off = 0

        for curr_on in ons:
            if curr_on < last_off: continue
            for time_off in offs:
                if time_off > curr_on:
                    last_off = time_off
                    csv_writer.writerow([name, curr_on, last_off])
                    break
            else:   # If sensor never deactivated
                csv_writer.writerow([name,curr_on, 'NONE']) # Save time of last act
                break

output_data.close()
