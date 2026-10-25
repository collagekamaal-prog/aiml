import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans, AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

data = load_iris()
x = data.data
y = data.target

# Elbow Method
wcss = []

for i in range(1, 6):
    km = KMeans(n_clusters=i, random_state=42, n_init=10)
    km.fit(x)
    wcss.append(km.inertia_)

plt.plot(range(1, 6), wcss, marker="o")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()

# K-Means
km = KMeans(n_clusters=3, random_state=42, n_init=10)
y_pred = km.fit_predict(x)

plt.scatter(x[:, 0], x[:, 1], c=y_pred)
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("K-Means Clustering")
plt.show()

print("K-Means cluster counts:")
for i in range(3):
    print("Cluster", i, ":", (y_pred == i).sum())

# Linkage Method and Dendrogram
z = linkage(x, method="ward")
dendrogram(z)
plt.title("Dendrogram")
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.show()

# Hierarchical Clustering
hc = AgglomerativeClustering(n_clusters=3)
y_pred_hc = hc.fit_predict(x)

plt.scatter(x[:, 0], x[:, 1], c=y_pred_hc)
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Hierarchical Clustering")
plt.show()

print("Hierarchical cluster counts:")
for i in range(3):
    print("Cluster", i, ":", (y_pred_hc == i).sum())
