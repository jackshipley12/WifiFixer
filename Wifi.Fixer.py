# we need to know everything
# terminal cod: sudo service network-manager restart

#import os
#os.system("sudo service network-manager restart")

connection_status = input("Do you want to rest internet? Please answer with 'Y' or 'N': ")
print(connection_status)

user_response = input()

if user_respone == 'Y':
    import os
    os.system("sudo service network-manager restart")