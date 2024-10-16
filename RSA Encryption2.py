import random
import math


# n= p.q
#phi(n) = phi(p.q)=phi(p).phi(q) = (p-1). (q-1)
#phi(n) = (p-1.q-1)

def is_prime (number):
    if number < 2:
        return False
    for i in range (2, number // 2 +1):
        if number % i == 0:
            return False
    return True

def input_prime ():
    prime = int(input("Please enter a prime number: "))
    return prime


p, q = input_prime(), input_prime()
while p==q:
    q= input_prime()
n = int(input("Please enter (n): "))
if n == p*q:
    print("n is right")
else:
    print("n is not right")
phi_n = int(input("Please enter phi(n): "))
if phi_n == (p-1) * (q -1):
    print("phi(n) is right")
else:
    print("phi(n) is wrong")

e = int(input("Please enter e: "))

if e in range(3,phi_n-1):
    if math.gcd(e, phi_n) == 1 and math.gcd(e, n) == 1:
        print("e is right")
else:
    print("e is wrong")

d = int(input("Please enter (d): "))

if (d * e) % phi_n == 1:
    print("d is right")
else:
    print("d is wrong")


message = input("Enter your message to Encrypt ")


print ("Prime number P: ", p)
print ("Prime number q: ", q)
print ("Public Key: ", e)
print ("Private Key: ", d)
print ("n: ", n)
print ("Phi of n: ", phi_n, " Secret")




message_encoded = [ord(ch) for ch in message]

print ("Message in ASCII code: ", message_encoded)

# (m ^ e) mod n = c 
ciphertext = [pow(ch, e, n) for ch in message_encoded]

print (message," Ciphered in: ", ciphertext)

Decodemsg= [pow(ch, d, n) for ch in ciphertext] 
print ("back to ASCII: ", Decodemsg)
msg = "".join (chr(ch) for ch in Decodemsg)
print("from ASCII to TEXT: ", msg)