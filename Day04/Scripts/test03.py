"""
    目标：改变函数运行顺序 插件
    需求：
        执行顺序修改为：增、改、查、删
"""
import pytest


class Test04():
    @pytest.mark.run(order=4)
    def test_delete(self):
        print("删除成功")
    @pytest.mark.run(order=3)
    def test_get(self):
        print("查询成功")
    # @pytest.mark.run(order=-3)
    def test_put(self):
        print("修改成功")
    @pytest.mark.run(order=1)
    def test_post(self):
        print("新增成功")