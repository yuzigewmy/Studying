import base64
from Crypto.Cipher import DES
from Crypto.Cipher import AES
import binascii
from hashlib import md5
def encode_Base_64():
    s=input("需要编码的数据：")
    b=base64.b64encode(s.encode("utf-8"))
    print(b.decode("utf-8"))
    pass
def decode_Base_64():
    s=input("需要解码的数据：")
    b=base64.b64decode(s.encode("utf-8"))
    print(b.decode("utf-8"))
def encode_DES():
    Key=input("输入你的八位key:")
    key=bytes(Key,encoding='utf-8')
    char=input("输入你的补位符：")
    s=input("需要加密的数据：")
    des=DES.new(key,DES.MODE_ECB)
    num=8-len(s) % 8
    plus=num*char
    s=s+plus
    # print(s)
    encrypt_text=des.encrypt(s.encode())
    encrypt_res=binascii.b2a_hex(encrypt_text)
    print(encrypt_res.decode("utf-8"))
def decode_DES():
    #key必须是8位
    Key=input("输入你的8位key:")
    key=bytes(Key,encoding='utf-8')
    des=DES.new(key,DES.MODE_ECB)
    Encrypt_res=input("需要解密的数据：")
    encrypt_res=bytes(Encrypt_res,encoding="utf-8")
    # print(encrypt_res)
    encrypt_text=binascii.a2b_hex(encrypt_res)
    decrypt_res=des.decrypt(encrypt_text)
    print(decrypt_res.decode('utf-8'))
def encode_AES():
    Key = input("输入你的8n位key:")
    key = bytes(Key, encoding='utf-8')
    char = input("输入你的补位符：")
    s = input("需要加密的数据：")
    aes = AES.new(key, AES.MODE_ECB)
    num = 16 - len(s) % 16
    plus = num * char
    s = s + plus
    # print(s)
    encrypt_text = aes.encrypt(s.encode())
    encrypt_res = binascii.b2a_hex(encrypt_text)
    print(encrypt_res.decode("utf-8"))
def decode_AES():
    #key的位数必须是8的倍数
    Key=input("输入你的8n位key:")
    key=bytes(Key,encoding='utf-8')
    aes=AES.new(key,AES.MODE_ECB)
    Encrypt_res=input("需要解密的数据：")
    encrypt_res=bytes(Encrypt_res,encoding="utf-8")
    # print(encrypt_res)
    encrypt_text=binascii.a2b_hex(encrypt_res)
    decrypt_res=aes.decrypt(encrypt_text)
    print(decrypt_res.decode('utf-8'))
def encode_md5():
    s=input("需要加密的数据：")
    new_md5=md5()
    new_md5.update(s.encode('utf-8'))
    print(new_md5.hexdigest())

def main():
    # 1.encode_Base_64()
    # 2.decode_Base_64()
    # 3.encode_DES()
    # 4.decode_DES()
    # 5.encode_AES()
    # 6.decode_AES()
    # 7.encode_md5()
    while True:
        print('-=-=-=-=-=-=-=-=-=-=-')
        print("# 1.encode_Base_64()\n# 2.decode_Base_64()\n# 3.encode_DES()\n# 4.decode_DES()\n# 5.encode_AES()\n# 6.decode_AES()\n# 7.encode_md5()")
        print('-=-=-=-=-=-=-=-=-=-=-')
        select=int(input("请选择你需要的加密解密方式："))
        if select<8:
            if select==1:
                encode_Base_64()
            elif select==2:
                decode_Base_64()
            elif select==3:
                encode_DES()
            elif select==4:
                decode_DES()
            elif select==5:
                encode_AES()
            elif select==6:
                decode_AES()
            elif select==7:
                encode_md5()
        else:
            print("不在选择范围之内")
if __name__=="__main__":
    main()
