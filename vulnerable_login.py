# Vulnerable Login System (no hashing, hardcoded credentials)
users = {"admin": "admin123"}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login successful!")
else:
    print("Invalid credentials.")
