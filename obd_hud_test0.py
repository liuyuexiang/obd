#import required libraries
import obd
#establish a connection with the OBD device
ports = obd.scan_serial() # return list of valid USB or RF ports
print (ports)
connection = obd.OBD()
# while len(connection.supported_commands) < 100:
# connection = obd.Async("/dev/rfcomm0", protocol = "6", baudrate = "9600", fast = False, timeout = 30)
#create a command varialbe
c = obd.commands.RPM
# FUEL_LEVEL
#query the command and store the response
response = connection.query(c)
#print the response value
print('engin speed',response.value)

#create a command varialbe
c = obd.commands.FUEL_LEVEL
# FUEL_LEVEL
#query the command and store the response
response = connection.query(c)
#print the response value
print('fuel level input',response.value)

c = obd.commands.FUEL_STATUS
response = connection.query(c)
print('Fuel System Status',response.value)

c = obd.commands.RUN_TIME
response = connection.query(c)
print('Engine Run Time ',response.value)


c = obd.commands.DISTANCE_W_MIL
response = connection.query(c)
print('Distance Traveled with MIL on',response.value)

c = obd.commands.DISTANCE_SINCE_DTC_CLEAR
response = connection.query(c)
print('Distance traveled since codes cleared',response.value)

c = obd.commands.STATUS_DRIVE_CYCLE
response = connection.query(c)
print('Monitor status this drive cycle',response.value)
print(response.value.FUEL_SYSTEM_MONITORING)

#close the connection
connection.close()