'''
This problem is similar to 34.

If n contains d digits and n is the sum of fifth powers of its digits, it must
hold true that
    10**(d-1) <= n <= d * (9**5)

10**(d-1) grows exponentially and d * (9**5) grows linearly. The above holds
true only when d <= 6. Thus the upper bound to test is 6 * (9**5)
'''

# start from 10 to avoid single digits number
print sum(i for i in range(10, 6*(9**5)) 
          if i == sum(x**5 for x in map(int, str(i))))

