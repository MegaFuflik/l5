def medians(list1, list2):    
    sortedLst = sorted(list1 + list2)
    lstLength = len(list1 + list2)
    flooredIndex = (lstLength - 1) // 2
   
    if (lstLength % 2):
        return sortedLst[flooredIndex]
    else:
        return (sortedLst[flooredIndex] + sortedLst[flooredIndex + 1])/2

if __name__ == "__main__":    
    print(medians([1,3],[2]))
    print(medians([1,2],[3,4]))
    print(medians([0,0],[0,0]))
    print(medians([2],[0]))