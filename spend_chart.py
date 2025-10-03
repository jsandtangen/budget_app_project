def create_spend_chart(categories):
    total_spent = 0
    category_spent = []

    total_spent = sum(-item['amount'] for category in categories for item in category.ledger if item['amount'] < 0)
    for category in categories:
        spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        category_spent.append(spent)
    
    percentages = [(spent / total_spent) * 100 for spent in category_spent]
    percentages = [int(percentage / 10) * 10 for percentage in percentages]

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for percentage in percentages:
            chart += " o " if percentage >= i else "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_length = max(len(category.name) for category in categories)
    category_names = [category.name.ljust(max_length) for category in categories]

    for i in range(max_length):
        chart += "     "  
        for name in category_names:
            chart += name[i] + "  " 
        chart += "\n"

    return chart.rstrip("\n")  
