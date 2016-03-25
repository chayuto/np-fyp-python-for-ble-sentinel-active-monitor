import serial, time

ser = serial.Serial("/dev/ttyO1", baudrate=9600)
ser.flushInput()
ser.flushOutput()
print "*****Write command to BLE112 RX to set it to scanning mode without flow control*****"
print "Written by ken lai kin yong for FYP sentinel active monitoring"
print "Port Open: " + ser.name
print "Writing command to BLE112....."
ser.write("\x05\x00\x01\x06\x02\x02")
print "WrITE complete"

print "\n"
print "Reading response from BLE112....."
x = ser.read(6)
print ' '.join(hex(ord(n)) for n in x)
print "Read complete"

print "\n"
print "Reading scan response........"
count = 0

while (count < 16):
      y = ser.read(18)
      print ' '.join(hex(ord(n)) for n in y)
      count = count + 1
      time.sleep(0.01)

print "Read 15 times complete"
ser.close
