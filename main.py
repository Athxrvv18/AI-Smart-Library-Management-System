# ================= IMPORTS =================
import cv2
from pyzbar.pyzbar import decode
import mysql.connector
import time
import RPi.GPIO as GPIO
from datetime import datetime, timedelta

# ================= GPIO SETUP =================
IR_ISSUE = 17     # Issue sensor
IR_RETURN = 26    # Return sensor

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_ISSUE, GPIO.IN)
GPIO.setup(IR_RETURN, GPIO.IN)

# ================= DATABASE =================
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="library"
)

cursor = db.cursor()
print("✅ Database Connected")

# ================= CAMERA =================
cap = cv2.VideoCapture(0)

# ================= FUNCTIONS =================

def scan_barcode(timeout=10):
    """Scan barcode within given time"""
    start_time = time.time()

    while time.time() - start_time < timeout:
        ret, frame = cap.read()
        barcodes = decode(frame)

        for barcode in barcodes:
            data = barcode.data.decode('utf-8')
            print("📌 Scanned:", data)
            return data

        cv2.imshow("Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    return None


def check_book(book_id, mode):
    query = "SELECT available FROM bookdatabase WHERE uid=%s"
    cursor.execute(query, (book_id,))
    result = cursor.fetchone()

    if not result:
        print("❌ Book Not Found")
        return False

    available = result[0]

    if mode == "issue" and available == 1:
        return True
    elif mode == "return" and available == 0:
        return True

    print("⚠️ Invalid Operation")
    return False


def issue_book(book_id, user_id):
    issue_date = datetime.now()
    return_date = issue_date + timedelta(days=7)

    query = """UPDATE bookdatabase 
               SET available=0, issuedto=%s, issuedate=%s, returndate=%s 
               WHERE uid=%s"""

    cursor.execute(query, (user_id, issue_date, return_date, book_id))
    db.commit()

    print("✅ Book Issued")
    print("Return Date:", return_date)


def return_book(book_id, user_id):
    query = """UPDATE bookdatabase 
               SET available=1, issuedto=NULL, issuedate=NULL, returndate=NULL 
               WHERE uid=%s"""

    cursor.execute(query, (book_id,))
    db.commit()

    print("✅ Book Returned")


# ================= MAIN LOOP =================

print("\n📚 Automated Library System Started...\n")

while True:

    print("\n👉 Waiting for user...")
    time.sleep(2)

    # ===== ISSUE MODE =====
    if GPIO.input(IR_ISSUE):
        print("\n📖 ISSUE MODE")

        print("Scan Book...")
        book_id = scan_barcode()

        if not book_id:
            print("❌ No Book Scanned")
            continue

        if not check_book(book_id, "issue"):
            continue

        print("Scan User ID...")
        user_id = scan_barcode()

        if not user_id:
            print("❌ No User Scanned")
            continue

        issue_book(book_id, user_id)
        time.sleep(3)


    # ===== RETURN MODE =====
    elif GPIO.input(IR_RETURN):
        print("\n📕 RETURN MODE")

        print("Scan Book...")
        book_id = scan_barcode()

        if not book_id:
            print("❌ No Book Scanned")
            continue

        if not check_book(book_id, "return"):
            continue

        print("Scan User ID...")
        user_id = scan_barcode()

        if not user_id:
            print("❌ No User Scanned")
            continue

        return_book(book_id, user_id)
        time.sleep(3)

# ================= CLEANUP =================
cap.release()
cv2.destroyAllWindows()
cursor.close()
db.close()
GPIO.cleanup()