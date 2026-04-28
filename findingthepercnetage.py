if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # Extract the list of scores for the specific student
    scores = student_marks[query_name]
    
    # Calculate the average
    average = sum(scores) / len(scores)
    
    # Print formatted to 2 decimal places
    print("{:.2f}".format(average))
