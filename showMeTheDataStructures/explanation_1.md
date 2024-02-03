#1 LRU Cache
Time complexity of methods:
__init__: O(1) (Initialize cache with a fixed size).
get: O(1) (Retrieve element from cache).
set: O(1) (Add or update elements in cache).


#2 File Recursion
We use a list to store paths as required by the problem. Appending an element to a list has a complexity of O(1), while extending a list has a complexity of O(k), where 'k' is the number of elements to be added.

We also use recursion, again as required by the problem. However, recursion introduces additional overhead, as it requires extra memory for function arguments, stack unwinding, and passing control back to the calling function, among other steps. This also takes some extra time. In this specific problem, there isn't a deep directory structure, so the memory or space used depends on the number of recursive calls, which determines the number of stack frames, multiplied by the space required for each stack frame. This would be O(n*m), with 'n' being the number of calls and 'm' being the space required for each frame


#3 Huffman Encoding
Counting Frequencies (O(n)): The algorithm starts by counting the frequencies of each character in the input text. This requires iterating through the entire input string, which has a time complexity of O(n), where n is the length of the input.

Priority Queue Operations (O(log n)): The algorithm uses a priority queue (min-heap) to manage the frequency nodes of characters. In each iteration, it removes the two nodes with the lowest frequencies from the queue and creates a new node with their sum. The insertion of a node into a min-heap has a time complexity of O(log n), where n is the number of nodes in the heap. In the worst case, the heap can contain all distinct characters, resulting in O(log n) complexity for each insertion.

Building the Huffman Tree (O(n * log n)): The process of repeatedly removing the two nodes with the lowest frequencies and creating a new node continues until there is only one node left in the heap, which represents the root of the Huffman tree. In the worst case, this process can take O(n) iterations, and each iteration involves an O(log n) operation. Therefore, the overall complexity for building the Huffman tree is O(n * log n).

Encoding and Decoding (O(n)): Once the Huffman tree is constructed, encoding and decoding individual characters have a time complexity of O(log n), but when applied to the entire input text, it becomes O(n).

The dominant factor in the worst-case time complexity is the construction of the Huffman tree, which is O(n * log n). This is because the number of nodes in the heap (and, by extension, the tree) can grow logarithmically with respect to the number of distinct characters in the input text. Hence, the overall worst-case time complexity of the Huffman algorithm is O(n * log n).


#4 Active Directory
The complexity of the is_user_in_group algorithm can be described as follows:
If we consider n as the number of user accounts in all groups and m as the number of groups, then the complexity of this algorithm depends on n and m.
In the worst case, the algorithm traverses all user accounts and groups in the entire group tree. Each time we check whether a user account is in a group or not, we need to compare the account with the list of user accounts in that group, which has O(n) complexity.
Additionally, we also iterate through all the child groups in a parent group. The number of visits to the subgroups depends on m.
Therefore, the total complexity of the algorithm is O(n * m) in the worst case, where n is the number of user accounts and m is the number of subgroups in the group tree.
To explain, the algorithm must consider each user account in each group and each subgroup in the group tree, so the complexity is proportional to the total number of user accounts and number of subgroups.

Note that this complexity can be a linear (O(n * m)) or sublinear complexity, depending on the specific structure of the group tree.




#5 Blockchain
Complexity of main methods:
Block.calc_hash(): This method calculates the hash code for each block using the hashlib library. Hash code calculation time is O(1), regardless of data size.
Chain.append(): This method adds a block to the chain. This operation typically has O(1) complexity because it only involves adding a block to the end of the string and updating the tail pointer.
Since both main methods (Block.calc_hash() and Chain.append()) have O(1) complexity, the total complexity of the test cases in main() is also O(1).
To summarize, the complexity of this code is O(1) for each method, because we do not have loops or complex algorithms that depend on the data size in the blockchain.

#6 Union & Intersection
The union method creates a set to store unique values from both linked lists. It then uses these unique values to create a new linked list.
The intersection method creates two sets to store the unique values of each linked list. It then finds common values between the two sets and uses them to create a new linked list.
The complexity of both methods is O(m + n), where m and n are the sizes of linked lists 1 and 2, respectively. Each linked list is traversed once, and the operations with the set having average complexity O(1). Therefore, the total complexity of the union and intersection methods is O(m + n).



