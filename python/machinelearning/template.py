import pandas as pd
import tkinter
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from tkinter import *

dataset = pd.read_csv('data/landprice1.csv')
X = dataset.iloc[:,0].values
Y = dataset.iloc[:,-1].values

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.4, random_state=0)

X_train1 = np.reshape(X_train,(-1,1))
Y_train1 = np.reshape(Y_train,(-1,1))
X_test1 = np.reshape(X_test,(-1,1))
Y_test1 = np.reshape(Y_test,(-1,1))

lin_regressor = LinearRegression()
lin_regressor.fit(X_train1,X_test1)

def model_pred():
    area1=entry.get()
    area = int(area1)

    tran_area = np.array([[area]])
    pred_price = lin_regressor.predict(tran_area)
    pred_price = str(pred_price)

    label1 = Label(window, text = pred_price, fg = 'red', font=('Courier',25))
    label1.pack()

    entry.delete(0, END)


window = Tk()
window.geometry("600x700")
window.title("Template Window")
label = Label(window,text="Enter the Area of the land in thousand Sq Foor", fg='red', font=("Courier",15))
label.pack()

area = StringVar()
area.set("")
entry = Entry(window, textvariable=area, fg ='green', width=10,font=('Courier', 15))
entry.pack()

pred_button = Button(window, text = "Predict", fg = 'red', command=model_pred, height=2, width=15)
pred_button.pack()

mainloop()
