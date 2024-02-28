#!/usr/bin/env python
# coding: utf-8

# # Greatest of 3 numbers

# In[1]:


def find_greatest(a, b, c):
    return max(a, b, c)

# Example usage:
print(find_greatest(10, 5, 20))


# # smallest of 3 numbers

# In[2]:


def find_smallest(a, b, c):
    return min(a, b, c)

# Example usage:
print(find_smallest(10, 5, 20))


# # print numbers in ascending order

# In[3]:


def swap_numbers(a, b):
    a, b = b, a
    return a, b

# Example usage:
x = 5
y = 10
x, y = swap_numbers(x, y)
print("x =", x)
print("y =", y)


# # print numbers in ascending order

# In[4]:


numbers = [5, 2, 8, 1, 9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)


# # print numbers in descending order

# In[5]:


numbers = [5, 2, 8, 1, 9]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)


# # print odd numbers and their count.

# In[6]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Odd Numbers:", odd_numbers)
print("Count of Odd Numbers:", len(odd_numbers))


# # print even numbers and their count.

# In[7]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even Numbers:", even_numbers)
print("Count of Even Numbers:", len(even_numbers))


# # print 1st 100 odd number

# In[8]:


odd_numbers = [i for i in range(1, 200) if i % 2 != 0][:100]
print(odd_numbers)


# # print 1st 100 even number

# In[9]:


even_numbers = [i for i in range(2, 201) if i % 2 == 0][:100]
print(even_numbers)


# # print multiples of 3 from 1 to 100

# In[10]:


multiples_of_3 = [i for i in range(1, 101) if i % 3 == 0]
print(multiples_of_3)


# # print 1-100 divisible by both 2 and 3

# In[11]:


divisible_by_2_and_3 = [i for i in range(1, 101) if i % 2 == 0 and i % 3 == 0]
print(divisible_by_2_and_3)


# # print total of first 100 numbers

# In[12]:


total = sum(range(1, 101))
print(total)


# # Multiply first 100 numbers

# In[13]:


import math
result = math.factorial(100)
print(result)


# # print any Multiplication table 

# In[14]:


def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Example usage:
multiplication_table(5)


# # print numbers 1 to 4 using break

# In[15]:


for i in range(1, 5):
    print(i)
    if i == 4:
        break


# # print numbers 1 to 10 except 5 using continue

# In[16]:


for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# # print last digit of a given number

# In[17]:


def last_digit(number):
    return number % 10

# Example usage:
print(last_digit(12345))


# # print second last digit of a given number 

# In[18]:


def second_last_digit(number):
    return (number // 10) % 10

# Example usage:
print(second_last_digit(12345))


# # printing finonacci number

# In[19]:


def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Example usage:
print(fibonacci(10))


# # printing factorial number

# In[20]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
print(factorial(5))


# # printing prime numbers

# In[21]:


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers(limit):
    primes = [num for num in range(2, limit + 1) if is_prime(num)]
    return primes

# Example usage:
print(prime_numbers(20))


# # printing palindrome numbers

# In[22]:


def is_palindrome(n):
    return str(n) == str(n)[::-1]

palindromes = [num for num in range(1, 1000) if is_palindrome(num)]
print(palindromes)


# # printing armstrong numbers

# In[23]:


def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == n

armstrong_numbers = [num for num in range(1, 1000) if is_armstrong(num)]
print(armstrong_numbers)


# # reverse a number in java

# In[24]:


def reverse_number(n):
    return int(str(n)[::-1])

# Example usage:
print(reverse_number(12345))


# # printing ascii values from A to Z

# In[25]:


ascii_values = {chr(i): i for i in range(ord('A'), ord('Z') + 1)}
print(ascii_values)


# # count the number of digits in a number

# In[26]:


def count_digits(n):
    return len(str(n))

# Example usage:
print(count_digits(12345))


# # sum the digits of a number

# In[27]:


def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Example usage:
print(sum_of_digits(12345))


# # reverse a number

# In[28]:


def reverse_number(n):
    return int(str(n)[::-1])

# Example usage:
print(reverse_number(12345))


# # accept an integer and count the factors of the number

# In[29]:


def count_factors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

# Example usage:
print(count_factors(12))

