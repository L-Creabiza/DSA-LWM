x = int(input('input an integer: '))
def cuberoot(x):
    x
    epsilon = 0.01
    num_guess = 0
    low = 0.0
    high = x
    guess = (high+low)/2.0
    while abs(guess**3-x) >= epsilon:
        if guess**3 < x:
            low = guess
        else :
            high = guess
        guess = (high+low)/2
        num_guess += 1
    print ('The Number of Guesses taken:', num_guess)
    print (guess, 'Is close to the cube root of', x)
 

cuberoot(x)
