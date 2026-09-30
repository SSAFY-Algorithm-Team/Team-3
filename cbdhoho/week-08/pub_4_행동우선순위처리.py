actions = [[0, 4, 5], [2, 1, 3], [3, 5, 2], [7, 2, 2]]

interrupted_count = 0
resolved_count = 0
discarded_count = 0

current_end = -1
current_priority = float('inf')

for order_time, priority, action_time in actions:
    if current_end != -1 and current_end <= order_time:
        resolved_count += 1
        current_end = -1
        current_priority = float('inf')
        
    if current_end == -1:
        current_end = order_time + action_time
        current_priority = priority
    else:
        if priority < current_priority:
            interrupted_count += 1
            current_end = order_time + action_time
            current_priority = priority
        else:
            discarded_count += 1
            
if current_end != -1:
    resolved_count += 1
    
print([interrupted_count, resolved_count, discarded_count])