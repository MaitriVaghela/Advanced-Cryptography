import random
import time

trying = 0
trying1 = 0
result = False
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


#Implementation of the generation of regular prime of b bits
def regularPrime():
    bits = {10}
    value = 0
    # try = 0
    # bits = {10,20,30,40,50,60,70}
    for el in bits:
        print("bit value is: [Regular Prime]", el)
        result = False
        print("value outide while loop[Regular Prime]",value)
        # regular prime
        while result == False:
            value = random.getrandbits(el)
            if value % 2 != 0:
                print("value inside if statement [Regular Prime]",value)
                result = miller_rabin(int(value),rounds)
                print(result)
            else:
                value = random.getrandbits(el)
                print("Value inside while loop [Regular Prime]",value)

        return int(value)
        #print("value outside while loop [Regular Prime]",value)
        #RSASafe(int(value))

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


def main():
    # It keeps track of time of the beginning of the evaluation.
    startTime = time.time()
    #regularPrime()
    print("MAin function [RSASafe]",RSASafe(10))
    # Time taken for the various evaluations is obtained
    finishTime = time.time()
    print("Time taken:", finishTime - startTime)

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

if __name__=='__main__':
    main()
