from user import User

class Credentials:
     """
     Class that generates new instances of credentials
     """
     credentials_list = []
     def save_credentials(self):


        Credentials.credentials_list.append(self)

     def delete_details(self):

        
        Credentials.credentials_list.remove(self)  
     
     def __init__(self,details):
         self.details = details

     @classmethod
     def find_by_details(cls,number):
          
          for detail in cls.credentials_list:
           for user in cls.user_list:
            if user.phone_number == number:
                return detail
