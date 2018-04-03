import time
import random
rounds = 1

#Implementation of the Miller Rabin primality testing
def miller_rabin(n, rounds):
    for _ in range(rounds):
        r = n-1
        s = 0
        while r % 2 == 0:
            s = s + 1
            r = r / 2
        for turns in range(5):
            prime = n
            a = random.randrange(2,n-1)
            y = squareAndMultiply(a, r, prime)
            # y = pow(int(a), int(r), int(prime))
            if y != 1 and y != prime - 1:
                x = 1
                while s - 1 >= x and prime - 1 != y:
                    y = pow(int(y), 2, int(prime))
                    if y == 1:
                        return False
                    x += 1
                    if y == prime - 1:
                        return True
                if y != prime - 1:
                    return False
            return True

#Implementation of the generation of RSA-safe prime of b bits.
def RSASafe(bits):
    rsa = False
    while rsa == False:
        result = False
        while result == False:
            #result = False
            value1 = random.getrandbits(bits)
            result = miller_rabin(int(value1),rounds)
        updatedValue = (2*value1)+1
        rsa = miller_rabin(updatedValue,rounds)
    return updatedValue

#This function implements the Square and Multiply Algorithm
def squareAndMultiply(base,exponent,modulus):
    #Converting the exponent to its binary form
    binaryExponent = []
    while exponent != 0:
        binaryExponent.append(exponent%2)
        exponent = exponent/2
    #Application of the square and multiply algorithm
    result = 1
    binaryExponent.reverse()
    for i in binaryExponent:
        if i == 0:
            result = (result*result) % modulus
        else:
            result = (result*result*base) % modulus
        #print i,"\t",result
    return result


#Implementaton of the Extended Euclid Algorithm for the calcuation of inverse
def extEuclid(a, b):

    if b == 0:
        return a, 1, 0
    else:
        d, e, f = extEuclid(b, a % b)
        x = f
        y = e - (a / b) * f
        return d, x, y

#Creation of subgroups and performing the functions likewise
def funcCal(x, a, b, (alpha, beta, prime, Q)):

    f = x % 3

    if f == 0:
        x = x*alpha % prime
        a = (a+1) % Q

    if f == 1:
        x = x * beta % prime
        b = (b + 1) % Q

    if f == 2:
        x = x*x % prime
        a = a*2 % Q
        b = b*2 % Q

    return x, a, b


#Implementation of the Pollard-RHO discrete logarithm
def pollard(alpha, beta, prime):

    Q = (prime - 1) / 2

    x = alpha*beta
    a = 1
    b = 1

    X = x
    A = a
    B = b

    for i in xrange(1, prime):
        x, a, b = funcCal(x, a, b, (alpha, beta, prime, Q))
        X, A, B = funcCal(X, A, B, (alpha, beta, prime, Q))
        X, A, B = funcCal(X, A, B, (alpha, beta, prime, Q))

        if x == X:
            break

    fT = a-A
    sT = B-b

    result = ((extEuclid(sT, Q)[1] * fT) % Q) + Q
    return result

def main():

    startTime = time.time()
    print("Final result is:",pollard(2, 56851, RSASafe(40)))
    finishTime = time.time()
    print("Time Taken:",finishTime - startTime)


if __name__=='__main__':
    main()
