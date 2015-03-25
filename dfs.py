from collections import deque
def depthFirst(startingNode, soughtValue):
   visitedNodes = set()
   stack = [startingNode]

   while len(stack) > 0:
      node = stack.pop()
      if node in visitedNodes:
         continue
      visitedNodes.add(node)
      if node.value == soughtValue:
         return True

      for n in node.adjacentNodes:
         if n not in visitedNodes:
            stack.append(n)
   return False
def bfs(startingNode,soughtValue):
   visitedNodes = set()
   queue = deque()
   queue.append(staticmethod)
   while len(stack) > 0:
      node = queue.popleft()
      if node in visitedNodes:
         continue
      visitedNodes.add(node)
      if node.value == soughtValue:
         return True
      for n in node.adjacentNodes:
         if n not in visitedNodes:
            queue.append(n)
   return False