def min_flips(s: str) -> int:
    count_flips = 0
    for i in range(0, len(s) - 1, 2):
        if s[i] != s[i + 1]:
            count_flips += 1
            
    return count_flips

if __name__ == '__main__':
    print(min_flips('101011'))
    print(min_flips('100110'))
    print(min_flips('110010'))