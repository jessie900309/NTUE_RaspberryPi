#!/usr/bin/env python
# -*- coding: utf8 -*-
import RPi.GPIO as GPIO
import mfrc522 as MFRC522
import signal
import requests

continue_reading = True
TARGET_URL = 'localhost'

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal, frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print("Welcome to the MFRC522 data write/read example")
print("Hold a tag near the reader")
print("Press Ctrl-C to stop.")

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    # Scan for cards
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    # If a card is found
    if status == MIFAREReader.MI_OK:
        print("Card detected")
    # Get the UID of the card
    (status, uid) = MIFAREReader.MFRC522_Anticoll()
    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        # Print UID
        print("UID length: ", len(uid))
        uid_len = len(uid) - 1
        uid_decimal = 0;
        for x in range(0, uid_len):
            uid_decimal = uid_decimal + uid[x] * 256 ** (uid_len - 1 - x)
        print("Card read UID decimal: " + str(uid_decimal))
        print("Card read UID hexcimal:0x{:X}".format(uid_decimal))

        # This is the default key for authentication
        key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        # Check if authenticated
        if status == MIFAREReader.MI_OK:

            # Variable for the data to write
            my_name = "jessie Hsieh    "
            data = []
            # Fill the data with my_name
            for x in range(0, 16):
                data.append(ord(my_name[x]))
            print("\n")

            # Write the data
            MIFAREReader.MFRC522_Write(8, data)

            # Check to see if it was written
            rdData = MIFAREReader.MFRC522_Read(8)

            # web
            nameData = "".join(chr(i) for i in rdData)
            r = requests.get('http://{0}/LogRecord_GET.php?TEMP_C={1}&TEMP_F={2}&HUMD={3}'.format(TARGET_URL, uid_decimal, nameData, "0"))
            print("uid = ", uid_decimal)
            print("name = ", nameData)
            print("Server Return Code :", r.status_code)

            # Make sure to stop reading for cards
            MIFAREReader.MFRC522_StopCrypto1()
            continue_reading = False
        else:
            print("Authentication error")
