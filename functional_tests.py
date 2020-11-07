from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser =webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Jane has heard about a cool new online todo app and she goes to check out the homepage
        self.browser.get('http://localhost:8000')
        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do' ,self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        #Jane is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        # Jane types  "Buy groceries" into a text box
        inputbox.send_keys('Buy groceries')
        # When she hits enter,the page updates,and now the page lists
        # "1: Buy groceries" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text=='1: Buy groceries' for row in rows))
        #There is still a text box inviting jane to add another item.
        # She enters "Book dentist appointment"

        self.fail('Finish the test!')

        # The page updates again, and now shows both items on her list.




if __name__=='__main__':
    unittest.main()
