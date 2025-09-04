import heapq
h = []
heapq.heappush(h, 4) 
heapq.heappush(h, 10)
heapq.heappush(h, 3)
heapq.heappush(h, 5)
heapq.heappush(h, 1)
x = heapq.heappop(h) 
top = h[0] 
h = [10,5,4,3,1]

heapq.heapify(h) 
print(h)


#Heap Sort tem complexidade O(n log n) no pior, melhor e caso médio, 
#pois a construção do heap é O(n) e cada remoção do maior elemento é O(log n).