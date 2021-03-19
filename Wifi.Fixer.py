

import os

user_input = input("Do you want to rest internet? Please answer with 'Y' or 'N': ")
print(user_input)

if user_input == "Y":
    os.system("sudo service network-manager restart")
    print("Wifi Reset.")
elif user_input == "N":
    print("Okay.")
else:
    print("Please enter 'Y' or 'N'")

