# sum1 = 0 #answer is 233168

# for i in range(1,1000):
#     if i%3 == 0 or i%5 == 0:
#         sum1 += i

# print(sum1)

######################################################################
# cache = {}

# def fib(n):
#     if n in cache:
#         return cache[n]

#     if n < 2:
#         value = 1

#     else:
#         value = fib(n-1) + fib(n-2)

    
#     cache[n] = value

#     return value

# print(fib(10))


####################################################################### Find target sum
# arr = [2, 5, 6, 7, 9, 13, 16, 19, 23]

# def targetSum(array, target):
#     i = 0
#     j = len(array)-1
    
#     while i != j:
#         if array[i] + array[j] == target:
#             return [i,j]
        
#         elif array[i] + array[j] > target:
#             j -= 1
        
#         else:
#             i += 1
    
#     return -1
    
    
# print(targetSum(arr, 42))

####################################################################### Count inversions in an array
#How many operations to make it sorted
# array = [10, 3, 9, 6, 1]
# output = []

# for i in range(len(array)):
#     for j in range(i+1, len(array[i:])):
#         if array[i] > array[j]:
#             output.append((array[i], array[j]))

# print(output)
# print(len(output))



####################################################################### 1481 Least Number of unique integers
# class Solution:
#     def findLeastNumOfUniqueInts(self, nums: List[int], k: int) -> int:
#         cache = {}
        
#         for num in range(len(nums)):
#             if nums[num] not in cache:
#                 cache[nums[num]] = 0
                
#             cache[nums[num]] += 1
            
#         cache = sorted(cache.items(), key = lambda x:x[1])
#         count = 0
#         l = 0
        
# #         for i, j in enumerate(cache):
# #             print(i,j)
# #             if j[1] <= k:
# #                 cache.pop(i)
                
# #             k -= j[1]
                
# #             if k == 0:
# #                 break
#         while k > 0:
#             if cache[l][1] <= k:
#                 # times.append(cache[l])
#                 count += 1
                
#             k -= cache[l][1]
            
#             l += 1
            
                
#         return len(cache) - count



# ####################################################################### 206 Reverse Linked List 1
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         prev = None
        
#         while head:
#             temp = head
#             head = head.next
#             temp.next = prev
#             prev = temp
            
#         return prev
        
    
####################################################################### 387 First unique character in string
# from collections import OrderedDict

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         cache = OrderedDict()
    
#         for i in range(len(s)):
#             if s[i] not in cache:
#                 cache[s[i]] = [0, i]
                
#             cache[s[i]][0] += 1
            
#         for x in cache:
#             if cache[x][0] == 1:
#                 return cache[x][1]
            
#         return -1


####################################################################### K Closest points to origin
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]: 
#         p = sorted(points, key = lambda x: x[0]**2 + x[1]**2)
#         return p[:k]


        # heap = [[-(i**2 + j**2), i, j] for i,j in points[:k]] 
        # heapq.heapify(heap)

        # for i,j in points[k:]:
        #     d = (i**2 + j**2)

        #     if -(heap[0][0]) > d:
        #         heapq.heapreplace(heap, [-d, i, j])

        # return [[i,j] for d,i,j in heap]




####################################################################### Economy Mart
# entries = [['INSERT', 'milk', 4], ['INSERT', 'coffee', 3], ['VIEW', '-', '-'], ['INSERT', 'gum', 1], ['VIEW', '-', '-'], ['INSERT', 'pizza', 2], ['INSERT', 'mouse', 6], ['INSERT', 'water', 2], ['INSERT', 'bag', 1], ['VIEW', '-', '-'], ['INSERT', 'creatine', 2], ['VIEW', '-', '-']]
# entries = [['INSERT', 'milk', 4], ['INSERT', 'coffee', 3], ['VIEW', '-', '-'], ['INSERT', 'pizza', 5], ['INSERT', 'gum', 1], ['VIEW', '-', '-']]
# entries2 = [['INSERT', 'milk', 4], ['INSERT', 'coffee', 3], ['INSERT', 'pizza', 5], ['INSERT', 'gum', 1], ['VIEW', '-', '-']]
# entries1 = [['INSERT', 'fries', 4], ['INSERT', 'soda', 2], ['VIEW', '-', '-'], ['VIEW', '-', '-'], ['INSERT', 'hamburger', 5], ['VIEW', '-', '-'], ['INSERT', 'nuggets', 4], ['INSERT', 'cookie', 1], ['VIEW', '-', '-'], ['VIEW', '-', '-']]

# def getItems(entries):
#     db, result, count = [], [], 0

#     for entry in entries:
#         if entry[0] == "INSERT":
#             db.append([entry[1], int(entry[2])])
        
#         if entry[0] == "VIEW":
#             db1 = updateDatabase(db)
#             count += 1
#             result.append(db1[count-1][0])
    
#     print(result)
        

# def updateDatabase(database):
#     database.sort(key = lambda x: (x[1], x[0]))
#     return database 
    
    
# getItems(entries)


####################################################################### Is same tree
def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q or (p.val != q.val):
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 

####################################################################### Subtree of another tree
def isSubtree(self, root, subRoot):
        def isSame(t, s):
            if not t and not s:
                return True
            
            if not t or not s:
                return False
            
            return (t.val == s.val) and isSame(t.left, s.left) and isSame(t.right, s.right)
            
            
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if isSame(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 



################################################################## Course schedule
def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        preMap = { i:[] for i in range(numCourses)}
        
        for crs, prereq in prerequisites:
            preMap[crs].append(prereq)
            
            
        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            
            if preMap[crs] == []:
                return True
            
            visited.add(crs)
            
            for pre in preMap[crs]:
                if not dfs(pre): 
                    return False
                
            visited.remove(crs)
            preMap[crs] = []
            
            return True
            
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        
        return True