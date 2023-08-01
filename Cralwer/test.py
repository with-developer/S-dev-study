# Step 1: XOR 연산으로 역변환
def reverse_xor(s):
    return ''.join(chr(ord(c) ^ 3) for c in s)

# Step 2: 뒤집기
def reverse_string(s):
    return s[::-1]

# Step 3: 시저 암호 역변환
def reverse_caesar_cipher(s):
    return ''.join(chr((ord(c) - 13) & 0x7F) if c.isalpha() else c for c in s)

target_string = "C@qpl==Bppl@<=pG<>@l>@Blsp<@l@AArqmGr=B@A>q@@B=GEsmC@ArBmAGlA=@q"
result2 = reverse_xor(reverse_string(reverse_caesar_cipher(target_string)))
print(result2)
