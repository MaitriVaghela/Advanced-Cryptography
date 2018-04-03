from fractions import gcd
import time
import random

trying = 0
trying1 = 0
result = False
rounds = 1

#Implementation of the Miller Rabin probabilistic primality Testing
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

#Implementation of the plain Pollard Rho factoring algorithm.
def pollardRho(n, seed=2, f = lambda x: x ** 2 + 1):
   iter = 0
   if n%2 == 0:
       return 2
   x, y, p = seed, seed, 1
   while p == 1:
    #Answer for question 5.26,page 232
     iter = iter + 1
     x = f(x) % n
     y = f(f(y)) % n
     p = gcd((x - y) % n,n)
   print("iterations are:",iter)
   if p == n :
       return None
   else:
       return p

#Implementation of the Pollard Rho algorithm using Brent's accumulator of k consecutive arguments to gcd.
def pollardRhoBrent(n, seed=2, f = lambda x: x ** 2 + 1):
    if n % 2 == 0:
        return 2
    x, y, p = seed, seed, 1
    count , z = 1, 1
    k = 10
    while p == 1:
        x = f(x) % n
        y = f(f(y)) % n
        z = (z*(x-y)) % n
        count = count + 1
        if (count % k) != 0:
            p = gcd(z,n)
            if 1 < p and p < n:
                print("Success")
                break
            else:
                z = 1
    if p == n:
        return None
    else:
        return p

def main():
    #It keeps track of time of the beginning of the evaluation of various algorithms of pollard rho.
    startTime = time.time()
    #Generation of the first RSA-safe prime of b bits.
    num1 = RSASafe(50)
    print(miller_rabin(num1, rounds))
    print("num1 is:", num1)
    # Generation of the second RSA-safe prime of b bits.
    num2 = RSASafe(50)
    print(miller_rabin(num2, rounds))
    print("num2 is:", num2)
    #Mulplication of the two RSA-safe prime of b bits to obtain a product which will be given as parameter to plain pollard rho algorithm and
    # pollard rho algorithm using Brent's accumulator of k consecutive arguments to gcd.
    val = int(num1) * int(num2)
    print("val is:",val)

    #Result of the plain pollard rho algorithm is obtained
    result = pollardRho(val, seed=2 ,f = lambda x: x ** 2 + 1 )
    print("Result of rho:",result)

    #Result of the pollard rho algorithm using Brent's accumulator of k consecutive arguments to gcd is obtained
    resultpRBrent = pollardRhoBrent(val, seed=2 ,f = lambda x: x ** 2 + 1 )
    print("Result of brent :",resultpRBrent)

    #Time taken for the various evaluations of the pollard rho algorithm is obtained
    finishTime = time.time()
    print("time taken for performance:", finishTime - startTime)


#Implementation of the Square and Multiply Algorithm
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
