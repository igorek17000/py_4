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
    if not var.isdigit():
        messageMenu("Only a NUMBER format its valid")
    else:
        return True



        

def newTrade():

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


                        
    v_symbol =  sym(),
    v_side = side(),
    v_limit_price = input("Limit price")
    v_size = input("Size order")
    v_lever = leve()
    v_stop = input("Stop limit")
    v_tkprofit = input("Take Profit")


    new_trade = {
        "id": len(dataJson),
        "symbol": v_symbol,
        "side": v_side, 
        "size": v_size,
        "price": v_limit_price,
        "leverage": v_lever ,
        "stop_loss": v_stop,
        "take_profit": v_tkprofit
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
