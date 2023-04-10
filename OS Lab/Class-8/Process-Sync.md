# `For Final`

# Process Synchronization
- Sync processes to work together by exchanging informations.

<br>

## Critical Section
 - A code section where sync issue can occurs.

### **Solutions**
 - Mutual Exclusion
 - Progress
 - Bounded Waiting
  
> Most viable option is `Mutex Lock`.

<br>

### **`Mutex Lock`**
 - It means `Mutual Exclusion Lock`.
 - Process that comes first or got the resources first will lock and other will wait untill occupied resources get free.
 - It can not ensure to fix or couse `Deadlock`

**`Limitations`**
 - Solves very limited numbers of problem.
 - Not all senario can be solve with it. (eg: Readers-Writers)

<br>

### **`Semaphore`**
 - It's a data type `(unsinged int)`.
 - It includes a few more functions.
    - `wait()` -> decrease semaphore value
    - `singnal()` -> increase semaphore value
  - 2 Types
    - Binary -> 0, 1
    - Counting -> 0 - N
  - It's value can't be lower than `0`.
> With `Binary Semaphore` we can implement `Mutex Lock`.

<br>

## Race Condition
 - Increase and decrease a variables value with condition....

<br>

# Sync + IPC (Inter Process Communication)
 - Can be done via many way. One of them is `Shared Memory`.



# Readers-Writers Problem
 - It's a problem where there will be only 2 types of process. Reader and writers. Reader will read a memory and writers will write data to the memory. Now, suppose all readers are tryiong to access the memory but only one of then got the access in general. But we can actually give access to all the reader because they won't the data. However, in `Mutex Lock` it's not possible. We have to use `Counting Semaphone` here. We also need to use `Binary Semaphore` to stop readers and writers access at the same time.

<br>

# Producer-Consumer Problem
 - Unlike readers-writers problem `Producer` and `Consumer` can't be allowed multiple process from any type. Because all of them is writing data.

```
I am too sleepy to write codes.
codes in the lab manual.
```

<!-- Dining Phelosopher Problem -->