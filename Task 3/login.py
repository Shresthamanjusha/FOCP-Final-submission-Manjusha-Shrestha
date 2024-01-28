def login(username, password):
    # The 'passwd.txt' file is opened  in read mode
    with open('passwd.txt', 'r') as file:
        # Go through every line in the file one by one.
        for line in file:
            # Use ':' as the delimiter to divide the line into fields.
            fields = line.split(':')            
            # Verify if the username and password are similar in the current line
            if fields[0] == username and fields[2].strip() == password:
            # If there is similar, return True indicating successful login
                return True
    
    # If no similar username and password are found, return False
    return False

if __name__ == "__main__":
    # Get user input for login credentials
    login_username = input("User:     ")
    login_password = input("Password: ")
    
    # Call the login function to check the credentials
    if login(login_username, login_password):
        # If login is successful, print "Access granted."
        print("Access granted.")
    else:
        # If login fails, print "Access denied."
        print("Access denied.")