import hashlib

def md5(message):    
    a0, b0, c0, d0 = 0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476

    def left_rotate(x, c):
        return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

    s = [
            [7, 12, 17, 22],
            [5, 9, 14, 20],
            [4, 11, 16, 23],
            [6, 10, 15, 21],
        ]

    k = [0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
        0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
        0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
        0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
        0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
        0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
        0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
        0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
        0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
        0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
        0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
        0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
        0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
        0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
        0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
        0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391]

    original_len = len(message) * 8
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += original_len.to_bytes(8, 'little')
    print(len(message))


    for i in range(0, len(message), 64):
        block = message[i:i + 64] 
        words = []

        A, B, C, D = a0, b0, c0, d0

        
        for j in range(0, 64, 4):
            words.append(int.from_bytes(block[j:j + 4], 'little')) 
    
        for i in range(64):

            if 0 <= i <= 15:
                F = (B & C) | (~B & D)
                g = i
            elif 16 <= i <= 31:
                F = (D & B) | (~D & C) # equivalente a função G
                g = (5 * i + 1) % 16
            elif 32 <= i <= 47:
                F = B ^ C ^ D  # equivalente a função H
                g = (3 * i + 5) % 16
            elif 48 <= i <= 63:
                F = C ^ (B | ~D) # equivalente a função I
                g = (7 * i) % 16


            F = (F + A + k[i] + words[g]) & 0xFFFFFFFF

            D, C, A = C, B, D
            B = (B + left_rotate(F, s[i // 16][i % 4])) & 0xFFFFFFFF

        a0 = (a0 + A) & 0xFFFFFFFF
        b0 = (b0 + B) & 0xFFFFFFFF
        c0 = (c0 + C) & 0xFFFFFFFF
        d0 = (d0 + D) & 0xFFFFFFFF

        # Hash final (a0, b0, c0, d0 em little-endian)
        return sum(x << (32 * i) for i, x in enumerate([a0, b0, c0, d0])).to_bytes(16, 'little').hex()
        
    
print(md5(b"hello world"))    
print(hashlib.md5(b"hello world").hexdigest())   
        
        

    




