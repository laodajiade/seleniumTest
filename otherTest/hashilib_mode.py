import hashlib
'加密'
def get_md5(passwd):
    m = hashlib.md5()
    m.update(passwd.encode('utf-8'))
    return m.hexdigest()

def register():
    username = input('请输入用户名：').strip()
    passwd = input('请输入密码：').strip()
    '加密'
    passwd_md5 = get_md5(passwd)
    '写入文件'
    with open('a.txt',mode='at',encoding='utf-8') as f:
        f.write('\n'+f'{username}|{passwd_md5}')

def login():
    with open('a.txt',mode='rt',encoding='utf-8') as f:
        print('login----------------------------')
        username = input('请输入用户名：').strip()
        passwd = get_md5(input('请输入密码：').strip())
        temp = f'{username}|{passwd}'
        for item in f:
            if temp == item:
                print('登录成功')
        #     temp = item.split('|')
        #     for i in range(len(temp)-1):
        #         usernametemp = temp[0]
        #         passwdtemp = temp[1]
        #         if usernametemp==username and passwdtemp==passwd:
        #             print('登录成功')
login()