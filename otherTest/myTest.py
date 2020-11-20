#
# #
# # result = [i**2 for i in range(1,11)]
# # result1 = [i for i in range(101) if i%2==0]
# # result2 = [f'第{i}个' for i in range(1,101)]
# #
# # myString = """
# # for i in range(5):
# #     print(i)
# # """
# # exec(myString)
# #
# # x = 10
# # expr = """
# # z = 30
# # sum = x + y + z
# # print(sum)
# # """
#
# # x = 10
# # expr = """
# # z = 30
# # sum = x + y + z
# # print(sum)
# # """
# # def func():
# #     y = 20
# #     exec(expr)
# #     #exec(expr, {'x': 1, 'y': 2})
# #     exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})
# #
# # func()
# # f = lambda a,b:max(a,b)
# # print(f(4,1))
# #
# # from functools import reduce
# # def func(x,y):
# #     return x+y
# # l = reduce(func,[11,2,3,4])
# # print(l)
# # print(l)
# #
# # def testF():
# #     myList=[]
# #     def testC(args):
# #         myList.append(args)
# #         return myList
# #     return testC
# #
# # temp = testF()
# # print(temp(100))
# # print(temp(300))
#
# # def testF(a,b):
# #     def testC():
# #         print(a+1)
# #         print(b+1)
# #     return testC()
# # a = 2
# # b = 3
# # __all__ = [b]
# # print(testF(a,b))
# # print(a)
# from functools import wraps
#
# mykey = False
# def testF(f):
#     def testC(*args,**kwargs):
#         if mykey:
#             result = f(*args, **kwargs)
#             return result
#         else:
#             chose = input("请输入字母y进行会议总结：").upper()
#             if chose == 'Y':
#                 print('动物们正在总结发言')
#                 mykey = True
#                 result = f(*args, **kwargs)
#                 return result
#             else:
#                 print("会议继续")
#     return testC
#
#
# @testF
# def animalAction():
#     print("蚂蚁正在搬家")
# @testF
# def catAction():
#     print("狗在乱吠")
#
# animalAction()
# catAction()
#
# import sys
# print(sys.path)
# if __name__ == '__main__':
#     print('测试')


import pickle
dic = {'one':1,'two':2}
bys = pickle.dumps(dic)
print(bys)
print(type(bys))
bysTo = pickle.loads(bys)
print(bysTo)