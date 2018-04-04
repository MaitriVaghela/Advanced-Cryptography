import math
import random
import time

y1 = []
y2 = []
p = 31847
alpha = 5
a = 7899
beta = 18074
temp = []
DecryValue = []
L1 = []
L2 = []
el1 = []
el2 = []
L1_rotate = []
L2_rotate = []
L5 = []
L6 = []
DecryValue_words = []
DecryValue_words_final = []
trial = []
rounds = 1

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



# This function implements the shanks algorithm
def shanks( prime, alpha, beta ):
    # Calculation of 1st and 2nd step of Shanks Algorithm
    #m = math.ceil(math.sqrt(prime))
    m = math.sqrt(prime)
    for j in range(0, int(m)):
        po = m * j
        x = pow(int(alpha),int(po),int(prime))
        #x = (first % p)
        L1.append([j, x])
    print("Before sorting L1")
    print(L1)

    # This function rotates the values in the tuples of a list for the purpose of sorting
    def rotate(l, n):
        return l[n:] + l[:n]

    for el in L1:
        L1_rotate.append(rotate(el, 1))
    L3 = sorted(L1_rotate, key=lambda x: x[0])
    print("after sorting L1")
    for el in L3:
        print(el)

    # Performing 3rd and 4th step of the shanks algorithm
    for i in range(0, int(m)):
        #s = -i
        firstexp = pow(alpha,prime-2,prime)
        secondexp = pow(firstexp, i, prime)
        thirdexp = (secondexp * beta) % prime
        L2.append([i, thirdexp])
    print("Before sorting L2")
    print(L2)

    # This function rotates the values in the tuples of a list for the purpose of sorting
    def rotate1(l, n):
        return l[n:] + l[:n]

    for el1 in L2:
        L2_rotate.append(rotate1(el1, 1))

    L4 = sorted(L2_rotate, key=lambda x: x[0])

    print("after sorting L2")
    for ely in L4:
        print(ely)

    l1_len = len(L3)
    l2_len = len(L4)

    x = 0
    y = 0
    # Calculation of 5th step
    for t in range(0, l1_len):
        for n in range(0, l2_len):
            if L3[t][0] == L4[n][0]:
                x = L3[t][1]
                y = L4[n][1]
                L6.append(n)
                L5.append(L4[n][0])
                break
    print("L5 is:")
    print(L6)
    print(L5)

    # Calculation of step 6.
    val_1 = ((m*x)+y)%(prime - 1)
    print("logarithmic value is:", val_1)

def main():
    startTime = time.time()
    shanks(RSASafe(40), 5, 9526)
    finishTime = time.time()
    print("Time taken:", finishTime - startTime)


if __name__ == '__main__':
    main()

