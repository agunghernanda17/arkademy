import re,string

def validpass(password):
    if len(password)==8 and re.findall('[^A-Za-z0-9]',password):
        for i in password:
            if i.islower():
                for j in password:
                    if j.isupper():
                        for k in password:
                            if k.isalnum(): 
                                return True
    else:
        return False

def main():

    while True:
        password = input("Enter password: ")
        if validpass(password):
            print("This is a valid password")
        else:
            print("Input error")

main()