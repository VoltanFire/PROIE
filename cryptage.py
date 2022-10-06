from hashlib import sha256
import os
import sys
import time

#Barre de progresssion
def updt(total, progress):

    barlength, status = 30, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(barlength * progress))
    text = "\r[{}] {:.0f}% {}".format("#" * block + "-" * (barlength - block), round(progress * 100, 0),status)
    sys.stdout.write(text)
    sys.stdout.flush()

def bar(runs = 100):
    for run_num in range(runs):
        time.sleep(.05)
        updt(runs, run_num + 1)





#Fonction de cryptage
def crypt(input,output,key):
    keys = sha256(key.encode("utf-8")).digest()

    with open(input,"rb") as f_input :
        with open(output,"wb") as f_output :
            i = 0
            
            while f_input.peek():
                c = ord(f_input.read(1))
                j = i % len(keys)
                b = bytes([c^keys[j]])
                f_output.write(b)
                i += 1
    os.remove(input)
