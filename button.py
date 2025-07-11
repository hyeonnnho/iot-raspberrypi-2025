import RPi.GPIO as GPIO
import time

buttonPin = 17
RED = 14
BLUE = 15
GREEN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN)

click_count = 0
last_click_time = 0

try:
        while True:
                if(GPIO.input(buttonPin)):
#                       print("button released")
                        time.sleep(0.2)
                else:
                        now = time.time()
                        if now - last_click_time > 1:
                                click_count = 0

                        click_count += 1
                        last_click_time = now

                        time.sleep(0.4)

                        if(click_count == 1):
                                GPIO.output(RED, GPIO.LOW)
                                print("LED RED")
                                time.sleep(0.5)
                        elif(click_count == 2):
                                GPIO.output(RED, GPIO.HIGH)
                                GPIO.output(BLUE, GPIO.LOW)
                                print("LED BLUE")
                                time.sleep(0.5)
                        elif(click_count == 3):
                                GPIO.output(RED, GPIO.HIGH)
                                GPIO.output(BLUE, GPIO.HIGH)
                                GPIO.output(GREEN, GPIO.LOW)
                                print("LED GREEN")
                                time.sleep(0.5)
                        elif(click_count == 4):
                                GPIO.output(RED, GPIO.HIGH)
                                GPIO.output(BLUE, GPIO.HIGH)
                                GPIO.output(GREEN, GPIO.HIGH)
                                print("LED OFF")
                                time.sleep(0.5)
                                click_count = 0

except KeyboardInterrupt:
        print("프로그램 종료")

finally:
        GPIO.cleanup()
