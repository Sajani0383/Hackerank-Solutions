if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    scores=sorted({s for _, s in records})
    second_lowest=scores[1]
    names=sorted([n for n, s in records if s==second_lowest])
    for n in names:
        print(n)
        
