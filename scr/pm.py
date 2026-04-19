from cryptography.fernet import Fernet
import os

# 1. وظيفة لإنشاء مفتاح تشفير (يتم تشغيلها مرة واحدة فقط)
def load_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    return open("secret.key", "rb").read()

# 2. تهيئة التشفير
key = load_key()
fer = Fernet(key)

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')
    
    # تشفير كلمة السر قبل حفظها
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + encrypted_pwd + "\n")
    print("Saved successfully!")

def view():
    if not os.path.exists("passwords.txt"):
        print("No passwords saved yet.")
        return

    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            try:
                # محاولة فك التشفير
                decrypted_pwd = fer.decrypt(passw.encode()).decode()
                print(f"User: {user} | Password: {decrypted_pwd}")
            except Exception:
                # إذا كان المفتاح خطأ أو البيانات تالفة
                print(f"User: {user} | Password: [Error: Cannot decrypt with current key]")

# الواجهة الرئيسية
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")