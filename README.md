<center><h1> Algorithms and Data Structures </h1></center>

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

---

### Binary Search

#

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

#

These are a set of recursive algorithmns. They are divised using two steps:

1. Figure out the simplest base case
2. Divide or decrease the problem until it becomes the base case

An example of one of these algorithms is Euclids Algorithm which is an algorithm for computing the greatest common divisor (GCD). This is done through successive division until there is no longer a remainder and we have arrived at the base case.

---

### Quick Sort

#

Quick-Sort is a type of recursive D&C algorithm. However, the idea behind the algorithm is focused on a pivot.

One of the items in the array, the goal is to put the pivot in the correct position in the final array. All items to the right are larger and all items to the left are smaller.

So, quicksort gives 2 arrays one with the numbers greater than the pivot and one with the numbers less than the pivot. What is returned by the algorithm is the combination of the 'small number array' pivot and 'large number array'.

The pivot is typically selected as the first element of the array.

#### Performance

On average quikcsort tkaes O(n log n) comparisons to sort items. however, in the worst case it is O(n^2)

#### Understanding Average Performance and Worst Case Performance

Quick sort doesnt check if the array is already sorted.

Worst Performance: If the array is already sorted the two arrays are created at every iteration one where the array is empty and the other with all of the remaining elements asside from the pivot. **The height of the call stack will be the length of the array**.

Average Case: In the average case, where the array isn't sorted, pivots are selected randomly. Hence the number of levels in the call stack is log(n).

#

NB: The constant almost never matters for simple search versus binary search, because O(log n) is so much faster than O(n) when your list gets big.

---

### Breadth First Search

#

Summary:

1. Keep a queue containing nodes to check.
2. Pop a node off the queue.
3. Check whether it matches the node you are looking for.
   4a. If yes then done.
   4b. If No add their neighbours to the queue.
4. Loop
5. If queue empty the node is not there.

This algorithm models the problem as a graph.

What is it trying to solve?

- Is there an existing path from A to B?
- What is the path from A to B?

First the algorithm looks through the entire network for a path adding nodes and their connecting nodes to a list until the relevant node has been found.

Once the node is found you want to figure out how many degrees of separation you are from that node. First Degree connections are added to a list for searching first and then second degrees and so on.

The data structure for holding the elements to be searched is called a _queue_. A queue has only two operations _enqueue_ and _dequeue_. A queue is **FIFO** First in first out. Compared to a stack which is **LIFO** Last in first out.

A record should also be kept of the nodes that have been searched to avoid infinite loops.

#### Performance

To search an entire network one needs to go along all edges O(E). Adding one person to the queue taking constant time O(1). Then do this for every node O(V).

Hence performance is on average O(E + V)

---

### Dykstras Algorithm

#

Steps in Short:

1. Find the node you can get to in the least amount of time.
2. Update the costs of the neighbors of this node.
3. Repeat until this is complete for all nodes
4. Calculate the final path.

Summary:

- Breadth first search is used to calc the shortest path for an _unweighted_ graph.
- Dijkstra's algorithm is used to calculate the sortest path for a _weighted_ graph.
- It works well when all the weights are postive.
- If you have negative weights, use the Bellman-Ford algorithm.

#### Problem its trying to solve.

Breadth first search will always find the shortest path. However, if you assume that the nodes have a time component attached to them. **Breadth First won't always find the fastest path**. In an unweighted graph use breatdth first search.

#### Terms

Weights: Numbers associated with edges. i.e Time from node a to b. Graphs can be either weighted or unweighted.

Recall that a undirected graph, each edge adds another cycle. Dijkstra's alog only works with _directed acyclic graphs_ (DAGs).

DAG: Every edge goes from earlier in ordering to later in ordering.

#### Understanding Negative weights

One cannot use Djikstras if there are negative weights.

This is because if you take the route of a negative edge it updates the values of the corresponding edges at the node you have arrived at. This is a big problem if the algorithm has already processed the node, if this is the case the algorithm will end.

If there are negative weights one should use Bellman-Ford.

#### Implementation

Not only do neighbors need to be stored but also costs. This is done with hash tables inside hash tables.

It will look something like the following:

```python
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {} # end node has no neighbors.
```

You weill also need a has table to store costs for each node.

```python
infinity = float('inf')
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity
```

Parents should also be represented:

```python
parents = {}
parents['a'] = "start"
parents['b'] = "start"
parents['fin'] = None

# then an array of nodes you have processed.
processed = []
```

In sudo code the implementation will be as follows:

While there are nodes to process:
Get the node closest to the start,
update costs for its neighbors,
if any of costs are updated:
update parents costs.
Mark node processed

---

### Greedy Algorithms

#

Quick Summary:

- Greedy algos optimize locally, hoping to end up with a global optimum.
- NP-complete problems have no known fast solution.
- If you have an NP-complete problem, your best bet is to use an approximation algo.
- Greedy algos are easy to write and fast to run, so they make for good approximation algorithms.

---

**Definition**: A greedy algorithm is any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage.

#### Approximation Algoritm

When calculating the exact solution will take too much time, an approximation alog is used. They are judged by:

1. How fast they are
2. How close they get to the optimal solution.

### NP Complete Problems

Definition: NP (non-deterministic polynomial time) complete problems have no known fast solution.

An exapme of a NP-complete problem is the travelling salesman problem.

Is it NP Complete?:

1. Your algorithm run quickly with a handful of items but really slows down with more items
2. "All combinations of X" usually point to an NP-complete problem.
3. If you have to calculate "every possible version" of X bc it can't be broken down it may be NP complete.
4. Can you restate the problem as the set-covering problem of the travelling-salesperson problem? If so then its NP-complete.

---

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

---

### Graphs

Graphs are an abstract datatype that model a set of connections.

Their structure is a finite set of **nodes** (or vertices), which are connected as unordered pairs. These connections are known as **edges**. Nodes that are connected are commonly reffered to as **neighbours**.

- _Directed Graph_: Contains an ordereed pair of vertices.

- _Undirected Graph_: Contains an unordered pair of vertices. Both nodes are eachothers neighbours. Hence no arrows in the diagram below.

![Graphs](/images/Graphs.png)

What does this look like in code?

Lets take the examples of English Cities and Towns

```python
graph = {}
graph["London"] = ["Watford", "Slough", "Croydon"]
graph["Watford"] = ["Luton"]
graph["Slough"] = ["Reading"]
graph["Croydon"] = []
graph["Luton"] = []
graph["Reading"] = []
```

The keys represent the nodes and the arrays are the neighbours.
