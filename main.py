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

FILE NAME: main.py
This file contains the main program loop.
"""
# Import nessesary modules
import json
import os
import hashlib
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# set authenticated flag to false by default
authenticated = False

# Load the config
try:
    with open('config.json', 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    # If the config file doesn't exist print an error message
    print("Config file not found. Please create a config.json file.")
    exit()

# Load the path to the storage folder
try:
    path_to_storage = os.path.join(config['path_to_storage'])
except FileNotFoundError:
    # If the path to the storage folder doesn't exist print an error message
    print(f"No such file or directory: '{config['path_to_storage']}'")
    exit()
if not os.path.join(path_to_storage, 'passwd.ivypaswd'):
    # If the password file doesn't exist print an error message
    print("No password file found. Please create a passwd.ivypaswd file using create_journal.py")
    exit()
# Ask user for password to journal and hash it SHA256
usr_passwd = hashlib.sha256(input("Please enter your password: ").encode()).hexdigest()
# Get stored password from file
with open(os.path.join(path_to_storage, 'paswd.ivypwd'), 'r') as f:
    stored_passwd = f.read()
# Check if the password is correct
if usr_passwd == stored_passwd.lower():
    # If the password is correct set authenticated flag to True
    print("Loading your journal!\n")
    authenticated = True
else:
    # If the password is incorrect print an error message and exit
    print("Wrong password")
    authenticated = False
    exit()
# Generate a new Fernet key from the entered password
usr_pwd = usr_passwd.encode()
salt = config['salt'].encode()
kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=100000)
key = base64.urlsafe_b64encode(kdf.derive(usr_pwd))
Fernet = Fernet(key)

def create_entry():
    """
    This function creates a new entry in the loaded journal
    """
    # Ask user for the title of the entry
    entry_name = input("Please enter the name of your entry: ").lower().replace(" ", "")
    # Ask user for the content of the entry
    entry_content = (f'{entry_name}\n\n{input("Please enter the content of your entry: ")}').encode()
    # Encrypt the entry_content
    enc_entry_content = Fernet.encrypt(entry_content)
    entry_content = ''
    # Save the entry_content to a file
    try:
        with open(os.path.join(path_to_storage, f'{entry_name}.ivyentry'), 'wb') as f:
            f.write(enc_entry_content)
            f.close()
        # Print a success message
        print(f"Entry '{entry_name}' created!")
        return
    except Exception as e:
        # If error occurs print the error message
        print("An exception occured: ", e)
        return

def list_entries():
    all_files=os.listdir(path_to_storage)
    entries = []
    for file in all_files:
        if file.endswith('.ivyentry'):
            entries.append(file.replace('.ivyentry', ''))
    print(entries)
    return

def read_entry():
    all_files=os.listdir(path_to_storage)
    search = f'{input("Please enter the entry name: ")}.ivyentry'
    if search in all_files:
        entry = os.path.join(path_to_storage, search)
        with open(entry, 'rb') as f:
            entry_content = f.read()
        entry_content = Fernet.decrypt(entry_content)
        print(entry_content.decode())
        return
    else:
        print("No such entry found")
        return

def delete_entry():
    all_files=os.listdir(path_to_storage)
    search = f'{input("Please enter the entry name: ")}.ivyentry'
    if search in all_files:
        entry = os.path.join(path_to_storage, search)
        os.remove(entry)
        print(f"Entry '{search}' deleted!")
        return
    else:
        print("No such entry found")
        return

# List of all valid choices to be offered to user
options = [
    '1. Create a new entry',
    '2. List all entries',
    '3. Read entry',
    '4. Delete an entry',
    '5. Exit'
]
# Print the options when authenticated
while authenticated:
    for option in options:
        print(option)
    # take user input for their choice
    choice = input("Select your option: ")
    # call specific function based on choice
    if choice == '1':
        create_entry()
    elif choice == '2':
        list_entries()
    elif choice == '3':
        read_entry()
    elif choice == '4':
        delete_entry()
    elif choice == '5':
        print("Bye Bye!")
        exit()
    else:
        print("Invalid choice")