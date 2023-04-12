def solution(array, commands):
    answer = []
    result = []
    
    for a in range(len(commands)):
        i = commands[a][0]
        j = commands[a][1]
        k = commands[a][2]
        
        answer = array[(i-1):j]
        answer = sorted(answer)
        result.append(answer[(k-1)])
        
    return result