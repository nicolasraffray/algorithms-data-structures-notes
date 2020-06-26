# Algorithms and Data Structures

These are my notes on the Grokking Algorithms textbook along with some implementation code done in Python.

## Binary Search

Binary Search is a search method used for a sorted array to seek out the desired value within that array by
repeatedly dividing the search interval in half. If the interval value is reset depending on whether the target
value is greater than or less than the interval value. This is done repeatedly until the interval value == target
value or the array is exausted.

### Performance

In general, for any list of n, binary search will take log2 n steps to run in the worst case, whereas simple search
will take n steps.
