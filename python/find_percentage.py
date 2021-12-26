import statistics

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        average = statistics.mean(scores)
        #average = sum(scores)/len(scores)
        scores.append("%.2f" % average)
        student_marks[name] = scores
    query_name = input()
    ans = student_marks[query_name]
    #
    print(ans.pop())