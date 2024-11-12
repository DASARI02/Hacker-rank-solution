if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    maxi = set(arr)
    a = sorted(maxi)
    print(a[-2])
