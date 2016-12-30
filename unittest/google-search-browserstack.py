import sys
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

try:
    USERNAME = sys.argv[1]
    BROWSERSTACK_ACCESS_KEY = sys.argv[2]
except IndexError:
    print("Please provide the username and browserstack access key as command line arguments.")
    sys.exit(1)

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        url = "http://%s:%s@hub.browserstack.com/wd/hub" %(
            USERNAME, BROWSERSTACK_ACCESS_KEY
        )

        self.driver = webdriver.Remote(
            command_executor=url,
            desired_capabilities=DesiredCapabilities.FIREFOX
        )

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.google.com")
        elem = driver.find_element_by_name("q")
        elem.send_keys("selenium")
        elem.submit()
        self.assertIn("Google", driver.title)

        def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
    unittest.main(argv=sys.argv[:1])
