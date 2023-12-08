# Stacks and Queues:
# part 1:
# -------------------------------

# class Stack:
#   def __init__(self):
#     self.items=[]
#
#   def isEmpty(self):
#     if len(self.items) == 0:
#       return True
#     else:
#       return False
#
#   def push(self, value):
#     self.items.append(value)
#
#   def pop(self):
#     if self.isEmpty():
#       return None
#     return self.items.pop()
#
#
# input_to_check = str(input("Enter the value to check if palindrome: "))
# input_reversed = ""
# pal_stack = Stack()
# for character in input_to_check:
#     pal_stack.push(character)
# while not pal_stack.isEmpty():
#     last_char = pal_stack.pop()
#     input_reversed += last_char
# if input_to_check.lower() == input_reversed.lower():
#     print("the input is palindrom ")
# else :
#     print("the input is not palindrom")

# -------------------------------------------------------------
# part 2:
# -------------------------------

# class Node:
#     def __init__(self, value, next):
#         self.value = value
#         self.next = next
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0
#
#     def isEmpty(self):
#         return self.size == 0
#
#     def addAtTail(self, value):
#         n = Node(value, None)
#         if self.size == 0:
#             self.head = n
#             self.tail = n
#             self.size = 1
#         else:
#             self.tail.next = n
#             self.tail = n
#             self.size += 1
#
#     def deleteHead(self):
#         if self.size == 0:
#             return None
#         elif self.size == 1:
#             temp = self.head.value
#             self.head = None
#             self.tail = None
#             self.size = 0
#             return temp
#
#         else:
#             temp = self.head.value
#             self.head = self.head.next
#             self.size -= 1
#             return temp
#
#
# class Queue:
#     def __init__(self):
#         self.items = LinkedList()
#
#     def enqueue(self, value):
#         self.items.addAtTail(value)
#
#     def dequeue(self):
#         if self.items.isEmpty():
#             return None
#         return self.items.deleteHead()
#
#
# expression = str(input("enter your expression to check if balanced:"))
# exp_queue = Queue()
# balanced = True
# for term in expression:
#     exp_queue.enqueue(term)
#     print(term)
# while not exp_queue.items.isEmpty():
#     term_to_check = exp_queue.dequeue()
#     if term_to_check == ")" or term_to_check == "]" or term_to_check == "}":
#         balanced = False
#         break
#     elif term_to_check == "(":
#         matched = False
#         exp_queue1 = exp_queue
#         while not exp_queue1.items.isEmpty():
#             term_to_match = exp_queue1.dequeue()
#             if term_to_match == ")":
#                 matched = True
#                 break
#         if not matched:
#             balanced = False
#             break
#     elif term_to_check == "[":
#         matched = False
#         exp_queue1 = exp_queue
#         while not exp_queue1.items.isEmpty():
#             term_to_match = exp_queue1.dequeue()
#             if term_to_match == "]":
#                 matched = True
#                 break
#         if not matched:
#             balanced = False
#             break
#     elif term_to_check == "{":
#         matched = False
#         exp_queue1 = exp_queue
#         while not exp_queue1.items.isEmpty():
#             term_to_match = exp_queue1.dequeue()
#             if term_to_match == "}":
#                 matched = True
#                 break
#         if not matched:
#             balanced = False
#             break
# if balanced:
#     print("the expression is balanced ")
# else:
#     print("the expression is not balanced ")

# -----------------------------------------------------------
# Stack:
# --------------------------

# class Stack:
#   def __init__(self):
#     self.items=[]
#
#   def isEmpty(self):
#     if len(self.items) == 0:
#       return True
#     else:
#       return False
#
#   def push(self, value):
#     self.items.append(value)
#
#   def pop(self):
#     if self.isEmpty():
#       return None
#     return self.items.pop()
#
#
# encoded_message = str(input("Enter the encoded message: "))
# message_stack = Stack()
# decoded_message = ""
# for character in encoded_message:
#     if character == "*":
#         decoded_message += message_stack.pop()
#     else:
#         message_stack.push(character)
# for i in range(len(message_stack.items)):
#     decoded_message += message_stack.pop()
# print(decoded_message)

# -----------------------------------------------------------
# Linked Lists- removing a node at a given location:
# -------------------------------

# class Node:
#
#     def __init__(self, value, next):
#         self.value = value
#         self.next = next
#
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0
#
#     def addAtHead(self, value):
#         n = Node(value, None)
#         if self.size == 0:
#             self.head = n
#             self.tail = n
#             self.size = 1
#         else:
#             n.next = self.head
#             self.head = n
#             self.size += 1
#
#     def addAtTail(self, value):
#         n = Node(value, None)
#         if self.size == 0:
#             self.head = n
#             self.tail = n
#             self.size = 1
#         else:
#             self.tail.next = n
#             self.tail = n
#             self.size += 1
#
#
#     def deleteHead(self):
#         if self.size == 0:
#             return None
#         elif self.size == 1:
#             temp = self.head.value
#             self.head = None
#             self.tail = None
#             self.size = 0
#             return temp
#
#         else:
#             temp = self.head.value
#             self.head = self.head.next
#             self.size -= 1
#             return temp
#
#     def deleteTail(self):
#         if self.size <= 1:
#             return self.deleteHead()
#
#         current = self.head
#         temp = self.tail.value
#         while current.next.next != None:
#             current = current.next
#
#         current.next = None
#         self.tail = current
#         self.size -= 1
#         return temp
#
#     def printLL(self):
#         if self.size == 0:
#             print("my LL is empty")
#         current = self.head
#         while current != None:
#             print(current.value, "->", end=" ")
#             current = current.next
#         print()
#
#     def deleteAtLocation(self, index):
#         if self.size == 0:
#             print("my LL is empty")
#         if index == 0 :
#             self.deleteHead()
#         if index == self.size-1:
#             self.deleteTail()
#         else:
#             current = self.head
#             for i in range(index-1):
#                 current = current.next
#             temp = current.next.value
#             current.next = current.next.next
#             return temp
#
#
# ll = LinkedList()
# ll.addAtTail(12)
# ll.addAtTail(56)
# ll.addAtTail(76)
# ll.addAtTail(11)
# ll.addAtTail(0)
# ll.printLL()
# ll.deleteAtLocation(3)
# ll.printLL()

