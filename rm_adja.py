#!/usr/bin/python3
#wrinting fuction to remove adjacent
def remove_adjacent(nums):
    a = set(nums)
    b = list(a)
    return b
#Writing function to pass the test
def test(got,expected):
    if got == expected:
        prefix='OK'
    else:
        prefix='X'
    print('%s got: %s expected: %s' %(prefix, repr(got), repr(expected)))

#main defination
def main():
    print('My python RemoveAdjacent Exercise')
    test(remove_adjacent([1,2,2,3]),[1,2,3])
    test(remove_adjacent([2,2,2,3,3]),[2,3])
    test(remove_adjacent([]),[])
#Boiler Plate
if __name__ == '__main__':
    main()

