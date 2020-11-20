'''
修改文件中的内容：
1、打开目标文件
2、以写的模式创建一个新文件
3、将目标文件的内容读出来改成新内容，写入新文件
4、将目标文件删除
5、将新文件重命名改成新文件
'''
import os
filepath = "E:\zyx"
with open(filepath+'\\'+'test.txt','w') as f :
    # content = f.read()
#     # print(content)
    # newcontent = content.replace('4','9')
    # print(newcontent)
    # f.seek(0)
    # f.write(newcontent)
    # f.write('333333333333333333')
    # print('seek:', f.tell())
    print(f.read())

    #f.write('11111111111111')
    # print('seek:',f.tell())
    f.seek(0)
    print(f.read())





