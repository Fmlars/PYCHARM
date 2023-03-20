while true:
    n = 0
    flag = 0

    a = input(int("1: Log In\n2: Sign Up\n"))

    if a = 1:
        f = open("saved.txt", "r"))
        usr = input("Username: ")

        for line in f:
            n + 1
            if usr in line:
                flag = 1
                break

        if flag == 0
            print("No Such Username\n")
        elif:
            psw = input("Password: ")
            if psw in line:
                print("Log In Succesful\n")
            else
                print(Wrong Password\n)


    elif a == 2:
        f = open("saved.txt", "r")
        usr1 = int(input("Username: "))
        for line in f:
            n + 1
            if usr1 in line:
                flag = 1
                break
        if flag == 0:
            psw1 = input("Password: ")
            f.close()
            f = open("saved.txt", "a")
            f.write(usr1+" "+psw1+"\n")
            print("Sign Up Succesful\n")

        else
            print"Username Already Exist"

    f.close()
