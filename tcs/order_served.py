'''
raj is running the busiest cafe in the city, it is also the most visited cafe by vips
vips buy costly beverage, it also give raj high profit. raj asked his workers to prefer serving VIP first because VIPs don't like to wait much time. whenever a person orders something raj gives priority value to the order and add it to the queue. the greater the value more important the order is. the worker starts to serve the order with high priority in queue ensuring that the VIPs gets their order quickly. however, those orders having low priority have to wait for a long time in queue, upsetting those people. this reduces the total number of people visiting the cafe and reducing the profit. but making first come first serve basis reduces the vips visiting the cafe.this also reduces the profit. 
raj came up with a new idea to keep the profit high. he introduced a new concept called dynamic priority. the priority of order changes while in the queue. raj will maitain queue of orders and assigned priority, adding new orders at the end. the order with high priority in queue will be served first. when an order gets served due to its high priority, the priority of orders before this in the queue will be increased by 1. if 2 orders having same priority then order that was enqued first will be will be served first. this strikes a balance between reducing the waiting time of vips and also serving other people without much delay. 
one day his friend visited the cafe and ordered something . as usual his order got some priority and got added in the queue. after sometime his friend lost his patience and asked when his order will be served. after that raj stopped adding new order to the queue and started calculating after how many orders his friend will get served , considering only orders currently in the queue. given the queue find after how many orders will raj friend be served
'''

import heapq

def when_will_friend_be_served(queue, friend_position):
    # Priority queue to serve orders by priority, storing (-priority, position) for max heap behavior
    max_heap = []
    n = len(queue)
    
    # Initialize the heap with all orders from the queue
    for i in range(n):
        priority, position = queue[i]
        heapq.heappush(max_heap, (-priority, position))  # Negative priority for max heap
    
    orders_served = 0
    
    while max_heap:
        # Get the highest priority order from the heap
        current_priority, current_position = heapq.heappop(max_heap)
        current_priority = -current_priority  # Convert back to positive
        
        # Check if this is the friend's order
        if current_position == friend_position:
            # Return the number of orders served before the friend's order is served
            return orders_served + 1
        
        # Increment the served orders counter
        orders_served += 1
        
        # Now we need to update the priorities of the orders ahead in the queue
        new_heap = []
        while max_heap:
            priority, position = heapq.heappop(max_heap)
            # Increment priority if this order was ahead of the served one
            if position < current_position:
                priority -= 1
            heapq.heappush(new_heap, (priority, position))
        
        max_heap = new_heap  # Rebuild the heap with updated priorities
    
    return -1  # In case the friend's order was not found (shouldn't happen)


# #o/p : 6
# queue = [(1, 0), (3, 1), (5, 2), (2, 3), (4, 4), (6, 5)]
# friend_position = 3

# result = when_will_friend_be_served(queue, friend_position)
# print(result)

# #o/p: 3
# queue = [(1, 0), (4, 1), (3, 2), (2, 3), (5, 4)]
# friend_position = 2

# result = when_will_friend_be_served(queue, friend_position)
# print(result)

len_of_queue = int(input())
values = input().split()
queue: list = []
for i in range(len_of_queue):
    queue.append((int(values[i].strip()), i))

pos_of_friend = int(input())
#print(queue, pos_of_friend)6
result = when_will_friend_be_served(queue, pos_of_friend-1)
print(result)



