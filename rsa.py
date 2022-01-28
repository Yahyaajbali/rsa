import math
from random import randrange, getrandbits
import numpy as np


def gen_potential_prime(length):

    pot_prime = getrandbits(length)
    pot_prime |= (1 << length - 1) | 1
    return pot_prime

def is_prime(n): #miller-rabin thingy to check if n is prime
    if n == 2 | n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    k = 128
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

def gen_prime(length):
    while True:
        pot_prime = gen_potential_prime(length)
        if is_prime(pot_prime):
            return pot_prime


def gen_prime_pair(length):
    while True:
        p = gen_prime(length)
        q = gen_prime(length)
        if p != q:
            return p, q
key_length = int(input("Enter key length: "))
two_primes = gen_prime_pair(key_length)

p = two_primes[0]
q = two_primes[1]

#public key
n = p * q #n
phi = (p - 1) * (q - 1) #phi

def gen_e(phi): #generates e
    while True:
        e = randrange(2, phi)
        if math.gcd(e, phi) == 1: #plus grand diviseur commun de e et phi, meaning e and phi are coprime
            return e
    
e = gen_e(phi) #e
#public key is n and e

#private key
k = 2#randrange(1, phi)
d = (1 + k * phi) / e
#private key is d

#message to encrypt
message  = input("number to encrypt: ")

#string to ascii

coded_message = int(message)

#encrypt 
def encrypt(coded_message, n, e):
    c = pow(int(coded_message), e, n) 
    return c

encrypted_message = encrypt(coded_message, n, e)


#decrypt
def decrypt(encrypted_message, d, n):
    f = pow(int(encrypted_message), int(d), int(n))
    return f

decrypted_message = decrypt(encrypted_message, d, n)

print("original message: " + message)
print("encrypted message: " + str(encrypted_message))
print("decrypted message: " + str(decrypted_message))