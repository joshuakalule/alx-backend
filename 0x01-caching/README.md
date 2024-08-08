# Caching Systems

Used to store data closer to the cpu for faster access.
A *caching system* is a mechanism used to store frequently accessed data in a location that is quickly and easily accesible.
This improves performance and efficiency of a system by reducing the time it takes to retrieve data.

## Definition of terms

- **cache miss**: when a block is not found in memory
- **capacity miss**: when a block cannot be added because the cache is full
- **compulsory miss**: when a block of cache has to be fetched from main memory for the first time
- **conflict miss**: when a block has been replaced in cache
- **Age bits**: tracks the order of access of blocks in cache. (Used by LRU, MRU, and PLRU)

## Cache systems design

1. **Block placement:** How the system decides where in cache to place a block from main memory. For example;

   i. *Direct mapping:* takes a block number and mods it with the number of lines in cache. Each block in main memory therefore can only be put in one slot  in cache.\
   ii. *Associative mapping:* each block can be placed anywhere in cache.\
   iii. *Set associative mapping:* ??

2. **Block identification:** How the system finds the block of main memory in the cache

3. **Block replacement (During cache miss):** How to choose which slot in cache is to be replaced with the new requested block from main memory.\
**Cache replacement policies**

- FIFO (First In First Out): evicts the block that was added to cache first
- LIFO (Last In Last Out): evicts the block that was added last
- LRU (Least Recently Used): evicts the least recently accessed block
- MRU (Most Recently Used): evicts the most recently used block
- PLRU* (Pseudo - Least Recently Used): generates approximate measures for replacement
- LFU (Least Frequently used): evicts the least frequently used block
- MFU (Most frequently used): evicts the most frequently used block

&emsp;&emsp;***Note:*** In case of a tie, *FIFO* is used as a tie breaker for the block to be evicted

4. **Write stategy:** How updates are propagated.
This occurs under two scenarios;\
a. *Write hit*: when data is present in cache\
&emsp;i. Write through: cache and main memory are both updated simultaneously\
&emsp;ii. Write Back: cache is updated in real time, main memory is only updated during replacement.\
b. *Write Miss:* When data is present in the cache\
&emsp;i. Write allocate: bring to cache then update\
&emsp;ii. update directly in main memory
