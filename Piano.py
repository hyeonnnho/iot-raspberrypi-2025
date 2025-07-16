import RPi.GPIO as GPIO
import time

# 부저 핀 설정
BUZZER_PIN = 18

# GPIO 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 부저 PWM 설정
pwm = GPIO.PWM(BUZZER_PIN, 440)  # 기본 440Hz
pwm.start(0)

# 음계 매핑
notes = {
    '1': 261,  # 도
    '2': 294,  # 레
    '3': 329,  # 미
    '4': 349,  # 파
    '5': 392,  # 솔
    '6': 440,  # 라
    '7': 493,  # 시
    '8': 523   # 도 (한 옥타브 위)
}

try:
    print("🎹 키보드 피아노 시작 (1~8 키 입력, q 입력 시 종료)")
    while True:
        key = input("▶ 누를 키: ")
        if key == 'q':
            break
        elif key in notes:
            pwm.ChangeFrequency(notes[key])
            pwm.ChangeDutyCycle(50)  # 소리 출력
            time.sleep(0.5)
            pwm.ChangeDutyCycle(0)   # 소리 끔
        else:
            print("⚠️ 1~8 또는 q만 입력 가능")

except KeyboardInterrupt:
    print("\n종료됨")

finally:
    pwm.stop()
    GPIO.cleanup()
