import sys

print("WELCOME TO WEBSITE DATA COLLECTION \n 1. Type 'START' to enter \n 2. Type 'EXTRACT' to print the existing data \n 3. Type 'EXIT' to close the program")
while True:
    preference = input("ENTER PREFERENCE: ")
    preference = preference.upper()
    if "START" in preference:
        website_name = input("enter name of website: ")
        website_url = input("enter URL of the website: ")
        website_name = website_name.upper()
        file = open("Text_Files/website_names.txt", "a")
        file.write(website_name + "," + website_url + "\n")
        file.close()
    if "EXIT" in preference:
        sys.exit()
    if "EXTRACT" in preference:
        file = open("Text_Files/website_names.txt", "r")
        file.seek(0)
        p = file.readlines()
        for i in p:
            print(i)
        file.close()
