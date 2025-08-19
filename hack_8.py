"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    result = []
    n = len(s)
    if n % 2 == 1:  # lista impar
        for i in range(n-1, -1, -1):
            result.append(f"{s[i]}-{i+1}")
    else:  # lista par
        for i in range(n, 0, -1):
            result.append(str(i))
    return result

print(fn_hack_8(["a", "b", "c", "d", "e"]))  # Output: ["e-5", "d-4", "c-3", "b-2", "a-1"]
print(fn_hack_8(["a", "b", "c"]))  # Output: ["c-3", "b-2", "a-1"]
print(fn_hack_8(["a", "b", "c", "d"]))  # Output: ["4", "3", "2", "1"]
print(fn_hack_8(["a", "b"]))  # Output: ["2", "1"]