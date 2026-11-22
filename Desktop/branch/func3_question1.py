def delete_user() :
    space = ''
    q = "C://Users//ASUS//Desktop//8th homework//users.txt"
    user = input('enter the user u want to remove : ')
    with open(q , 'r') as q2 :
        a = q2.readlines()
        for i in a :
            i = i.strip('\n')
            b = i.split(',')
            if user not in b :
                space += i  +'\n'
            with open(q , 'w') as q3:
                q3.write(space)
                print(f'{user} has been removed from the system')