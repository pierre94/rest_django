# encoding: utf-8
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
# Create your tests here.


def aes_encrypt(message, key):
    length = 16
    count = len(message)
    add = length - (count % length)
    message = message+('\0' * add)
    # 被加密的必须是16的倍数，不足的部分用'\0'补充

    cryptor = AES.new(key, AES.MODE_CBC, key)
    ciphertext = cryptor.encrypt(message)

    # 将加密后的结果以16进制返回
    return b2a_hex(ciphertext)


def aes_decrypt(message, key):
    cryptor = AES.new(key, AES.MODE_CBC, key)
    plain_text = cryptor.decrypt(a2b_hex(message))

    #去除多余的'\0'

    return plain_text.rstrip('\0')
