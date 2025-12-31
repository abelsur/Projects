# abel surafel assignment 3 CSE 5311

import csv
import math
from collections import defaultdict
import heapq

data = "/Users/abelsurafel/Downloads/assignment-3-graph-algorithms-abelsur/data"
nodes = f"{data}/nodes.csv"
edges = f"{data}/edges.csv"


def load_graph():
    id_to_name = {}
    name_to_id = {}

    with open(nodes, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            nid = int(row["node_id"])
            name = row["name"].strip()
            id_to_name[nid] = name
            name_to_id[name] = nid

    if "Orlanda" in name_to_id and "Orlando" not in name_to_id:
        name_to_id["Orlando"] = name_to_id["Orlanda"]

    graph = defaultdict(list)
    with open(edges, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            u = int(row["node1"])
            v = int(row["node2"])
            latency = int(row["latency"])
            bandwidth = int(row["bandwidth"])

            graph[u].append((v, latency, bandwidth))
            graph[v].append((u, latency, bandwidth))  # undirected

    return graph, id_to_name, name_to_id



def reconstruct_path(prev, start, end):    
    if start == end:
        return [start]
    if prev[end] is None:
        return []  # no path
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return path


def path_to_names(path, id_to_name):
    return " -> ".join(id_to_name[n] for n in path)


# connected components 

def connected_components(graph, node_ids):
    visited = set()
    components = []

    for node in node_ids:
        if node in visited:
            continue
        stack = [node]
        visited.add(node)
        comp = []
        while stack:
            u = stack.pop()
            comp.append(u)
            for v, _, _ in graph[u]:
                if v not in visited:
                    visited.add(v)
                    stack.append(v)
        components.append(comp)
    return components


# latency

def shortest_path_latency(graph, node_ids, start, end):   
    dist = {nid: math.inf for nid in node_ids}
    prev = {nid: None for nid in node_ids}

    dist[start] = 0
    heap = [(0, start)] 

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        if u == end:
            break
        for v, latency, _ in graph[u]:
            nd = d + latency
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(heap, (nd, v))

    path = reconstruct_path(prev, start, end)
    return dist[end], path


#  max bandwidth 

def widest_path_bandwidth(graph, node_ids, start, end):
    max_bw = {nid: 0 for nid in node_ids}
    prev = {nid: None for nid in node_ids}

    max_bw[start] = float("inf") 
    heap = [(-max_bw[start], start)]  # max-heap

    while heap:
        neg_bw, u = heapq.heappop(heap)
        bw_u = -neg_bw

        if bw_u < max_bw[u]:
            continue
        if u == end:
            break

        for v, _, edge_bw in graph[u]:     
            candidate = min(bw_u, edge_bw)
            if candidate > max_bw[v]:
                max_bw[v] = candidate
                prev[v] = u
                heapq.heappush(heap, (-candidate, v))

    path = reconstruct_path(prev, start, end)
    return max_bw[end], path


def main():
    graph, id_to_name, name_to_id = load_graph()
    node_ids = list(id_to_name.keys())

    comps = connected_components(graph, node_ids)
    print(f"Number of connected components: {len(comps)}")
    for i, comp in enumerate(comps, start=1):
        names = [id_to_name[nid] for nid in comp]
        print(f"  Component {i}: {names}")
    print()

    # problem 1
    def solve_latency(src_name, dst_name):
        s = name_to_id[src_name]
        t = name_to_id[dst_name]
        dist, path = shortest_path_latency(graph, node_ids, s, t)
        print(f"Optimal latency route from {src_name} to {dst_name}:")
        print(f"  Path: {path_to_names(path, id_to_name)}")
        print(f"  Total latency: {dist} ms\n")

    solve_latency("Dallas", "Seattle")
    solve_latency("Los Angeles", "New York")
    solve_latency("Orlando", "Chicago")  

    # problem 2
    def solve_bandwidth(src_name, dst_name):
        s = name_to_id[src_name]
        t = name_to_id[dst_name]
        bw, path = widest_path_bandwidth(graph, node_ids, s, t)
        print(f"Maximum-bandwidth path from {src_name} to {dst_name}:")
        print(f"  Path: {path_to_names(path, id_to_name)}")
        print(f"  Maximum bandwidth: {bw} Gbps\n")

    solve_bandwidth("Atlanta", "New York")
    solve_bandwidth("Dallas", "Seattle")
    solve_bandwidth("Chicago", "New York")


if __name__ == "__main__":
    main()
