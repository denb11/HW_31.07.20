
def friend_list():
    friends = ""
    friend = None

    while friend != "":
        friend = input("Fried name?: ")
        friends += friend + ", "
        if friend == "":
            print("stop")
    print("User friends:", friends[:-4] , ".")


friend_list()
