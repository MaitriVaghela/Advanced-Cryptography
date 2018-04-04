y1 = []
y2 = []
alpha = 'C'
a = 11
beta = 'E'

prod=[]
prodInverse=[]
midResult=[]
result = []

#A representation of the Galois field on 27 elements
multiTable = [[0 , 0,  0  ,0 , 0 , 0 , 0 , 0 , 0 , 0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0 , 0],
  [0  ,1  ,2  ,3  ,4  ,5  ,6  ,7  ,8  ,9 ,10, 11, 12, 13, 14, 15 ,16 ,17 ,18 ,19 ,20 ,21 ,22 ,23 ,24 ,25 ,26],
 [0  ,2  ,1  ,6  ,8  ,7  ,3  ,5  ,4 ,18, 20, 19, 24, 26 ,25 ,21 ,23 ,22 , 9 ,11 ,10 ,15 ,17 ,16 ,12 ,14 ,13],
 [0 , 3 , 6 , 9 ,12 ,15 ,18 ,21 ,24 ,11 ,14 ,17 ,20 ,23 ,26 , 2 , 5 , 8 ,19 ,22 ,25 , 1 , 4 , 7 ,10 ,13 ,16],
 [0 , 4  ,8 ,12 ,16 ,11 ,24 ,19 ,23 ,20 ,21 ,25 , 5 , 6 , 1 ,17 , 9 ,13 ,10 ,14 ,15 ,22 ,26 ,18 , 7 , 2 , 3],
 [0  ,5  ,7 ,15, 11, 13 ,21 ,26 ,19 , 2 , 4 , 6 ,17 ,10 ,12 ,23 ,25 ,18 , 1 , 3 , 8 ,16 , 9 ,14 ,22 ,24 ,20],
 [0  ,6 , 3 ,18 ,24 ,21 , 9 ,15 ,12 ,19 ,25 ,22 ,10 ,16, 13,  1 , 7 , 4 ,11, 17 ,14 , 2 , 8 , 5 ,20 ,26, 23],
 [ 0 , 7 , 5 ,21 ,19 ,26 ,15 ,13 ,11 , 1 , 8 , 3 ,22 ,20 ,24 ,16 ,14 , 9 , 2 , 6 , 4 ,23 ,18 ,25 ,17 ,12 ,10],
 [0 , 8 , 4 ,24, 23, 19, 12, 11, 16, 10, 15 ,14 , 7 , 3 , 2 ,22 ,18 ,26 ,20 ,25 ,21 ,17 ,13 , 9 , 5 , 1 , 6],
 [0 , 9 ,18 ,11 ,20 , 2 ,19 , 1 ,10 ,17 ,26 , 8 ,25 , 7, 16 , 6 ,15 ,24, 22 , 4 ,13 , 3 ,12 ,21, 14 ,23 , 5],
[0 ,10 ,20 ,14, 21,  4 ,25,  8 ,15, 26 , 6 ,16 , 1 ,11 ,18 ,12 ,22 , 5 ,13 ,23 , 3 ,24 , 7 ,17 , 2 , 9 ,19],
[0 ,11 ,19, 17 ,25 , 6 ,22 , 3 ,14 , 8 ,16 ,24 ,13 ,21 , 5 ,18 , 2 ,10 , 4 ,12 ,23 , 9 ,20 , 1 ,26 , 7 ,15],
[0 ,12 ,24 ,20 , 5 ,17 ,10 ,22 , 7 ,25 , 1 ,13 ,15 ,18 , 3 , 8 ,11 ,23 ,14 ,26 , 2 , 4 ,16 ,19 ,21 , 6 , 9],
[0 ,13 ,26 ,23 , 6 ,10 ,16 ,20 , 3 , 7 ,11 ,21 ,18 , 4 ,17 ,14 ,24 , 1 , 5 ,15 ,19 ,25,  2, 12 , 9 ,22 , 8],
[0, 14 ,25 ,26 , 1 ,12 ,13 ,24 , 2 ,16 ,18 , 5 , 3 ,17, 19, 20 , 4 ,15 ,23 , 7 , 9 ,10 ,21 , 8 , 6 ,11 ,22],
[0, 15, 21,  2, 17 ,23 , 1 ,16 ,22 , 6 ,12 ,18 , 8 ,14 ,20 , 7 ,13 ,19 , 3 , 9 ,24 , 5 ,11 ,26 , 4 ,10 ,25],
[0 ,16, 23,  5,  9 ,25 , 7 ,14 ,18 ,15 ,22 , 2 ,11 ,24 , 4 ,13 ,20 , 6 ,21 , 1 ,17 ,26 , 3 ,10 ,19 , 8 ,12],
[0 ,17, 22 , 8 ,13 ,18 , 4 , 9 ,26 ,24 , 5 ,10 ,23,  1, 15, 19,  6 ,14 ,12 ,20 , 7 ,11 ,25 , 3 ,16 ,21 , 2],
[0 ,18 , 9 ,19 ,10 , 1 ,11 , 2 ,20 ,22 ,13 , 4 ,14 , 5 ,23 , 3 ,21, 12, 17,  8, 26,  6, 24, 15 ,25 ,16 , 7],
[0 ,19 ,11 ,22 ,14 , 3 ,17 , 6 ,25 , 4 ,23 ,12 ,26 ,15 , 7 , 9 , 1 ,20 , 8 ,24 ,16 ,18 ,10 , 2 ,13 , 5 ,21],
[0 ,20 ,10 ,25 ,15 , 8 ,14 , 4 ,21 ,13 , 3 ,23 , 2 ,19 , 9 ,24 ,17 , 7 ,26 ,16 , 6 ,12 , 5 ,22 , 1 ,18 ,11],
[0 ,21 ,15 , 1 ,22 ,16 , 2 ,23 ,17 , 3, 24,  9,  4 ,25 ,10,  5, 26, 11,  6, 18, 12,  7 ,19 ,13 , 8 ,20 ,14],
[0 ,22, 17 , 4 ,26 , 9 , 8 ,18 ,13 ,12 , 7 ,20 ,16 , 2 ,21 ,11 , 3 ,25 ,24 ,10 , 5 ,19 ,14 , 6 ,23 ,15 , 1],
[0, 23, 16,  7, 18, 14,  5 ,25 , 9 ,21 ,17 , 1 ,19 ,12,  8 ,26 ,10 , 3 ,15 , 2 ,22 ,13 , 6 ,20 ,11 , 4 ,24],
[0 ,24 ,12 ,10 , 7 ,22 ,20 ,17 , 5 ,14 , 2 ,26 ,21 , 9 , 6 , 4 ,19, 16, 25, 13,  1,  8 ,23 ,11 ,15 , 3 ,18],
[0 ,25 ,14 ,13 , 2, 24, 26 ,12 , 1 ,23 , 9 , 7 , 6 ,22 ,11 ,10 , 8 ,21 ,16 , 5 ,18 ,20 ,15 , 4 , 3 ,19 ,17],
[0 ,26 ,13 ,16 , 3 ,20 ,23 ,10 , 6 , 5 ,19 ,15 , 9 , 8 ,22 ,25 ,12 , 2 , 7 ,21 ,11 ,14 , 1 ,24 ,18 ,17 , 4]]

