import numpy as np
#import os # might need to add path to mingw-w64/bin for cvxopt to work
#os.environ["PATH"] += os.pathsep + ...
import cvxopt

def svmlin(X, t, C, ex):
    # Linear SVM Classifier
    #
    # INPUT:
    # X        : the dataset                  (dim x num_samples)
    # t        : labeling                     (num_samples x 1)
    # C        : penalty factor for slack variables (scalar)
    #
    # OUTPUT:
    # alpha    : output of quadprog function  (num_samples x 1)
    # sv       : support vectors (boolean)    (1 x num_samples)
    # w        : parameters of the classifier (1 x dim)
    # b        : bias of the classifier       (scalar)
    # result   : result of classification     (1 x num_samples)
    # slack    : points inside the margin (boolean)   (1 x num_samples)

    #####Insert your code here for subtask 2a#####
    return alpha, sv, w, b, result, slack



