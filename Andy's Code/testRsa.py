'''
Author: AndyYe
Date: 2022-12-12 18:41:09
LastEditors: AndyYe
LastEditTime: 2022-12-12 18:51:43
FilePath: \Andy's Code\testRsa.py
Description: 

Copyright (c) 2022 by AndyYe, All Rights Reserved. 
'''
import rsa
import json
import pickle
import base64

# rsa加密
def rsaEncrypt(str):
    # 生成公钥、私钥
    (pubkey, privkey) = rsa.newkeys(512)
    print("公钥:\n%s\n私钥:\n%s" % (pubkey, privkey))
    # 明文编码格式
    content = stri.encode("utf-8")

    # 公钥加密
    crypto = rsa.encrypt(content, pubkey)
    str(crypto)

    return (crypto, privkey)


# rsa解密
def rsaDecrypt(str, pk):
    # 私钥解密
    content = rsa.decrypt(str, pk)
    con = content.decode("utf-8")
    return con


if __name__ == "__main__":
    stri, pk = rsaEncrypt("what the fuck")
    print("加密后密文：\n%s" % str)

    content = rsaDecrypt(str, pk)
    print("解密后明文：\n%s" % content)

# import rsa
# import base64

# publicKeySpkiDer = base64.b64decode('MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAt14jQ0+D8+gpsCPIrCoWVgw8qmH6izDXQTSqHngcGkjuuK58TOOgUo/lari7uTAg5s0ng42WYwQw3uXqa4aKOUMfcLvmn9pALNY3q9oXZa9plxemGR9itlTrY6ZKOX2FrRTB42K6F6YUnMTtjotw/6E3lNQJpFYwyT1EhLV/TP2ds7NVbNEMX+kRcelxD9Cwwigfv+2eljUJP/lQUoNTEJr6oQRibPMSBCRBbljUq5fDSxGrm0WKFLcxDwcf57/qekeWeFkysdzOTSlOQfGs8WLGho3pMNal0uCzEi2SIVPnkg3cNs6nCJ/Y3LCwUcOk1kRJqyZqk46s4iFzEElGqQIDAQAB')
# publicKey = rsa.PublicKey.load_pkcs1_openssl_der(publicKeySpkiDer)
# print(publicKeySpkiDer)
# print(publicKey)

# (encryptdata, PrivateKey) = RsaEncrypt(SendData)
# print('encrypted data is ' + str(encryptdata))

import rsa

(pubkey, privkey) = rsa.newkeys(1024)
print(pubkey)
pub = pubkey.save_pkcs1()
with open('public.pem','wb+')as f:
    f.write(pub)
print(pub)

pri = privkey.save_pkcs1()
with open('private.pem','wb+')as f:
    f.write(pri)

message = '789'.encode('utf8')
with open('public.pem','rb') as publickfile:
     p = publickfile.read()
pubkey = rsa.PublicKey.load_pkcs1(p)
#
with open('private.pem','rb') as privatefile:
     p = privatefile.read()
privkey = rsa.PrivateKey.load_pkcs1(p)

#
#  # 用公钥加密、再用私钥解密
crypto = rsa.encrypt(message, pubkey)
message1 = rsa.decrypt(crypto, privkey)
print(message1)
