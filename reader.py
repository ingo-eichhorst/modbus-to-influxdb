#!/usr/bin/env python
import minimalmodbus
import time
from influxdb import InfluxDBClient

# SETUP CONNECTION TO MODBUS DEVICE
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1, mode='rtu', debug = False)
instrument.serial.baudrate = 9600
instrument.serial.timeout = 0.2

# SETUP CONNECTION TO INFLUXDB
client = InfluxDBClient(host='localhost', port=8086, username="admin", password="admin", database='energy')
client.create_database('energy')

def save_data(name, data):
    # print('{} - {}'.format(name, data))
    json_body = [
      {
        "measurement": name,
        "fields": {
          "value": data
        }
      }
    ]
    client.write_points(json_body)

def read_register(name, register, type):
    if(type=="float"):
        data = instrument.read_float(register, number_of_registers=2)
        save_data(name, data)

    elif(type=="int64"):
        int = instrument.read_long(register+2)
        save_data(name, int)

    elif(type=="string"):
      	data = instrument.read_string(register, number_of_registers=2)
        save_data(name, data)

while True:
    read_register('Strom Phase 1', 2999, "float")
    read_register('Strom Phase 2', 3001, "float")
    read_register('Strom Phase 3', 3003, "float")
    read_register('Strommittel', 3009, "float")

    read_register('Spannung L1-N', 3027, "float")
    read_register('Spannung L2-N', 3029, "float")
    read_register('Spannung L3-N', 3031, "float")
    read_register('Spannung L-N Mittel', 3035, "float")

    read_register('Wirkleistung Phase 1', 3053, "float")
    read_register('Wirkleistung Phase 2', 3055, "float")
    read_register('Wirkleistung Phase 3', 3057, "float")
    read_register('Gesamt-Wirkleistung', 3059, "float")

    read_register('Gesamt-Leistungsfaktor', 3083, "float")
    read_register('Frequenz', 3109, "float")

    read_register('Wirkenergie Phase 1', 3517, "int64")
    read_register('Wirkenergie Phase 2', 3521, "int64")
    read_register('Wirkenergie Phase 3', 3525, "int64")
    read_register('Gesamt-Wirkenergie', 3203, "int64")

    #read_register('Gesamt-Blindleistung', 3067, "string")
    #read_register('Gesamt-Scheinleistung', 3075, "string")

    time.sleep(20)
