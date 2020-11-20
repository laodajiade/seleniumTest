import unittest
# 1、编写测试用例
# 2、构造套件
# 3、将单个测试用例添加到套件
# 4、运行套件

# 优化测试用例，同一个类中，test开头的函数就是一个用例
class My(unittest.TestCase):
    def setUp(self):
        self.source = 'selenium'

    def testBlank(self):
        expect = 'selen ium'
        result = expect.replace(" ","")
        self.assertEqual(self.source,result)
        print('testBlank测试完成')
    def testBlankOrd(self):
        expect = 'selenium*'
        result = expect.replace("*","")
        self.assertEqual(self.source,result)
        print('testBlankOrd测试完成')

if __name__ == '__main':
    my = My()
    myTestSuite = unittest.TestSuite()
    myTestSuite.addTest(my('testBlank')) #套件中添加用例
    myTestSuite.addTest(my('testBlankOrd')) #套件中添加用例
    # TestRunner 类作为测试用例的基本执行环境,来驱动整个单元测试过程，
    # 单元测试时一般不直接使用 TestRunner 类，而是使用其子类 TextTestRunner 来完成测试，
    runner = unittest.TextTestRunner()
    #runner = unittest.TestRunner
    # 运行套件
    runner.run(myTestSuite)