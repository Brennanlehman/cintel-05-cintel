
from collections import deque

# Create an empty deque
empty_deque = deque()
print(empty_deque) 

# Create a deque by passing in a list with values
temp_deque_F = deque( [56, 58, 47, 54, 55] )
print(temp_deque_F)  

# Create a deque by passing in a list variable
temp_list_C = [5, 6, 8, 4, 3, 2]
temp_deque_C = deque( temp_list_C )
print(temp_deque_C )

temp_deque_F.append(60)
temp_deque_F.append(62)
temp_deque_F.append(64)
temp_deque_F.append(61)
print(temp_deque_F)

temp_deque_F.pop()  
temp_deque_F.popleft()
print(temp_deque_F)

len(temp_deque_F) 
print(len(temp_deque_F))
