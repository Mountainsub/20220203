import subprocess
import asyncio
import multiprocessing
import threading
import pandas as pd
import numpy as np
import time 
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from request5.rakuten_rss import rss , rss2 
from lib.ddeclient import DDEClient
#並列処理
def get_lines(cmd):
    '''
    :param cmd: str 実行するコマンド.
    :rtype: generator
    :return: 標準出力 (行毎).
    '''
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    #while True:
    line = proc.stdout.readline()
    if line:
        yield line
    return





#dde_ware = []

def Main(k):
        
    calc = 0
        #dde_ware, calc = rss("現在値",k)[0], rss("現在値",k)[1]
    #print(k)
    return rss("現在値",k)    
        
    



def calculation(dde_ware, indexes_weight):
        #t1 = time.time()
    calc = rss2("現在値",0, dde_ware, indexes_weight)
            
        #t2 = time.time()
    return calc

if __name__ == '__main__':  
    count = 0
    firstLoop = True
    while count <= 2142:
        if firstLoop:
            for line in get_lines(cmd='python main2.py ' + str(count)+ ' T'): # ファイル読み込み　第一引数はスタートナンバー                
                string = "file_"+ str(round(count / 126)) + ".txt"
                f = open(string, 'w')
                f.write(line.decode('sjis')) 
                #print(count)
                #time.sleep(0.1)
        count += 126
        if count >= 2142:
            s = 0
            t1 = time.time()
            for i in range(17): 
                with open('file_'+ str(i) + '.txt', 'r') as f:
                    for num in f:
                        num.rstrip("\n")
                                #if not num.isnumetric() :
                                #    print("error", i)
                                #    break
                        if num == "Traceback (most recent call last):\n":
                            break                           
                        num = float(num)
                        break
                    if num == "Traceback (most recent call last):\n":
                        continue
                    s += num
            t2 = time.time()
            print("経過時間:"+ str(t2-t1),s)
            count = 0
            firstLoop = False

                        



"""
if __name__ == '__main__':
    target_a = []
    temp = []
    for i in range(2):
        k = 126 * (i)   
        
        #print()
        print('started')
    #dde_ware, indexes_weight = temp[1], temp[2] 
    #calculation(dde_ware, indexes_weight)

  
    t2 = threading.Thread(target=thread2)
    t1.start()
    t2.start()
    
    #count = 0
    
"""



