class User:
    """User class"""
    common_var = "Something in common"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"User [name={self.name}, age={self.age}]"


bob = User('Bob', 30)
ann = User('Anna', 24)
bob.id = 1
print(bob.__str__())
print(bob.id)
print(bob.__doc__)
print(bob.common_var)

print(ann.__str__())
# AttributeError: 'User' object has no attribute 'id'
# print(ann.id)
print(ann.__doc__)
print(ann.common_var)
