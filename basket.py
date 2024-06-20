class Basket():

    def __init__(self, items=None):
        if items is None:
            self.basket = []
        else:
            self.basket = items

    def add_item(self, item):
        self.basket.append(item)

    def print_contents(self):
        print(self.basket)

def main():
    items = ["apple", "pear", "potato"]
    basket = Basket(items)

    basket.print_contents()
    
    basket.add_item("orange")
    basket.print_contents()


if __name__ == "__main__":
    main()
