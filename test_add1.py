from parameterized import parameterized
import unittest


# 实现加法的方法
def add(x, y):
    return x + y
test_data = [(1,1,2),(1,0,1),(-1,2,1),(0,0,0)]

class TestAdd(unittest.TestCase):
    @parameterized.expand(test_data)

    def test_add(self,a,b,result):
        res = add(a,b,)
        self.assertEqual(res,result)









if __name__ == '__main__':
    unittest.main()