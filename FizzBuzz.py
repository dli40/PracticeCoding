#GET INFO HERE
with open fp as ("FizzBuzz.txt", r):
    line = fp.read()
    x = str(line[0])
    y=str(line[2])
    z=str(line[4])
    for i in range(1,z+1):
        if i%x ==0 and i%y==0:
            print('FizzBuzz')
        else if i%x==0:
            print('Fizz')
        else:
            print('Buzz') #Could probably do this in 3 lines of code:2 statements: switch?/
        
