from user import User

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
     