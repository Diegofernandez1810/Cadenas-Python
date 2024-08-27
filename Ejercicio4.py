phone_number = input("Enter the phone number in the format prefix-number-extension: ")

components = phone_number.split('-')

number = components[1]

print(f"The phone number without the prefix and extension is: {number}")
