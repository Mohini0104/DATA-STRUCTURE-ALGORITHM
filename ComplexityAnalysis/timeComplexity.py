#TC->O(N)
i,m = 0 ,0
n= int(input)
while i <n:
    i +=1
    m +=2

#TC->O(N^2) : Nested Loop
i = 1
while i<=n:
    j =1
    while j<=n:
        k = k+1
        j+=1
    i +=1
# n+n+n.............n -> n*n ->n^2

#TC -> O(N + M)
i = 1
k = 0
m = int(input())
while i<=n:
    i+=1
j = 1
while j<=n:
    k = k+1
    j +=1

#TC -> O(logn)
i = 1
while i<=n:
    i*=2
'''
1st iteration value of i is 1
2nd iteration value of i is 2
3rd iteration value of i is 4
4th iteration value of i is 8
5th iteration value of i is 16
.
.
.
kth iteration 2^k (k is the number of iterations)
 2^k >= n ->k = log2(n)
'''

#TC -> O(logn)
i = n 
while i >= 1:
    i/=2

#TC ->O(sqrt(n))
i = 1
while i*i <=n: #I<= sqrt(n)
    i +=n

#TC -> O(nlogn)
i = 1
while i<=n: #outer loop and runs only for n iterations 
    j = 1
    while j<=n: #inner loop makes n/i iterations
        j += i
    i +=1
#(n/1 + n/2 +n/3 +n/4..........)
#sum(n/i) -> n*sum(1/i) -> n*(1/1+ 1/2 +1/3.......... ->) -> nlogn

#TC->O(N^5)
i = 1
while i<=n: #n iteration here
    j=i
    while j <= i*i: # n^2
        if j%i == 0:
            k = 0
            while k <j: #n^2
                k +=1

        j +=1
    i +=1

'''
4 paradigms of algorithms:
->Brute Force
->Gredy
->DP
->Divide and Conquer(D&C)

'''
'''
Divide and Conquer- 
TC:
T(n) = a*T(n/b) + o(n^d log^bn)
'''
