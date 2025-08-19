"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    result = []
    counter = 1
    
    for item in s:
        if isinstance(item, dict):
            new_item = {}
            for k, v in item.items():
                new_item[str(counter)] = str(counter+1)
                counter += 2
            result.append(new_item)
        elif isinstance(item, set):
            new_item = set()
            for _ in item:
                new_item.add(str(counter))
                counter += 1
            result.append(new_item)
    return result
print(fn_hack_10([{"a": "b"}, {"c", "d"}, {"e": "f"}]))  # Output: [{"1": "2"}, {"3", "4"}, {"5": "6"}]