# -----------------------------------------------------------------
# Graphs:
# Part 1:
# -----------------------------------------------------------------
class Node:
  def __init__(self,value,next):
    self.value=value
    self.next=next


class LinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
    self.size=0

  def addAtHead(self,value):
    n=Node(value,None)
    if self.size==0:
      self.head=n
      self.tail=n
      self.size=1
    else:
      n.next=self.head
      self.head=n
      self.size+=1

  def addAtTail(self,value):
    n=Node(value,None)
    if self.size==0:
      self.head=n
      self.tail=n
      self.size=1
    else:
      self.tail.next=n
      self.tail=n
      self.size+=1

  def search(self,info):
    if self.size==0:
      return False

    current=self.head

    while current != None:
      if current.value == info:
        return True
      else:
        current=current.next
    return False

  def deleteHead(self):
    if self.size==0:
      return None
    elif self.size==1:
      temp=self.head.value
      self.head=None
      self.tail=None
      self.size=0
      return temp

    else:
      temp=self.head.value
      self.head=self.head.next
      self.size-=1
      return temp


  def deleteTail(self):
    if self.size <= 1:
      return self.deleteHead()

    current = self.head
    temp = self.tail.value
    while current.next != self.tail:
      current = current.next

    current.next=None
    self.tail=current
    self.size-=1
    return temp

  def printLL(self):
    if self.size == 0:
      print("my LL is empty")
    current = self.head
    while current!= None:
      print(current.value, "->", end=" ")
      current = current.next
    print()

  def deleteValue(self, value):
    elements = []
    while self.size > 0:
      temp = self.deleteHead()
      if temp != value:
        elements.append(value)
    for i in elements:
      self.addAtHead(i)


class AdjacencyList:
  def __init__(self, V):
    self.list_LL=[]
    for i in range(V):
      self.list_LL.append(LinkedList())

  def addEdge(self, vs, ve):
    if not self.list_LL[vs].search(ve):
      self.list_LL[vs].addAtHead(ve)

  def deleteEdge(self, vs, ve):
    if self.list_LL[vs].search(ve):
      self.list_LL[vs].deleteValue(ve)

  def showGraph(self):
    for i in range(len(self.list_LL)):
      print("(", i, ")", end="")
      self.list_LL[i].printLL()

#Part 3:
  def getVerticesInCommon(self, v1, v2):
    V=len(self.list_LL)
    print("the  common verticies are: ")
    for i in range(V):
      if self.list_LL[v1].search(i) and self.list_LL[v2].search(i):
        print(i, end=" ")
    print()

# checkEdge and printDirectlyConnected are the functions for part 1

  def checkEdge(self, city1, city2):
    edge_found = self.list_LL[city1].search(city2) or self.list_LL[city2].search(city1) #this is to mimic an undirected graph
    if edge_found:
        print("There is a route between city ", city1, " and city ", city2)
    else:
        print("There is not a route between city ", city1, " and city ", city2)

  def printDirectlyConnected(self, city):
      print("the cities directly connected to city", city, "are: ")
      self.list_LL[city].printLL()


g2 = AdjacencyList(4)
g2.addEdge(0, 1)
g2.addEdge(0, 2)
g2.addEdge(0, 3)
g2.addEdge(1, 3)
g2.addEdge(1, 2)
g2.addEdge(3, 1)
g2.addEdge(3, 2)
g2.addEdge(3, 0)
g2.addEdge(2, 3)
g2.showGraph()
g2.getVerticesInCommon(0, 3)
# g2.checkEdge(2, 1)
# g2.printDirectlyConnected(1)
# -----------------------------------------------------------------
# Part 2: I did not figure it out... here is what i found about it on
# (https://www.geeksforgeeks.org/detect-cycle-in-a-graph/)
# -----------------------------------------------------------------

# from collections import deque
#
#
# class Graph:
#     def __init__(self, V):
#         self.V = V
#         self.adj = [[] for _ in range(V)]
#
#     def addEdge(self, v, w):
#         self.adj[v].append(w)
#
#     def isCyclic(self):
#         inDegree = [0] * self.V
#         q = deque()
#         visited = 0
#
#         # Calculate in-degree of each vertex
#         for u in range(self.V):
#             for v in self.adj[u]:
#                 inDegree[v] += 1
#
#         # Enqueue vertices with 0 in-degree
#         for u in range(self.V):
#             if inDegree[u] == 0:
#                 q.append(u)
#
#         # BFS traversal
#         while q:
#             u = q.popleft()
#             visited += 1
#
#             # Reduce in-degree of adjacent vertices
#             for v in self.adj[u]:
#                 inDegree[v] -= 1
#                 # If in-degree becomes 0, enqueue the vertex
#                 if inDegree[v] == 0:
#                     q.append(v)
#
#         return visited != self.V  # If not all vertices are visited, there is a cycle
#
#
# # Main driver code
# g = Graph(6)
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 3)
# g.addEdge(4, 1)
# g.addEdge(4, 5)
# g.addEdge(5, 3)
#
# if g.isCyclic():
#     print("Graph contains a cycle.")
# else:
#     print("Graph does not contain a cycle.")

# -----------------------------------------------------------------
