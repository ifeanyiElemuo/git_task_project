admin_username = 'admin'
admin_password = 'password'

username = input("Username: ").lower()
password = input("Password: ")

if username == admin_username and password == admin_password:
    print('\nLogin successful!')
else:
    print('\nLogin failed! Incorrect username or password.')
