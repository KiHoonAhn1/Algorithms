T = int(input())
for tc in range(1, T+1):
    N, word = input().split()
    N = int(N)
    num_byte = ''
    for text in word:
        num = ord(text)-55 if ord(text) >= 65 else int(text)
        for i in range(3, -1, -1):
            num_byte += '1' if num & (1 << i) else '0'

    print(f'#{tc} {num_byte}')