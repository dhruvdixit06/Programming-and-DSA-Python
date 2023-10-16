# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    hi=-999999999999
    shi=-999999999999
    for i in arr:
        t=i
        if i>hi:
            t=hi
            hi=i
        if t<hi and t>shi:
            shi=t
    print(shi)
