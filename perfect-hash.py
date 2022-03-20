# =====================================================================================
# =================     Python code for perfect hash function        ==================
# ================= COSC607: Algorithm Design Techniques - Project 1 ==================
# =================            Mariam Alzaabi - 100044533            ==================
# =====================================================================================

import random
import os

inF = open("test-in.txt", "r")
outF = open("test-out.txt", "w")
n = int(inF.readline())
keys_size = [0] * 8*n
keys_hashes = []
keys_hashes2 = []
keys = []

def is_prime_number(x):
    if(x >= 2):
        for y in range(2,x):
            if not (x % y):
                return (False)
    else:
        return (False)
    return (True)

class HashTable:
    def __init__(self, n, k):
        self.n = n
        self.k = k
    def gen_parameters(self):
        p = random.randint(pow(10,4),2*pow(10,4))
        while (is_prime_number(p) == False):
            p = random.randint(pow(10,4),2*pow(10,4))
        a = random.randint(1,p-1)
        b = random.randint(0,p-1)
        return (p, a, b)
    def hash_func1(self, p, a, b):
        m = 8*n
        return ((a*self.k + b) % p) % m
    def hash_func2(self, p, a, b, m):
        return ((a*self.k + b) % p) % m

for i in range(n):
    key = int(inF.readline())
    keys.append(key)
    h = HashTable(n, key)
    y = h.gen_parameters()
    if (i == 0):
        outF.write(str(8*n) + " ")
        outF.write(str(y[1]) + " ")
        outF.write(str(y[2]))
        outF.write("\n")
    hash_1 = h.hash_func1(y[0], y[1], y[2])
    keys_hashes.append(hash_1)
    keys_size[hash_1] = keys_size[hash_1] + 1

hash_table = []
for i in range(len(keys_size)):
    k = [None] * pow(keys_size[i], 2)
    hash_table.append(k)

mxy = [[0 for x in range(3)] for y in range(len(keys_size))] 

for i in range(n):
    h2 = HashTable(n, key)
    y2 = h.gen_parameters()
    m2 = pow(keys_size[keys_hashes[i]], 2)
    hash_2 = h.hash_func2(y2[0], y2[1], y2[2], m2)
    while (hash_table[keys_hashes[i]][hash_2] != None):
        y2 = h.gen_parameters()
        m2 = pow(keys_size[keys_hashes[i]], 2)
        hash_2 = h.hash_func2(y2[0], y2[1], y2[2], m2)
    keys_hashes2.append(hash_2)
    hash_table[keys_hashes[i]][hash_2] = keys[i]
    mxy[keys_hashes[i]][0] = m2
    mxy[keys_hashes[i]][1] = y2[1]
    mxy[keys_hashes[i]][2] = y2[2]

for i in range(len(mxy)):
    outF.write(str(mxy[i][0]) + " ")
    outF.write(str(mxy[i][1]) + " ")
    outF.write(str(mxy[i][2]))
    outF.write("\n")

for i in range(n):
    outF.write(str(keys[i]) + " ")
    outF.write(str(keys_hashes[i]) + " ")
    outF.write(str(keys_hashes2[i]))
    outF.write("\n")

inF.close()
outF.close()

