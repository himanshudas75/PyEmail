import sys
import os

linux = ['Linux','linux','LINUX']
windows = ['Windows','windows','WINDOWS']

pl = sys.platform
if pl in linux:
    cmd = 'clear'
elif pl in windows:
    cmd = 'cls'
else:
    cmd = 'none'

def clean():
    if cmd == 'none':
        print("Error cleaning the terminal...")
        return
    os.system(cmd)
    return