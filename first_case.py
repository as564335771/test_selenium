

class FirstCase(object):
    def test_login_email_error(self):
        login('34',111)

    def test_login_username_error(self):
        login('34', 111)

    def test_login_code_error(self):
        login('34', 111)

    def test_login_success(self):
        login('34', 111)
