from collections import defaultdict
def highFive(items: any) :
        dict = defaultdict(list)

        for stu_id, score in items:
                dict[stu_id].append(score)

        result = []

        for stuid in sorted(dict.keys()):
            average_score = sorted(dict[stuid],reverse=True)[:5]
            result.append([stuid,sum(average_score) //5])
        return result
                


        

print(highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))