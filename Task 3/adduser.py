def add_user(username, real_name, password):
    # 'passwd.txt' file is opened in append mode and the new user information is written
    with open('passwd.txt', 'a') as file:
        file.write(f'{username}:{real_name}:{password}\n')
    print("User Created.")

if __name__ == "__main__":
    # obtain user input for new user information
    new_username = input("Enter new username: ")
    new_real_name = input("Enter real name: ")
    new_password = input("Enter password: ")
    
    # 'passwd.txt' file is opened in read mode to verify for existing usernames
    with open('passwd.txt', 'r') as file:
    # Extract existing usernames from every line in the file
        existing_users = [line.split(':')[0] for line in file.readlines()]
        
    # verify if the new username already exists
    if new_username in existing_users:
        print("Cannot add. Most likely username already exists.")
    else:
    # If the username is not already in use, include the new user
        add_user(new_username, new_real_name, new_password)