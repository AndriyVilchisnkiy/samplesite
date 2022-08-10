from collections import Counter
def frequency_sort(items):
    # your code here
    return sorted(items, reverse=True, key=lambda x: (items.count(x), -items.index(x)))


