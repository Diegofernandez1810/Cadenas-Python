email = input("Enter your email address: ")

username = email.split('@')[0]

new_email = f"{username}@ceu.es"

print(f"Your new email address is: {new_email}")
