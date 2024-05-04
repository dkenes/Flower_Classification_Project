import matplotlib.pyplot as plt
import networkx as nx


def PlotGraph(G):
    # node'larin pozisyonlarini ayarlama
    pos = nx.circular_layout(G)
    # graph'i cizdirip ekrana yazdirma
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
''' dijkstra'nin en kisa yol algoritmasini kullanarak 4. node'dan diger nodelara olan 
en kisa yolu cizdiren fonksiyon'''
# diger en kisa yol cizimlerini gormek icin cikan pencereyi kapatin. pencere kapaninca yeni bir pencere acilacak.
def PlotShortestPaths(G):
    for j in range(0,4):
        node = '{}'.format(j)
        # bazi node'lara baska node'lardan herhangi bir yol olmadigi icin ve 2 node'unu silecegimiz icin grafik cizimi icin böyle bir kosul koydum.
        if not (G.has_node(node) and nx.has_path(G,'4',node)):
            continue
        shortest_path = nx.dijkstra_path(G, '4', node)
        # En kisa yolu gosteren edge'leri cizdirme
        shortest_path_edges = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)]

        
        fig, ax = plt.subplots()

        # node'larin pozisyonlarini ayarlama 
        pos = nx.circular_layout(G)

        # graph'i ve en kisa yolu cizdirme
        nx.draw(G, pos=pos, ax=ax, with_labels=True)
        nx.draw_networkx_edges(G, pos=pos, ax=ax, edgelist=shortest_path_edges, edge_color='r', width=3)
        
        edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}

        # edge'lerin agirliklarini cizdirme
        nx.draw_networkx_edge_labels(G, pos=pos, ax=ax, edge_labels=edge_labels)

        # cizimi goster
        plt.show()
def main():
    # digraph olusturma
    G = nx.DiGraph()

    # graph'a ayritlari ekleme 
    G.add_edge('0', '1', weight=5)
    G.add_edge('0', '2', weight=3) 
    G.add_edge('0', '4', weight=2) 
    G.add_edge('1', '2', weight=2) 
    G.add_edge('1', '3', weight=6) 
    G.add_edge('2', '1', weight=1) 
    G.add_edge('2', '3', weight=2) 
    G.add_edge('4', '3', weight=4) 
    G.add_edge('4', '2', weight=10) 
    G.add_edge('4', '1', weight=6)

    # diger graph cizimlerini gormek icin programi calistirdiginizda cikan ekrani kapatin, 
    # bir sonraki cizim gelecek.
    PlotGraph(G)
    PlotShortestPaths(G)
    # 2 Node'unu silme islemi
    G.remove_node('2')
    PlotGraph(G)
    PlotShortestPaths(G)

main()
