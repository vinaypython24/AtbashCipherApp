#import os
from atbash_cipher.encryption import encryption

def file_encryption(inputfile,outputfile):
    print(inputfile)
    file1 = open(inputfile, "r+")
    str=file1.read()
    print(str)
    str=encryption(str)
    print(str)
    f = open(outputfile, "a")
    f.write(str)
    f.close()
