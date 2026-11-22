q = "C://Users//ASUS//Desktop//8th homework//users.txt"
def add_user(): 
    while True :
        username = input('enter ur username : ')
        Password = input('enter ur password : ')
        status = input('enter ur status [active|blocked]: ' )
        lst = ''
        lst = username +','+ Password+',' + status
        the_user = lst.split(',')
        with open(q , 'r') as q2 :
            a = q2.readlines()
            for i in a :
                    i = i.strip('\n')
                    b = i.split(',')
                    if b[0] in the_user :
                        print(f'user has already been selected choose another user name!')
                        break
                    if b[0] not in the_user :
                        with open(q , 'a') as q1 :
                            q1.write(lst)
                            q1.write('\n')
                            break   
        ans = input('do you want to add another user? [y|n] : ').strip().lower()
        if ans != 'y' : 
            break