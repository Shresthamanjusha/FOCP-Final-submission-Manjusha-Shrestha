def change_password(username, current_password, new_password):
    # The 'passwd.txt' file is opened in read mode to read all lines
    with open('passwd.txt', 'r') as file:
        lines = file.readlines()
    
    # The 'passwd.txt' file is opened in write mode to overwrite with modified content
    with open('passwd.txt', 'w') as file:
        # Go through every line in the file one by one.
        for line in lines:
            # Split the line into fields using ':' as the delimiter
            fields = line.split(':')
            
        # Check if the username and current password are similar in the current line
            if fields[0] == username and fields[2].strip() == current_password:
                # If there is similarity, write the line with the new password
                file.write(f'{fields[0]}:{fields[1]}:{new_password}\n')
                print("Password changed.")
            else:
                # If there is no similarity, write the line back to the file unchanged
                file.write(line)

if __name__ == "__main__":
    # Get user input for the username, current password, new password, and password confirmation
    user_to_change = input("User:             ")
    current_password = input("Current Password: ")
    new_password = input("New Password:     ")
    confirm_password = input("Confirm:          ")
    
    # Check if the new password and confirmation match
    if new_password == confirm_password:
    # If they match, call the change_password function
        change_password(user_to_change, current_password, new_password)
    else:
    # If they don't match, print an error message
        print("Passwords do not match. No change made.")