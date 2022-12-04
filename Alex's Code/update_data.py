login_username="a1"
login_password="b"
#如何找这两个值

flag_for_username=0

f = open("login.txt", "r")
line_list = f.readlines()
data_dict = {}
for item in line_list:
    if item[-1] == '\n':
        item = item[:-1]
    temp_list = item.split(",")
    data_dict[temp_list[0]] = temp_list[1]
f.close()

for keys in data_dict.keys():
    if keys==login_username:
        flag_for_username=1

if flag_for_username!=1:
    f = open("login.txt","a")
    f.write(login_username+","+login_password+"\n")
    f.close()

else:
    print("please change the username")
#可能多填循环


# for keys, values in data_dict.items():
#     print(keys, values)
#     if keys == self.entry_username.get() and values == self.entry_password.get():
#         flag = 1