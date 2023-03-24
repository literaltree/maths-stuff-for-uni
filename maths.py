def gcd(num1, num2):
    numGCD = 1
    if num1 == num2:
        numGCD = int(num1)
        return numGCD
    
    elif num1 < num2:
        if num2 % num1 == 0:
            numGCD = int(num1)
            return numGCD
        for i in range(int(num1//2), 0, -1):
            if num2 % i == 0 and num1 % i == 0:
                numGCD = i
                return numGCD
    
    elif num1 > num2:
        if num1 % num2 == 0:
            numGCD = int(num2)
            return numGCD
        
        for i in range(int(num2//2), 0, -1):
            if num1 % i == 0 and num2 % i == 0:
                numGCD = i
                return numGCD
    return numGCD

def lcm(num1, num2):
    if num1 == num2:
        numLCM = num1
        return numLCM
    
    elif num1 < num2:
        for i in range(1, int(num1) + 1):
            currentGuess = num2 * i
            if currentGuess % num1 == 0:
                numLCM = int(currentGuess)
                return numLCM
            
    elif num1 > num2:
        for i in range(1, int(num2) + 1):
            currentGuess = num1 * i
            if currentGuess % num1 == 0 and currentGuess % num2 == 0:
                numLCM = int(currentGuess)
                return numLCM
    return -1


if __name__ == '__main__':
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
    numGCD = gcd(num1, num2)
    numLCM = lcm(num1, num2)
    print(f'GCD = {numGCD}')
    print(f'LCM = {numLCM}')