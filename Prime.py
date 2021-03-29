    def countPrimes(self, n: int) -> int:
        isPrime = [False,False] + [True] * (n-2)
        i = 2
        
        while i*i < n:
            if isPrime[i]:
                j=i*i
                while j < n:
                    isPrime[j] = False
                    j +=i
        
            i += 1
        
        print(isPrime)