from base.find_element import FindElement


class RegisterPage(object):
    def __init__(self,driver):
        self.fd = FindElement(driver)
    def get_email_element(self):
        return self.fd.get_element('user_name')