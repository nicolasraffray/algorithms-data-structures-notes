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

On big O charts the input size goes along the x-axis and time along the y.

##### Why should Big O be used?

It establishes the worst case run of your algorithm, the most number of iterations it will take the algorithm.

#### Big O Examples:

![BigO](/images/BigO_graph.png)

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

An example of one of these algorithms is Euclids Algorithm which is an algorithm for computing the greatest common divisor (GCD). This is done through successive division until there is no longer a remainder and we have arrived at the base case.

---

### Quick Sort

Quick-Sort is a type of recursive D&C algorithm. However, the idea behind the algorithm is focused on a pivot.

One of the items in the array, the goal is to put the pivot in the correct position in the final array. All items to the right are larger and all items to the left are smaller.

So, quicksort gives 2 arrays one with the numbers greater than the pivot and one with the numbers less than the pivot. What is returned by the algorithm is the combination of the 'small number array' pivot and 'large number array'.

The pivot is typically selected as the first element of the array. However another popular method is to just select the first element of the array.

#### Performance

On average quikcsort tkaes O(n log n) comparisons to sort items. however, in the worst case it is O(n^2)

#### Understanding Average Performance and Worst Case Performance

Quick sort doesnt check if the array is already sorted.

Worst Performance: If the array is already sorted the two arrays are created at every iteration one where the array is empty and the other with all of the remaining elements asside from the pivot. **The height of the call stack will be the length of the array**.

Average Case: In the average case, where the array isn't sorted, pivots are selected randomly. Hence the number of levels in the call stack is log(n).

#

NB: The constant almost never matters for simple search versus binary search, because O(log n) is so much faster than O(n) when your list gets big.

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

---

### Hash Tables

From a high level perspective a hash stable is a key value lookup. Strings are typically used as the key but it can be any value. Ideally we want to store values in an array, and have the strings correspond to the values. To do this we use a **Hash Function**.

**Hash Function:** Takes in a string converts it to an integer and then re-maps that integer into and index for the array in question. The array is often much smaller than the number of hash codes. Hence the mapping looks something like:

String -> Hash Code -> Index

Ideally you want your hash function top mapp evenly across the array

Collisions: Because there are an infinite number of strings but only a finite number of hashcodes the same string can be matched to the same hashcode. Also two things with different hash codes could actually wind up with the same index.

Dealing With Collitions:

- Chaining: When there are collisions store them in a linked list. These linked list will contain the values you want and the original keys.

- Low Load factor = (Number of items in hash table)/(Total number of Slots) when the load factor is greater than 1 you should think about resizing the array. The lower the load factor the fewer the amound of collisions. You should also consider that you don't want to resize too oftes as it is quite computationally expensive.

Hash Table To Do:

- Different methods of dealing with collisions.
- Growth and Shrinkage of HashTables.

#### Performance and Runtime

In a well constructed HashTable Runtime should be O(1).

If the hash function is bad the worst case is linear time, O(n). If linked lists get long in the hash table it increases the time for search, get and put.

![BigO](/images/Hash_performance.png)

#### Hash Table Use Case

Hash Tables can be used for Caching.

**Caching:** A cache is a temporary storage area. For example, the files you automatically request by looking at a Web page are stored on your hard disk in a cache subdirectory under the directory for your browser. When you return to a page you've recently looked at, the browser can get those files from the cache rather than the original server, saving you time and saving the network the burden of additional traffic.
