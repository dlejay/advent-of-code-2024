from collections import defaultdict

def get_LAN(filename: str) -> dict[str: set]:
    with open(filename) as file:
        pairs = [line.strip().split("-") for line in file.readlines()]
    LAN = defaultdict(set)
    for pair in pairs:
        LAN[pair[0]].add(pair[1])
        LAN[pair[1]].add(pair[0])
    return LAN


def process_part1(filename: str) -> None:
    LAN = get_LAN(filename)
    sets_of_three_with_t = []
    for key in LAN:
        for x in LAN[key]:
            for y in LAN[key] & LAN[x]:
                if {key, x, y} not in sets_of_three_with_t and (
                    key.startswith("t") or x.startswith("t") or y.startswith("t")
                ):
                    sets_of_three_with_t.append({key, x, y})
    print(f"There are {len(sets_of_three_with_t)} sets of three with at least one starting with 't'.")

def open_neighbourhood(graph: dict[str: set], node: str) -> dict[str: set]:
    if node not in graph:
        return {}
    Ω = defaultdict(set)
    for n in graph[node]:
        Ω[n] = graph[node] & graph[n]
    return Ω

def mcs(graph: dict[str, set[str]], cache: dict[frozenset[str], int] = {}) -> int:
    """
    Takes an unordered graph and a cache, and returns the size of its maximal clique.
    """
    # Convert the graph into a hashable representation (frozenset of nodes)
    nodes = frozenset(graph.keys())
    if nodes in cache:
        return cache[nodes]
    
    if len(graph) == 0:
        return 0

    # Recursively compute the maximal clique size
    max_clique_size = 1 + max(
        mcs(open_neighbourhood(graph, n), cache) for n in graph
    )
    
    # Store the result in the cache
    cache[nodes] = max_clique_size
    return max_clique_size

def process_part2(filename: str) -> None:
    LAN = get_LAN(filename)
    cache = {}
    max_size = mcs(LAN, cache)
    nodes_in_mc = set()
    for node in sorted(LAN, key=lambda node: len(LAN[node]), reverse=True):
        if len(LAN[node]) < max_size - 1:
            continue
        if mcs(open_neighbourhood(LAN, node)) == max_size - 1:
            nodes_in_mc.add(node)
        if len(nodes_in_mc) == max_size:
            break
    password = ",".join(sorted(nodes_in_mc))
    print("The password is:", password)


if __name__ == "__main__":
    process_part1("input.txt")
    process_part2("input.txt")
