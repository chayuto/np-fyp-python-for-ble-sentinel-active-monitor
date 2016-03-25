import serial,time

#Python script to connect to the sentinel active watch fall detection attribute and get its data 

ser = serial.Serial("/dev/ttyO1", baudrate=9600)
ser.flushInput()
ser.flushOutput()
print "*****Python script to get fall detection data*****"
print "Written by ken lai kin yon for FYP sentinel active monitoring"
print "Port open: " + ser.name

print "Writing command to get attribute from watch"
ser.write("\x09\x00\x05\x04\x05\x00\x17\x00\x01\x01")
print "Write complete"

print "\n"

print "Printing response from BLE112....."
a = ser.read(16)
print ' '.join(hex(ord(n)) for n in a)
print "Read confirmation response complete"

print "\n"
print "Printing watch attribute......."
b = ser.read(18)
print ' '.join(hex(ord(n)) for n in b)


print "print fall detection data complete"
