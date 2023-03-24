def prime_factorisation(num):
    factors = []
    for i in range(num):
        for i in range(2, int(num//2)):
            if num % i == 0:
                num /= i
                factors.append(i)
                break
    factors.append(int(num))
    return factors

if __name__ == '__main__':
    prime_factorisation(int(input('Number: ')))