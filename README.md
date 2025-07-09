# iot-raspberrypi-2025

### RPI.FPIO 모듈
- GPIO.setmode(GPIO.BOARD)      # wPi
- GPIO.setmode(GPIO.BVM)        # BCM
- GPIO.setup(channel.GPIO.mode) # 사용할 핀의 모드 설정(IN/OUT)
- GPIO.cleanup()                # 모든 핀 초기화
- GPIO.output(channel, state)   # HIGH(1) / LOW(0)
- GPIO.input(channel)           

