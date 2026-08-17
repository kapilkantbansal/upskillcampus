from storage import load_data, save_data
import bcrypt
import getpass
import base64
from encryption import derive_key, generate_salt

def authenticate():
    data = load_data()
    master = data['master_password']
    if master == "":
        print("Welcome!")
        pwd = getpass.getpass("Create your master password: ")
        data["master_password"] = hash_master_password(pwd)
        print("Password created sucessfully")
        salt=generate_salt()
        data["salt"]=base64.b64encode(salt).decode()
        save_data(data)
        
    else:
        pwd = getpass.getpass("Enter your master password: ")
        if verify_master_password(pwd, master):
            print("Sucessfully logged")
            
        else:
            print("Invalid password")
            return False
        
    salt=base64.b64decode(data['salt'])
    key=derive_key(pwd,salt)
    return key


def hash_master_password(plain_password: str) -> str:
    """Takes a plain text password, salts/hashes it, and returns a secure string."""
    password_bytes = plain_password.encode('utf-8')
    salt = bcrypt.gensalt()
    secure_hash = bcrypt.hashpw(password_bytes, salt)
    return secure_hash.decode('utf-8')


def verify_master_password(plain_password: str, stored_hash: str) -> bool:
    """Compares a typed password attempt with the stored secure hash. Returns True or False."""
    password_bytes = plain_password.encode('utf-8')
    hash_bytes = stored_hash.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hash_bytes)
