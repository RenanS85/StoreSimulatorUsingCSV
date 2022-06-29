from PySimpleGUI import PySimpleGUI as sg
import csv
def read_stock():
    stock = []
    with open ('stock.csv', 'r') as file:
        data = csv.DictReader(file)
        for d in data:
            if d['price']:
                d['price'] = float(d['price'])
            if d['amount']:
                d['amount'] = float(d['amount'])
            stock.append(d)
    return stock

def vender_prod(est,code):
    sale_code = int(code)
    if est[sale_code]['amount'] <= 0:
        not_availabe = [
            [sg.Text('Product is not avaiable...')],
            [sg.Button('OK',key = 'ok')]
        ]
        window = sg.Window('Sorry', not_availabe,size=(150,150))
        event, value = window.read()
        if event == 'ok':
            window.close()
        
    else:
        selected = [
            [sg.Text(f'You selected {est[sale_code]["name"]}')],
            [sg.Text(f'price R$ {est[sale_code]["price"]:.2f}')],
            [sg.Text('Number of Units'),sg.Input(size=(10,1),key = 'units')],
            [sg.Button('OK',key = 'ok')]
        ]
        window = sg.Window('Sorry', selected,size=(200,200))
        event, value = window.read()
        
        units = int(value['units'])
        total_price = est[sale_code]['price'] * units

        selling_table = [
            [sg.Text(f'You selected: {units} of {est[sale_code]["name"]}')],
            [sg.Text(f'Total R$ {total_price :.2f}')],

        ]
        
        if 10 < units <= 99:#5%
            desc1 = total_price*0.05
            pre_desc1 = total_price - desc1
            five_disc = [sg.Text(f'Didcount: 5%\nPrice: {pre_desc1:.2f}\nEconomy: {desc1:.2f}')]
            selling_table.append(five_disc)


        elif 100 <= units <= 999:
            desc2 = total_price * 0.1
            pre_desc2 = total_price - desc2
            ten_disc = [sg.Text(f'Didcount: 10%\nPrice: {pre_desc2:.2f}\nEconomy: {desc2:.2f}')]
            selling_table.append(ten_disc)

        elif 1000 <= units:
            desc3 = total_price * 0.15
            pre_desc3 = total_price - desc3
            fif_disc = [sg.Text(f'Didcount: 15%\nPrice: {pre_desc3:.2f}\nEconomy: {desc3:.2f}')]
            selling_table.append(fif_disc)

        selling_table.append([sg.Button('Continue',key='continue')])
        selling_table.append([sg.Button('Cancel',key='cancel')])
        window = sg.Window('Sell', selling_table,size=(200,200))
        event, value = window.read()

        if event == 'continue':
            withdrawal = est[sale_code]['amount'] - units
            est[sale_code]['amount'] = withdrawal
            window.close
            with open('stock.csv', 'w', newline='') as file:
                field_name =['name','price','amount']
                w = csv.DictWriter(file, fieldnames=field_name)
                w.writeheader()
                w.writerows(est)

            sell_ok = [
            [sg.Text('Product was sell !')],
            [sg.Button('OK',key = 'ok')]
            ]
            window = sg.Window('Confirming sale', sell_ok,size=(150,150))
            event, value = window.read()
            if event == 'ok':
                window.close
        else:
            sell_cancel = [
            [sg.Text('Sale canceled !')],
            [sg.Button('OK',key = 'ok')]
            ]
            window = sg.Window('Sale cancel', sell_cancel,size=(150,150))
            event, value = window.read()
            if event == 'ok':
                window.close()

def tabela_desc ():

    discount_table = [
        [sg.Text('DISCOUNT TABLE')],
        [sg.Text(f'units :  10 - 99 units --> 5%off\n'
        f'units : 100 - 999 units --> 10% off\n'
        f'units : 1000 or more  --> 15% off')
    ]]
    window = sg.Window('Discount', discount_table,size=(300,150))
    event, value = window.read()


def show(stock_obj):
    stock = stock_obj
    stock_layout = [
            [sg.Text('Stock')], ]
    c=0
    for dic in stock:
        stock_layout.append([sg.Text(f'CÓDIGO {c} --> {dic}')])
        c+=1
    window = sg.Window('Stock', stock_layout, size =(500,500))
    event, value = window.read()

    
   
        


















