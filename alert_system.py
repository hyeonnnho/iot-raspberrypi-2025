import RPi.GPIO as GPIO
import time

LED_PIN = 14
BUZZER_PIN = 18
BUTTON_PIN = 23

is_active = False

Melody = [880, 440, 880, 440, 880]

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 풀업 버튼

# PWM 부저
buzzer_pwm = GPIO.PWM(BUZZER_PIN, 1000)  # 1kHz
buzzer_pwm.stop()

def toggle_alert(channel):
        global is_active

        is_active = not is_active  # 상태 토글

        if not is_active:
                GPIO.output(LED_PIN, GPIO.HIGH)
                buzzer_pwm.stop()
                print("경고 멈춤")

GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=toggle_alert, bouncetime=300)

try:
    print("▶ 시스템 시작 (버튼 눌러주세요)")
    while True:
        if is_active:
                print("⚠️ 경고 시작!")
                for i in range(0, len(Melody)):
                        GPIO.output(LED_PIN, GPIO.LOW)
                        buzzer_pwm.start(50)
                        buzzer_pwm.ChangeFrequency(Melody[i])
                        time.sleep(0.3)
                        GPIO.output(LED_PIN, GPIO.HIGH)
                        time.sleep(0.1)
        else:
                time.sleep(1)

except KeyboardInterrupt:
    print("\n종료 중...")

finally:
    buzzer_pwm.stop()
    GPIO.cleanup()
    print("GPIO 정리 완료.")
