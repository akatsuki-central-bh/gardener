import time
import RPi.GPIO as GPIO

class Component():
  def __init__(self, pin):
    self.pin = pin

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(self.pin, GPIO.OUT)

  def toggle_with_delay(self, delay):
    self.on()
    time.sleep(delay)
    self.off()

  def on(self):
    GPIO.output(self.pin, GPIO.HIGH)

  def off(self):
    GPIO.output(self.pin, GPIO.LOW)
