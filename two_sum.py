array=[2,4,5,6,7]
target=9

def two_sum(array, target):
    prevsum={}
    for i, num in enumerate(array):
        diff=target-num
        if diff in prevsum:
            return [array[prevsum[diff]],array[i]]
        prevsum[num]=i
    return None

print(two_sum(array, target))