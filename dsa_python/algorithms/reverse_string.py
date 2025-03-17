def reverse_string(s: str) -> str:
    res = []
    
    for i in range(len(s) - 1, -1, -1):
        res.append(s[i])
        
    return ''.join(res)
    
if __name__ == '__main__':
    print(reverse_string('car'))