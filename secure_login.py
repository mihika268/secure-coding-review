import hashlib

# Store user credentials securely (hashed password)
users = {
    "admin": hashlib.sha256("admin123".encode()).hexdigest()
}

# Take user input
username = input("Enter username: ")
password = input("Enter password: ")

# Hash the entered password
hashed_input = hashlib.sha256(password.encode()).hexdigest()

# Validate login securely
if username in users and users[username] == hashed_input:
    print("✅ Login successful!")
else:
    print("❌ Invalid credentials.")
