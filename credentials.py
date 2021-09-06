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
     
     def __init__(self,platform_name,username,password):

      self.platform_name = platform_name
      self.username = username
      self.password = password

      
     @classmethod
     def find_by_number(cls,number,detail):
          
          for user in cls.user_list:
            if user.phone_number == number:
                for detail in cls.credentials_list:
                 return detail  
    
     @classmethod   
     def user_exist(cls,number):
        
        for user in cls.user_list:
            if user.phone_number == number:
                return True

        return False
    
     @classmethod
     def display_details(cls,detail):
        '''
        method that returns the contact list
        '''
        return cls.credentials_list
     