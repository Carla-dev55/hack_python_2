"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    if s == [0]:
        return [0]
    
    result = []
    for i in range(len(s)):
        num = i + 1
        if i % 2 == 0:
            result.append(str(num))
        else:
            result.append(num)
    return result

print(fn_hack_7(["a", "b", "c", "d", "e"]))  # Output: ["1", 2, "3", 4, "5"]
print(fn_hack_7([0]))  # Output: [0]
