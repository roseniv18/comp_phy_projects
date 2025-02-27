from numpy import linspace, zeros, ones_like
import time
import networkx as nx
import pylab as plt
from memory_profiler import profile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test the computation time of 2 approaches of calculating
# the Hermite Polynomials:
# 1. Recursive approach (2^n complexity)
# 2. Iterative approach (n complexity)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~


@profile
def recursive_hermite(n, x):
    if n == 0:
        return ones_like(x)
    elif n == 1:
        return 2 * x
    else:
        return 2 * x * recursive_hermite(n - 1, x) - 2 * (n - 1) * recursive_hermite(
            n - 2, x
        )


@profile
def iterative_hermite(n, x):
    H = zeros((n + 1, len(x)))
    H[0] = ones_like(x)
    if n > 0:
        H[1] = 2 * x
        for i in range(2, n + 1):
            H[i] = 2 * x * H[i - 1] - 2 * (i - 1) * H[i - 2]
    return H


# Test both approaches
x = linspace(-4, 4, 100)
n = 10

print("Testing recursive approach:")
result_recursive = recursive_hermite(n, x)

print("\nTesting iterative approach:")
result_iterative = iterative_hermite(n, x)


def create_computation_tree(n):
    G = nx.DiGraph()

    def add_edges(node, depth):
        if depth <= 0:
            return
        left_child = f"H({node-1})"
        right_child = f"H({node-2})"

        if node > 1:
            G.add_edge(f"H({node})", left_child)
            add_edges(node - 1, depth - 1)
        if node > 2:
            G.add_edge(f"H({node})", right_child)
            add_edges(node - 2, depth - 1)

    # Create the tree
    G.add_node(f"H({n})")
    add_edges(n, n)

    # Plotting
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightblue",
        node_size=2000,
        arrowsize=20,
        font_size=10,
        font_weight="bold",
    )
    plt.title(f"Computation Tree for Hermite Polynomial H({n})")
    plt.show()


# Create visualization for n=5
create_computation_tree(5)
