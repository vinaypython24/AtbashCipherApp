import os
import threading
from atbash_cipher.fileEncryption import file_encryption

class Atbash_Cipher():
    def __init__(self,input_path,output_path): # Atbash_Cipher class initialize by 2 parameter
        self.input_path=input_path
        self.output_path=output_path

    def atbash_cipher(self):
        if not os.path.exists(self.input_path): # here we are checking that input folder present or not
            print('input path not exist')
            return
        else:
            if not os.path.exists(self.output_path):  # output not present than we create it
                os.mkdir(self.output_path)
        files = os.listdir(self.input_path)
        for file in files:
            print(file)
            if (file.endswith('.txt')): # this validation is for txt
                t1 = threading.Thread(target=file_encryption,
                                      args=(self.input_path + '\\' + file, self.output_path + '\\' + file,))
                t1.start()


if __name__ == "__main__":
    input_path = 'D:\\vinay\\TestFiles\\Input'  # input folder we base files files from encryption
    output_path = 'D:\\vinay\\TestFiles\\Output'  # output folder encrypted files
    at_cip = Atbash_Cipher(input_path, output_path)
    at_cip.atbash_cipher()



