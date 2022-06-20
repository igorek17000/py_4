import json
import os
from tkinter import N


from kuko_api_market import getPriceToken
#from kuko_api_user import amout_usd_account

dataJson = json.load(open('json/trade.json', 'r', ))


def open_Json(direction, type):
    d = json.load(open(direction, type))
    return d


def percentage_down(entryPrice, leverage, actualPrice ):
    percent_down = (actualPrice / entryPrice * leverage) - 1
    if percent_down > 1:
        messageMenu("Your price its over liquidation point")
        return False
    else:
        return percent_down



def clear_console():
    os.system('clear')


def messageMenu(mesage):
    clear_console()
    spaces(3)
    print(mesage)
    spaces(3)
    input("Press any key to Contunue: ")
    spaces(3)


def questionMenu(message):

    while True:

        clear_console()
        spaces(3)
        print(message)
        spaces(3)
        op = input("Press Y to accept or N to reget: ")
        spaces(3)
        if op == "y" or op == "Y":
            return True
        if op == "n" or op == "N":
            return False


def Condition_Bottom(key, var):
    if var == key or var == key.upper():
        return True
    else:
        return False


def spaces(n):
    x = 0
    while x <= n:
        print()
        x += 1


def top():
    clear_console()
    spaces(3)


def saveTrade():
    with open('json/trade.json', 'w') as outfile:
        json.dump(dataJson, outfile)


def checkABC(var):
    if not var.isalpha():
        messageMenu("Only ABC format its valid")
        return False
    else:
        return True


def mainScreen(price):
    clear_console()
    spaces(1)

    print("MAIN TRADING 0.4")
    spaces(3)

    print("BTC Price: ", price)
    spaces(3)
    print("A for Activate a Trade")
    spaces(1)
    print("E for Edit the Trade JSON")
    spaces(1)
    print("Q for Quit")
    spaces(1)


def checkNUM(var):
    if not var.isalnum():
        messageMenu("Only a NUMBER format its valid")
    else:
        return True


def newTrade(amout_usd_account):

    clear_console()

   

    def sym():
        while True:
            top()
            op = input("Name of the coin: ")

            if checkABC(op):

                if not op.isupper():
                    op = op.upper()
                    return op + 'USDT'

                else:
                    return op + 'USDT'

            else:
                pass

    def side():
        while True:
            top()
            op = input("Long or Short?:")

            if op == 'l' or op == 'L':
                op = 'long'
                return op

            if op == 'S' or op == 's':
                op = 'short'
                return op
            else:
                messageMenu("Enter a valid key")
                pass

    def leve():
        while True:
            top()
            op = input("Leverage Level: ")
            if checkNUM(op):
                op = int(op)
                if op > 0 and op < 25:
                    return op
                else:
                    if op < 1:
                        messageMenu("You cant enter a negative leverage")
                        pass
                    if op > 25:
                        messageMenu("Leverage too hight, lower it")
                        pass

    def limit_price(actual_price_token):
        while True:
            top()
            print("Actual price: ", getPriceToken(v_symbol))
            spaces(1)
            print("Trade Type: ", v_side)
            spaces(3)

            print(v_side)
            op = input("Enter a limit price: ")

            if checkNUM(op):
                op = float(op)
                if v_side == ('long',):

                    if op > actual_price_token:
                        if questionMenu("You want to put a higher price in a LONG limit, are you sure?"):
                            return op
                    else:
                        return op
                if v_side == ('short',):
                    if op < actual_price_token:
                        if questionMenu("You want to put a lower price in a SHORT limit, are you sure?"):
                            return op
                    else:
                        return op

    def size(actual_token_price, actual_account_USD_ammount):

        account_usd_with_lever = (actual_account_USD_ammount * v_lever)

        def size_calc(op):

            trade_usd_cost = (op * actual_token_price)

            if trade_usd_cost > account_usd_with_lever:
                messageMenu(
                    "Your size its higher than your whole account. Lower the size or Increment the Leverage")
                return False
            if trade_usd_cost > (account_usd_with_lever / 2):

                if questionMenu("Do you want to trade more than HALF or your account?"):
                    print("pepe")
                    return True
                else:
                    return False

        def percent(ammout, per):
            return round((( ammout / actual_token_price ) * per), 4)

        while True:
            top()
            print(f"Actual {v_symbol} price in USD is: {actual_token_price}")
            spaces(1)
            print(f"Actal USD ammount in Account: {actual_account_USD_ammount}")
            spaces(1)
            print(f"Actual USD ammount in Account by Leverage:{account_usd_with_lever} (x{v_lever})")
            spaces(1)

            print("25%: ", percent(account_usd_with_lever, 0.25))
            spaces(1)
            print("50%: ", percent(account_usd_with_lever, 0.5))
            spaces(1)
            print("75%: ", percent(account_usd_with_lever, 0.75))
            spaces(1)

            # if questionMenu("Do you want to enter the size instased of ", v_symbol, "ammount?"):
            #op = input("Enter a Size in USD:")
            op = input("Enter a size for trade: ")
            op = float(op)
            if size_calc(op):
                return op

    def stop(limit_price, side, type_limit, actual_account_USD_ammount):

        while True:
            top()

            order = None

            print(f"Limit Entry Price: {v_limit_price}")

            def loss_win_calc(type, op1, actual_account_USD_ammount):
                if type == "stop_l":
                    loss = ((op1 / v_limit_price) -1) * v_lever
                    if loss > (actual_account_USD_ammount * loss):
                        messageMenu(f"Your Stop Loss should be LOWER than your liquidation (${})")

            if type_limit == "stop_l":

                order = "Stop Loss Order Limit Price: "
            
            else:

                order = "Take Profit Order Limit Price: "

            op = input(order)
            
            if checkNUM(op):
                op = float(op)
                
                if type_limit == "stop_l":

                    if side == ('long',):
                        if op > limit_price:
                            messageMenu("In a LONG, your Stop Loss should be a number LOWER than your entry")
                        else:
                            return op
                    if side == ('short',):
                        if op < limit_price:
                            messageMenu("In a SHORT, your Stop Loss should be a number HIGHER than your entry")
                        else:
                            return op
                    
                
                if type_limit == "take_p":

                    if side == ('long',):
                        if op < limit_price:
                            messageMenu("In a LONG, your Take Profit should be a number HIGHER than your entry")
                        else:
                            return op
                    if side == ('short',):
                        if op > limit_price:
                            messageMenu("In a SHORT, your Take Profit should be a number LOWER than your entry")
                        else:
                            return op




    # v_symbol = sym(),
    # v_side = side(),
    # v_limit_price = limit_price(getPriceToken(v_symbol))
    # v_lever = leve()
    v_symbol = "XBTUSDM"
    v_side = ('long',)
    v_limit_price = 17000
    v_lever = 3
    v_size = size(getPriceToken(v_symbol), amout_usd_account)
    v_stop = stop(v_limit_price, v_side, "stop_l")
    v_tkprofit = stop(v_limit_price, v_side, "take_p")

    new_trade = {
        "id": len(dataJson),
        "symbol": v_symbol,
        "side": v_side,
        "size": v_size,
        "price": v_limit_price,
        "leverage": v_lever,
        "stop_loss": v_stop,
        "take_profit": v_tkprofit,
        "original_price": amout_usd_account
    }

    dataJson.append(new_trade)
    JsonOrder()


