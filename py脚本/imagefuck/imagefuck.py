from PIL import Image
pic = Image.open("ffflag.png")
w,h = pic.size[0],pic.size[1]
print(w,h)
s = ['']*34*30
f=0
for i in range(h):
    for j in range(w):
        s[f] = pic.getpixel((j,i))
        f += 1
print(s)
count = {}
for item in s:
    count[item] = count.get(item, 0) + 1
print(count)#计算出每种RGB的出现的次数
#{(0, 0, 0, 0): 1, (0, 255, 0, 255): 427, (255, 255, 0, 255): 38, (0, 128, 0, 255): 211, (255, 0, 0, 255): 76, (128, 0, 0, 255): 76, (128, 128, 0, 255): 38, (0, 255, 255, 255): 34, (0, 128, 128, 255): 32, (0, 0, 255, 255): 64, (178, 34, 34, 255): 23}
#其中[]和<>应该相等，去生成一个ctfshow{之后发现规律
print(s[2])
flag = ""
t = 0
for i in range(h):
    for j in range(w):
        if(i%2==0):#一排排扫过去发现不对，对比之后发现应该是S型，只需要判断高度为单双数即可
            s = pic.getpixel((j,i))
        else:
            s = pic.getpixel((29-j,i))
        if(s==(0, 255, 0, 255)):
            flag += '+'
            t += 1
        if (s == (255, 255, 0, 255)):
            flag += '['
            t += 1
        if (s == (0, 128, 0, 255)):
            flag += '-'
            t += 1
        if (s == (255, 0, 0, 255)):
            flag += '>'
            t += 1
        if (s == (128, 0, 0, 255)):
            flag += '<'
            t += 1
        if (s == (128, 128, 0, 255)):
            flag += ']'
            t += 1
        if (s == (0, 0, 255, 255)):
            flag += '.'
            t += 1
print(flag)
