#Sorting Strings, using Insertion Sort:
def insertionSort(list1):
  border = 1
  while border < len(list1):
    current = border
    while current > 0 and list1[current].lower() < list1[current-1].lower():
        # if the characters are compared when they are lowerCase,
        # we will not run into a problem such as Z comes before a,
        # and the order will be alphabetically correct
      list1[current], list1[current-1] = list1[current-1], list1[current]
      current -= 1
    border += 1
  print(list1)


listA = ['aA', 'b', 'BD', 'Bc', 'D']
insertionSort(listA)


#Sorting numbers in desc order:
def mergeSort(list1, start, end):
    if start == end:
        return
    mid = (start + end) // 2
    mergeSort(list1, start, mid)
    mergeSort(list1, mid + 1, end)
    merge(list1, start, mid, end)


def merge(list1, start, mid, end):
    new_list = []
    ind1 = start
    ind2 = mid + 1

    while ind1 <= mid and ind2 <= end:
        if list1[ind1] > list1[ind2]:
            # only changed this line, to sort the elements in descending order.
            new_list.append(list1[ind1])
            ind1 += 1
        else:
            new_list.append(list1[ind2])
            ind2 += 1

    while ind1 <= mid:
        new_list.append(list1[ind1])
        ind1 += 1

    while ind2 <= end:
        new_list.append(list1[ind2])
        ind2 += 1

    list1[start:end + 1] = new_list


list2 = [1, 2, 11, 5, 4, 3, 15]
mergeSort(list2, 0, len(list2)-1)
print(list2)
