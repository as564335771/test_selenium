from handle.register_handle import RegisterHandle


class RegisterBusiness(object):
    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)
    #执行操作
    def login(self):
        self.register_h.send_user_email()
        if self.register_h.get_user_text('请输入有效的电子邮件地址'):
            print('邮箱检验成功')
            return True

        elif self.register.get_user_text('字符长度大于4'):
            print('用户名检验成功')
        self.register.send_user_name(name)
        self.register.send_user_password(password)
        self.register.send_user_name(code)

