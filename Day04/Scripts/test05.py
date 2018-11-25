import pytest
"""
    目标：学习fixture

    1. 将普通函数修饰成 工厂函数
       操作：在普通函数之上 使用@pytest.fixture()进行修饰，就是工厂函数(另类的setup)
"""

# 设置工厂函数
@pytest.fixture(autouse=True)
def before():
    print("before被执行")
# 通过函数形式来运行fixture
# @pytest.mark.usefixtures("before")
class Test04():
    def test_delete(self):
        print("删除成功")
    # 通过参数方式 运行 fixture
    # def test_get(self,before):
    #     print("查询成功")
    # 通过函数形式运行 fixture
    def test_put(self):
        print("修改成功")
    def test_post(self):
        print("新增成功")