"""實驗一 3個LED控制
分別給于編號 LED1,LED2,LED3，執行:
(1) LED1:亮(ON)1分鐘;LED2&LED3暗(OFF)
(2) LED1:OFF；LDE2:閃爍5次，間隔1秒，當LED2 ON 時，Buzzer發出聲音；LED3:OFF
(3) LED1 & LED2:OFF；LED3:ON 1分鐘
(4) LED1:OFF；LDE2:閃爍3次，間隔1秒，當LED2 ON 時，Buzzer發出聲音；LED3:OFF
repeat (1)到(4)
"""

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
LED1 = 17
LED2 = 27
LED3 = 22
BUZZER1 = 18
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(BUZZER1, GPIO.OUT)


def stepDONE():
    GPIO.output(LED1, False)
    GPIO.output(LED2, False)
    GPIO.output(LED3, False)
    GPIO.output(BUZZER1, False)


def step1():
    GPIO.output(LED1, True)
    GPIO.output(LED2, False)
    GPIO.output(LED3, False)
    GPIO.output(BUZZER1, False)
    sleep(60)
    stepDONE()


def step2():
    GPIO.output(LED1, False)
    GPIO.output(LED3, False)
    for i in range(5):
        GPIO.output(LED2, True)
        GPIO.output(BUZZER1, True)
        sleep(1)
        GPIO.output(LED2, False)
        GPIO.output(BUZZER1, False)
        sleep(1)
    stepDONE()


def step3():
    GPIO.output(LED1, False)
    GPIO.output(LED2, False)
    GPIO.output(LED3, True)
    GPIO.output(BUZZER1, False)
    sleep(60)
    stepDONE()


def step4():
    GPIO.output(LED1, False)
    GPIO.output(LED3, False)
    for i in range(3):
        GPIO.output(LED2, True)
        GPIO.output(BUZZER1, True)
        sleep(1)
        GPIO.output(LED2, False)
        GPIO.output(BUZZER1, False)
        sleep(1)
    stepDONE()


def main():
    try:
        while (True):
            step1()
            step2()
            step3()
            step4()
    except KeyboardInterrupt:
        print("========== user STOP ==========")
    except:
        print("======= other Exception =======")
    finally:
        GPIO.cleanup()
    print("====== GPIO cleanup done =====")
    print("======== end of main() =======")


main()
