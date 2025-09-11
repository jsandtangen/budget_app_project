from category import Category
from spend_chart import create_spend_chart

# Example Usage
if __name__ == "__main__":
    food = Category('Food')
    food.deposit(1000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')

    clothing = Category('Clothing')
    food.transfer(50, clothing)

    print(food)

    # Creating a spend chart
    print(create_spend_chart([food, clothing]))
