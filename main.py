from storage import initialize, load_data, save_data
from auth import authenticate
from encryption import encrypt_password, decrypt_password
initialize()

key=authenticate()

def show_menu():
    print("1: ADD CREDENTIALS")
    print("2: VIEW CREDENTIALS")
    print("3: SERCH CREDENTIALS")
    print("4: DELETE CREDENTIALS")
    print("5: EXIT")


def add(key):
    print("===ADD CRDENTIALS===")
    web = input("Enter the website name: ")
    data = load_data()
    usr = input("Enter the usernme: ")
    pwd = input("Enter the password: ")
    data["data"][web] = {
        "username": usr,
        "password": encrypt_password(pwd,key)
    }
    save_data(data)

def view(key):
    print("===VIEW CREDENTIALS")
    data=load_data()
    vault=data["data"]
    if not vault:
        print("VAULT IS EMPTY!")
    else:
        print("Saved websites are: ")
        for site in vault:
            print(f"{site}")

def search(key):
    print("===SEARCH CREDENTIALS===")
    data = load_data()
    query = input("Enter the website name: ")
    if query in data["data"]:
        print("Data Found!")
        info = data["data"][query]
        print(f"USERNAME: {info['username']}")
        print(f"PASSWORD: {decrypt_password(info['password'],key)}")
    else:
        print("NO such website exist in database")

def delete(key):
    print("===DELETE CREDENTILS===")
    data = load_data()
    site_to_delete = input("Enter the website name: ")
    if site_to_delete in data["data"]:
        del data["data"][site_to_delete]
        save_data(data)
        print("Data deleted sucessfully")
    else:
        print("No such website exist")

def exit_program(key):
    quit()

if not key:
    exit()

print("===PASSWORD MANAGER===")

while True:
    show_menu()
    try:
        input_user = int(input("Enter the choice: "))
        mapping = {
            1: add,
            2: view,
            3: search,
            4: delete,
            5: exit_program
        }
        func = mapping[input_user]
        if func:
            func(key)
        else:
            print("Invalid choice")
    except ValueError:
        print("Enter correct format")
    except KeyError:
        print("Enter correct format")
