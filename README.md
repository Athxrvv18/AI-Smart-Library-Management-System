# 📚 Automated Library Management System (Raspberry Pi)

## 🚀 Project Overview

The **Automated Library Management System** is an IoT-based project designed to automate traditional library operations like book issuing and returning.

This system eliminates manual work by using:

* Barcode scanning
* Raspberry Pi automation
* MySQL database
* IR sensors for user interaction
* LCD display for real-time feedback

The project improves efficiency, reduces human error, and provides a modern smart-library experience.

---

## 🎯 Objectives

* Automate book issue and return process
* Reduce manual errors and workload
* Provide real-time feedback to users
* Maintain accurate database records
* Implement fine calculation and due date system

---

## ⚙️ Features

* 📷 Barcode-based book identification
* 🪪 User ID card scanning
* 📅 Automatic due date (7 days)
* 💰 Fine calculation for late return
* 📟 LCD display for instructions and status
* 🔔 IR sensor-based user detection
* 📧 Email notification system
* 🗄️ MySQL database integration

---

## 🏗️ System Architecture

The system consists of:

* **Raspberry Pi** → Main controller
* **Camera (USB)** → Barcode scanning
* **IR Sensors** → Detect issue/return action
* **LCD (16x2)** → Display messages
* **MySQL Database** → Store records

---

## 🔌 Hardware Requirements

* Raspberry Pi 4 Model B
* USB Camera
* IR Sensors (2)
* 16x2 LCD Display (I2C)
* Breadboard & Jumper Wires
* Power Adapter

---

## 💻 Software Requirements

* Python 3
* MySQL / MariaDB
* OpenCV
* Pyzbar
* RPi.GPIO
* RPLCD
* smbus2

---

## 📦 Libraries Used

```bash
opencv-python
pyzbar
mysql-connector-python
RPi.GPIO
pillow
RPLCD
smbus2
```

---

## 📂 Project Structure

```
Automated-Library-Management-System/
│
├── main.py
├── ProjectCode.py
├── NewLibrarySQL.ino
├── database.sql
├── requirements.txt
├── README.md
├── images/
```

---

## 🧠 Working Principle

### 📌 Book Issuing Process

1. User places hand near IR sensor
2. System activates camera
3. Book barcode is scanned
4. User ID card is scanned
5. Book is issued for 7 days
6. Database is updated
7. Confirmation shown on LCD

---

### 📌 Book Return Process

1. User selects return using IR sensor
2. Book barcode is scanned
3. User ID is verified
4. System checks due date
5. Fine is calculated if overdue
6. Database is updated
7. Status shown on LCD

---

## 🗄️ Database Design

### 📘 Book Table

* Book ID
* Book Name
* Availability
* Issued To
* Issue Date
* Return Date

### 👤 User Table

* User ID
* Name
* Email
* Issued Books Count
* Fine

---

## 🧾 Sample SQL Commands

* CREATE DATABASE
* CREATE TABLE
* INSERT / UPDATE / DELETE

---

## 📟 LCD Display Usage

The 16x2 LCD shows:

* "Scan Book"
* "Scan ID"
* "Book Issued"
* "Return Successful"
* "Fine Applied"

---

## ⚡ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Automated-Library-Management-System.git
cd Automated-Library-Management-System
```

### 2️⃣ Install Libraries

```bash
pip install -r requirements.txt
```

### 3️⃣ Setup Database

* Install MySQL/MariaDB
* Create database
* Import `database.sql`

### 4️⃣ Run Project

```bash
python main.py
```

---

## 📸 Output

(Add your project images here)

* Hardware setup
* LCD output
* Barcode scanning

---

## 🔧 Future Improvements

* Mobile App Integration
* Cloud Database
* Face Recognition
* Web Dashboard (Admin Panel)
* RFID instead of barcode

---

## 🧪 Test Cases

* Valid book issue
* Invalid barcode
* Late return fine
* Multiple book issue
* Wrong user scan

---

## ⚠️ Troubleshooting

* Camera not working → Check OpenCV installation
* LCD not displaying → Check I2C address
* Database error → Verify credentials
* IR sensor issue → Check GPIO pins

---

## 👨‍💻 Author

**Atharv**
Computer Science Engineering Student

---

## ⭐ Acknowledgement

This project is inspired by real-world automation systems and embedded IoT solutions.

---

## 📌 Conclusion

This project demonstrates:

* Embedded Systems
* Computer Vision
* Database Management
* Real-world automation

It is a complete smart system suitable for academic and practical applications.

---
