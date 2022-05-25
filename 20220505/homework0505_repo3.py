"""實驗三 LCD and Ultrasonic
(1) 即時將ultrasonic偵測到的障礙物距離顯示在LCD上，包含cm 和inch
(2) 當障礙物距離小於5cm播放音樂
(3) ctrl+c 結束程式
"""

import RPi.GPIO as GPIO
import sys
import smbus2
import threading
from time import time
from time import sleep
from RPLCD.i2c import CharLCD

pin_ultraTrig = 27
pin_ultraEcho = 17
pin_buzzer = 22

sys.modules['smbus'] = smbus2
lcd = CharLCD('PCF8574', address=0x27, port=1, backlight_enabled=True)
print("=========== LCD setup done ==========")

musicPlay = False
stopThread = False
print("====== variable setup done ==========")

musicNoteDict = {
    "dot-Do": 262, "dot-Re": 294, "dot-Mi": 330, "dot-Fa": 349, "dot-So": 392, "dot-La": 440, "dot-Si": 494,
    "Do": 523, "Re": 587, "Mi": 659, "Fa": 698, "So": 784, "La": 880, "Si": 988,
    "Do-dot": 1046, "Re-dot": 1175, "Mi-dot": 1318, "Fa-dot": 1397, "So-dot": 1568, "La-dot": 1760, "Si-dot": 1976,
}

musicLittleStar = [
    "Do-dot", "Do-dot", "So-dot", "So-dot", "La-dot", "La-dot", "So-dot",
    "Fa-dot", "Fa-dot", "Mi-dot", "Mi-dot", "Re-dot", "Re-dot", "Do-dot",
    "So-dot", "So-dot", "Fa-dot", "Fa-dot", "Mi-dot", "Mi-dot", "Re-dot",
    "So-dot", "So-dot", "Fa-dot", "Fa-dot", "Mi-dot", "Mi-dot", "Re-dot",
    "Do-dot", "Do-dot", "So-dot", "So-dot", "La-dot", "La-dot", "So-dot",
    "Fa-dot", "Fa-dot", "Mi-dot", "Mi-dot", "Re-dot", "Re-dot", "Do-dot"
]


def printException(e, funcName):
    print("now at state %s()" % (funcName))
    print(e)


def stepInit():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin_buzzer, GPIO.OUT)
        GPIO.setup(pin_ultraTrig, GPIO.OUT)
        GPIO.setup(pin_ultraEcho, GPIO.IN)
        GPIO.output(pin_ultraTrig, False)
        print("========== GPIO.setup done ==========")
        print("\n\n")
        print("=====================================")
        print("=====================================")
        print("==== press keyboard ^C to finish ====")
        print("=====================================")
        print("=====================================")
        print("\n\n")
    except:
        print("now at state stepInit()")


def runBuzzer():
    try:
        while True:
            global musicPlay, stopThread
            p = GPIO.PWM(pin_buzzer, 100)
            p.start(80)
            for note in musicLittleStar:
                if (not musicPlay) or stopThread:
                    p.stop()
                    if stopThread:
                        print('======= buzzer thread stopped =======')
                        return "Thread end"
                    break
                p.ChangeFrequency(musicNoteDict[note])
                sleep(0.5)
            p.stop()
    except Exception as exception:
        printException(e=exception, funcName="runBuzzer")
        return "Thread end"


def runLCD(d_cm, d_in):
    try:
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string(" " + str(d_cm) + " cm")
        lcd.cursor_pos = (1, 0)
        lcd.write_string(" " + str(d_in) + " in")
    except Exception as exception:
        printException(e=exception, funcName="runLCD")
        return "Thread end"


def ultrasonicTrig():
    try:
        GPIO.output(pin_ultraTrig, True)
        sleep(0.001)
        GPIO.output(pin_ultraTrig, False)
    except Exception as exception:
        printException(e=exception, funcName="ultrasonicTrig")


def ultrasonicEcho(value, timeout):
    try:
        count = timeout
        while GPIO.input(pin_ultraEcho) != value and count > 0:
            count = count - 1
    except Exception as exception:
        printException(e=exception, funcName="ultrasonicEcho")


def ultrasonicDistance():
    while True:
        try:
            if stopThread:
                lcd.clear()
                print('======= ultra thread stopped ========')
                return "Thread end"
            ultrasonicTrig()
            ultrasonicEcho(True, 5000)
            start = time()
            ultrasonicEcho(False, 5000)
            end = time()
            distance_cm = round(((end - start) * 34000 / 2), 3)
            distance_in = round(distance_cm * 0.3937, 3)
            runLCD(distance_cm, distance_in)
            global musicPlay
            if distance_cm > 5:
                musicPlay = False
            else:
                musicPlay = True
            sleep(0.2)
        except Exception as exception:
            printException(e=exception, funcName=ultrasonicDistance)


def main():
    stepInit()
    try:
        buzzerThread = threading.Thread(target=runBuzzer)
        buzzerThread.start()
        ultraThread = threading.Thread(target=ultrasonicDistance)
        ultraThread.start()
        while True:
            print("raspi working...")
            sleep(1)
    except KeyboardInterrupt:
        print("\n\n\n")
        print("============= user STOP =============")
    except Exception as exception:
        print("\n\n\n")
        print("========== other Exception ==========")
        printException(e=exception, funcName="main")
    finally:
        global stopThread
        stopThread = True
        GPIO.cleanup()
        print("========== GPIO cleanup done ========")
        print("============ end of main() ==========")


main()
