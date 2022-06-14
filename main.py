from functions import deleteAll, welcome, dataJson, JsonOrder, showTrades, options, activate_Menu, newTrade, Condition_Bottom, \
    saveTrade, deleteTrade, spaces, clear_console, messageMenu, top, spaces


JsonOrder()
"""Loading file"""

while True:
    clear_console()
    spaces(1)
    print("MAIN TRADING 0.4")
    spaces(3)
    print("A for Activate a Trade")
    spaces(1)
    print("E for Edit the Trade JSON")
    spaces(1)
    print("Q for Quit")
    spaces(1)

    op = input()
    clear_console()
    if Condition_Bottom("q", op):
        break

    if Condition_Bottom("a", op):

        while True:
            clear_console()
            spaces(3)
            activate_Menu()
            spaces(1)
            print("Press T for adding more trades. ")
            spaces(1)
            print("Press S for stop all the actual tradings")
            spaces(1)
            print("Press Q for back to main menu")
            spaces(1)

            op1 = input()

            if Condition_Bottom("t", op1):
                pass
            if Condition_Bottom("q", op1):
                break
            if Condition_Bottom("s", op1):
                spaces(3)
                print("All trading Stopped")
                spaces(1)
                input()
                pass



    if Condition_Bottom("e", op):

        while True:
            clear_console()
            welcome()
            spaces(3)
            JsonOrder()
            op1 = None
            showTrades(dataJson)
            spaces(3)
            op = input("(A)dd, (D)elete, (Q)uit ?")

            if Condition_Bottom("q", op):
                break
            if Condition_Bottom("a", op):
                newTrade()
                saveTrade()
            if Condition_Bottom("d", op):

                while True:
                    clear_console()
                    top()
                    showTrades(dataJson)
                    spaces(2)
                    
                    op1 = input("Select the trade you want to Delete: ")
                    spaces(3)
                    print("Press Q for Cancell")

                    if Condition_Bottom("q", op1):
                        messageMenu("Operation Cancelled")
                        break
                    
                    else: 
                        deleteTrade(op1)
                        JsonOrder()
                        saveTrade()
                    
                        



