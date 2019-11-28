import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

a_star_nodes_generated = [1, 5, 9, 23, 59, 99, 157, 401, 889, 1487, 5743, 15311, 35764, 62869, 84242]
ids_nodes_generated = [1, 5, 15, 67, 133, 239, 1648, 6574, 17269, 23877, 156943, 699291, 2816096, 6602826, 8943144]
bfs_nodes_generated = [1, 12, 35, 156, 306, 527, 3676, 14730, 38595, 53343, 350915, 1563733, 6297070, np.nan, np.nan]
dfs_nodes_generated = [1, 4250, 68237, 82798, 159894, 51820, 111950, 284777, 159572, 99462, 143527, 192137, 585214,
                       np.nan, np.nan]
x = range(0, 15)
fig, ax = plt.subplots(figsize=(10, 7))
ax.plot(x, a_star_nodes_generated, label='A*')
ax.plot(x, ids_nodes_generated, label='IDS')
ax.plot(x, bfs_nodes_generated, label='BFS')
ax.plot(x, dfs_nodes_generated, label='DFS')
ax.yaxis.set_major_formatter(ScalarFormatter())
ax.grid(True)
ax.set_yscale('log')
for axis in [ax.xaxis, ax.yaxis]:
    formatter = ScalarFormatter()
    formatter.set_scientific(False)
    axis.set_major_formatter(formatter)
ax.legend()
ax.set_title("Scalability of Search Methods", fontsize=14)
ax.set_xlabel("Problem Difficulty (Optimal Solution Depth)", fontsize=12)
ax.set_ylabel("Nodes Generated (Log Scale)", fontsize=12)

fig.show()
