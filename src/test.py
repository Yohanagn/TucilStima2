import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from convex_hull import convexhull

def graph(df, data, namagraph, label1, label2, x, y, namalabel):

    plt.figure(figsize = (10, 6))
    size = len(df['Target'].unique())
    colors = ['b','r','g']

    plt.title(namagraph)
    plt.xlabel(label1)
    plt.ylabel(label2)
        
    for i in range(size):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[x,y]].values
        hull = convexhull(bucket)

        plt.scatter(bucket[:, 0], bucket[:, 1], label=namalabel[i], color=colors[i])
        for simplex in hull:
            plt.plot(bucket[simplex, 0], bucket[simplex, 1], color=colors[i])
        
    plt.legend()
    plt.show()

def pasangantitik(df,data,x,y):
    graph(df, data,f"{data.feature_names[x]} vs. {data.feature_names[y]}", data.feature_names[x],data.feature_names[y],x,y,data.target_names)

data = datasets.load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
pasangantitik(df, data, 0, 1)
    
