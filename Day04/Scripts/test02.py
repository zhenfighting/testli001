"""
    特殊函数：setup/teardown
    级别：函数级别、类级别
    函数级别：
        1. setup
            机制：测试函数运行之前首先被执行
        2. teardown
            机制：函数运行之后被执行
    类级别：
        1. setup_class
            机制：类运行之前首先会被执行
        2. teardown_class
            机制：类运行之后会被执行

    注意：pytest对于特殊函数是区分大小写，只能小写 (setup\teardown setup_class\teardown_class)
"""

class TAest02():
    # 类级别
    def setup_class(self):
        print("setup_class被执行")
    def teardown_class(self):
        print("teardown_class被执行")

    # 函数级别
    def setup(self):
        print("setup被执行")
    def teardown(self):
        print("teardown被执行")

    def test01(self):
        print("test01被执行")

    def test02(self):
        print("test02被执行")
    def test_login(self):
        print("test_login被执行")
    def iweb_login(self):
        print("iweb_login被执行")

