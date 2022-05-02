from random import *


class DH_Endpoint(object):
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None

    def generate_partial_key(self):
        partial_key = self.public_key1 ** self.private_key
        partial_key = partial_key % self.public_key2
        return partial_key

    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r ** self.private_key
        full_key = full_key % self.public_key2
        self.full_key = full_key
        return full_key

    def encrypt_message(self, message):
        encrypted_message = ""
        key = self.full_key
        for c in message:
            encrypted_message += chr(ord(c) + key)
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = ""
        key = self.full_key
        for c in encrypted_message:
            decrypted_message += chr(ord(c) - key)
        return decrypted_message


def easy_number(diap):
    from math import sqrt

    def is_prime(n):
        if (n <= 1):
            return False
        if (n == 2):
            return True
        if (n % 2 == 0):
            return False

        i = 3
        while i <= sqrt(n):
            if n % i == 0:
                return False
            i = i + 2

        return True

    def prime_generator():
        n = 1
        while True:
            n += 1
            if is_prime(n):
                yield n

    generator = prime_generator()
    easy = []
    for i in range(diap):
        easy.append(next(generator))
    take = easy[randint(0, len(easy))]
    return take


message = input('Сообщение которое будет шифроваться: ')
chislo = int(input('Диапазон числа: '))
s_public = easy_number(chislo)
s_private = easy_number(chislo)
m_public = easy_number(chislo)
m_private = easy_number(chislo)
Sadat = DH_Endpoint(s_public, m_public, s_private)
Michael = DH_Endpoint(s_public, m_public, m_private)
s_partial = Sadat.generate_partial_key()
print(s_partial)
m_partial = Michael.generate_partial_key()
print(m_partial)
s_full = Sadat.generate_full_key(m_partial)
print(s_full)
m_full = Michael.generate_full_key(s_partial)
print(m_full)
m_encrypted = Michael.encrypt_message(message)
print(m_encrypted)
message = Sadat.decrypt_message(m_encrypted)
print(message)
