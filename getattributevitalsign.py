import serial,time

#Python script to connect to the sentinel active watch vital sign attribute and get its data. After that export the data in a text file 

ser = serial.Serial("/dev/ttyO1", baudrate=9600)
ser.flushInput()
ser.flushOutput()
print "*****Python script to get vital sign data*****"
print "Written by ken lai kin yon for FYP sentinel active monitoring"
print "Port open: " + ser.name

print "Writing command to get attribute from watch"
ser.write("\x09\x00\x05\x04\x05\x00\x10\x00\x01\x01")
print "Write complete"

print "\n"

print "Printing response from BLE112....."
a = ser.read(6)
print ' '.join(hex(ord(n)) for n in a)
print "Read confirmation response complete"

f = open('vitaldata.txt', 'w') #Open a text file to export data to 

print "\n"
print "Printing watch attribute......."
count = 0
while (count < 16):
      b = ser.read(18)
      print ' '.join(hex(ord(n)) for n in b)
      c = ' '.join(hex(ord(n)) for n in b)
      f.write(c + "\n")
      count = count + 1
      time.sleep(0.01)

print "print vital sign data complete"
