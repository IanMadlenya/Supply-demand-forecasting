
from basemodel import BaseModel
from sklearn.neighbors import KNeighborsClassifier
from preprocess.preparedata import ScaleMethod
import numpy as np
from sklearn import preprocessing
from sklearn.pipeline import Pipeline

class KNNModel(BaseModel):
    def __init__(self):
        BaseModel.__init__(self)
        self.usedFeatures = [1,4,5,6,7]
        self.randomSate = None
        self.excludeZerosActual = True
#         self.scaling = ScaleMethod.MIN_MAX
        self.test_size = 0.3
        return
    def setClf(self):
        clf = KNeighborsClassifier(n_neighbors = 10)
        min_max_scaler = preprocessing.MinMaxScaler()
        self.clf = Pipeline([('scaler', min_max_scaler), ('estimator', clf)])
        return
    def getTunedParamterOptions(self):
#         tuned_parameters = [{'n_neighbors': np.arange(2, 150, 1)}]
        tuned_parameters = [{'estimator__n_neighbors': [5,10]}]
        return tuned_parameters




if __name__ == "__main__":   
    obj= KNNModel()
    obj.run()