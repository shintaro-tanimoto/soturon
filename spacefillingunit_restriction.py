"""
A: 正四面体
B: 正六面体
C: 正八面体
D: 正三角柱
E: 正六角柱
F: 正八角柱
G: 正十二角柱
H: 立方八面体
I: 二十・十二面体
J: 切頂四面体
K: 切頂八面体
L: 切頂六面体
M: 斜方立方八面体
N: 斜方切頂立方八面体
"""
def restriction(unit_number):
#元コードなし
    if unit_number == 8:
        # 条件(立体番号8)
        n = 3
        restricted_edges = [(1,2)]
        node_names = ["C","A","A"] 
        node_weights = [1,2,2] 
        return n, restricted_edges, node_names, node_weights
#元コードなし
    elif unit_number == 9:
        # 条件(立体番号9)
        n = 3
        restricted_edges = []
        node_names = ["B","A","A"]
        node_weights = [1,2,2]
        return n, restricted_edges, node_names, node_weights
#元コードなし
    elif unit_number == 10:
        # 条件(立体番号10)
        n = 3
        restricted_edges = [(1,2)]
        node_names = ["E","A","A"]
        node_weights = [1,2,2]
        return n, restricted_edges, node_names, node_weights
#元コードなし        
    elif unit_number == 11:
        # 条件(立体番号11)
        n = 3
        restricted_edges = [(1,2)]
        node_names = ["G","A","A"]
        node_weights = [1,2,2]
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 12:
        # 条件(立体番号12)
        n = 4
        restricted_edges = [(0,2),(1,3)]
        node_names = ["D","D","D","D"] 
        node_weights = [1,1,1,1]
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 13:
        # 条件(立体番号13)
        n = 4
        restricted_edges = [(0,3),(1,2),(2,3)]
        node_names = ["J","J","A","A"] 
        node_weights = [1,1,2,2] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 14:
        # 条件(立体番号14)
        n = 4
        restricted_edges = [(1,2),(1,3),(2,3)]
        node_names = ["M","B","A","A"] 
        node_weights = [1,2,3,3] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 15:
        # 条件(立体番号15)
        n = 4
        restricted_edges = [(2,3)]
        node_names = ["K","H","J","J"] 
        node_weights = [1,2,3,3] 
        return n, restricted_edges, node_names, node_weights
#修正した
    elif unit_number == 16:
        # 条件(立体番号16)
        n = 4
        restricted_edges = []
        node_names = ["N","F","F","F"] 
        node_weights = [1,2,2,2] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 17:
        # 条件(立体番号17)
        n = 4
        restricted_edges = [(2,3)]
        node_names = ["N","L","J","J"] 
        node_weights = [1,2,3,3] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 18:
        # 条件(立体番号18)
        n = 5
        restricted_edges = [(1,4),(2,3),(3,4)]
        node_names = ["C","D","D","A","A"] 
        node_weights = [1,2,2,3,3] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 19:
        # 条件(立体番号19)
        n = 5
        restricted_edges = [(2,3),(2,4),(3,4)]
        node_names = ["M","H","B","B","B"] 
        node_weights = [1,2,3,3,3] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 20:
        # 条件(立体番号20)
        n = 5
        restricted_edges = [(2,3),(2,4),(3,4)]
        node_names = ["N","K","B","B","B"] 
        node_weights = [1,2,3,3,3] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 21:
        # 条件(立体番号21)
        n = 6
        restricted_edges = [(0,4),(0,5),(1,2),(1,3),(2,3),(2,5),(3,4),(4,5)] 
        node_names = ["C","C","A","A","A","A"] 
        node_weights = [1,1,2,2,2,2] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 22:
        # 条件(立体番号22)
        n = 6
        restricted_edges = [(0,1),(0,4),(0,5),(1,2),(1,3),(2,3),(2,4),(3,5),(4,5)] 
        node_names = ["B","B","D","D","D","D"] 
        node_weights = [1,1,2,2,2,2] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 23:
        # 条件(立体番号23)
        n = 6
        restricted_edges = [(0,1),(2,4),(2,5),(3,4),(3,5)]
        node_names = ["B","B","D","D","D","D"] 
        node_weights = [1,1,2,2,2,2] 
        return n, restricted_edges, node_names, node_weights
#修正した
    elif unit_number == 24:
        # 条件(立体番号24)
        n = 6
        restricted_edges = [(0,4),(0,5),(1,2),(1,3),(2,3),(4,5)]
        node_names = ["E","B","B","B","D","D"] 
        node_weights = [1,2,2,2,3,3] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 25:
        # 条件(立体番号25)
        n = 6
        restricted_edges = [(1,2),(3,4),(3,5),(4,5)]
        node_names = ["G","E","E","B","B","B"] 
        node_weights = [1,2,2,3,3,3] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 26:
        # 条件(立体番号26)
        n = 8
        restricted_edges = [(0,5),(0,6),(0,7),(2,3),(2,4),(2,7),(3,4),(3,5),(4,6),(5,6),(5,7),(6,7)]
        node_names = ["K","M","F","F","F","B","B","B"] 
        node_weights = [1,2,3,3,3,4,4,4] 
        return n, restricted_edges, node_names, node_weights
#修正した
    elif unit_number == 27:
        # 条件(立体番号27)
        n = 9
        restricted_edges = [(0,2),(0,5),(1,3),(1,4),(1,5),(1,6),(1,7),(2,4),(2,5),(2,6),(2,8),(3,5),(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(6,8),(7,8)]
        node_names = ["E","A","A","A","A","A","A","A","A"] 
        node_weights = [1,2,2,2,2,2,2,2,2] 
        return n, restricted_edges, node_names, node_weights
#修正した
    elif unit_number == 28:
        # 条件(立体番号28)
        n = 10
        restricted_edges = [(0,1),(0,3),(0,4),(0,8),(0,9),(1,3),(1,4),(1,6),(1,7),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(3,4),(3,5),(3,6),(3,8),(4,7),(4,9),(5,6),(5,7),(5,8),(5,9),(6,7),(6,8),(6,9),(7,8),(7,9),(8,9)]
        node_names = ["C","C","D","D","D","D","A","A","A","A"] 
        node_weights = [1,1,2,2,2,2,3,3,3,3] 
        return n, restricted_edges, node_names, node_weights

    else:
        print("error")
        return None, None, None, None