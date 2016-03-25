import serial

ser = serial.Serial("/dev/ttyO1", baudrate=9600)
ser.flushInput()
ser.flushOutput()
print "*****Write command to BLE112 to direct connect to sentinel watch*****"
print "Written by Ken Lai Kin Yong for FYP sentinel active monitoring"
print "Port open: " + ser.name
print "Writing command to BLE112...."
ser.write("\x13\x00\x0f\x06\x03\x7b\xd8\x60\x80\x07\x00\x00\x3c\x00\x3c\x00\x64\x00\x00\x00")
print "Write complete"
print "Reading response from BLE112....."
x = ser.read(7)
print ' '.join(hex(ord(n)) for n in x)
y = ser.read(19)
print ' '.join(hex(ord(n)) for n in y)
print "Read complete"
print "Directly connected to sentinel watch"
ser.close
