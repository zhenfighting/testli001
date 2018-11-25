"""
    目标：失败重试 插件
"""
import pytest
class Test04():
    def test_delete(self):
        print("删除成功")
    def test_get(self):
        print("查询成功")
        assert 0
    def test_put(self):
        print("修改成功")
    def test_post(self):
        print("新增成功")