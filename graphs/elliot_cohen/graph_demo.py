import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


data_endpoint = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS6EqRuTDVTI1ClwCusN3a7D96p7EbwcmvC4u0Lqj4poN93AyHa6JNXiPaN84AlZUPpqDkoKNlBV0A5/pub?gid=0&single=true&output=csv'
A = pd.read_csv(data_endpoint, header=0, index_col=0)  
A.fillna(0, inplace=True)  
G = nx.from_numpy_matrix(A.values)
G = nx.from_pandas_adjacency(A)

degree = nx.degree_centrality(G)
betweenness = nx.betweenness_centrality(G)
eigenvector = nx.eigenvector_centrality(G)

visual_scalar = 100

plt.figure(1)
nx.draw_circular(G, with_labels=True)

plt.figure(2)
nx.draw_kamada_kawai(G, with_labels=True, node_size=[val * visual_scalar for val in degree.values()])

plt.figure(3)
nx.draw_kamada_kawai(G, with_labels=True, node_size=[val * visual_scalar for val in betweenness.values()])

plt.figure(4)
nx.draw_kamada_kawai(G, with_labels=True, node_size=[val * visual_scalar for val in eigenvector.values()])

plt.show()



