
data = [ ["obi", 8],["uche", 3], ["onyeka", 3], ["sandra", 4], ["chioma", 7], ["emma", 6] ]
#data = [ ["Rachel", -50], ["Mawer", -50], ["sheen", -50], ["shaheen", 51] ]
def ck():
    def sortByScore(el):
        return [el[1], el[0]]
    ls = []
    scores = set({})
    #for _ in range(int(input("Enter no of students: "))):
    for _ in data:
        #name = input("Enter student name: ")
        #score = float(input("Enter student score: "))
        name = _[0]
        score = _[1]
        ls.append([name, score])
        scores.add(score)
    ls.sort(key = sortByScore)
    least_score = ls[0][1]
    filtered = filter(lambda x: x[1] == ls[1][1] and x[1] != least_score, ls)
    #filtered = filter(lambda x: x[1] == second_least, ls)
    for n in filtered:
        print(n[0])
    #print(f"{ls[0][0]}\n{ls[1][0]}")
    print(ls)
    #print(ls[0][0])
    #print(ls[1][0])

def ck():
    def sortByScore(el):
        return [el[1], el[0]]
    ls = []
    for _ in range(int(input("Enter no of students: "))):
    #for _ in data:
        name = input("Enter student name: ")
        score = float(input("Enter student score: "))
        #name = _[0]
        #score = _[1]
        ls.append([name, score])
    ls.sort(key = sortByScore)
    least_score = ls[0][1]
    filtered = filter(lambda x: x[1] > least_score, ls)
    second = list(filtered)[0][1]
    for n in ls:
        if n[1] == second:
            print(n[0])
    #print(ls)
    #print(ls[0][0])
    #print(ls[1][0])

ck()

def sortByScore(el):
    return [el[1], el[0]]
    #return el[1]

#data = [ ["obi", 8],["uche", 3], ["onyeka", 3], ["sandra", 4], ["chioma", 7], ["emma", 6] ]
#data.sort(key=sortByScore)
#print(data)