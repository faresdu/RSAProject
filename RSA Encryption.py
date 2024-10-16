import random
import math

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def input_prime():
    while True:
        prime = int(input("Please enter a prime number: "))
        if is_prime(prime):
            return prime
        else:
            print(f"{prime} is not a prime number. Please try again.")

p = input_prime()
q = input_prime()
while p == q:
    print("p and q must be different. Please enter a different prime number for q.")
    q = input_prime()

#Calc n and phi(n)
n = p * q
phi_n = (p - 1) * (q - 1)

print(f"Calculated n: {n}")
print(f"Calculated phi(n): {phi_n}")

#input e and verify it
while True:
    e = int(input("Please enter e (must be coprime with phi(n) and between 1 and phi(n)): "))
    if 1 < e < phi_n and math.gcd(e, phi_n) == 1:
        print("e is valid.")
        break
    else:
        print("e is not valid. Please try again.")
#input d and verify it
while True:
    d = int(input("Please enter d (should satisfy d * e ≡ 1 (mod phi(n))): "))
    if (d * e) % phi_n == 1:
        print("d is valid.")
        break
    else:
        print("d is not valid. Please try again.")

message = input("Enter your message to Encrypt: ")

#print everything
print(f"\nPrime number P: {p}")
print(f"Prime number Q: {q}")
print(f"Public Key (e): {e}")
print(f"Private Key (d): {d}")
print(f"n: {n}")
print(f"Phi of n: {phi_n} (Secret)")

#transfer the chars of the text to ASCII
message_encoded = [ord(ch) for ch in message]
print(f"Message in ASCII code: {message_encoded}")

#use our RSA to encrypt the text
ciphertext = [pow(ch, e, n) for ch in message_encoded]
print(f"Ciphered message: {ciphertext}")

#decode the text
decoded_msg = [pow(ch, d, n) for ch in ciphertext]
print(f"Back to ASCII: {decoded_msg}")
msg = "".join(chr(ch) for ch in decoded_msg)
print(f"From ASCII to TEXT: {msg}")