#cipher text to be decrypted
cipherText = [['K','H'],['P','X'], ['N','K'],['H','R'], ['T','F'],['V','Y'],['E','H'], ['F','A'], ['T','W'], ['J','D'], ['U','J']]

#mapping of alphabets to numbers
valuesToNum = {'A':1,'B':2,'C':3,'D':4, 'E':5, 'F':6, 'G':7, 'H':8,
                       'I':9, 'J':10, 'K':11, 'L':12,'M':13, 'N':14,'O':15, 'P':16,
                       'Q':17, 'R':18, 'S':19, 'T':20,'U':21,'V':22,'W':23, 'X':24,'Y':25, 'Z':26}

#mapping of numbers to alphabets
numToValues = {1:'A',2:'B',3:'C',4:'D', 5: 'E', 6:'F', 7:'G', 8:'H',
                       9:'I', 10:'J', 11:'K', 12:'L',13:'M', 14:'N',15:'O', 16:'P',
                       17:'Q', 18:'R', 19:'S', 20:'T',21:'U',22:'V',23:'W', 24:'X',25:'Y', 26:'Z'}
def main():
    #Division of alphabets into y1 and y2.
    for el in cipherText:
        y1.append(el[0])
        y2.append(el[1])

    #Raised y1 to 'a'
    for el in y1:
        x = valuesToNum[el]
        res = multiTable[x][x]
        for i in range(9):
            res = multiTable[res][x]
        prod.append(res)
    #print("prod is:",prod)

    #Found the inverse of y1
    for el in prod:
        for i in range(len(multiTable)):
            if multiTable[i][el] == 1:
                prodInverse.append(i)
    #print("prodInverse is:",prodInverse)

    #Final computation of product of y1 and y2
    for i in range(0,len(prodInverse)):
        q = prodInverse[i]
        p = valuesToNum[y2[i]]
        res2 = multiTable[p][q]
        result.append(res2)
    #print(result)

    #Final output is being printed
    print("The final output is:")
    for el in result:
        print(numToValues[el])

if __name__ == '__main__':
    main()