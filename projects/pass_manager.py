from cryptography.fernet import Fernet

#key + password + test to encrypt = random text
#random text + key + password = text to encrypt


#encryption key
'''
def write_key():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)'''

def load_key():
  file = open("key.key", 'rb')
  key = file.read()
  file.close()
  return key

#convert master password into bytes with .encode
master_pwd = input("what is the master password? ")
#key= load_key() + master_pwd.encode()
#fer = Fernet(key)
if master_pwd != "EMun0z2.52":
  print("not correct")
else:
  pass

#opening file to read all the paswords in 'r' or read mode
def view():
  with open('password.txt', 'r') as f:
    for line in f.readlines():
      data = line.rstrip()
      user1, user,passw = data.split("|")
      print("user:", user, "| password:", Fernet.decrypt(passw.encode()).decode())

#adding account, username, and password to the same file
def add():
  name = input('Account Name: ')
  user1= input("username: ")
  pwd = input("password: ")

  with open('passwords.txt', 'a') as f:
    f.write(name + "|" + user1 + "|" + Fernet.encrypt(pwd.encode()).decode() + "\n")

while True:
  mode = input("would you like to add a new password or view existing ones?(view or add)")
  if mode == "q":
    break
  if mode == "view":
    view()
  elif mode == "add":
    add()
  else:
    print('Invalid mode.')
    continue 