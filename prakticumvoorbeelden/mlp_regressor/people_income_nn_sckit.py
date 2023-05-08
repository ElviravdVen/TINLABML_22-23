# https://jamesmccaffrey.wordpress.com/2023/03/13/regression-people-income-using-a-scikit-mlpregressor-neural-network/
# people_income_nn_sckit.py

# predict income
# from sex, age, state, politics

# sex  age   state   income  politics
#  1  0.24  1  0  0  0.2950  0  0  1
# -1  0.39  0  0  1  0.5120  0  1  0
# state: michigan = 100, nebraska = 010, oklahoma = 001
# conservative = 100, moderate = 010, liberal = 001

import numpy as np
from sklearn.neural_network import MLPRegressor
import warnings

warnings.filterwarnings("ignore")  # early-stop warnings

# ---------------------------------------------------------


def accuracy(model, data_x, data_y, pct_close=0.10):
    # accuracy predicted within pct_close of actual income
    # item-by-item allows inspection but is slow
    n_correct = 0
    n_wrong = 0
    predicteds = model.predict(data_x)  # all predicteds
    for i in range(len(predicteds)):
        actual = data_y[i]
        pred = predicteds[i]

        if np.abs(pred - actual) < np.abs(pct_close * actual):
            n_correct += 1
        else:
            n_wrong += 1
    acc = (n_correct * 1.0) / (n_correct + n_wrong)
    return acc


# ---------------------------------------------------------


def accuracy_q(model, data_x, data_y, pct_close=0.10):
    # accuracy within pct_close of actual income
    # all-at-once is quick
    n_items = len(data_y)
    preds = model.predict(data_x)  # all predicteds

    n_correct = np.sum((np.abs(preds - data_y) < np.abs(pct_close * data_y)))
    result = n_correct / n_items
    return result


# ---------------------------------------------------------


def main():
    # 0. get ready
    print("\nBegin scikit neural network regression example ")
    print("Predict income from sex, age, State, politics ")
    np.random.seed(1)
    np.set_printoptions(precision=4, suppress=True)

    # 1. load data
    print("\nLoading data into memory ")
    train_file = "people_train.csv"
    train_xy = np.loadtxt(
        train_file, usecols=range(0, 9), delimiter=",", comments="#", dtype=np.float32
    )
    train_x = train_xy[:, [0, 1, 2, 3, 4, 6, 7, 8]]
    train_y = train_xy[:, 5]

    test_file = "people_test.csv"
    test_xy = np.loadtxt(
        test_file, usecols=range(0, 9), delimiter=",", comments="#", dtype=np.float32
    )
    test_x = test_xy[:, [0, 1, 2, 3, 4, 6, 7, 8]]
    test_y = test_xy[:, 5]

    print("\nTraining data:")
    print(train_x[0:4])
    print(". . . \n")
    print(train_y[0:4])
    print(". . . ")

    # ---------------------------------------------------------

    # 2. create network
    # MLPRegressor(hidden_layer_sizes=(100,),
    #  activation='relu', *, solver='adam', alpha=0.0001,
    #  batch_size='auto', learning_rate='constant',
    #  learning_rate_init=0.001, power_t=0.5, max_iter=200,
    #  shuffle=True, random_state=None, tol=0.0001,
    #  verbose=False, warm_start=False, momentum=0.9,
    #  nesterovs_momentum=True, early_stopping=False,
    #  validation_fraction=0.1, beta_1=0.9, beta_2=0.999,
    #  epsilon=1e-08, n_iter_no_change=10, max_fun=15000)

    params = {
        "hidden_layer_sizes": [10, 10],
        "activation": "relu",
        "solver": "adam",
        "alpha": 0.0,
        "batch_size": 10,
        "random_state": 0,
        "tol": 0.0001,
        "nesterovs_momentum": False,
        "learning_rate": "constant",
        "learning_rate_init": 0.01,
        "max_iter": 1000,
        "shuffle": True,
        "n_iter_no_change": 50,
        "verbose": False,
    }

    print("\nCreating 8-(10-10)-1 relu neural network ")
    net = MLPRegressor(**params)

    # ---------------------------------------------------------

    # 3. train
    print(
        "\nTraining with bat sz = "
        + str(params["batch_size"])
        + " lrn rate = "
        + str(params["learning_rate_init"])
        + " "
    )
    print("Stop if no change " + str(params["n_iter_no_change"]) + " iterations ")
    net.fit(train_x, train_y)
    print("Done ")

    # ---------------------------------------------------------

    # 4. evaluate model
    # score() is coefficient of determination for MLPRegressor
    print("\nCompute model accuracy (within 0.10 of actual) ")
    acc_train = accuracy(net, train_x, train_y, 0.10)
    print("\nAccuracy on train = %0.4f " % acc_train)
    acc_test = accuracy(net, test_x, test_y, 0.10)
    print("Accuracy on test = %0.4f " % acc_test)

    # print("\nModel accuracy quick (within 0.10 of actual) ")
    # acc_train = accuracy_q(net, train_x, train_y, 0.10)
    # print("\nAccuracy on train = %0.4f " % acc_train)
    # acc_test = accuracy_q(net, test_x, test_y, 0.10)
    # print("Accuracy on test = %0.4f " % acc_test)

    # ---------------------------------------------------------

    # 5. use model
    # no proba() for MLPRegressor
    print("\nSetting X = M 34 Oklahoma moderate: ")
    X = np.array([[-1, 0.34, 0, 0, 1, 0, 1, 0]])
    income = net.predict(X)  # divided by 100,000
    income *= 100000  # denormalize
    print("Predicted income: %0.2f " % income)

    # ---------------------------------------------------------

    # 6. TODO: save model using pickle
    # import pickle
    # print("Saving trained network ")
    # path = "people_income_net.sav"
    # pickle.dump(model, open(path, "wb"))

    # use saved model
    # X = np.array([[-1, 0.34, 0,0,1,  0,1,0]]],
    #   dtype=np.float32)
    # with open(path, 'rb') as f:
    #   loaded_model = pickle.load(f)
    # inc = loaded_model.predict(X)
    # print(inc)

    print("\nEnd scikit binary neural network demo ")


if __name__ == "__main__":
    main()
