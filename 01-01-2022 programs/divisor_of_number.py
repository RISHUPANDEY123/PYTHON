def divisor_of_number(n):
  x = [i for i in range(1,n+1) if not n % i]
  return x
print(divisor_of_number(int(input("enter a number:"))))
