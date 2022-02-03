base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

flag = ''
with open('1.txt', 'r') as f:
    for line in f.readlines():
        line = line[:-1]
        num = line.count('=')
        if num == 0:
            continue
        lastchar = line[-(num + 1)]
        # print(line,num,lastchar)
        myindex = base64chars.index(lastchar)
        # print(myindex)
        bin_str = bin(myindex)[2:].zfill(6)
        # print(bin_str)
        flag += bin_str[6 - 2 * num:]
        # print(bin_str[6-2*num:])
print(''.join([chr(int(flag[i:i + 8], 2)) for i in range(0, len(flag), 8)]))
