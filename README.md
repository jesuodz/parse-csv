# CSV Parser script

## Client's problem description:

I have a csv file that has sensor data. Looking for a python script to step through it, and create a new csv file with on and off times. csv file is currently in this format:

`sensorname, temperature, v1, voltage,inputdate,inputtime,unixtimestamp.`

* When a sensor temperature is greater than 5000, it is considered on.
* When a sensor temperature is less than 5000, it is considered off. The data is in chronological order by unixtimestamp.
* Result csv should have data that looks like: 

`sensorname, unixtimestamp_on, unixtimestamp_off`.
