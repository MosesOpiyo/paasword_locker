import pyperclip

class User:
    """
     Class that generates new instances of users
    """
    user_list = []
    
    def save_user(self):

        '''
        save_password method saves password objects into password_list
        '''

        User.user_list.append(self)
    
    def delete_user(self):

        '''
        delete_password method deletes a saved passsword from the password_list
        '''

        User.user_list.remove(self)  

    def __init__(self,name,email,phone_number,password):

     self.name = name
     self.email = email
     self.phone_number = phone_number
     self.password = password


    @classmethod
    def find_by_number(cls,number):
          
          for user in cls.user_list:
            if user.phone_number == number:
                return user  
    
    @classmethod   
    def user_exist(cls,number):
        
        for user in cls.user_list:
            if user.phone_number == number:
                return True

        return False
    
    @classmethod
    def display_users(cls):
        '''
        method that returns the contact list
        '''
        return cls.user_list
    
    @classmethod
    def copy_email(cls,number):
           user_found = User.find_by_number(number)
           pyperclip.copy(user_found.email)
