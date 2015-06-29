import os
import sys
from subprocess import Popen

from log_helper import *

TAG = 'cmd_or_shell'

#TODO terminal simulator should be a better plan
def os_system_sync(command):
    '''
        Returns:
            A arrayList of exec stdout, except stderr;
            stderr will be print on screen;
    '''
    result_list = []

    #TODO a locker should be needed here
    cmd = command + ' > .tmp'
    os.system(cmd)
    print_vorbase(TAG, cmd)
    
    with open('.tmp') as f:
        for line in f:
            result_list.append(line)
            result_list.append('\n')
    return result_list

def os_popen_sync(command):
    '''
        Caution:
            don't use this method unless stdout need to be read synchronously
    '''

    result_list = []
    cmd = command
    print_vorbase(TAG, cmd)

    sub2 = Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    while True:
        ret1 = Popen.poll(sub2)
        if ret1 == 0:
            break
        elif ret1 is None:
            time.sleep(0.2)
        else:
            break
        result_list.append(sub.stdout.read())
    return result_list

def os_popen_async(command):
    os.popen(command)


