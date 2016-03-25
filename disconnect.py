import serial

ser = serial.Serial("/dev/ttyO1", baudrate=9600)
ser.flushInput()
ser.flushOutput()
print "***** Write command to BLE112 Rx to disconnect from sentinel active watch without flow control*****"
print "Written by Ken Lai Kin Yong for FYP sentinel active monitoring project"
print "Port open: " + ser.name
print "Writing command to BLE112...."
ser.write("\x05\x00\x01\x03\x00\x00")
print "Write complete"
print "Reading response from BLE112....."
x = ser.read(7)
print ' '.join(hex(ord(n)) for n in x)
y = ser.read(7)
print ' '.join(hex(ord(n)) for n in y)
print "Read complete"

ser.close
