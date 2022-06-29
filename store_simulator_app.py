from utilities_package.utilities import *
from utilities_package.modify_stock import *
from PySimpleGUI import PySimpleGUI as sg
from os.path import isfile
from os import remove


sg.theme('dark blue 1')
exist_file = isfile("./stock.csv")

if exist_file:
    stock = read_stock()
    stock_show = [
        [sg.Text('This is your stock')]]
    c=0
    for dic in stock:
        stock_show.append([sg.Text(f'CÓDIGO {c} --> {dic}')])
        c+=1
    stock_show.append([sg.Text('If you are running this simulator for at least the second time,\n'
    'your last stock will be reused. If you want you can create a new Stock')])
    stock_show.append([sg.Button('Create new stock',key = 'create')])
    stock_show.append([sg.Button('Continue with last stock',key = 'continue')])

    window = sg.Window('Sell', stock_show, size =(500,500))
    event, value = window.read()
    if event == 'create':
        window.close()
        remove('./stock.csv')
        register()
    elif event == 'continue':
        window.close()
        pass
if not exist_file:
    register()
    stock = read_stock()

while True:
    layout = [
        [sg.Text('Welcome to my store', pad=('35px'))],
        [sg.Button('Sell', key='sell',size=(20,1))],
        [sg.Button('Add product',key ='add_product',size=(20,1))],
        [sg.Button('Add product amount',key ='add_amount',size=(20,1))],
        [sg.Button('Delete product',key ='delete',size=(20,1))],
        [sg.Button('Discount Table', key='discount',size=(20,1))],
        [sg.Button('Stock', key='stock',size=(20,1))],
        [sg.Button('Exit', key='exit',size=(20,1))]
    ]
    window = sg.Window('Store', layout, size=(200,400))
    event,value = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'sell':
        window.close()
        layout_sell = [
            [sg.Text('Products for selling')], ]
        c=0
        for dic in stock:
            layout_sell.append([sg.Text(f'CÓDIGO {c} --> {dic}')])
            c+=1
        layout_sell.append([sg.Text('Product Code'),sg.Input(size= 10, key='code')])
        layout_sell.append([sg.Button('Sell',key='sell')])
        window = sg.Window('Sell', layout_sell, size =(500,500))
        event, value = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'sell':
            window.close()
        vender_prod(stock,value['code'])

    elif event == 'add_product':
        window.close()
        register()
        stock = read_stock()  

    elif event == 'add_amount':
        window.close()
        layout_add = [
            [sg.Text('Products')], ]
        c=0
        for dic in stock:
            layout_add.append([sg.Text(f'CÓDIGO {c} --> {dic}')])
            c+=1
        layout_add.append([sg.Text('Product Code'),sg.Input(size= 10, key='amount')])
        layout_add.append([sg.Button('Add',key='add')])
        window = sg.Window('Sell', layout_add, size =(500,500))
        event, value = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'add':
            window.close()
        add_amount(stock,value['amount'])
        stock = read_stock()  

    elif event == 'delete':
        window.close()
        delete_layout = [
            [sg.Text('Products')], ]
        c=0
        for dic in stock:
            delete_layout.append([sg.Text(f'CÓDIGO {c} --> {dic}')])
            c+=1
        delete_layout.append([sg.Text('Product Code'),sg.Input(size= 10, key='delete')])
        delete_layout.append([sg.Button('Delete',key='add')])
        window = sg.Window('Sell', delete_layout, size =(500,500))
        event, value = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'delete':
            window.close()
        delete_prod(stock,value['delete'])
        stock = read_stock()  

    elif event=='discount':
        tabela_desc()
            
    elif event=='stock':
         show(stock)

    elif event == 'exit':
        exit()











