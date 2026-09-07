
username = input("Username:")
password = input("Password:")
if username == 'admin' and password == 'admin123':
    print("Login Sucessful")
else:
    print("Invalid Credentials")


bill = int(input("Enter the bill:"))
if bill > 99:
    print("Final Bill:", bill)
else:
    print("Final Bill:",bill+30)