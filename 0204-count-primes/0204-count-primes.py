class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        listt = self.getsieve(n)
        count = 0
        for i in range(2,len(listt)):
            count += listt[i]
            listt[i] = count
        return listt[-1]   

    def getsieve(self, n):
        prime = [0]*n
        for i in range(2,n):
            prime[i] = 1
        i = 2
        while i*i<=n:
            if prime[i] == 1:
                for j in range(i*i,n,i):
                    prime[j] = 0
            i += 1
        return prime