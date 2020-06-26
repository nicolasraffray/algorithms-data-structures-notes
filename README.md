# Algorithms and Data Structures

These are my notes on the Grokking Algorithms textbook along with some implementation code done in Python.

### Big O Notation

The goal of Big O Notation is to describe the speed of an algorithm in terms of the number of operations needed to perform a given task and a an input set.

Big O describes how the algorithm performs as the input set grows.

##### Why should Big O be used?

It establishes the worst case run of your algorithm, the most number of iterations it will take the algorithm.

#### Big O Examples:

![GitHub Logo](/images/BigO_graph.png)

- O(log(n)) - _Log Time_: Binary Search
- O(n) - _Linear Time_: Simple search
- O(n \* log n): Quicksort
- O(n^2): A slow sorting algorithm, like selection sort
- O(n!): A really slow algorithm, like the traveling salesperson.

### Binary Search

Binary Search is a search method used for a sorted array to seek out the desired value within that array by repeatedly dividing the search interval in half. If the interval value is reset depending on whether the target value is greater than or less than the interval value. This is done repeatedly until the interval value == target value or the array is exausted.

#### Performance

In general, for any list of n, binary search will take log2 n steps to run in the worst case, whereas simple search will take n steps.

i.e. if you have an array of 128 length it will take 7 steps to get there. If that is doubled it will take 8. This is worked out using log base 2

### Selection Sort

Find the mininum element of the array and insert it into the beginning of the new array. Repeat looking in the main unsorted array for the next minimum value until all elements have been exhaused.

This process is O(n^2) as you have to go through n elements for the array n times.

## Data Structures

A data structure is a collection of data values, the relationships among them, and the functions or operations that can be applied to the data

### Linked Lists

Each item stores the address of the next item in the list. A bunch of
random memory addresses are linked together.

#### Pros

- You never have to move your items.

- Memory which isn't clustered together can be used.

- inserting and deleteing an element is O(1). Insertion can be done anywhere in the list, all memory locations will be updated.

#### Cons

- Difficult to access quckly an element in a list as you have to follow the trail of memory addresses

- Reading an element is O(n)

### Arrays

Arrays store data in memory sequentially so all the memory addresses are known.

#### Pros

- Can quickly lookup data from memory as the location is known.

- Reading an element is O(1)

#### Cons

- Big arrays are inefficient to store.

- Inserting an element into the beginning of an array is O(n). Inserting an element into the middle of an array requires relocation of all elements that come after it. Worse, if there is no space all elements need to be copied to a location where there is memory.

- Deleting an element in an array is O(n).
  NB: Given the next slot is available inserting an element to the end of an array is O(1)

### Arrays or Lists Which are used More?

Of corse it depends on the use case. Arrays are generally used more as they allow for random access from memory.

**_random access_**: Sequential access means reading the elements one by one, starting
at the first element. Linked lists can only do sequential access.

**_sequential access_**: Random access
means you can jump directly to the nth element

Alternatively a combination can be used. For example one can have an array of memory addresses that lead to lists for insertion or deletion.
