def pascalLine(lineNum):
    if(lineNum == 0):
        return [1]
    prev_array = pascalLine(lineNum - 1)
    row = [0] * (len(prev_array) + 1)
    row[0] = 1
    row[-1] = 1
    if(len(prev_array) > 1):
        for i in range(len(prev_array) - 1):
            row[i+1] = prev_array[i] + prev_array[i+1]
    return row

print(pascalLine(5))
