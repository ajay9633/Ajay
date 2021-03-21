def bubble(lists):
    for i in range(len(lists) - 1, 0, -1):
        for x in range(i):
            if lists[x] > lists[x + 1]:
                temp = lists[x]
                lists[x] = lists[x + 1]
                lists[x + 1] = temp
    return lists


sort_me = [9, 2, 1, 4, 7, 6, 5, 3, 8]
print(bubble(sort_me))
