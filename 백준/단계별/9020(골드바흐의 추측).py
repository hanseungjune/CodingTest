import sys, math

def get_primes(n):
    # 소수 판별을 위한 배열 초기화
    sieve = [True] * (n+1)
    sieve[0], sieve[1] = False, False
    
    # 에라토스테네스의 체 알고리즘
    # 2부터 sqrt(n)까지의 모든 수를 순회하면서,
    # 현재 수가 소수인 경우 그 수의 배수들을 전부 False로 변경한다.
    for i in range(2, int(math.sqrt(n))+1):
        if sieve[i]:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    
    # 소수 리스트 구하기
    primes = []
    for i in range(2, n+1):
        if sieve[i]:
            primes.append(i)
    return primes

def goldbach_partition(n, primes):
    # 차이가 가장 작은 두 소수를 찾는 과정
    min_diff = sys.maxsize
    result = (0, 0)
    for p in primes:
        # 현재 소수가 n // 2보다 크면,
        # 그 이후의 소수들과 합으로 n을 나타낼 수 없다.
        if p > n // 2:
            break
        if n - p in primes:
            # 차이가 가장 작은 두 소수를 찾는다.
            if min_diff > n - 2 * p:
                min_diff = n - 2 * p
                result = (p, n - p)
    return result

# 1. 10000 이하의 소수 리스트 구하기
primes = get_primes(10000)

# 2. 골드바흐 파티션 구하기
for _ in range(int(input())):
    n = int(input())
    p1, p2 = goldbach_partition(n, primes)
    print(p1, p2, sep=' ')