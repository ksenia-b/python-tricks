# Instance method:
#   - can modify object instance state
#   - can modify instance state

# Class Method:
#   - can't modify object instance state
#   - can modify class state

# Static Method:
#   - Can't modify object instance state
#   - Can't modify class state

class MyClass():
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


# obj = MyClass()
# obj.classmethod

# example with Pizza
class Pizza():
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr(self):
        return f'Pizza({self.ingredients})'


print(Pizza(['cheese', 'tomatoes']))
print(Pizza(['cheese', 'tomatoes', 'ham']))
print(Pizza(['cheese', 'tomatoes', 'ham', 'cucumbers']))

# But don't want to remember all of the ingredients
# just use @classmethod

# example with Pizza
class Pizza():
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr(self):
        return f'Pizza({self.ingredients})'

    @classmethod
    def create_margherita(cls):
        return cls(['cheese', 'tomatoes'])

    @calssmethod
    def create_prosciutto(cls):
        return cls(['cheese', 'tomatoes', 'ham'])

Pizza.create_margherita()
Pizza.create_prociutto()