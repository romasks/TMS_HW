# См. предыдущую задачу, но вместо шифра Цезаря
# использовать шифр Виженера.

key = "power"

message = "May the Force be with You".lower()
crypted_message = "uhn qrm mdomm it tsbo nle"

def transform_char(ch, pos, dest):
    base = ord('a')
    num = ord(ch) - base
    shift = ord(key[pos % len(key)])
    res = (num + shift * dest) % 26

    return chr(res + base)

def transform_string(msg, dest):
    transformed_array = []
    for index in range(0, len(msg)):
        ch = msg[index]
        if ch == ' ':
            transformed_array.append(ch)
        else:
            pos = index - message[0:index].count(' ')
            res = transform_char(ch, pos, dest)
            transformed_array.append(res)

    return "".join([str(ch) for ch in transformed_array])

print(transform_string(message, 1))
print(transform_string(crypted_message, -1))

assert(transform_string(message, 1) == crypted_message)
assert(transform_string(crypted_message, -1) == message)

crypted = transform_string(message, 1)
encrypted = transform_string(crypted, -1)
assert(encrypted == message)