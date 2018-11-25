"""
    目标：基于pytest实现参数化
    语法：@pytest.mark.parametrize("参数名",[参数值])
        参数名：无论多少个必须为一个字符串
            1). 单个参数：参数名必须为字符串
            2). 多个参数：首先必须为一个字符串，参数名之间使用逗号分隔 如："username,password..."
        参数值：值的格式必须为列表-无论多少个参数多个值
            1). 单个参数值：直接为列表即可，如果有多个值，使用逗号分隔；
            2). 多个参数值：首先指的格式为列表，列表嵌套元祖，如：[("第一轮参数1的值","第一轮参数2的值"),("第二轮参数1的值","第二轮参数2的值")]
    注意：
        1. parametrize无法通过助写完成，必须手动编写或粘贴。
        2. 参数引用的时候必须和参数化定义的名称一致。

"""
import pytest

def get_data():
    return [("admin","123456","登录成功"),("user01","234567","登录失败")]

class Test05():
    # 单个参数名参数化使用方式
    # @pytest.mark.parametrize("username",["admin"," admin01","user01不存在"])
    # def test_login(self,username):
    #     print("用户名为：",username)
    # 多个参数名使用方式
    @pytest.mark.parametrize("username,password,expect_result",get_data())
    def test_login(self,username,password,expect_result):
        print("用户名为：",username)
        print("密码为：",password)
        print("预期结果为：",expect_result)