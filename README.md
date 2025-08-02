# Secure Coding Review – CodeAlpha Cybersecurity Internship (Task 3)

This repository contains a code review of a basic login system developed in Python. The objective of this task is to identify and address security vulnerabilities in a simple authentication program by comparing an insecure version with an improved secure version.

## Files Included

- `vulnerable_login.py`: Basic login system with insecure practices such as plain-text password storage.
- `secure_login.py`: A more secure version of the login system using password hashing.
- `Secure_Coding_Review_Report.md`: Documentation of identified issues and recommended fixes.
- `screenshots/`: Folder containing screenshots of both successful and failed login attempts.

## How to Run

Both Python files can be executed from a terminal. The user will be prompted to enter a username and password. Based on the correctness of the input, the script will return either a login success or failure message.

## Test Cases

| Username | Password   | Output             |
|----------|------------|--------------------|
| admin    | admin123   | Login successful   |
| admin    | wrongpass  | Invalid credentials|
| user     | admin123   | Invalid credentials|

## Summary of Findings

The initial version of the login system contained multiple security risks including hardcoded credentials, no password hashing, and no input sanitization. These were addressed in the secure version using Python's `hashlib` module for hashing and better coding practices.

---

Prepared by: Mihika Pal  
Internship:  CodeAlpha Cybersecurity  
Task:        Secure Coding Review 

