from curses.panel import bottom_panel
from email.message import Message
import json
import os


dataJson = json.load(open('json/trade.json', 'r', ))


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


def back(actual, before):
    if Condition_Bottom("b", actual):
        return before()
    else:
        pass


def checkNUM(var):
    if not var.isdigit():
        messageMenu("Only a NUMBER format its valid")
    else:
        return True


def newTrade():

    clear_console()

    def show_Size_USD(size, price, leverage):
        usd = (price * size) / leverage
        print(usd)
        return usd

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
                op = 'l'
                return op

            if op == 'S' or op == 's':
                op = 's'
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

    def size():
        while True:
            op = input("Enter your size: ")
            print("Your size is: ", show_Size_USD)
            print("Press any key to contunue:")
            op1 = input()
            while True:
                if not Condition_Bottom("q", op1):
                    return op
                else:
                    pass

    def price():
        while True:
            op = input("Enter your price: ")
            if not checkNUM(op):
                messageMenu("Try to put a number")
            else:
                return int(op)

    def stopl(type, side, price):
        while True:
            top()
            op = input("Limit Price Trigger: ")
            op = int(op)

            if type == "limit":
                if side == "long":
                    if price > op:
                        return op
                    else:
                        messageMenu(
                            "In a Long, you cannot enter a Stop Loss lower than your buy price")
                        pass
                if side != "long":
                    if price < op:
                        return op
                    else:
                        messageMenu(
                            "In a Short, you cannot enter a Stop Loss higher than your buy price")
                        pass
            if type == "market":
                messageMenu("Unnused feature for now")

    id = len(dataJson)
    v_symbol = sym()
    v_side = side()
    v_type = "limit"
    v_price = price()
    v_leverage = leve()
    v_size = size()
    v_stop_lose = v_price * 0.95
    #v_stop_lose = stopl(v_type, v_side, v_price)

    new_trade = {
        "id": id,
        "side": v_side,
        "symbol": v_symbol,
        "type": v_type,
        "size": v_size,
        "leverage": v_leverage,
        "price": v_price,
        "stop": v_stop_lose
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
            print("ID:", x["id"], "SIDE:", x["side"], "symbol:", x["symbol"], "PRICE:", x["price"],
                  "SIZE:", x["size"], "LEVERAGE X:", x["leverage"], "STOP PRICE:", x["stop"])


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
