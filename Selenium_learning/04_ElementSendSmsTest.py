from selenium import webdriver
from time import sleep
import unittest


class SendMsgCase(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.get('https://h5.ele.me/login/#redirect=https%3A%2F%2Fwww.ele.me%2Fhome%2F')
        self.dr.implicitly_wait(10)

    #   封装CSS定位方法
    def by_css(self, css):
        return self.dr.find_element_by_css_selector(css)

    #   手机号码输入框定位
    def mobile_phone_input_box(self):
        return self.by_css('[type = "tel"]')

    #  【免费获取验证码】按钮定位
    def send_msg_button(self):
        return self.by_css('.CountButton-3e-kd')

    #   获取 发送验证码成功 文本信息
    def send_msg_successful_text(self):
        return self.by_css('#registerContainer > div > div.codeSendHint').text

    #   发送验证码
    def send_msg(self, mobile_phone):
        self.mobile_phone_input_box().send_keys(mobile_phone)
        self.send_msg_button().click()

    #   测试用例
    def test_send_msg_button(self):
        # 发送验证码
        self.send_msg('178****5756')
        sleep(2)

        #   验证【免费获取验证码】按钮 被禁用
        self.assertFalse(self.send_msg_button().is_enabled())

        # 期望结果
        expected_result = '已发送'

        # 预期结果
        actual_result = self.send_msg_button().text

        # 验证 实际结果包含预期结果 “已经发送”
        self.assertTrue(expected_result in actual_result)

    def test_login_with_smscode(self):
        # 连接到redis服务器取出smscode，点击登陆 获取状态返回码是否正确
        pass

    def tearDown(self):
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
