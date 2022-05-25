"""第一題
使⽤set型別完成下列問題:
本班期末考試
數學及格的有: Tom, John, Mary, Jimmy, Sunny, Amy，
英⽂及格的有: John, Mary, Tony, Bob, Pony, Tom, Alice，
分別印出數學及格但英⽂不及格的名單、數學不及格但英⽂及格的名單、兩科都及格的名單、最後印出全班總共有幾個同學
"""

mathPass = {"Tom", "John", "Mary", "Jimmy", "Sunny", "Amy"}
engPass = {"John", "Mary", "Tony", "Bob", "Pony", "Tom", "Alice"}

print("數學及格但英⽂不及格的學生 : ", mathPass.difference(engPass))
print("數學不及格但英⽂及格的學生 : ", engPass.difference(mathPass))
print("兩科都及格的學生 : ", mathPass.intersection(engPass))
print("全班學生人數 : ", len(mathPass.union(engPass)))

"""第二題
使⽤dict，list型別完成下列問題:
Tom作業成績為 80, 100, 90, 95
John作業成績為 100, 93, 75, 80
請以dict型別存放兩個同學的資料key:名字，value:分數列表(list)分別算出兩位同學的平均分數並且印出
"""

scoreDict = {"Tom": [80, 100, 90, 95], "John": [100, 93, 75, 80]}

for name, scoreList in scoreDict.items():
    sum = 0
    for score in scoreList:
        sum += score
    average = str(sum / len(scoreList))
    print(name + "的平均分數 : " + average)
