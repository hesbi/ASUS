q = "C://Users//ASUS//Desktop//8th homework//users.txt"
def find_user() :
    find = input('enter the username u want to find : ')
    with open(q , 'r') as q2 :
        a = q2.readlines()
        for i in a :
            i = i.strip('\n')
            b = i.split(',')
            if find in b :
                print(f'the user "{find}" does does exist in the system')
            if find not in b :
                print(f'user "{find}" doesnt exist in the system')