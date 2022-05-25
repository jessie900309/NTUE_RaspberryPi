"""實驗二(2)
(1) 7-Segment由Key來控制
(2) Ultrasonic不再被Key控制，而是獨立在主程式運作，每隔3秒顯示障礙物的距離
"""

import RPi.GPIO as GPIO
from time import time
from time import sleep

GPIO.setmode(GPIO.BCM)
pin_segA = 24
pin_segB = 23
pin_segC = 21
pin_segD = 20
pin_segE = 16
pin_segF = 25
pin_segG = 12
pin_ultraTrig = 27
pin_ultraEcho = 17
pin_key = 2
sevenSegmentPin = [pin_segG, pin_segF, pin_segE, pin_segD, pin_segC, pin_segB, pin_segA]

sevenSegmentStringDict = {
    0: "0111111",
    1: "0000110",
    2: "1011011",
    3: "1001111",
    4: "1100110",
    5: "1101101",
    6: "1111101",
    7: "0000111",
    8: "1111111",
    9: "1101111",
    10: "1110111",
    11: "1111100",
    12: "0111001",
    13: "1011110",
    14: "1111001",
    15: "1110001"
}

userPressCount = 0


def stepInit():
    try:
        GPIO.setup(pin_key, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(pin_ultraEcho, GPIO.IN)
        GPIO.setup(pin_ultraTrig, GPIO.OUT)
        for pin in sevenSegmentPin:
            GPIO.setup(pin, GPIO.OUT)
        print("========== GPIO.setup done ==========")
        for pinIndex in range(7):
            value = int(sevenSegmentStringDict[0][pinIndex])
            GPIO.output(sevenSegmentPin[pinIndex], value)
        print("====== 7-Segment setup done =========")
        GPIO.output(pin_ultraTrig, False)
        print("====== ultraTrig setup done =========")
        global userPressCount
        userPressCount = 0
        print("====== variable setup done ==========")
        print("\n\n")
        print("=====================================")
        print("=====================================")
        print("=== press button to ++ the number ===")
        print("==== press keyboard ^C to finish ====")
        print("=====================================")
        print("=====================================")
        print("\n\n")
    except:
        print("now at state stepInit()")


def sevenSegmentControl(number):
    try:
        for pinIndex in range(7):
            value = int(sevenSegmentStringDict[number][pinIndex])
            GPIO.output(sevenSegmentPin[pinIndex], value)
    except:
        print("now at state sevenSegmentControl()")
        print("now number = ", number)


def ultrasonicEcho(value, timeout):
    count = timeout
    while GPIO.input(pin_ultraEcho) != value and count > 0:
        count = count - 1


def ultrasonicDistance():
    try:
        GPIO.output(pin_ultraTrig, True)
        sleep(0.001)
        GPIO.output(pin_ultraTrig, False)
        ultrasonicEcho(True, 5000)
        start = time()
        ultrasonicEcho(False, 5000)
        end = time()
        distance = round(((end - start) * 34000 / 2), 3)
        print("the distance = ", distance, " cm")
    except:
        print("now at state ultrasonicDistance()")


def keyAndSevenSegmentControl(pin_key):
    global userPressCount
    userPressCount += 1
    userPressCount %= 16
    sevenSegmentControl(userPressCount)


def main():
    stepInit()
    try:
        GPIO.add_event_detect(pin_key, GPIO.FALLING, callback=keyAndSevenSegmentControl, bouncetime=200)
        while (True):
            ultrasonicDistance()
            sleep(3)
    except KeyboardInterrupt:
        print("\n\n")
        print("============= user STOP =============")
    except:
        print("\n\n")
        print("========== other Exception ==========")
    finally:
        GPIO.cleanup()
        print("========== GPIO cleanup done ========")
        print("============ end of main() ==========")


main()
