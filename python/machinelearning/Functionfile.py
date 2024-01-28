import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

def readFile():
    dataset = pd.read_csv('data/landprice.csv')
    X = dataset.iloc[:,0].values
    Y = dataset.iloc[:,-1].values

    return X,Y

def split_data(X,Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.4, random_state=0)
    return X_train, X_test, Y_train, Y_test

def model_Train(X_train,Y_train,X_test, Y_test):
    # without this, expected 2d array, got 1d array instead
    X_train1 = np.reshape(X_train,(-1,1))
    Y_train1 = np.reshape(Y_train,(-1,1))
    X_test1 = np.reshape(X_test,(-1,1))
    Y_test1 = np.reshape(Y_test,(-1,1))

    lin_regressor = LinearRegression()
    #lin_regressor.fit(X_train1,Y_train1)
    lin_regressor.fit(X_train1,X_test1)

    #y_pred = lin_regressor.predict(X_test1)
    y_pred = lin_regressor.predict(Y_train1)
    r_square = r2_score(y_test1,y_pred)

    Area = 37
    tran_Area = np.reshape(Area, (-1,1))
    #tran_Area = np.array([[34]])
    pred_price=lin_regressor.predict(tran_Area)

    return lin_regressor

def visualize_result(X_train1, Y_train1, X_test1, Y_test1, lin_regressor):
    #plt.scatter(X_train1, T_train1, color = 'blue')
    plt.scatter(X_train1, X_test1, color = 'blue')
    
    X_train2 = np.reshape(X_train1, (-1,1))
    plt.plot(X_train2, lin_regressor.predict(X_train2), color='red')

    plt.title('Area vs Price of the Land')
    plt.xlabel("Area of the Land in thousand Square Foot")
    plt.ylabel("Price of the Land in Million USD")
    plt.show()

def main():
    X,Y = readFile()
    X_train, X_test, Y_train, Y_test = split_data(X,Y)
    lin_regressor = model_Train(X_train, X_test, Y_train, Y_test)
    visualize_result(X_train, X_test, Y_train, Y_test, lin_regressor)

    

if __name__ == "__main__":
    main()
