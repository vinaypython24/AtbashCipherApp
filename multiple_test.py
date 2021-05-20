import pytest

from atbash_cipher.encryption import encryption

input_path='D:\\vinay\\TestFiles\\Input'  # input folder we base files files from encryption
output_path='D:\\vinay\\TestFiles\\Output'   # output folder encrypted files
def test_method1(input,output):
    str=encryption('ABC ZYX')
    print(str)
    assert str == 'ZYX ABC'


test_method1(input_path,output_path)