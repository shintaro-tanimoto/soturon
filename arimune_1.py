import copy
import math
import itertools
import matplotlib.pyplot as plt #グラフの可視化
import networkx as nx #NetwrokXの導入
import time

start = time.perf_counter()

def make_path(c,e): #辺eをパスcに追加
   c. append (e)

def search (a,e,i,m,comp,c,n) : # 追加する辺の探素
   if len(e)==n-1: # 全域木の辺の数は（頂点数）-1なので辺の数がnー1となれば出力する
      b=copy. deepcopy (e)
      make_path(c,b)
   for j in range (i,m) : # iからmまで
      a_0=a [j] [0] #head
      a_1=a [j] [1] #tail
      if comp [a_0] !=comp [a_1] : # バックトラック法により全域木を探索
         comp2=copy. deepcopy (comp)
         e.append (j)
         t=min(comp [a_0], comp [a_1]) # 連結成分番号の最小値
         s=max(comp [a_1], comp [a_1]) # 連結成分番号の最大値
         for k in range (len (comp)) : # 最大値を最小値で置き換える
            if comp [k] ==s:
               comp [k] =t
         search (a,e,j+1,m,comp,c,n)
         comp=comp2
         e.pop ()

def make_edges (c,a,d,n) : # 描画のための辺データの作成
   for i in range (len (c) ) :
      f=[]
      for j in range (n-1) :
         f. append (a [c [i] [j]] )
      d.append (f)

# 条件文その１：頂点数
n = 8
verts =list(range(n)) # 頂点のリスト
a = list(itertools.combinations(range(n), 2)) # 辺のリスト
m=len(a) # 辺の数
comp= [i for i in range (n) ]
e= [] # 変数の初期化
c= [] # 全域木の候補の辺リスト
d= [] # 全域木の候補リスト
N=0 # 全域木の数の確認用
t1=[] # 全域木にフィルターした後のリスト
t=[] # 制約によるフィルター後のリスト
search (a, e, 0, m, comp, c, n)# 全域木の探索 →cが出力
make_edges (c, a, d, n) # →全域木グラフの辺データリストd?が出力
k=len (c) # グラフの数

for i in range (k) : # 木であるかの判定でフィルターをかける
   G = nx.Graph()
   G.add_nodes_from(verts)
   G.add_edges_from(d[i])
   if nx.is_tree(G): # 木である場合、 tに追加
      t1. append (d[i])
      N +=1 # Nで全域木の数をカウントする
   else: # 木でない場合、Falseを出力
      pass

print(k)
print(N)

# 制約のフィルター(立体番号12)
for i in range(len(t1)):
   if  (0,5) in t1[i] or (0,6) in t1[i] or (0,7) in t1[i] or (2,3) in t1[i] or (2,4) in t1[i] or (3,4) in t1[i] or (2,7) in t1[i] or (3,5) in t1[i] or (4,6) in t1[i] or (5,6) in t1[i] or (5,7) in t1[i] or (6,7) in t1[i]:
      pass
   else:
      t. append (t1[i])

print("制約による絞り込み", len(t))

for i in range(len(t)): # 同型判定とグラフの取り除き
  #  print(i, "i")
   m = 0 # 管理用の変数
   for j in range(i+1, len(t)): # i番目とi+1番目以降の全てのグラフに対してこの操作を行う
        j = j-m # 同型だった場合の番号調整
        G1 = nx.Graph()
        # 以下頂点の重み付け
        G1.add_node(0, name = "A", weight=1)
        G1.add_node(1, name = "B", weight=2)
        G1.add_node(2, name = "C", weight=3)
        G1.add_node(3, name = "C", weight=3)
        G1.add_node(4, name = "C", weight=3)
        G1.add_node(5, name = "D", weight=4)
        G1.add_node(6, name = "D", weight=4)
        G1.add_node(7, name = "D", weight=4)
        # 条件付与終了
        G1.add_edges_from(t[i])
        labels = {n: G1.nodes[n]['weight'] for n in G1.nodes}
        colors = [G1.nodes[n]['weight'] for n in G1.nodes]
        G2 = nx.Graph()
        # 以下頂点の重み付け
        G2.add_node(0, name = "A", weight=1)
        G2.add_node(1, name = "B", weight=2)
        G2.add_node(2, name = "C", weight=3)
        G2.add_node(3, name = "C", weight=3)
        G2.add_node(4, name = "C", weight=3)
        G2.add_node(5, name = "D", weight=4)
        G2.add_node(6, name = "D", weight=4)
        G2.add_node(7, name = "D", weight=4)
        # 条件付与終了
        G2.add_edges_from(t[j])
        labels = {n: G1.nodes[n]['weight'] for n in G1.nodes}
        colors = [G1.nodes[n]['weight'] for n in G1.nodes]
        # node matchの指定
        nm = nx.isomorphism.categorical_node_match(["name","name"], ["A","B"])

        if nx.is_isomorphic(G1, G2, node_match=nm):
           del t[j] # 同型だったj番目をリストから削除する
           m +=1 # リストから一つ削除されたので、j+1番目がj番目、j＋2番目がj+1番目に移動することに対する修正をかけるために変数mに+1
          #  print("iso")
        else:
           pass
"""
for i in range (len(t)) : # 求めたグラフの描画
   G = nx.Graph()
   G.add_nodes_from(verts)
   G.add_edges_from(t[i])
   pos = nx.circular_layout(G)
   nx.draw(G, pos, with_labels=True, labels=labels, node_color=colors)
  #  nx.draw(G, pos, with_labels=True)
   plt.show()
"""
print("Sn、同型性判定による絞り込み ",N, len(t)) # 全域木の数と、そのうち同形を除いた数

end = time.perf_counter() #計測終了
print('{:.2f}'.format((end-start)))