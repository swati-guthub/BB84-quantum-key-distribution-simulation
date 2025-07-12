import random

def generate_bits(n):
  bits = [random.randint(0,1) for _ in range(n)] 
  return bits
def generate_bases(n):
  bases = [random.choice(['+', 'x']) for _ in range(n)]
  return bases

def encode_qubits(bits, bases):
    return [(bit, base) for bit, base in zip(bits, bases)]

def measure_qubits(qubits, bob_bases):
    result = []
    for (bit, base), bob_base in zip(qubits, bob_bases):
        if base == bob_base:
            result.append(bit)
        else:
            result.append(random.randint(0, 1))
    return result
def extract_key(alice_bases, bob_bases, alice_bits, bob_bits):
    key = []
    for a_base, b_base, a_bit, b_bit in zip(alice_bases, bob_bases, alice_bits, bob_bits):
        if a_base == b_base:
            key.append(a_bit) 
    return key

n = 20  

alice_bits = generate_bits(n)
alice_bases = generate_bases(n)
qubits = encode_qubits(alice_bits, alice_bases)

bob_bases = generate_bases(n)
result = measure_qubits(qubits, bob_bases)

final_key = extract_key(alice_bases, bob_bases, alice_bits, result)
print("Alice Bits:       ", alice_bits)
print("Alice Bases:      ", alice_bases)
print("Bob Bases:        ", bob_bases)
print("result: ", result)
print("Final Shared Key: ", final_key)
print("Key Length:       ", len(final_key))