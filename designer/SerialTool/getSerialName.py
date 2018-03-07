import serial
import serial.tools.list_ports

port_list = list(serial.tools.list_ports.comports())

print(port_list)

if len(port_list) <= 0:
    print("Serial port can't find")
else:
    port_list_0 = list(port_list[0])
    port_serial = port_list_0[0]
    ser = serial.Serial(port_serial,  115200,  timeout = 10)
    
