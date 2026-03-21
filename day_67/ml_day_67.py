import pandas as pd

data = {
    "Annual_Income": [15, 16, 17, 18, 50, 52, 54, 56, 90, 92, 94, 96],
    "Spending_Score": [10, 12, 14, 16, 40, 42, 44, 46, 80, 82, 84, 86]
}

df = pd.DataFrame(data)

print(df)

X = df[["Annual_Income", "Spending_Score"]]

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=42)

kmeans.fit(X)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_

print("Cluster Labels:", labels)
print("Centroids:\n", centroids)

df["Cluster"] = labels

print(df)

import matplotlib.pyplot as plt

wcss = []

for i in range(1, 6):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 6), wcss, marker='o')
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()

plt.scatter(df["Annual_Income"], df["Spending_Score"], c=df["Cluster"], cmap="viridis")

plt.scatter(centroids[:, 0], centroids[:, 1], color="red", marker="X", s=200)

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")

plt.show()



# Insights:

# 1. Customers are grouped into 3 distinct clusters based on annual income and spending score.

# 2. Cluster 2 represents low-income, low-spending customers 
#    (average income ≈ 16.5, spending ≈ 13) → Budget customers.

# 3. Cluster 0 represents medium-income, medium-spending customers 
#    (average income ≈ 53, spending ≈ 43) → Regular customers.

# 4. Cluster 1 represents high-income, high-spending customers 
#    (average income ≈ 93, spending ≈ 83) → Premium customers.

# 5. The clustering shows a strong positive relationship between income and spending.

# 6. High-income, high-spending customers (Cluster 1) are the most valuable segment 
#    and should be targeted with premium products and offers.

# 7. Medium customers (Cluster 0) can be targeted with upselling strategies 
#    to move them into the premium segment.

# 8. Low-income customers (Cluster 2) can be targeted with budget-friendly offers 
#    and discounts to increase engagement.

# 9. The model successfully identified clear and well-separated customer segments, 
#    indicating strong clustering performance.