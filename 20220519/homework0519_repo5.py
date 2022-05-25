"""實驗五 DHT22 & Web
(1) 完成DHT22溫溼度量測，並上傳華氏溫度，攝氏溫度，濕度，量測時間到MySQL(MariaDB)資料庫，並能夠顯示這些資料在瀏覽器上。
"""

import time
import board
import adafruit_dht
import requests
import RPi.GPIO as GPIO

TARGET_URL = 'localhost'

# Initial the dht device, with data pin connected to GPIO4:
dhtDevice = adafruit_dht.DHT22(board.D4)

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.2f} F / {:.2f} C    Humidity: {:.2f}% \n".format(
                temperature_f, temperature_c, humidity
            )
        )
        r = requests.get('http://{0}/LogRecord_GET.php?TEMP_C={1}&TEMP_F={2}&HUMD={3}'.format(TARGET_URL, temperature_c, temperature_f, humidity))
        print("Server Return Code :", r.status_code)
        print(r.text)
        time.sleep(2.0)

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        GPIO.cleanup()
        raise error
