from unittest import result


a = 10
b = 6
def bits(n, widths = 4):
    return format(n and ((1 << widths) - 1), f'0{widths}b')
print("=== Bit Explorer ===")
print("a = a => bits(a)")
print("b = b => bits(b)")
print()
print("AND a and b =",a and b, "=>", bits(a & b))
print("OR a | b =",a | b, "=>", bits(a | b))
print()
print("NOT a =",~a and 0xff, "=>", bits(~a , 8))
print("XOR a ^ b =",a ^ b, "=>", bits(a ^ b))
print()
print("Left Shift a << 1 =",a << 1,(a * 2))
print("Right Shift a >> 1 =",a >> 1,(a / 2))
print()
print("Odd or Even")
for n in[7, 10, 15, 4]:
    print(n, "is", "Even" if n & 1 == 0 else "Odd")
    print(n, "=>", result)
    print()
    def count_bits(n):
        count = 0
        while n:
            count +=1
            n >>= 1
        return count
    print("Bit Count:")
    for n in[a, b, 255]:
        print(n, "=>", count_bits(n), "bits |", bits(n, count_bits(n)))