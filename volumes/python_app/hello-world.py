def count(maxNum=10, multiplier=1):
    result = []
    for x in range(0, maxNum):
        result.append(x * multiplier)
        pass
    return result


cnt = count
args = {'multiplier': 3}
cntSummary = cnt(**args)
print(cntSummary)
