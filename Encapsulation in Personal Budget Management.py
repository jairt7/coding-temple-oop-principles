# Encapsulation in Personal Budget Management

# Task 1: Define Budget Category Class
# Create a class `BudgetCategory` with private attribute for category name and allocated budget.
# Initialize these attributes in the constructor.

class BudgetCategory:
    def __init__(self, category, budget, expenses):
        self.__category = category
        self.__budget = budget
        self.__expenses = expenses

# Task 2: Implement Getters and Setters
# Write getter and setter methods for both the category name and the allocated budget.
# Ensure that the setter methods include validation (e.g., budget should be a positive number).

    def get_category(self):
        return self.__category
    
    def set_category(self, new_category):
        self.__category = new_category
    
    def get_budget(self):
        return self.__budget
    
    def set_budget(self, new_budget):
        if new_budget > 0:
            self.__budget = new_budget
        else:
            print("Budget should be a positive number.")

# Task 3: Add Budget Functionality
# Implement a method to add expenses to a category and adjust the budget accordingly.
# Validate the expense amount before making deductions from the budget.

    def add_expenses(self, amount):
        budget = self.get_budget()
        if amount <= budget:
            self.__expenses += amount
        else:
            print("Expense must be less than total budget.")

# Task 4: Display Budget Details
# Create a method to display the details of a budget category, including the name, allocated budget,
# and remaining budget after expenses.

    def display_category_summary(self):
        name = self.get_category()
        budget = self.get_budget()
        remaining_budget = budget - self.__expenses
        print(f"The {name} budget was ${budget}, and after expenses it is now ${remaining_budget}.")

food = BudgetCategory("food", 500, 0)
food.add_expenses(30)
food.display_category_summary()
video_games = BudgetCategory("Video Games", 200, 60)
video_games.add_expenses(30)
video_games.display_category_summary()
# Let me know if there's anything I did wrong, or anything else I need to do. Thanks!