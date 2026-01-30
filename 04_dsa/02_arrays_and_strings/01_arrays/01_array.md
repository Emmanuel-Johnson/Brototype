# Arrays

## 1. WHAT

An **array** is a data structure used to store multiple values of the same type in a single, continuous memory block, so they can be accessed using an index.

## 2. WHY

Arrays solve the problem of managing many related values efficiently. Without arrays, handling repeated variables becomes messy, repetitive, and hard to scale or process.

## 3. WHERE

Arrays are used at the data-handling layer of applications, such as:

* Storing request data
* Processing input lists
* Buffering results
* Holding records in memory during execution

## 4. HOW

* Memory is allocated for a fixed number of elements
* Each element is stored at a specific index
* Elements are accessed or updated directly using their index value

## 5. WHEN

**Use arrays when:**

* The data size is known in advance
* Fast access by index is required

**Do not use arrays when:**

* Frequent insertions or deletions in the middle are needed

## 6. EXAMPLE

In a web application, an array can store a list of product prices fetched from the database to calculate totals or apply discounts.

## 7. PROS & CONS

**Pros:**

* Fast access
* Simple structure
* Efficient memory usage

**Cons:**

* Fixed size
* Inserting or deleting elements can be costly

## 8. COMMON MISTAKES

* Accessing elements out of bounds
* Using arrays where dynamic resizing is frequently required
