# Program cek palindrom menggunakan stack

def cek_palindrom(kata):
    stack = []

    # push semua huruf ke stack
    for huruf in kata:
        stack.append(huruf)

    # pop untuk membalik kata
    balik = ""
    while stack:
        balik += stack.pop()

    # cek hasil
    if kata == balik:
        return True
    else:
        return False


# Input user
kata = input("Masukkan kata: ").lower().replace(" ", "")

if cek_palindrom(kata):
    print("Palindrom ✅")
else:
    print("Bukan Palindrom ❌")