# 온습도 센서에서 읽은 값을 DB에 저장
import time
import board
import adafruit_dht
import mysql.connector

# DHT 센서 설정
dht = adafruit_dht.DHT11(board.D23)

# DB 연결 설정
conn = mysql.connector.connect(
    host="localhost",
    user="sensor_user",
    password="sensor_pass",
    database="test"
)
cursor = conn.cursor()

try:
    while True:
        try:
            temp = dht.temperature
            humi = dht.humidity

            if temp is not None and humi is not None:
                print(f"Temp: {temp}, Humi: {humi}")

                sql = "INSERT INTO dht_data (temperature, humidity) VALUES (%s, %s)"
                cursor.execute(sql, (temp, humi))
                conn.commit()
            else:
                print("센서 값이 None입니다.")

            time.sleep(2)

        except RuntimeError as e:
            print("센서 오류:", e.args[0])
            time.sleep(2)

except KeyboardInterrupt:
    print("종료합니다.")

finally:
    cursor.close()
    conn.close()