import unittest

class TestStringMethods(unittest.TestCase):
    def test_middleduplicates(self):
        self.assertEquals(findval([1,3,4,5,6,7,7,7,8,11,12,12,13],7),3)

    def test_allduplicates(self):
        self.assertEquals(findval([6,6,6,6,6,6,6,6,6,6,6],6),11)

    def test_rightduplicates(self):
        self.assertEquals(findval([1,3,4,5,9,9,9,9,9,9,9,9,9],9),9)

    def test_leftduplicates(self):
        self.assertEquals(findval([3,3,3,3,3,3,3,3,8,11],3),8)

    def test_noduplicates(self):
        self.assertEquals(findval([1,3,4,5,6,7,8,11,15,54,88],7),1)


def findval(sortedlist, num):
    ''' Perform two binary searches, to detect the number of instances of the element in the list     
    :param sortedlist: List of sorted ints including duplicates
    :param num: search element 
    :return: the count of the element within the sortedlist 
    '''

    # find the min index of num
    start=0
    end=len(sortedlist)-1
    while end!=start:
        mid = (end+start) / 2
        if num==sortedlist[mid] or num < sortedlist[mid] :
            # answer is to the left
            end=mid
        else:
            # move right
            start=mid+1
    leftindex=start

    # find the max index of num
    start=0
    end=len(sortedlist)-1
    while end!=start:
        mid = (end+start) / 2
        if num==sortedlist[mid] or num > sortedlist[mid] :
            # answer is to the right of mid
            start = mid+1
        else:
            # move left
            end = mid

    # handle edge case of num is the last element in the list
    if start!=len(sortedlist)-1:
        rightindex=start-1
    else:
        rightindex = start

    #+1 for 0 based index
    total=(rightindex-leftindex)+1
    return total

def main():
    unittest.main()

if __name__ == "__main__":
    main()
