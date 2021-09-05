import unittest
from user import User
from credentials import Credentials
import pyperclip 

class TestUser(unittest.TestCase):
    
    def setUp(self):
      
      self.new_user = User("James","james@ms.com","0712345678","james@ms2021") # create password object
      self.new_details = Credentials("Iam a 20 yaer old man.Happy to be alive.")

    def test__init(self):
        
        self.assertEqual(self.new_user.name,"James")
        self.assertEqual(self.new_user.email,"james@ms.com")
        self.assertEqual(self.new_user.phone_number,"0712345678")
        self.assertEqual(self.new_user.password,"james@ms2021")
        self.assertEqual(self.new_details,"Iam a 20 yaer old man.Happy to be alive.")
    
    def tearDown(self):
            
            User.user_list = []

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    def test_save_details(self):
        self.new_details.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_users(self):
        self.new_user.save_user()
        test_user = User("user","test@user.com","0711223344","testuser@2021")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)   
    def test_save_multiple_details(self):
        self.new_details.save_credentials()
        test_details = Credentials("this is a user detail")  
        test_details.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2) 

    def test_delete_user(self):
        self.new_user.save_user()
        test_user = User("user","test@user.com","0711223344","testuser@2021")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)
    def test_delete_details(self):
        self.new_details.save_credentials()
        test_details = Credentials("this is a user detail") 
        test_details.save_credentials()
        self.new_details.delete_details()
        self.assertEqual(len(Credentials.credentials_list),1)


    def test_find_contact_by_number(self):
         
         self.new_user.save_user()
         test_user = User("user","test@user.com","0711223344","testuser@2021") # new contact
         self.new_details.save_credentials()
         test_details = Credentials("this is a user detail") 
         test_user.save_user()

         found_contact = User.find_by_number("0711223344")

         self.assertEqual(found_contact.email,test_user.email)    

    def test_user_exist(self):
        self.new_user.save_user()
        test_user = User("user","test@user.com","0711223344","testuser@2021") # new contact
        test_user.save_user()

        user_exists = User.user_exist("0711223344")
        self.assertTrue(user_exists)
    
    def test_display_all_users(self):
          self.assertEqual(User.display_users(),User.user_list)

    def test_copy_email(self):  
          self.new_user.save_user()
          User.copy_email("0711223344")

          self.assertEqual(self.new_user.email,pyperclip.paste())    

if __name__== '__main__':
    unittest.main()