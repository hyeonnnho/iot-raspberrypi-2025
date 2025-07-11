import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

RED = 14
BLUE = 15
GREEN = 18

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)


try:
    while True:
        GPIO.output(RED, GPIO.HIGH)
        GPIO.output(GREEN, GPIO.HIGH)
        GPIO.output(BLUE, GPIO.LOW)
        print("BLUE")
        time.sleep(0.5)
        GPIO.output(BLUE, GPIO.HIGH)
        time.sleep(0.5)

        GPIO.output(RED, GPIO.LOW)
        GPIO.output(GREEN, GPIO.HIGH)
        GPIO.output(BLUE, GPIO.HIGH)
        print("RED")
        time.sleep(0.5)
        GPIO.output(RED, GPIO.HIGH)
        time.sleep(0.5)

        GPIO.output(RED, GPIO.HIGH)
        GPIO.output(GREEN, GPIO.LOW)
        GPIO.output(BLUE, GPIO.HIGH)
        print("GREEN")
        time.sleep(0.5)
        GPIO.output(GREEN, GPIO.HIGH)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("프로그램 종료")

finally:
    GPIO.cleanup()
