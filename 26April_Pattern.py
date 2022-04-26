from tkinter import filedialog
import pyautogui as p
import time
import os
import tkinter as tk
from datetime import datetime

#PATTERN 1

#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 

n=int(input('Enter value of n\n'))
i = 1
while i <= n:
    j = i
    while j < n:
        # display space
        print(' ', end=' ')
        j += 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = n
while i >= 1:
    j = i
    while j <= n:
        print(' ', end=' ')
        j += 1
    k = 1
    while k < i:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1


time.sleep(5)
# (p.screenshot()).save('Pattern1.png')
pic=p.screenshot()
# root=Tk()
# root.withdraw()
folder=filedialog.askdirectory()
curr=datetime.now()
curr=curr.replace(microsecond=0)
# file=os.path.join(folder,'Pattern1.png')
format="%y_%b_%d_%H_%M_%S"
curr=datetime.strftime(curr,format)
file_name="Pattern1"+curr+".png"
file=os.path.join(folder,file_name)
pic.save(file)


#PATTERN 2

# *   *   *   *   *
#   *   *   *   *
#     *   *   *
#       *   *
#         *

n=int(input('Enter value of n\n'))

for i in range(n,1,-1):
    for j in range(0, n-i):
        print(" ",end='')
    for j in range(i,(2*i)-1):
        print("*",end="")
    for j in range(1, i-1):
        print("*",end="")
    print()

time.sleep(5)
# (p.screenshot()).save('Pattern2.png')
pic=p.screenshot()
# root=Tk()
# root.withdraw()
folder=filedialog.askdirectory()
curr=datetime.now()
curr=curr.replace(microsecond=0)
# file=os.path.join(folder,'Pattern2.png')
format="%y_%b_%d_%H_%M_%S"
curr=datetime.strftime(curr,format)
file_name="Pattern2"+curr+".png"
file=os.path.join(folder,file_name)
pic.save(file)