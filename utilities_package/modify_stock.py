from asyncio import events
import csv
from os.path import isfile
from PySimpleGUI import PySimpleGUI as sg

class Product:
    def __init__(self,name,price,amount):
        self.name = name
        self.price = price
        self.amount = amount

def dic_obj(obj):
    return obj.__dict__

def again():
    again = [
    [sg.Text('ADD MORE PRODUCTS?')],
    [sg.Button('YES',key='yes'), sg.Button('NO, THANKS',key='no')]]

    
    window = sg.Window('More products', again)

    while True:
        event, value = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'yes':
            window.close()
            return True
        elif event == 'no':
            window.close()
            return False
        break




def register():
    stock = []
    while True:
        layout = [
            [sg.Text('ADD PRODUCTS TO STOCK')],
            [sg.Text('Product Name: '),sg.Input(size=(20,1),key='name')],
            [sg.Text('Product Price: '),sg.Input(size=(20,1),key='price')],
            [sg.Text('Product Amount: '),sg.Input(size=(20,1),key='amount')],
            [sg.Button('Register Product',key='register')]
        ]
        window = sg.Window('Stock', layout)
        event,value = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'register':
            name = value['name']
            price = value['price']
            amount = value['amount']
            product = Product(name,price,amount)
            dictionary = dic_obj(product)
            stock.append(dictionary)
            window.close()
            ag = again()
            if ag:
                continue
            else:
                break

    exist_file = isfile("./stock.csv")
    if not exist_file:
        with open('stock.csv', 'w', newline='') as file:
            w = csv.DictWriter(file, fieldnames=dictionary.keys())
            w.writeheader()
            w.writerows(stock)
    if exist_file:
        with open('stock.csv', '+a', newline='') as file:
            w = csv.DictWriter(file, fieldnames=dictionary.keys())
            w.writerows(stock)



def add_amount(est,code):
    add_code = int(code)
    selected = [
        [sg.Text(f'You selected {est[add_code]["name"]}')],
        [sg.Text('Number of Units to add'),sg.Input(size=(10,1),key = 'units')],
        [sg.Button('OK',key = 'ok')]
    ]
    window = sg.Window('add', selected,size=(300,200))
    event, value = window.read()
    
    units = int(value['units'])
    
    table = [
        [sg.Text(f'You are adding: {units} of {est[add_code]["name"]}')]
    ]
    table.append([sg.Button('Continue',key='continue')])
    table.append([sg.Button('Cancel',key='cancel')])
    window = sg.Window('Sell', table,size=(300,200))
    event, value = window.read()

    if event == 'continue':
        add = est[add_code]['amount'] + units
        est[add_code]['amount'] = add
        window.close
        with open('stock.csv', 'w', newline='') as file:
            field_name =['name','price','amount']
            w = csv.DictWriter(file, fieldnames=field_name)
            w.writeheader()
            w.writerows(est)

        add_ok = [
        [sg.Text('Product amount was add !')],
        [sg.Button('OK',key = 'ok')]
        ]
        window = sg.Window('Confirming add', add_ok,size=(150,150))
        event, value = window.read()
        if event == 'ok':
            window.close
    else:
        add_cancel = [
        [sg.Text('Add canceled !')],
        [sg.Button('OK',key = 'ok')]
        ]
        window = sg.Window('Sale cancel', add_cancel,size=(150,150))
        event, value = window.read()
        if event == 'ok':
            window.close()

def delete_prod(est,code):
    stock = est
    del_code = int(code)
    selected = [
        [sg.Text(f'You will delete {est[del_code]["name"]}')],
        [sg.Button('OK',key = 'ok')],
        [sg.Button('Cancel',key = 'cancel')]]
    window = sg.Window('Delete', selected, size=(300,200))
    event,value = window.read()
    if event == 'ok':
        window.close()
        stock.pop(del_code)
        with open('stock.csv', 'w', newline='') as file:
            field_name = ['name','price','amount']
            w = csv.DictWriter(file, fieldnames=field_name)
            w.writeheader()
            w.writerows(stock)
    elif event == 'cancel':
        pass
