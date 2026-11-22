q = "C://Users//ASUS//Desktop//8th homework//users.txt"
def generate_report() :
    blocked = 0
    active = 0
    with open(q , 'r') as q2 :
            a = q2.readlines()
            for i in a :
                i = i.strip('\n')
                b = i.split(',')
                if b[2] == 'blocked' :
                    blocked += 1
                if b[2] == 'active' :
                    active += 1
            print(f'{blocked} users are blocked \n{active} users are active')