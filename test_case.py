from login import get_username,get_password
def test_login_username():
    #预期结果：自己登录的账号
    expect_username = 'test01'
    #实际结果：显示再页面上的账号
    acult_username = get_username()

    assert expect_username == acult_username

def test_login_password():
    #预期结果：自己登录的账号
    expect_password = 'test01'
    #实际结果：显示再页面上的账号
    acult_password =get_password()

    assert expect_password == acult_password
