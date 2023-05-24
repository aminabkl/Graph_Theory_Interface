import os

from flask import Flask, render_template, request
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from bfs import bfs
from dfs import dfs


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_nodes = int(request.form['num_nodes'])
        adj_matrix = np.zeros((num_nodes, num_nodes), dtype=int)

        for i in range(num_nodes):
            for j in range(num_nodes):
                adj_matrix[i][j] = int(request.form[f'adj_matrix_{i}_{j}'])

        graph = nx.DiGraph(adj_matrix)

        dfs_result = list(map(str, dfs(graph, 0))) if dfs(graph, 0) else None
        bfs_result = list(map(str, bfs(graph, 0))) if bfs(graph, 0) else None


        img_folder = "C:\\Users\\lenovo\\Desktop\\TG GUI Flask\\static\\img"
        # delete existing images in folder
        for filename in os.listdir(img_folder):
            file_path = os.path.join(img_folder, filename)
            os.unlink(file_path)

        fig = plt.figure(1)
        fig.clf()
        plt.title('Graph')
        nx.draw(graph, with_labels=True)
        plt.savefig(os.path.join(img_folder, 'graph.png'), format='png')

        return render_template('result.html', bfs_result=bfs_result, dfs_result=dfs_result)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
