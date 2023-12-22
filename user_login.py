# create admin account with admin username and password
admin_username = 'admin'
admin_password = 'password'

# for user log in, prompt user for username and password
username = input("Username: ").lower()
password = input("Password: ")

# check if user input matches the login parameters for admin
if username == admin_username and password == admin_password:
    print('\nLogin successful!')
else:
    print('\nLogin failed! Incorrect username or password.')
