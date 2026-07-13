secret_code = 13
access_key = 9

def bits(number, width=4):
    return format(number & ((1 << width)-1), f"0{width}b")

print("Secret Code:", secret_code, "Binary:", bits(secret_code))
print("Access Key:", access_key, "Binary:",bits(access_key))

print("Bits and Binary")
print("Secret Code Binary:", bits(secret_code))
print("Access key Binary:", bits(access_key))

#AND and OR
and_result = secret_code & access_key
or_result = secret_code | access_key

print("AND and OR")
print("AND Result:", and_result, "Binary:", bits(and_result))
print("OR Result:",or_result, "Binary:",bits(or_result))

#NOT and XOR
not_result = (~secret_code) & 0b1111
xor_result = secret_code ^ access_key

print("NOT and XOR")
print("NOT Secret Code within 4 bits:", not_result, "Binary:",bits(not_result))
print("XOR Result:", xor_result, "Binary:",bits(xor_result))

#ODD or EVEN with XOR
xor_check = secret_code ^ 1
print("Secret Code XOR 1:", xor_check)

if xor_check == secret_code - 1:
    print("Secret Code is Odd because XOR with 1 reduced it by 1.")
else:
    print("Secret Code is Even because XOR with 1 increased it by 1.")

#Counting BITS
bit_count = secret_code.bit_count()
print("Number of 1 bits in Secret Code:", bit_count)

