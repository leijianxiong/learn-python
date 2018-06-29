#/usr/bin/env python3
# coding: utf-8

import base64


def safe_base64_decode(s):
    s = s.decode('utf-8')
    s = s + ''.join(('=' for x in range(len(s) % 4)))
    return base64.b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA')
print('ok')

