class ShoeInventory:

    def __init__(self, shoe_sizes):

        self.inventory = {size: 0 for size in shoe_sizes}



    def add_shoes(self, size, quantity):

        self.inventory[size] += quantity



    def sell_shoes(self, size):

        if self.inventory.get(size, 0) > 0:

            self.inventory[size] -= 1

            return True

        return False



class TransactionManager:

    def __init__(self, shoe_inventory):

        self.shoe_inventory = shoe_inventory

        self.total_revenue = 0



    def process_transactions(self, customer_requests):

        for size, price in customer_requests:

            if self.shoe_inventory.sell_shoes(size):

                self.total_revenue += price



# Read input

X = int(input())  # Total number of shoes

shoe_sizes = list(map(int, input().split()))  # Shoe sizes available

N = int(input())  # Number of customer requests



# Initialize shoe inventory

inventory = ShoeInventory(shoe_sizes)



# Populate initial inventory

for size in shoe_sizes:

    inventory.add_shoes(size, X // len(shoe_sizes))



# Initialize transaction manager

transaction_manager = TransactionManager(inventory)



# Process transactions

for _ in range(N):

    size, price = map(int, input().split())

    transaction_manager.process_transactions([(size, price)])



# Print total revenue

print(transaction_manager.total_revenue)
