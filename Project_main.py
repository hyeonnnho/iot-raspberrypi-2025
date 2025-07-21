import RPi.GPIO as GPIO
import time
import requests
import re

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
                url = "https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=kO1Tgnr9TLxJvLP6nOk7%2FiGG08nKUk1WitMOzpjpV%2B%2B7ipktapacBpdqPiLPWiVeZj8XdrYE%2BYlvjv9S8Yv52g%3D%3D&returnType=xml&numOfRows=100&pageNo=1&sidoName=%EB%B6%80%EC%82%B0&ver=1.0"
                response = requests.get(url)

                pm10 = re.findall(r'<pm10Value>(.+)</pm10Value>', response.text)
                pm25 = re.findall(r'<pm25Value>(.+)</pm25Value>', response.text)
                stationName = re.findall(r'<stationName>(.+)</stationName>', response.text)

                findNum = stationName.index('대연동')

                print("pm10: ", pm10[findNum])
                print("pm25: ", pm25[findNum])
                print("stationName: ", stationName[findNum])

                pm25 = int(pm25[findNum])
                if pm25 <= 30:
                        GPIO.output(RED, GPIO.HIGH)
                        GPIO.output(GREEN, GPIO.HIGH)
                        GPIO.output(BLUE, GPIO.LOW)
                elif pm25 >= 31 and pm25 <= 80:
                        GPIO.output(RED, GPIO.HIGH)
                        GPIO.output(GREEN, GPIO.LOW)
                        GPIO.output(BLUE, GPIO.HIGH)
                elif pm25 >= 81 and pm25 <= 150:
                        GPIO.output(RED, GPIO.LOW)
                        GPIO.output(GREEN, GPIO.HIGH)
                        GPIO.output(BLUE, GPIO.LOW)
                elif pm25 >= 151:
                        GPIO.output(RED, GPIO.LOW)
                        GPIO.output(GREEN, GPIO.HIGH)
                        GPIO.output(BLUE, GPIO.HIGH)

                for i in range(3):
                        time.sleep(1)

except KeyboardInterrupt:
        pass

finally:
        GPIO.cleanup()
