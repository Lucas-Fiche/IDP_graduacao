import heapq

def dijkstra(graph, start, n):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    distances = dijkstra(graph, 1, n)

    max_distance = -1
    for i in range(2, n + 1):
        if distances[i] < float('inf'):
            max_distance = max(max_distance, distances[i])
    
    if max_distance == -1:
        print("Impossivel chegar")
    else:
        print(f"Casa mais distante a {max_distance} metros")

if __name__ == "__main__":
    main()
