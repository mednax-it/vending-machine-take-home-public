class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class VendingMachine:

    def __init__(self):

        self.items = [
            Item("Cola", 1.00),
            Item("Chips", 0.50),
            Item("Candy", 0.65),
        ]

        self.money_inserted = 0.00

    def display_items(self):
        for code, item in enumerate(self.items, start=1):
            print(f"[{code}] - {item.name} (${item.price:.2f})")

    def insert_money(self, money):
        if money <= 0.00:
            raise ValueError
        self.money_inserted += money

def main():

    vending_machine = VendingMachine()
    vending_machine.display_items()

    while True:
        try:
            user_selection = int(input("Please enter item code: "))
        except ValueError:
            continue
        if user_selection in range(1, len(vending_machine.items)+1):
            break
    item = vending_machine.items[user_selection-1]
    print(f"You've selected \"{item.name}\" - the price is ${item.price:.2f}")
    while vending_machine.money_inserted < item.price:
        print(f"You've inserted ${vending_machine.money_inserted:.2f} into the machine so far.")
        while True:
            try:
                money_to_insert = float(input("Please enter the amount of money you'd like to insert: "))
                vending_machine.insert_money(money_to_insert)
            except ValueError:
                continue
            else:
                break
    print(f"Thank you! Please take your \"{item.name}\".")
    print(f"The remaining change in the machine is ${vending_machine.money_inserted - item.price:.2f}.")

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
