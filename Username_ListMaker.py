with open('HackerFollower_HTML.txt', 'r') as file:            #Filter Usernames from HTML
    string = file.read()
    list = string.split()
    hackaccount_list = []
    for word in list:
        if 'title' in word:
            word = word.replace('title=', '')
            word = word.replace('"', '')
            hackaccount_list.append(word)



with open('MyFollower_HTML.txt', 'r') as file:            #Filter Username from HTML
    string = file.read()
    list = string.split()
    myaccount_list = []
    for word in list:
        if 'title' in word:
            word = word.replace('title=', '')
            word = word.replace('"', '')
            myaccount_list.append(word)

listofUsers = [name for name in hackaccount_list if name not in myaccount_list]    #Users that follow hacker and not me

# with open('Check_Users.txt', 'w') as file:                #Writes Username into Another File for Easy Check
#     for name in listofUsers:
#         file.write(f'{name}\n')

with open('Check_Users.txt', 'r') as file:
    OfficialList = [word.replace('\n', '') for word in file]            #Final List of Usernames after Check




