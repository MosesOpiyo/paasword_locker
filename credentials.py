from user import User
import random
import string

class Credentials:
     """
     Class that generates new instances of credentials
     """
     credentials_list = []
     def save_credentials(self):


        Credentials.credentials_list.append(self)

     def delete_credentials(self):

        
        Credentials.credentials_list.remove(self)  
     
     def __init__(self,platform_name,username,user_password):

      self.platform_name = platform_name
      self.username = username
      self.user_password = user_password

      
     
     @classmethod
     def find_by_platform_name(cls,username):
          
          for credential in cls.credentials_list:
            if credential.username == username:
                return credential  

     @classmethod   
     def credential_exist(cls,username):
        
        for credential in cls.credentials_list:
            if credential.username == username:
                return True

        return False
    
     @classmethod
     def display_credentials(cls):
        '''
        method that returns the contact list
        '''
        return cls.credentials_list
     @classmethod
     def password_generator(cls,length):
        """
        this method generates a random password with letters, symbols and digits
        Args: 
            length: This is the desired length of the password
        """
        characters = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        return "".join(random.choice(characters) for i in range(length))