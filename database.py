import mysql.connector
from datetime import datetime, timedelta

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="library"
)

cursor = db.cursor()


def check_book(book_id, mode):
    query = "SELECT available FROM bookdatabase WHERE uid=%s"
    cursor.execute(query, (book_id,))
    result = cursor.fetchone()

    if not result:
        print("Book Not Found")
        return False

    available = result[0]

    if mode == "issue" and available == 1:
        return True
    elif mode == "return" and available == 0:
        return True

    print("Invalid Operation")
    return False


def issue_book(book_id, user_id):
    issue_date = datetime.now()
    return_date = issue_date + timedelta(days=7)

    query = """UPDATE bookdatabase 
               SET available=0, issuedto=%s, issuedate=%s, returndate=%s 
               WHERE uid=%s"""

    cursor.execute(query, (user_id, issue_date, return_date, book_id))
    db.commit()

    print("Book Issued Successfully")


def return_book(book_id, user_id):
    query = """UPDATE bookdatabase 
               SET available=1, issuedto=NULL, issuedate=NULL, returndate=NULL 
               WHERE uid=%s"""

    cursor.execute(query, (book_id,))
    db.commit()

    print("Book Returned Successfully")