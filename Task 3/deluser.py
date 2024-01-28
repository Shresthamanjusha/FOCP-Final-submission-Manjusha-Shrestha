def delete_user(username):
    # The 'passwd.txt' file is opened in read mode to read all lines
    with open('passwd.txt', 'r') as file:
        lines = file.readlines()

    # The 'passwd.txt' file is opened in write mode to overwrite with modified content
    with open('passwd.txt', 'w') as file:
        # Go through every line in the file one by one.
        for line in lines:
        # Check if the current line does not start with the specified username
            if not line.startswith(username + ":"):
        # If it doesn't start with the username, write the line back to the file
                file.write(line)

    print("User Deleted.")

if __name__ == "__main__":
    # acquire user input for the username to be deleted
    delete_username = input("Enter username: ")
    
    # Call the delete_user function with the specified username
    delete_user(delete_username)