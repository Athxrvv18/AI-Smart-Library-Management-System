import cv2
from pyzbar.pyzbar import decode
from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
import time
import mysql.connector
from datetime import datetime, timedelta

# ---------------- LCD ----------------
lcd = CharLCD('PCF8574', 0x27)   # change if your address is 0x3F

# ---------------- GPIO ----------------
ISSUE_PIN = 17
RETURN_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(ISSUE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RETURN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# ---------------- CAMERA ----------------
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

# ---------------- DATABASE ----------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",   # 🔥 CHANGE THIS
    database="library_db"
)
cursor = db.cursor()

# ---------------- FUNCTION ----------------
def scan_barcode(message):
    lcd.clear()
    lcd.write_string(message)

    start = time.time()
    while time.time() - start < 15:
        ret, frame = cap.read()
        if not ret:
            continue

        barcodes = decode(frame)
        for barcode in barcodes:
            return barcode.data.decode('utf-8')

    return None

# ---------------- MAIN LOOP ----------------
try:
    while True:
        lcd.clear()
        lcd.write_string("Place Hand...")
        time.sleep(1)

        # Detect Mode
        if GPIO.input(ISSUE_PIN) == 0:
            mode = "ISSUE"
        elif GPIO.input(RETURN_PIN) == 0:
            mode = "RETURN"
        else:
            continue

        lcd.clear()
        lcd.write_string(mode + " MODE")
        time.sleep(2)

        # Scan Book
        book_id = scan_barcode("Scan Book")
        if not book_id:
            lcd.clear()
            lcd.write_string("No Book Found")
            time.sleep(2)
            continue

        print("Book:", book_id)

        # Scan User
        user_id = scan_barcode("Scan User")
        if not user_id:
            lcd.clear()
            lcd.write_string("No User Found")
            time.sleep(2)
            continue

        print("User:", user_id)

        # ---------------- ISSUE ----------------
        if mode == "ISSUE":
            issue_date = datetime.now()
            return_date = issue_date + timedelta(days=7)

            cursor.execute(
                "UPDATE bookdatabase SET available=0, issuedto=%s, issuedate=%s, returndate=%s WHERE uid=%s",
                (user_id, issue_date, return_date, book_id)
            )
            db.commit()

            lcd.clear()
            lcd.write_string("Book Issued")

        # ---------------- RETURN ----------------
        else:
            cursor.execute(
                "UPDATE bookdatabase SET available=1, issuedto=NULL, issuedate=NULL, returndate=NULL WHERE uid=%s",
                (book_id,)
            )
            db.commit()

            lcd.clear()
            lcd.write_string("Book Returned")

        time.sleep(3)

except KeyboardInterrupt:
    GPIO.cleanup()
    lcd.clear()
    cap.release()
    cv2.destroyAllWindows()
    cursor.close()
    db.close()