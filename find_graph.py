import itertools
import copy
import networkx as nx
import matplotlib.pyplot as plt
import spacefillingunit_restriction as rest

def main():
    unit_number = 27
    filtered_edges_list = find_filtered_edges_list(unit_number)
    #print(filtered_edges_list)

def find_filtered_edges_list(unit_number):
    # 条件
    n, restricted_edges, node_names, node_weights = rest.restriction(unit_number)

    # 頂点数 n の全域木
    edges_list = enumerate_spanning_trees(n)

    print(f"頂点数 {n} の全域木の数: {len(edges_list)}")

    # 制約によるフィルタリング
    filtered_edges_list = filter_edges(edges_list,restricted_edges)

    print(len(filtered_edges_list))
    """
    unique_graphs = make_unique_graphs(filtered_edges_list,node_names,node_weights)

    print(f"同型判定の絞り込みによる全域木の数{len(unique_graphs)}")
    draw_graph(unique_graphs)
    """
    return filtered_edges_list

# Union-Find
class UnionFind():
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return False  

        if self.rank[x_root] < self.rank[y_root]:
            self.parents[x_root] = y_root
        else:
            self.parents[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1
        return True

# 全域木列挙
def enumerate_spanning_trees(n):
    vertices = list(range(n))
    edges = list(itertools.combinations(vertices, 2))  # 完全グラフの辺
    all_trees = []

    def backtrack(index, selected_edges):
        if len(selected_edges) == n - 1:
            all_trees.append(copy.deepcopy(selected_edges))
            return
        if index == len(edges):
            return

        u, v = edges[index]

        # 現在の selected_edges に基づいて UnionFind を初期化
        uf = UnionFind(n)
        for a, b in selected_edges:
            uf.union(a, b)

        # 辺 (u, v) を加えても閉路ができなければ追加
        if uf.union(u, v):
            selected_edges.append((u, v))
            backtrack(index + 1, selected_edges)
            selected_edges.pop()

        # 辺を加えない場合も探索
        backtrack(index + 1, selected_edges)

    backtrack(0, [])
    return all_trees

# 制約によるフィルタリング
def filter_edges(edges,restricted_edges):
    filtered_edges_list = []
    for i in edges:
        skip = False
        for j in restricted_edges:
            if j in i:
                skip = True
                break
        if not skip:
            filtered_edges_list.append(i)

    return filtered_edges_list

# グラフの作成
def make_graph(edges, names, weights):
    G = nx.Graph()
    for i in range(len(names)):
        G.add_node(i, name = names[i], weight = weights[i])

    G.add_edges_from(edges)
    return G

# グラフの同型判定
def make_unique_graphs(edges_list ,node_names, node_weights):
    unique_node_names = list(set(node_names))
    nm = nx.isomorphism.categorical_node_match("name", unique_node_names)
    temp=[]
    unique_graphs=[]
    for i in range(len(edges_list)):
        if i in temp:
            continue
        G1 = make_graph(edges_list[i],node_names,node_weights)
        unique_graphs.append(G1)
        for j in range(i+1,len(edges_list)):
            G2 = make_graph(edges_list[j],node_names,node_weights)
            if nx.is_isomorphic(G1, G2, node_match=nm):
                temp.append(j)
    return unique_graphs

# グラフの描画
def draw_graph(graphs_list):
    pos = nx.circular_layout(graphs_list[0])
    labels = {n: graphs_list[0].nodes[n]['weight'] for n in graphs_list[0].nodes}
    colors = [graphs_list[0].nodes[n]['weight'] for n in graphs_list[0].nodes]

    for i in graphs_list:
        nx.draw(i, pos, with_labels=True, labels=labels, node_color=colors)
        plt.show()

if __name__ == "__main__":
    main()