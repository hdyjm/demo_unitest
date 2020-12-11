import unittest
from login import get_username,get_password
#使用Testase
class TestLogin(unittest.TestCase):

    #初始化用例

    def setUp(self) -> None:
        print('每次执行用例前执行')

    #清空方法
    def tearDown(self) -> None:
        print('每次执行完用例执行')
    def test_login_username(self):
        print('获取用户名测试用例')
        # 预期结果：自己登录的账号
        expect_username = 'test01'
        # 实际结果：显示再页面上的账号
        acult_username = get_username()
        self.assertEqual(expect_username,acult_username)

        #assert expect_username == acult_username

    def test_login_password(self):
        print('获取密码测试用例')
        # 预期结果：自己登录的账号
        expect_password = 'test01'
        # 实际结果：显示再页面上的账号
        acult_password = get_password()
        self.assertEqual(expect_password,acult_password)

       # assert expect_password == acult_password

#unittest.main()
#创建一个测试套件
#suite = unittest.TestSuite()

#suite.addTest(TestLogin('test_login_username'))
#suite.addTest(TestLogin('test_login_password'))

#lst = [TestLogin('test_login_username'),TestLogin('test_login_password')]
#suite.addTests(lst)
suite = unittest.TestLoader().discover('.',pattern='test*.py')
runner = unittest.TextTestRunner()
runner.run(suite)
