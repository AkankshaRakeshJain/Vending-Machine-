import os
class VendingMachine:
    power_status = False
    def __init__(self):
        if VendingMachine.power_status == False:
            self.power()

        self.dict_print = {
            'chips':{'code':'A1','price':30,'quantity':2},
            'chocolate':{'code':'A2','price':20,'quantity':2},
            'juice':{'code':'A3','price':20,'quantity':2},

            'pastry':{'code':'B1','price':40,'quantity':2},
            'ice-cream':{'code':'B2','price':40,'quantity':2},
            'snacks':{'code':'B3','price':50,'quantity':2},
        }

        while VendingMachine.power_status == True:
            pop_dict = self.quantity()
            if pop_dict != True:
                if self.dict_print[pop_dict]['quantity'] == 0:
                    self.dict_print.pop(pop_dict)
            self.display()
            if len(self.dict_print) > 0:      
                choice = input('Your Choice: ')
                for product_name,product_info in self.dict_print.items():
                    for key in product_info:
                        if product_info[key] == choice:                
                            pay = int(input('Please pay Rs{}: '.format(product_info['price'])))
                            if product_info['price'] == pay:
                                product_info['quantity'] -= 1
                                print('Collect your product')
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print()
                            else:
                                print('Wrong amount')
                else:
                    print('Incorrect input. Try again')
            else:
                print('Empty Machine. Powering OFF')
                VendingMachine.power_status = False
        

    def quantity(self):
        for product_name,product_info in self.dict_print.items():
            if product_info['quantity'] == 0:
                return product_name
            else:
                return True    
    
    def power(self):
        VendingMachine.power_status = True
        return VendingMachine.power_status

    def display(self):
        for product_name,product_info in self.dict_print.items():             
            print(product_name)
            for key in product_info:
                if key != 'quantity':
                    print(key,' : ',product_info[key])
        print()

vm = VendingMachine()
        
