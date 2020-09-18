
import numpy as np


class KNearestNeighbors():
    def __init__(self, X_train, y_train, n_neighbors=5, weights='uniform'):

        self.X_train = X_train
        self.y_train = y_train

        self.n_neighbors = n_neighbors
        self.weights = weights

        self.n_classes = 3

    def euclidian_distance(self, a, b):
        '''
        calculates the distances between the training
        data points and the data that we would like to classify
        '''
        return np.sqrt(np.sum((a - b)**2, axis=1))

    def kneighbors(self, X_test, return_distance=False):
        '''
        Finds the distances between each point in the test dataset
        and the rest of the dataset (training dataset)
        '''
        dist = []
        neigh_ind = []

        #each row corresponds to a list of distances between one test data point and all of the training data.
        point_dist = [self.euclidian_distance(x_test, self.X_train) for x_test in X_test]

        #Loop over each row
        for row in point_dist:
            #enumerate each row so we don't lose the indices of training data points that we calculated the distances with
            #enumarate has an automatic counter
            enum_neigh = enumerate(row)
            #sort each row according to the distances
            sorted_neigh = sorted(enum_neigh,
                                  key=lambda x: x[1])[:self.n_neighbors]

            #indices values
            ind_list = [tup[0] for tup in sorted_neigh]
            #distances values
            dist_list = [tup[1] for tup in sorted_neigh]

            dist.append(dist_list)
            neigh_ind.append(ind_list)

        if return_distance:
            return np.array(dist), np.array(neigh_ind)

        return np.array(neigh_ind)

    def predict(self, X_test):
        '''
        predict classes that the test data points belong to
        '''
        #each neighbor has equal weight in deciding the class label
        if self.weights == 'uniform':
            neighbors = self.kneighbors(X_test)
            y_pred = np.array([
                np.argmax(np.bincount(self.y_train[neighbor]))
                for neighbor in neighbors
            ])

            return y_pred
        #weights chosen as distance
        if self.weights == 'distance':

            dist, neigh_ind = self.kneighbors(X_test, return_distance=True)

            inv_dist = 1 / dist

            mean_inv_dist = inv_dist / np.sum(inv_dist, axis=1)[:, np.newaxis]

            proba = []

            for i, row in enumerate(mean_inv_dist):

                row_pred = self.y_train[neigh_ind[i]]

                for k in range(self.n_classes):
                    indices = np.where(row_pred == k)
                    prob_ind = np.sum(row[indices])
                    proba.append(np.array(prob_ind))

            predict_proba = np.array(proba).reshape(X_test.shape[0],
                                                    self.n_classes)

            y_pred = np.array([np.argmax(item) for item in predict_proba])

            return y_pred

    def score(self, X_test, y_test):
        '''
        returns the percentage of correctly classified labels
        '''
        y_pred = self.predict(X_test)

        return float(sum(y_pred == y_test)) / float(len(y_test))