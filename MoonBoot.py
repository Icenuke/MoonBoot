#!/usr/bin/python
# -*- coding: utf8 -*-

# import libraries
import sys
import os
from re import sub
from winreg import CreateKey, SetValueEx, OpenKey, HKEY_CURRENT_USER, KEY_SET_VALUE, REG_SZ, DeleteKey, KEY_ALL_ACCESS, EnumKey


'''
    Create a persistance in  computer
    use the path of exe, directory and add this in
    a register to launch this app, directory in reboot

'''
def persistance(name, path):
    # if the path is a directory then add explorer to permit the opening
    if path.find('.') == -1 and name != path:
        path = "explorer " + path

    # replace the double anti slashes by one
    path = path.replace('\\\\', '\\')

    # create a key in register
    CreateKey(HKEY_CURRENT_USER,'Software\Microsoft\Windows\CurrentVersion\Run')
    # open the key in register
    key = OpenKey(HKEY_CURRENT_USER, 'Software\Microsoft\Windows\CurrentVersion\Run', 0, KEY_SET_VALUE)
    # add the value in the key
    # key is the path in the register
    # name is the name of new key
    # path is the path of new key
    SetValueEx(key, name, 0, REG_SZ, path)
    # close key
    key.Close()

    print("The " + name + " in " + path + " Launch in the next Boot.")


'''
    Delete the persistance add before
    use the name to removed the key in the
    register to do not launch in the reboot

'''
def delPersistance(name):
    k = 'Software\Microsoft\Windows\CurrentVersion\Run'
    # open the key in register
    key = OpenKey(HKEY_CURRENT_USER, k, 0, KEY_ALL_ACCESS)
    # open the subkey
    subKey = OpenKey(key, name, 0, KEY_ALL_ACCESS)
    # remove the keys in the register
    DeleteKey(key, subKey)
    # print(EnumKey(key, 0))
    # close key and sub key
    key.Close()
    subKey.Close()

    print("The %s in /HKCU/%s is removed of the Register." %(name, k))


'''
    Open file to record the path and the name
    and work it to have a good string

'''
def openFile():
    fileBoot = [fileDir for fileDir in os.listdir() if fileDir.find('.conf') != -1]
    fileBoot = fileBoot[0]

    # open the file in read mode
    with open(fileBoot, 'r') as boot:
        # create dictionary with the information, path, name
        listFile = {str(file[:-1].split()[0]): sub(r'[,\'[\]]', '', str(file.split()[1:]))for file in boot.readlines()}

    # if addBoot in dir then start adding
    if fileBoot == 'addBoot.conf':
        print("Start Adding Launch in Boot...")
        # iter in the dict to call persistance
        for name, path in listFile.items():
            persistance(name, path)

    # if delboot in dir then start removing
    elif fileBoot == 'delBoot.conf':
        print("Start Deleted Launch in Boot...")
        # open file in read mode
        for name, path in listFile.items():
            delPersistance(name)

    else:
        print("no file addBoot.conf/delBoot.conf in directory...")


if __name__=="__main__":
    print("""
                 _  _                _____                 _
                / \/ \   ___    ___ (_  _ \  ___    ___  _| |_
               | .  . | / _ \  / _ \  |   / / _ \  / _ \(_   _)
               | |\/| || |_| || |_| |_| _ \| |_| || |_| | | |_
               \_|  |_/ \___/  \___/(_____/ \___/  \___/  `.__)
                                        Developed by Icenuke.

    """)

    # Call the function to open the file which have
    # the path of directory, exe
    openFile()
    input("Press a Key to close the window")
