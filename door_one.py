names = ['jaime', 'tammy', 'sandra', 'sarah', 'anthony']
password = "jaimet33"

your_name = (input("Please enter your name: "))

while your_name not in names:
    new_name = (input("I don't know you, Enter your name to be appended to the club: "))
    names.append(new_name)
    print("Name successfully appended!")
    pass_in = (input("what is the password? "))
    if pass_in != password:
        print("Incorrect Password, try again")
        continue
    elif pass_in == password:
        break

while your_name in names:
    pass_in = (input("what is the password? "))
    if pass_in != password:
        print("Incorrect Password, try again")
        continue
    elif pass_in == password:
        break
print("Access Granted, now at: door two")
import door_two.py
