def format_hex(number, bits):
    number = int(number)
    bits = int(bits)
    result = hex(number)[2:].zfill(bits // 4)
    return result


a = input()
b = input()
try:
    hex_str = format_hex(a, b)
    print(hex_str)
except:
    print("type int")
