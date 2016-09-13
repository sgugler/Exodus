from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'], random_state=0)

fig, ax = plt.subplots(3, 3)

plt.suptitle("iris_pairplot")
for i in range(3):
    for j in range(3):
        ax[i, j].scatter(X_train[:, j], X_train[:, i + 1], c=y_train, s=20)
        ax[i, j].set_xticks(())
        ax[i, j].set_yticks(())
        if i == 2:
            ax[i, j].set_xlabel(iris['feature_names'][j])
        if j == 0:
            ax[i, j].set_ylabel(iris['feature_names'][i + 1])
        if j > i:
            ax[i, j].set_visible(False)
# plt.show()

knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train, y_train)

KNeighborsClassifier(algorithm="auto", leaf_size=30, metric="minkowski",
                     metric_params=None, n_jobs=1, p=2,
                     weights='uniform')

#y_prediction = knn.predict(X_test)
#mean_pred = np.mean(y_prediction == y_test)
# print(mean_pred)
score_pred = knn.score(X_test, y_test)

print(score_pred)