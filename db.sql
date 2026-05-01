-- ================================
-- 1. CREATE DATABASE
-- ================================
CREATE DATABASE IF NOT EXISTS library;
USE library;

-- ================================
-- 2. USERS TABLE
-- ================================
CREATE TABLE IF NOT EXISTS usersdatabase (
    lid VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    issued INT DEFAULT 0,
    fine FLOAT DEFAULT 0
);

-- ================================
-- 3. BOOKS TABLE
-- ================================
CREATE TABLE IF NOT EXISTS bookdatabase (
    uid VARCHAR(50) PRIMARY KEY,
    bookname VARCHAR(255) NOT NULL,
    available INT DEFAULT 1,
    issuedto VARCHAR(50),
    issuedate DATETIME,
    returndate DATETIME,

    CONSTRAINT fk_user
    FOREIGN KEY (issuedto)
    REFERENCES usersdatabase(lid)
    ON DELETE SET NULL
);

-- ================================
-- 4. INSERT SAMPLE USERS
-- ================================
INSERT INTO usersdatabase (lid, name, email) VALUES
('U001', 'Atharv', 'atharv@gmail.com'),
('U002', 'Rahul', 'rahul@gmail.com'),
('U003', 'Sneha', 'sneha@gmail.com');

-- ================================
-- 5. INSERT SAMPLE BOOKS
-- ================================
INSERT INTO bookdatabase (uid, bookname) VALUES
('B001', 'Python Programming'),
('B002', 'Data Structures'),
('B003', 'Operating Systems'),
('B004', 'Computer Networks');

-- ================================
-- 6. TEST QUERIES
-- ================================
-- View all users
SELECT * FROM usersdatabase;

-- View all books
SELECT * FROM bookdatabase;

-- ================================
-- 7. ISSUE BOOK (MANUAL TEST)
-- ================================
-- Example: Issue B001 to U001
UPDATE bookdatabase
SET available = 0,
    issuedto = 'U001',
    issuedate = NOW(),
    returndate = DATE_ADD(NOW(), INTERVAL 7 DAY)
WHERE uid = 'B001';

-- Increase issued count
UPDATE usersdatabase
SET issued = issued + 1
WHERE lid = 'U001';

-- ================================
-- 8. RETURN BOOK (MANUAL TEST)
-- ================================
-- Example: Return B001
UPDATE bookdatabase
SET available = 1,
    issuedto = NULL,
    issuedate = NULL,
    returndate = NULL
WHERE uid = 'B001';

-- Decrease issued count
UPDATE usersdatabase
SET issued = issued - 1
WHERE lid = 'U001';

-- ================================
-- 9. CHECK OVERDUE (OPTIONAL)
-- ================================
SELECT * FROM bookdatabase
WHERE returndate < NOW();