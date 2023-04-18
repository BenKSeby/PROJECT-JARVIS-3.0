import pickle
import time
import sys
# file = open("data.dat", "rb")
# # record = []
# # for i in range(3):
# #     name = input("name: ")
# #     cs = input("class: ")
# #     ls = [name, cs]
# #     pickle.dump(ls, file)
# # file.close()
# found = 0
# nm = input("enter name to be searched: ")
# try:
#     while True:
        
#         rec = pickle.load(file)
#         #print(rec)
#         if(rec[0] == nm):
#             print("record found")
#             print(rec)
#             print(rec[0], rec[1])
#             found = 1
#             break
# except:
#     if(found == 0):
#         print("no record present")
#     file.close()
# print("program ends")
def data():
    while True:
        file = open("User_Data/user_credentials.dat", "ab+")
        print("WELCOME TO PROJECT-JARVIS\nPLEASE ENTER THE DETAILS TO REGISTER\n")
        time.sleep(2)
        print("1. Type 'start' to start register\n2. Type 'exit' to exit\n3. Type 'extract' to extract data\n")
        time.sleep(1)
        prefer = input("Enter Preference: ")
        prefer = prefer.lower()

        if prefer == "start":
            file = open("User_Data/user_credentials.dat", "ab")
            USER_ID = input("Enter USER_ID(In Numbers): ")
            file.seek(0)
            found = 0
            while True:
                try:
                    rec = pickle.load(file)
                    if(rec[0] == USER_ID):
                        print("Data already exists !\n")
                        found = 1
                        data()
                except:
                    if(found == 0):
                        break
            USERNAME = input("Enter USERNAME: ")
            USERNAME = USERNAME.upper()
            file.seek(0)
            found1 = 0
            while True:
                try:
                    rec = pickle.load(file)
                    if(rec[1] == USERNAME):
                        print("Data already exists !\n")
                        found1 = 1
                        data()
                except:
                    if(found1 == 0):
                        break
            PASSWORD = input("Enter PASSWORD: ")
            RE_PASSWORD = input("Re-Enter PASSWORD: ")
            if PASSWORD == RE_PASSWORD:
                ls = [USER_ID, USERNAME, PASSWORD]
                pickle.dump(ls, file)
                time.sleep(2)
                print("\nRegistered Successfully !\n")
            else:
                print("Password re-entered not same !\n")

        if prefer == "extract":
            file.seek(0)
            print("Extracting Data: \n")
            while True:
                try:
                    rec = pickle.load(file)
                    print(rec[0] +  " | " + rec[1])

                except:
                    print("\nEnd of line\n")
                    
                    data()
        
        if prefer == "exit":
            print("Exiting Program\n")
            file.close()
            sys.exit()
data()