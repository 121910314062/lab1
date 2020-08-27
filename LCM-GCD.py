#LCM and GCD for three numbers

def lcm(x, y, z):
    gcd2 = gcd(y, z)
    gcd3 = gcd(x, gcd2)
    lcm2 = y*z // gcd(x, lcm2)
    lcm3 = x*lcm2 // gcd(x, lcm2)
    return (lcm3, gcd3)

h=input("press:1 for two numbers LCM or \n Press:2 for three nubers LCM\n :")
if h== "2":
    x = int(input("Number 1: "))
    y = int(input("Number 2: "))
    z = int(input("Number 3: "))
    (res1, res2) = lcm(x, y, z)
    print("The LCM of " + str(x) + " And " + str(y) + " And " + str(z))