def JsonOrder():
    i = -1
    for x in dataJson:
        i = i + 1
        x["id"] = i


def deleteTrade(y):

    if y == "all":
        if questionMenu("Are you sure you want to delete ALL the trades?"):
            deleteAll()
            messageMenu("All trades has been Deleted")
            return True
        else:
            messageMenu("Operation Cancelled")
            return False
    else:

        if checkNUM(y):
            y = int(y)
            print(y)
            if y < 0 or y > len(dataJson):
                messageMenu("Out of range!")
                pass

            else:
                if questionMenu("You want to delete the trade?"):
                    y_int = int(y)

                    for x in dataJson:

                        if x["id"] == y_int:

                            dataJson.pop(y_int)
                            messageMenu("The trade has been deleted")

                else:
                    messageMenu("Operation Canceled")


def welcome():
    print("Trading File Editor")


def showTrades(data):
    if data == None:
        print("Empty trades")
    else:
        for x in data:
            spaces(1)
            print("ID:", x["id"], "TRADE:", x["symbol"], "SIDE:", x["side"], "PRICE:", x["price"],
                  "SIZE:", x["size"], "LEVERAGE X:", x["leverage"], "STOP PRICE:", x["stop_loss"], "TAKE PROFTI: ", x["take_profit"])


def options(op):
    if op == "a" or op == "A":
        newTrade()
        saveTrade()
        print("Trade Saved!")

    if op == "d" or op == "D":
        op3 = input("Witch?")
        deleteTrade(op3)
        saveTrade()

    if op == "s" or op == "S":
        showTrades(dataJson)

    if op == "all" or op == "ALL":
        deleteAll()


def deleteAll():

    dataJson.clear()
    saveTrade()


def tradeFileEdit():
    JsonOrder()
    op = input("Add, Show, Delete, Quit ?")


def make_trade(op1):
    for x in dataJson:
        if x["id"] == op1:
            print("Trading: ", x)


def activate_Menu():
    print("Activate Trade")
    showTrades(dataJson)
    spaces(3)
    print("Wich trade you want to make?")
    spaces(2)
    print("Press Q for Cancel")
    op = input()
    if Condition_Bottom("q", op):
        clear_console()
        pass
    else:
        make_trade(int(op))
