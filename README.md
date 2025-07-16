# iot-raspberrypi-2025

## 라즈베리파이 관리/조작
- putty : 윈도우에서 **원격 터미널 접속(SSH, Telnet 등)**을 가능하게 해주는 오픈소스 클라이언트 프로그램
    - 리눅스 기반
- VNC : 원격 컴퓨터의 화면을 그대로 전송하여 **GUI(그래픽 사용자 인터페이스)**로 제어
- Qt Designer : Qt 프레임워크 기반 애플리케이션의 사용자 인터페이스(UI)를 시각적으로 설계

### RPI.FPIO 모듈
- GPIO.setmode(GPIO.BOARD)      # wPi
- GPIO.setmode(GPIO.BVM)        # BCM
- GPIO.setup(channel.GPIO.mode) # 사용할 핀의 모드 설정(IN/OUT)
- GPIO.cleanup()                # 모든 핀 초기화
- GPIO.output(channel, state)   # HIGH(1) / LOW(0)
- GPIO.input(channel)           

### 라즈베리파이
- VCC : 5V or 3.3V
- S : SIGNAL
- `-` : GND
- pinout
    ```bash
    >> pinout
        3V3  (1) (2)  5V
        GPIO2  (3) (4)  5V
        GPIO3  (5) (6)  GND
        GPIO4  (7) (8)  GPIO14
        GND  (9) (10) GPIO15
        GPIO17 (11) (12) GPIO18
        GPIO27 (13) (14) GND
        GPIO22 (15) (16) GPIO23
        3V3 (17) (18) GPIO24
        GPIO10 (19) (20) GND
        GPIO9 (21) (22) GPIO25
        GPIO11 (23) (24) GPIO8
        GND (25) (26) GPIO7
        GPIO0 (27) (28) GPIO1
        GPIO5 (29) (30) GND
        GPIO6 (31) (32) GPIO12
        GPIO13 (33) (34) GND
        GPIO19 (35) (36) GPIO16
        GPIO26 (37) (38) GPIO20
        GND (39) (40) GPIO21
    ```

## PYENV가상환경 설치
```bash
# 설치
sudo apt install python3-venv
# 가상환경 만들기
python3 -m venv [폴더이름]
# 가상환경 활성화
source [폴더이름]/bin/activate
## 이후에 필요한 패키지 설치
## pip install pyqt5
## pip install adafruit-circuitpython-dht

```
### LED
- LED[소스](./led.py)

### BUTTON
- BUTTON[소스](./button.py)

### 온습도 센서
- DHT11 센서[소스](./dht11.py)

- DHT11 센서와 DB 연결[소스](./dht11data.py)

#### MySQL 설치
```bash
sudo apt update
sudo apt install mysql-server
sudo systemctl status mysql
```

- DB 접속 : `sudo mysql`
- DB 정보 보기 : `SHOW Databases;`
- 데이터베이스 만들기
- 데이터베이스 접속 : `USE test`
- 테이블 만들기
- 테이블 확인 : `SHOW Tables;`
- 테이블 보기 : `SELECT * FROM dht_data;`
- 나가기 : \q
- 도움말 : \h

### PyQt5
- 가상환경 실행
- 패키지 설치
    - pip install PyQt5

- VNC 환경에서 QT Designer 설치
```bash
sudo apt update
sudo apt install qttools5-dev-tools
```

- VNC > 열매 > 개발 > Qt 5 Designer
    - GUI로 창 구성
    - *.ui로 저장
    ```python
    import sys
    from PyQt5.QtWidgets import *
    from PyQt5 import uic

    class WindowClass(QDialog):
        def __init__(self, parent = None):
                super().__init__(parent)
                self.ui = uic.loadUi("design1.ui", self) # UI파일을 파이썬 코드로 불러옮
                self.ui.show()

        def slot1(self):        # 버튼 누를 때 동작
                print("Bye Bye~~")

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        myWindow = WindowClass()
        app.exec_()

    ```

### Buzzer
- BUZZER[소스](./buzzer.py)
- 키보드를 사용한 Piano[소스](./Piano.py)
- 알람 시스템[소스](./alert_system.py)

### Relaymodule
- Relaymodule 정상 테스트[소스](./relaymodule.py)

- NC/COM/NO
    - NC : 평소(릴레이가 꺼졌을 때) 닫혀 있는 회로. 즉, 항상 전기가 흐르는 상태.
    - COM : 공통 단자. 입력 전압이 들어오는 곳 (보통 +전원이나 신호선).
    - NO : 평소에는 열려 있음. 릴레이가 작동하면 닫혀서 전기가 흐르게 됨.