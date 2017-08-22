import os

ip = {}


def gen_ip(array):

    filename = '{} {}.bat'.format(array[0], array[1])
    print(filename)

    batch = 'netsh interface ip set address name="本地连接" static {} 255.255.0.0 172.18.66.254 1 \r\n' \
            'netsh interface ip set dns name="本地连接" static 61.147.37.1 \r\n' \
            'ipconfig/all \r\n' \
            'pause \r\n' \
            'close'

    filedata = batch.format(array[1])
    print(filedata)

    with open(filename, 'wb') as fd:
        fd.write(bytes(filedata, 'ANSI'))

with open('ip.txt', 'rb') as fd:
    for line in fd:
        l = line.decode(encoding='ANSI').strip()
        print(l)

        a = l.split(' ')

        gen_ip(a)
