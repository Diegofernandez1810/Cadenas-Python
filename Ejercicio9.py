birthdate = input("Enter your birthdate in the format dd/mm/yyyy: ")

day, month, year = birthdate.split('/')

print(f"Day: {day.zfill(2)}")
print(f"Month: {month.zfill(2)}")
print(f"Year: {year}")
