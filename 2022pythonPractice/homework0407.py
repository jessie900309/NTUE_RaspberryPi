"""撰寫一為多選題測驗打分數的程式
假設總共有8個生與10個題目,學生的答案儲存於一個二维串列裡。
每一學生針對各問題的答案,如以下串列所示。學生針對各問題的答案:
學生0:ABACCDEEAD
學生1:DBABCAEEAD
學生2:EDDACBEEAD
學生3:CBAEDCEEAD
學生4:ABDCCDEEAD
學生5:BBECCDEEAD
學生6:BBACCDEEAD
學生7:EBECCDEEAD
解答:DBDCCDAEAD
撰寫的程式要對測驗評分,並顯示果。其將各生的答與答正確的題數,最後顯示結果。
"""

studentAnswer = [
    ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
    ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
    ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
    ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
    ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
    ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
    ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
    ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
]

trueAnswer = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']

for stu in studentAnswer:
    stuScore = 0
    for listIndex in range(0, 10):
        if stu[listIndex] == trueAnswer[listIndex]:
            stuScore += 1
    print("學生", studentAnswer.index(stu), "共", stuScore, "題回答正確")
