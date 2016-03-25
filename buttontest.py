from bbio import *

def setup():
  pinMode(GPIO0_27,INPUT)

def loop():
  X=digitalRead(GPIO0_27)
  print X
  delay(500)

run(setup, loop) 
