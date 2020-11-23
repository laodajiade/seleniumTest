import re

#print(re.match('www','www.baidu.com'))
# print(re.match('www','baidu.www.com'))  #.span()表示从起始位置开始匹配
# print(re.search('www','baidu.www.com'))
# print(re.findall('www','baidu.www.www.com'))
# patten = re.compile('<.*?>')
# result = patten.findall('<a> b <c>')
# print(result)
# patten1 = re.compile(r'(a{6})*')
# result1 = patten1.findall("abaabaaabaaaabaaaaabaaaaaaba")
# print(result1)
# result2 = re.findall(r'.', "hello 2 I'm a 32 str12312ing 30")
# print(result2)

# result1 = re.findall('foo.$','foo1\nfoo2\n')
# print(result1)
# result2 = re.findall('<.*?>?','<aaaaa>b<ccccccc>')
# print(result2)

# result3 = re.findall('a{0,5}?','bcdefaaaabbbbbb')
# print(result3)

# result4 = re.findall('^[321]','123456')
# print(result4)

# result5 = re.findall('a|bbb','44444bbbbbccccccaaa')
# result6 = re.search('a|bbb','44444bbbbbccccccaaa')
# print(result5)

# pam = r'(.+) \1'
# result6 = re.findall(pam,'com the the com www  www')
# print(result6)
#
# fla = r'(\d+)\1'
# result7 = re.findall(fla,'com the the com 77e77 77')
# print(result7)

strings = 'Words, words, words.'
stringsItem = re.split(r'\b', strings)
print(stringsItem)

print('添加一个代码更改')

print('添加第二个代码更改')