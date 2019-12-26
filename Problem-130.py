'''
284. Peeking Iterator - https://leetcode.com/problems/peeking-iterator/
Approach - 1) For peak we won't go to next element
           2) For next we return the current element and we go to the next element
           3) for peak and next we store it in cache
'''
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    current=None
    iterator=None
    
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator=iterator
        
        if self.iterator.hasNext():
            self.current=self.iterator.next()
            

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.current

    def next(self):
        """
        :rtype: int
        """
        temp=self.current
        
        if self.iterator.hasNext():
            self.current=self.iterator.next()
        else:
            self.current=None
        return temp
            

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.current!=None

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].