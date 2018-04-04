from collections import defaultdict

# y**2 = x**3+x+28 is the elliptic curve 'E'.
points = defaultdict(list)

residueValues = []
xValues = []
res4Values=[]
yPoints = []
for x in range(71):
    #value of the equation is calculated
    res1 = (x**3)+x+28
    res2 = res1 % 71
    #Quadratic residue is calculated and verified
    po = (71-1) / 2
    res3 = res2 ** po
    res4 = res3 % 71
    #Calculating y points for the x/res4 values
    if res4 == 1 or res4 == 0:
        res4Values.append(float(res4))
        xValues.append(x)
        residueValues.append(res2)
        for i in range(71):
            ans = (i**2)
            ans1 = ans % 71
            if ans1 == res2:
                points[x].append(i)
                yPoints.append(i)
#print(xValues)
#print(yPoints)
#print(residueValues)
#Lenght of yPoints has been added to 1 while displaying because of the presence of infinity in the group
# Basically yPoints is the number of points on E
#print("length of yPoints:",len(yPoints)+1)
print(points)
# for val in points:
#     print(val,points[val][0])
#     print(val,points[val][1])
# print(len(points))

print("========order of the element============")
mulInv = 1

for val in points:
    x1 = val
    x2 = val
    y1 = points[val][0]
    y2 = points[val][0]
    count = 0

    while count < 37:
        if x1 != x2 and count < 37:
            num = y2 - y1
            dem = x2 - x1
            for i in xrange(0,71):
                if (dem*i) % 71 == 1:
                    mulInv = i
            lamb = num * mulInv
            x3 = ((lamb)**2)-x1-x2
            y3 = (lamb*(x1-x3))-y1
            count = count + 1
            print("count:",(x1,count))
            if x3 == x1 and y3 == y1:
                break

        if x1 == x2 and y1 == ((-y2) % 71) and count < 37:
            break

        if x1 == x2 and y1 == y2 and count<37:
            num1 = (3*((x1)**2)) + 1
            den = 2*y1
            if i in range(0,71):
                if (den*i) % 71 == 1:
                    mulInv = i
            lamb = num1 * mulInv
            x3 = ((lamb) ** 2) - x1 - x2
            y3 = (lamb * (x1 - x3)) - y1
            count = count + 1
            print("Count:",x1,count)
            if x3 == x1 and y3 == y1:
                break
    print(x1,y1)

