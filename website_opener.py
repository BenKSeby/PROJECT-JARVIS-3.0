# # string to search in file
# with open(r'website_names.txt', 'r') as fp:
# 	# read all lines using readline()
# 	lines = fp.readlines()
# 	for row in lines:
# 		# check if string present on a current line
# 		word = 'YOUTUBE'
# 		#print(row.find(word))
# 		# find() method returns -1 if the value is not found,
# 		# if found it returns index of the first occurrence of the substring
# 		if row.find(word) != -1:
# 			print('string exists in file')
# 			number= lines.index(row)
# 			print('line Number:', number)
# 			fp.seek(number)
# 			data = fp.readline(number)
import webbrowser
# 			print(data)
def website(name):
    print("receive data: " + name)
    file = open("Text_Files/website_names.txt", "r")
    p = file.readlines()
    for i in p:
        if name.strip() in i:
            print(i + "\n")
            i = i.split(",")
            WEBSITE_LINK = i[1]
            file.close()
            webbrowser.open_new(WEBSITE_LINK)
            from repetition import first
            first()


			
