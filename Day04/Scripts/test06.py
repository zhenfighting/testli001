import pytest
"""
    目标：学习@pytest.fixture(参数)
    
"""

# 设置工厂函数
# @pytest.fixture(scope="class",autouse=True,params=[1,2,3])
# @pytest.fixture(params=[1,2,3,4])
@pytest.fixture(scope="module")
def before():
    return "hello"

class Test04():
    def test_delete(self):
        print("删除成功")
    def test_get(self,before):
        print("查询成功",before)
    def test_put(self):
        print("修改成功")
    def test_post(self):
        print("新增成功")