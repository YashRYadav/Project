import pandas as pd
import tkinter as ttk

model=pd.read_pickle('BikePrice.pickle')

app=ttk.Tk()
app.configure(background='white')
app.geometry('300x300')
app.title('Used Bikes Price Predictor')

kms_driven=ttk.Variable(app)
ttk.Label(app,text='Kilometers driven',padx=15,pady=15).grid(row=0,column=0)
ttk.Entry(app,textvariable=kms_driven,width=10).grid(row=0,column=1)

age=ttk.Variable(app)
ttk.Label(app,text='Age of bike',padx=15,pady=15).grid(row=1,column=0)
ttk.Entry(app,textvariable=age,width=10).grid(row=1,column=1)


power=ttk.Variable(app)
ttk.Label(app,text='Power (in horsepowers)',padx=15,pady=15).grid(row=2,column=0)
ttk.Entry(app,textvariable=power,width=10).grid(row=2,column=1)

result=ttk.Variable(app)
result.set('0')
ttk.Label(app,textvariable=result,pady=20,font=('Arial',20)).grid(row=5,column=0,columnspan=2)

def prediction():
    global model
    query_data={
        'kms_driven':[eval(kms_driven.get())],
        'power':[eval(power.get())],
        'age':[eval(age.get())]
    }
    price=model.predict(pd.DataFrame(query_data))
    result.set(round(price[0],2))

ttk.Button(app,text='Predict',command=prediction,font=('Arial',20)).grid(row=4,column=0,columnspan=2)


app.mainloop()