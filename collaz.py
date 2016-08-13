
def collatz(num):
    if(num % 2 == 0):
        print(num // 2)    
        return(num // 2)
    else:
        print(3 * num + 1)
        return(3 * num +1)
    
    
print('Syötä kokonaisluku')

while True:
    try:
        qnum = int(input())
        break
    except ValueError:
        print('Tuo ei ollut kokonaisluku kokonaan')

while(qnum != 1):
    qnum = collatz(qnum)
    
    

