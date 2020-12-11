from HTMLTestRunner import HTMLTestRunner
import unittest
suite = unittest.TestLoader().discover('.',pattern='test*.py')

#runner = unittest.TextTestRunner()
#runner.run(suite)

test_report = 'test_report.html'
with open(test_report,'wb')as f:
    runner = HTMLTestRunner(f,title='测试报告',description='当前版本：v1.0')
    runner.run(suite)