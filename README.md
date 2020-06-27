# Algorithms and Data Structures

These are my notes on the Grokking Algorithms textbook along with some implementation code done in Python.

## Key Concepts

### Recursion

The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called as recursive function.

Every Recursive function has two componentes:

- **_base case_:** The moment when the function does not call itself preventing an infinite loop.
- **_recursive case_:** The moment when the function calls itself.

#### The Stack

Description: It is a set of information that describes the set of active subroutines of a program. When a subroutine is completed it is removed from the stack. Hence, it has two actions:

- **_push_:** Add a new item to the top of the stack
- **_pop_:** Remove the topmost iteam and read it

Note: When you call a function from another function, the calling function is paused in a partially completed state. The recursive function still has access to the higher functions variables. However, not other variables in the stack.

Recursion uses lots of memory, this is because each iteration it continuously saves informations from each of the function calls.

Further Reading for later: Tail Recursion

---

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

---

## Algorithms

### Binary Search

Binary Search is a search method used for a sorted array to seek out the desired value within that array by repeatedly dividing the search interval in half. If the interval value is reset depending on whether the target value is greater than or less than the interval value. This is done repeatedly until the interval value == target value or the array is exausted.

#### Performance

In general, for any list of n, binary search will take log2 n steps to run in the worst case, whereas simple search will take n steps.

i.e. if you have an array of 128 length it will take 7 steps to get there. If that is doubled it will take 8. This is worked out using log base 2

---

### Selection Sort

Find the mininum element of the array and insert it into the beginning of the new array. Repeat looking in the main unsorted array for the next minimum value until all elements have been exhaused.

#### Performance

This process is O(n^2) as you have to go through n elements for the array n times.

---

### Divide and Conquer

These are a set of recursive algorithmns. They are divised using two steps:

1. Figure out the simplest base case
2. Divide or decrease the problem until it becomes the base case

## Data Structures

---

A data structure is a collection of data values, the relationships among them, and the functions or operations that can be applied to the data

---

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

---

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
