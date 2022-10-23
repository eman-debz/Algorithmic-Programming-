binary = '1000101'
def solution(binary):
    gaps = []
    count = 0
    if '0' not in binary:
        return 0
    if binary.count('1') < 2:
        return 0
    for i in range(len(binary)-1):
        if binary[i] == '1' and binary[i+1] == '0' :
            pass
        if binary[i] == '0':
            count +=1
        if binary[i+1] == '1' and binary[i] == '0' :
            gaps.append(count)
            count = 0
    if len(gaps) < 1:
        return 0
    return max(gaps)

print(solution(binary))