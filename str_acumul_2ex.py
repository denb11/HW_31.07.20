
def friend_list(n):
    friends = ""
    friend = None

    while friend != "":
        m:int = 1
        while m <= n:
            m += 1
            friend = input("Friend name?: ")
            friends += friend + ", "
        else:
            break
    else:
        pass
    print("User friends:", friends[:-2] , ".")

friend_list(int(input("Num of friends: ")))
print("It's all...")
