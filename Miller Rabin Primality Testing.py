#Find the largest error probability of Miller-Rabin primality testing algorithm for odd integers between 115,000 and 125,000.

#time has been imported to calcuate the time taken to find largest error probability of Miller-Rabin primality testing algorithm for odd integers.
import time

# Miller-Rabin probabilisitic primality test has been divided into two parts.
#The first part i.e, miller_rabin(n, rounds) function deals with the initialisation of 'r' and 's' and calling the function miller_rabin2(n, r, s, turns) for further works.
#The results of the the function miller_rabin2(n, r, s, turns) are appended into the array.
def miller_rabin(n, rounds):
    array = []
    for _ in range(rounds):
        r = n-1
        s = 0
        while r % 2 == 0:
            s = s + 1
            r = r / 2
        for turns in range(2,n-1):
            array.append(miller_rabin2(n, r, s, turns))
    return array


#This function uses squareAndMulitply function for modular exponentiation.
#This function also further implements the Miller-Rabin probabilisitic primality test.
def miller_rabin2(prime, r, s, a):
    y = squareAndMultiply(a, r, prime)
    #y = pow(int(a), int(r), int(prime))
    if y != 1 and y != prime - 1:
        x = 1
        while s-1 >= x and prime-1 != y:
            y = pow(int(y), 2, int(prime))
            if y == 1 :
                return False
            x += 1
            if y == prime - 1:
                return True
        if y != prime - 1:
            return False
    return True

#This function will finally complete the probabilistic evaluation of Miller-Rabin primality test.
def main():
    start_time = time.time()
    n = {115231,119341,118301,115669,115921,121301, 117157, 121153, 117569,122221}
    rounds = 1
    print("Prime we are testing is " + str(n))

    #This part will find the largest error probability of Miller-Rabin primality testing algorithm for given values in the 'n'.
    for ele in n:
        miller = miller_rabin(ele, rounds)
        rabin = 0
        for element in (miller):
            if element == True:
                rabin = rabin + 1
        rabin = rabin / float(len(miller))
        print(ele,rabin)

    #The commented part will find the largest error probability of Miller-Rabin primality testing algorithm for odd integers between 115,000 and 125,000.
    #for ele in range(115000,125000):
        #if ele % 2==0:
            #continue
        #else:
            #miller = miller_rabin(ele, rounds)
            #rabin = 0
            #for element in (miller):
                #if element == True:
                    #rabin = rabin + 1
            #rabin = rabin / float(len(miller))
            #print(ele,rabin)

    finish_time = time.time()
    print("time taken:"+ (str(finish_time - start_time)) +"seconds")

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

