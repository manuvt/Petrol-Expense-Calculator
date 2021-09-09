import tkinter as tk
import requests
import pandas as pd
def generate():
    try:
        result = float(num2.get())/float(num1.get()) * today_fuel_price * float(num3.get())
    except Exception as ex:
        print(ex)
        result = 'error'

    num4.set(result)

# --- main ---
url= "https://www.goodreturns.in/petrol-price-in-tiruvallur.html#Last+10+Days+Petrol+Rate+in+Tiruvallur"
r = requests.get(url)
df_list = pd.read_html(r.text)
df = df_list[0]
fuel_price=df[1][1]
today_fuel_price=float(fuel_price[1:-1])
print("Today's fuel price is  ",today_fuel_price)

root = tk.Tk()
root.title('Petrol Expense Calculator')

num1 = tk.StringVar()
num2 = tk.StringVar()
num3 = tk.StringVar()
num4 = tk.StringVar()


tk.Label(root, text="Enter the Mileage:").grid(row=0, column=0)
tk.Label(root, text="Enter the Distance:").grid(row=1, column=0)
tk.Label(root, text="No. of Trips:").grid(row=2, column=0)
tk.Label(root, text="Total expense per month in Rs.").grid(row=3, column=0)

tk.Entry(root, textvariable=num1).grid(row=0, column=1)
tk.Entry(root, textvariable=num2).grid(row=1, column=1)
tk.Entry(root, textvariable=num3).grid(row=2, column=1)
tk.Entry(root, textvariable=num4).grid(row=3, column=1)


button = tk.Button(root, text="Calculate", command=generate)
button.grid(row=4, column=1)

root.mainloop()
