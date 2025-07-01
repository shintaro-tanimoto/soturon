def restriction(unit_number):
#元コードなし
    if unit_number == 8:
        # 条件(立体番号8)
        n = 3
        restricted_edges = [(1,2)]
        node_names = ["A","B","B"] 
        node_weights = [1,2,2] 
        return n, restricted_edges, node_names, node_weights
#元コードなし
    elif unit_number == 9:
        # 条件(立体番号9)
        n = 3
        restricted_edges = []
        node_names = ["A","B","B"]
        node_weights = [1,2,2]
        return n, restricted_edges, node_names, node_weights
#元コードなし
    elif unit_number == 10:
        # 条件(立体番号10)
        n = 3
        restricted_edges = [(1,2)]
        node_names = ["A","B","B"]
        node_weights = [1,2,2]
        return n, restricted_edges, node_names, node_weights
#元コードなし        
    elif unit_number == 11:
        # 条件(立体番号11)
        n = 3
        restricted_edges = [(1,2)]
        node_names = ["A","B","B"]
        node_weights = [1,2,2]
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 12:
        # 条件(立体番号12)
        n = 4
        restricted_edges = [(0,2),(1,3)]
        node_names = ["A","A","A","A"] 
        node_weights = [1,1,1,1] # NetworkXコードでは全てweight=1だが、図を見る限りは異なる可能性があるため、調整の余地あり
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 13:
        # 条件(立体番号13)
        n = 4
        restricted_edges = [(0,3),(1,2),(2,3)]
        node_names = ["A","A","B","B"] 
        node_weights = [1,1,2,2] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 14:
        # 条件(立体番号14)
        n = 4
        restricted_edges = [(1,2),(1,3),(2,3)]
        node_names = ["A","B","C","C"] 
        node_weights = [1,2,3,3] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 15:
        # 条件(立体番号15)
        n = 4
        restricted_edges = [(2,3)]
        node_names = ["A","B","C","C"] 
        node_weights = [1,2,3,3] 
        return n, restricted_edges, node_names, node_weights
#修正した
    elif unit_number == 16:
        # 条件(立体番号16)
        n = 4
        restricted_edges = []
        node_names = ["A","B","B","B"] 
        node_weights = [1,2,2,2] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 17:
        # 条件(立体番号17)
        n = 4
        restricted_edges = [(2,3)]
        node_names = ["A","B","C","C"] 
        node_weights = [1,2,3,3] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 18:
        # 条件(立体番号18)
        n = 5
        restricted_edges = [(1,4),(2,3),(3,4)]
        node_names = ["A","B","B","C","C"] 
        node_weights = [1,2,2,3,3] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 19:
        # 条件(立体番号19)
        n = 5
        restricted_edges = [(2,3),(2,4),(3,4)]
        node_names = ["A","B","C","C","C"] 
        node_weights = [1,2,3,3,3] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 20:
        # 条件(立体番号20)
        n = 5
        restricted_edges = [(2,3),(2,4),(3,4)]
        node_names = ["A","B","C","C","C"] 
        node_weights = [1,2,3,3,3] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 21:
        # 条件(立体番号21)
        n = 6
        restricted_edges = [(0,4),(0,5),(1,2),(1,3),(2,3),(2,5),(3,4),(4,5)] 
        node_names = ["A","A","B","B","B","B"] 
        node_weights = [1,1,2,2,2,2] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 22:
        # 条件(立体番号22)
        n = 6
        restricted_edges = [(0,1),(0,4),(0,5),(1,2),(1,3),(2,3),(2,4),(3,5),(4,5)] 
        node_names = ["A","A","B","B","B","B"] 
        node_weights = [1,1,2,2,2,2] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 23:
        # 条件(立体番号23)
        n = 6
        restricted_edges = [(0,1),(2,4),(2,5),(3,4),(3,5)]
        node_names = ["A","A","B","B","B","B"] 
        node_weights = [1,1,2,2,2,2] 
        return n, restricted_edges, node_names, node_weights
#修正した
    elif unit_number == 24:
        # 条件(立体番号24)
        n = 6
        restricted_edges = [(0,4),(0,5),(1,2),(1,3),(2,3),(4,5)]
        node_names = ["A","B","B","B","C","C"] 
        node_weights = [1,2,2,2,3,3] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 25:
        # 条件(立体番号25)
        n = 6
        restricted_edges = [(1,2),(3,4),(3,5),(4,5)]
        node_names = ["A","B","B","C","C","C"] 
        node_weights = [1,2,2,3,3,3] 
        return n, restricted_edges, node_names, node_weights

    elif unit_number == 26:
        # 条件(立体番号26)
        n = 8
        restricted_edges = [(0,5),(0,6),(0,7),(2,3),(2,4),(3,4),(2,7),(3,5),(4,6),(5,6),(5,7),(6,7)] #cite: 15
        node_names = ["A","B","C","C","C","D","D","D"] 
        node_weights = [1,2,3,3,3,4,4,4] 
        return n, restricted_edges, node_names, node_weights
#元データが論文にない
    elif unit_number == 27:
        # 条件(立体番号27)
        n = 9
        restricted_edges = [(0,2),(0,5),(1,3),(1,4),(1,5),(1,7),(1,8),(2,4),(2,5),(2,6),(2,8),(3,5),(3,6),(3,7),(3,8),(4,5),(4,6),(4,7),(4,8),(5,6),(5,7),(6,8)]
        node_names = ["A","B","B","B","B","B","B","B","B"] 
        node_weights = [1,2,2,2,2,2,2,2,2] 
        return n, restricted_edges, node_names, node_weights
#元データが論文にない
    elif unit_number == 28:
        # 条件(立体番号28)
        n = 10
        restricted_edges = [(0,1),(0,3),(0,4),(0,8),(0,9),(1,3),(1,4),(1,5),(1,7),(1,8),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(3,4),(3,5),(3,6),(3,8),(4,7),(4,9),(5,6),(5,7),(5,8),(5,9),(6,7),(6,8),(6,9),(7,8),(7,9),(8,9)]
        node_names = ["A","A","B","B","B","B","C","C","C","C"] 
        node_weights = [1,1,2,2,2,2,3,3,3,3] 
        return n, restricted_edges, node_names, node_weights

    else:
        print("error")
        return None, None, None, None