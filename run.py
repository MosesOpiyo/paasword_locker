#!/usr/bin/env python3.8
from user import User
from credentials import Credentials

def create_user(name,email,phone_number,password):
    '''
    Function to create a new contact
    '''
    new_user = User(name,email,phone_number,password)
    return new_user
def create_credentials(platform_name,username,user_password):
    new_credential = Credentials(platform_name,username,user_password)
    return new_credential

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()
def save_credentials(credential):
    credential.save_credential()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
def del_credential(credential):
    credential.delete_credential()

def find_user(number):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_number(number)
def find_credential(username):
    return Credentials.find_by_platform_name(username)

def check_existing_user(number):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.user_exist(number)
def check_credential_exists(username):
    return Credentials.credential_exist(username)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()
def display_credentials():
    return Credentials.display_credentials()


def main():
    print("Welcome to the user list.What is your name?")
    user_name = input()
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
            print("Use these short codes : cu - create a new user, du - display user, fu -find a user, ex -exit the user list ")

            short_code = input().lower()

            if short_code == 'cu':
                print("New User")
                print("-"*10)

                print ("Name ....")
                Name = input()

                print ("Email ....")
                Email = input()

                print ("Phone number ....")
                Phone_number = input()

                print ("Password ....")
                Password = input()

                print("platform name .....")
                platform_name = input()

                print("Username in the platform ....")
                username = input()

                print("Your platform password ....")
                user_password = input()


                save_users(create_user(Name,Email,Phone_number,Password,platform_name,username,user_password)) # create and save new contact.
                print ('\n')
                print(f"New User {Name} created")
                print ('\n')

            elif short_code == 'du':
                 if display_users():
                    print("Here is a list of all your users")
                    print('\n')

                    for user in display_users():
                        print(f"{user.name} {user.email} ..{user.phone_number}")
                    for credential in display_credentials():
                        print(f"{credential.username} {credential.platform_name} {credential.user_password}")
                    

                    print('\n')
                 else:
                        print('\n')
                        print("You dont seem to have any users saved yet")
                        print('\n')

            elif short_code == 'fu':
                        print("Enter the number you want to search for")

                        search_number = input()
                        if check_existing_user(search_number):
                                    search_user = find_user(search_number)
                                    print(f"{search_user.name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_user.phone_number}")
                                    print(f"Email address.......{search_user.email}")
                                    print("Enter username in the platform")

                                    search_username = input()

                                    if check_credential_exists(search_username):
                                        search_name = find_credential(search_username)
                                        print(f"{search_name.username}")
                                        print('-'*10)
                                        print(f"platform name......{search_name.platform_name}")
                                        print(f"platform password.....{search_name.user_password}")


                        else:
                                    print("That contact does not exist")
                        

            elif short_code == "ex":
                            print("Bye .......")
                            break

            else:
                            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()