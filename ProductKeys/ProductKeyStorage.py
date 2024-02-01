#!/usr/bin/env python3
"""
LocksmithOS product key storage tool
A place to store Windows product keys, and also product keys for other software
"""
# Start of script
# Import section
import os()
import random()
# Functions
"""
# TODO
Specific GUI and menu for each program/OS
"""
def windowsProductKeyMain():
    print("Select a version of Windows to check for a Product Key database")
    print("LIST UNAVAILABLE")
    def windowsProductKey95():
        str win95KeyList = ["XXXXX-XXXXX-XXXXX-XXXXX-XXXXX", ""] # Each additional new key should be given a new entry
        '''
        Keys have a specific pattern that needs to be specified later in the program.
        The rest of the text in this comment block is sourced from: https://codegolf.stackexchange.com/questions/205597/checking-a-windows-95-oem-key-for-validity
        
        Introduction
        ====
        Windows 95 used a very simple algorithm for verifying license keys. The scheme of an OEM license key always looked like this:

        xxxyy-OEM-NNNNNNN-zzzzz

        The day can be anything within 001-366, and the year cannot be lower than 95 or above 03.

        xxx represents the day of the year the key was printed on (for example 192 = 10th of July) and is a number between 001-366. yy represents the year the key was printed on and cannot be lower than 95 or above 03.

        This means for example, a key with 19296 as the first segment was printed on 10th of July 1996.

        The second segment is always OEM.

        The third segment (NN..) is always starts with 00 and the sum of the digits has to be divisible by 7

        The fourth segment is irrelevant, provided the field is the appropriate length, but has to be filled out with digits.
        '''
        enterNewWin95Key = str(input("Enter a new Windows 95 product key, or strike enter to view existing keys"))
        enterNewWin95Key == enterNewWin95Key.upper()
        if len(enterNewWin95Key) != 25
            print("Total number of keys: " + str(len(win95KeyList))
            print(str(win95KeyList))
            noMore = input("Press [ENTER] key to exit the Windows 95 key tool")
            break
        else:
            enterComment = str(input("Enter a comment about this key"))
            win95KeyList.append(enterNewWindows95Key)
            win95KeyList.append(enterComment)
            break
    def windowsProductKey98():
        # Tool for storing Windows 98 product keys
        ''' Coming soon '''
    def windowsProductKey2000():
        # Tool for storing Windows 2000 product keys
        ''' Coming soon '''
    def windowsProductKeyME():
        # Tool for storing Windows ME product keys
        ''' Coming soon '''
    def windowsProductKeyXP():
        # Tool for storing Windows XP product keys
        ''' Coming soon '''
    def windowsProductKey2003():
        # Tool for storing Windows Server 2003 product keys
        ''' Coming soon '''
    def windowsProductKeyVista():
        # Tool for storing Windows Vista product keys
        ''' Coming soon '''
    def windowsProductKey2008():
        # Tool for storing Windows Server 2008 product keys
        ''' Coming soon '''
    def windowsProductKey7():
        # Tool for storing Windows 7 product keys
        ''' Coming soon '''
    def windowsProductKey2012():
        # Tool for storing Windows Server 2012 product keys
        ''' Coming soon '''
    def windowsProductKey8():
        # Tool for storing Windows 8 product keys
        ''' Coming soon '''
    def windowsProductKey2016():
        # Tool for storing Windows Server 2016 product keys
        ''' Coming soon '''
    def windowsProductKey10():
        # Tool for storing Windows 10 product keys
        ''' Coming soon '''
    def windowsProductKey2019():
        # Tool for storing Windows Server 2019 product keys
        ''' Coming soon '''
    def windowsProductKey11():
        # Tool for storing Windows 11 product keys
        ''' Coming soon '''
    def windowsProductKey2022():
        # Tool for storing Windows Server 2022 product keys
        ''' Coming soon '''
def microsoftOfficeProductKeysMain():
    print("Select a version of Microsoft Office to check for a Product Key database")
    print("LIST UNAVAILABLE")
    def msoffice95productkey():
        # Tool for storing Microsoft Office 95 product keys
        ''' Coming soon '''
    def msoffice97productkey():
        # Tool for storing Microsoft Office 97 product keys
        ''' Coming soon '''
    def msoffice2000productkey():
        # Tool for storing Microsoft Office 2000 product keys
        ''' Coming soon '''
    def msofficeXPproductkey():
        # Tool for storing Microsoft Office XP product keys
        ''' Coming soon '''
    def msoffice2003productkey():
        # Tool for storing Microsoft Office 2003 product keys
        ''' Coming soon '''
    def msoffice2007productkey():
        # Tool for storing Microsoft Office 2007 product keys
        ''' Coming soon '''
    def msoffice2010productkey():
        # Tool for storing Microsoft Office 2010 product keys
        ''' Coming soon '''
    def msoffice2013productkey():
        # Tool for storing Microsoft Office 2013 product keys
        ''' Coming soon '''
    def msoffice2016productkey():
        # Tool for storing Microsoft Office 2016 product keys
        ''' Coming soon '''
    def msoffice2019productkey():
        # Tool for storing Microsoft Office 2019 product keys
        ''' Coming soon '''
    def msoffice2021productkey():
        # Tool for storing Microsoft Office 2021 product keys
        ''' Coming soon '''
    def msoffice2024productkey():
        # Tool for storing Microsoft Office 2024 product keys
        ''' Coming soon '''
def programmersRefProductKey():
    print("Want to add support for another type of product key? Recommend one at the source repository")
    print("GitHub: https://github.com/seanpm2001/LocksmithOS_ProductKeys/issues/")
    break
# Variables
''' Sample variables for now '''
pi = float(3.14)
hellowld = str("Hello World")
universe1 = int(42)
# Main program
print("Product key manager for LocksmithOS")
print("Options:\nWindows Product Key (ID: WinProKey)\nMicrosoft Office Product Key (ID: MSOProKey)\nOther product key (ID: ProgrammerRef)")
codeEnter = str(input("Enter a code to continue"))
codeEnter == codeEnter.upper()
if (codeEnter == "WINPROKEY"):
    return windowsProductKeyMain()
    break
elif (codeEnter == "MSOPROKEY"):
    return microsoftOfficeProductKeysMain()
    break
elif (codeEnter == "PROGRAMMERREF"):
    return programmersRefProductKey()
    break
else:
    print("Invalid ID entered. Please try again.")
    # return restartProgram()
    break
noMore = input("Press [ENTER] key to quit")
break
""" File info
File type: Python 3 source file (*.py)
File version: 1 (2023, Wednesday, December 20th at 07:04 pm PST)
Line count (including blank lines and compiler line): 173
"""
# End of script

