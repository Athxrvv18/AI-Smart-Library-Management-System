from scanner import scan_barcode
from database import issue_book, return_book, check_book
import RPi.GPIO as GPIO
import time

IR_ISSUE = 5
IR_RETURN = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_ISSUE, GPIO.IN)
GPIO.setup(IR_RETURN, GPIO.IN)

print("System Ready...")

while True:
    if GPIO.input(IR_ISSUE):
        print("Issue Mode Activated")
        book_id = scan_barcode()

        if check_book(book_id, mode="issue"):
            user_id = scan_barcode()
            issue_book(book_id, user_id)

    elif GPIO.input(IR_RETURN):
        print("Return Mode Activated")
        book_id = scan_barcode()

        if check_book(book_id, mode="return"):
            user_id = scan_barcode()
            return_book(book_id, user_id)

    time.sleep(1)