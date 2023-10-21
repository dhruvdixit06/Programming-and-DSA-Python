# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    arr=[]
    scoreArr=[]
    nameArr=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
        scoreArr.append(score)
    minScore= 9999999999
    secMinScore=9999999999
    t=9999999999
    for i in arr:
        t=i[1]
        if i[1]<minScore:
            t=minScore
            minScore=i[1]
        if t<secMinScore and t>minScore:
            secMinScore=t
    for i in arr:
        if i[1]==secMinScore:
            nameArr.append(i[0])
    nameArr.sort()
    for i in nameArr:
        print(i)