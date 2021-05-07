from django.test import LiveServerTestCase
from selenium import webdriver # web driver module that allows test to interacting with chrome driver
from selenium.webdriver.common.keys import Keys



class NameFormTest(LiveServerTestCase):  
  #NameFormtest class will inherit methods from the LiverServerTestCase classes 
  
  #will launch live django server and once down teardown. Amid this selenium will excute the the series of functional test
  #emulating a users actions


  def testform(self):
    selenium = webdriver.Chrome()

    #This is used to select your url for your site which in this case is localhost 
    selenium.get('http://127.0.0.1:8000/')

    #find the html form element you need to submit with name. In this case "id_name" is way name need to inputted.
    name = selenium.find_element_by_id('id_name')
    
    #similar to above but finding the submit element
    submit = selenium.find_element_by_id('submit_button')

    #populate the form with name 
    name.send_keys('Raphael')

   

    #this line pushes the submit form button
    submit.send_keys(Keys.RETURN)

    #checking the result of redirect page /welcome; search page source looks at entire html document for "Lebron James"

    assert 'Raphael' in selenium.page_source

    