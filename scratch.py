def norm():
    x= 0
    while x == 0:
        num =  int(input('type: '))
        for i in range(num):
            print(" " * (num - i - 1)+ "* " * (i + 1))
        for i in range(num-1):
            print((" " * (i+1)) + "* " * (num -1-i))

        a = str(input('parar? (y/n) : '))
        if a == 'y':
            print('your application has been stoped')
            break


#norm()
def invert():
    x = 0
    while x == 0:
        num = int(input('type: '))
        for i in range(num):
            print((" " * i) + "* " * (num - i))
        for i in range(num - 1):
            print((" " * (num -i- 2)) + "* " * (i + 2))

        a = str(input('parar? (y/n) : '))
        if a == 'y':
            print('your application has been stoped')
            break


#invert()




def palimcheck():
   x = 0
   while x ==0:
        list = []
        han1 = []
        print(' ')
        print('that program check if your input is a palindrome')
        string = str(input('input a word, (x)to quit:'))
        if string.lower() =='x':
            break
        for i in string:
            list.append(i.lower())
            han1.append(i.lower())
        list.reverse()
        if (han1 == list):
            print(' ')
            print('{} is a actual palindrome'.format(string))
        else:
            print('no in the hell {} is a palindrome'.format(string))




def app():
    x = True
    while x == True:
        print('choose what kind of print you whant:')
        Choice = str(input('default(A), inverted(B), plalimodro check(C)  stop(X)'))
        if Choice == 'A':
            norm()
        if Choice == 'B':
            invert()
        if Choice == 'C':
            palimcheck()
        if Choice == 'X':
            break

def locker():
        app()



locker()