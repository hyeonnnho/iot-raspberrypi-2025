import RPi.GPIO as GPIO
import time

buzzerPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)

pwm = GPIO.PWM(buzzerPin, 1000)  # 1kHz
pwm.start(50)  # 50% duty cycle

time.sleep(1)

pwm.stop()
GPIO.cleanup()
