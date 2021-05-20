# This is mirror encryption
def encryption(str):
    new_str=''
    for i in range(len(str)):
        ascii=ord(str[i])
        if (ascii >= 65 and ascii <= 90):
            ascii = 155 - ascii  # 155 is the sum of ascii value of A=65,Z=122
        if(ascii>=97 and ascii<=122):
            ascii = 219 - ascii # 219 is the sum of ascii value of a=97,z=122
        new_str=new_str+chr(ascii)
    return new_str

















