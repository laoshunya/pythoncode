# 字符串

a ='小刘'
b = "小胡"
c = """小谷"""

print(a)
print(a+"喜欢"+b)

d = "小谷今年13岁了，他喜欢小胡"
# 字符串长度
print(len(d))
# 格式化
e = '{}喜欢{}'.format(a,c)
print(e)
e1 = '小谷今年{}岁了，他喜欢{}'.format(14,c)
print(e1)
f = "小谷今年%d岁了，他喜欢%s"%(13,b)
print(f)
# 查找字符串是否包含某个字符串
g1 = d.find(a)
print(g1)
g2 = d.find(b)
print(g2)
# 把字符串中的 old（旧字符串） 替换成 new(新字符串)
h1 = d.replace(c,b)
print(h1)

# 获取下标
# g3 = d.index(a)
# print(g3)
g4= d.index(b)
print(g4)