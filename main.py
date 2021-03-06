from functions import mainScreen, welcome, dataJson, JsonOrder, showTrades, activate_Menu, newTrade, Condition_Bottom, \
    saveTrade, deleteTrade, spaces, clear_console, messageMenu, top, spaces

from kuko_api_user import amout_usd_account


JsonOrder()
"""Loading file"""


while True:

    mainScreen("amout_usd")

    print("USDT ammount: ", amout_usd_account)

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
                newTrade(amout_usd_account)
                saveTrade()
            if Condition_Bottom("q", op1):
                break
            if Condition_Bottom("s", op1):
                messageMenu("All trades has been stoped")
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
                newTrade(amout_usd_account)
                saveTrade()
            if Condition_Bottom("d", op):

                while True:
                    clear_console()
                    top()
                    showTrades(dataJson)
                    spaces(2)

                    print("Select the trade you want to Delete: ")
                    spaces(1)
                    print("Press Q for Cancell")
                    op1 = input()

                    if Condition_Bottom("q", op1):
                        break

                    else:
                        deleteTrade(op1)
                        JsonOrder()
                        saveTrade()
