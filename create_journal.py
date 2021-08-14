"""
===============================================
================= IVY JOURNAL =================
===============================================

A fully encrypted journal that can be used to store personal info/data.

Author: Vachan MN
github: vachanmn123
email: vachanmn123@gmail.com
discord: TakedownIvy#3869

This program needs a `config.json` file to work.

FILE NAME: `create_journal.py`
This program allows you to create a new journal.
"""

# Warn the user about the file structure
input("THIS PROGRAM WILL USE THE DIRECTORY SPECIFIED IN THE `config.json` FILE AS ITS ROOT DIRECTORY AND CREATE FILES INSIDE IT. IF YOU ARE FINE WITH THIS PLEASE PRESS [ENTER], ELSE PRESS `ctrl + C`")
# import the nessesary modules
import json
import hashlib
import os

# load the config file
with open('config.json') as f:
    config = json.load(f)

# Get the jounal location
path_to_storage = config['path_to_storage']

# Warn the user about losing data if password is forgotten
print("You will now set a new password, this password is the only way you can access the journal, if you lose it all the data in your jounal WILL BE UNACCESSABLE!")
# Ask user for a new password
new_paswd = input("Please enter a new password")
if input("Confirm: ") == new_paswd:
    print("Creating new journal...")
    with open(os.path.join(path_to_storage, 'passwd.ivypwd'), 'wb') as pwdfile:
        # Encrypt the password
        pass_hash=hashlib.sha256(new_paswd.encode()).digest()
        # Write the encrypted password to the file
        pwdfile.write(pass_hash)
    print("New journal created!")
else:
    # If the user didn't enter the password correctly, warn them and exit
    print("Password mismatch!")
    exit()