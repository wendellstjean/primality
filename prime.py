from math import sqrt
from random import randint
def isPrime(n : int) -> bool:
  """ Returns true if n is prime.\n
      Uses trial division to determine if n is prime. Returns false if n is less
      than 2 or has a factor other than 1 or n.
  """
  if n==2: return True
  if n<2 or n%2==0: return False
  for i in range(2, sqrt(n)):
    if n%i==0: return False
  return True


def millerTest(n : int, d : int) -> bool:
  a=randint(2, n-2)
  x=(a**d) % n
  if x==1 or x==n-1: return True
  while d != (n-1):
    x=(x*x) % n
    if x ==1: return False
    if x==n-1: return True


def isPrime2(n : int,k : int =1) -> bool:
  """ Returns true if n is prime using the Miller-Rabin test.\n
      Uses the Miller-Rabin test to determine if n is prime. k is the number of times the test is run. 
      Increasing k reduces the margin of error. Returns false if any of the k tests returns false.
  """
  if n==2: return True
  if n<2 or n%2==0: return False
  d=n-1
  while d%2==0: d //=2
  for i in range(k):
    if not millerTest(n, d): return False
  return True