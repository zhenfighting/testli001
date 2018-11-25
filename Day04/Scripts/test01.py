import pytest


class Test01():
    def test001(self):
        print("test001被执行")
    def tesat002(self):
        print("test002被执行")
        # assert 0

# 以下运行方式 只是作为调试使用
if __name__ == '__main__':
    pytest.main("-s test01.py")

    """
        运行结果：
            . ：为成功
            F ：失败
    """