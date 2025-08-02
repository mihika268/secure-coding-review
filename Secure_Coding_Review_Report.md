# Secure Coding Review Report 

## Overview

This report outlines the security vulnerabilities identified in a simple Python-based login system and the steps taken to remediate them. The goal was to compare insecure coding practices with secure implementations.

## Application Details

- Language: Python 3
- Application Type: Command-line login system

## Vulnerabilities Identified

1. **Plain-text password storage**  
   - The original code stored passwords directly in the script.
   - This exposes sensitive information if the code is accessed or shared.

2. **No password hashing**  
   - Passwords were compared in plain text, making the system vulnerable to data leaks.

3. **Hardcoded credentials**  
   - Usernames and passwords were hardcoded, limiting scalability and security.

## Remediation Steps

- Passwords are now hashed using SHA-256 with Python's `hashlib` library.
- Removed all hardcoded sensitive data from logic.
- Implemented hashed comparison instead of plain-text validation.

## Files Submitted

- vulnerable_login.py
- secure_login.py
- README.md
- Secure_Coding_Review_Report.md
- screenshots/ folder with login outputs

---

Prepared by: Mihika Pal  
Task:        Secure Coding Review  
Internship:  CodeAlpha Cybersecurity
