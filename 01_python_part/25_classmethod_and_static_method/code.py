class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print(f"Called static_method. We don't get any object or class info here.")

# test = ClassTest()
# test.instance_method()
# ClassTest.instance_method(test)

instance = ClassTest() # create a new object of type ClassTest
instance.instance_method()

ClassTest.class_method()
ClassTest.static_method()

# -- What are they used for? -- https://realpython.com/instance-class-and-static-methods-demystified/

# Instance methods are used for most things. When you want to produce an action that uses the data stored in an object.
# Static methods are used to just place a method inside a class because you feel it belongs there (i.e. for code organisation, mostly!)
# Class methods are often used as factories.

# Instance Methods
# The first method on MyClass, called method, is a regular instance method. That’s the basic, no-frills method type you’ll use most of the time. You can see the method takes one parameter, 
# self, which points to an instance of MyClass when the method is called (but of course instance methods can accept more than just one parameter).
# Through the self parameter, instance methods can freely access attributes and other methods on the same object. This gives them a lot of power when it comes to modifying an object’s state.
# Not only can they modify object state, instance methods can also access the class itself through the self.__class__ attribute. This means instance methods can also modify class state.

# Class Methods
# Let’s compare that to the second method, MyClass.classmethod. I marked this method with a @classmethod decorator to flag it as a class method.
# Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called.
# Because the class method only has access to this cls argument, it can’t modify object instance state. That would require access to self. However, class methods can still modify class state that applies across all instances of the class.

# Static Methods
# The third method, MyClass.staticmethod was marked with a @staticmethod decorator to flag it as a static method.
# This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters).
# Therefore a static method can neither modify object state nor class state. Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)
        # return Book(name, Book.TYPES[1], page_weight)


# heavy = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)

# print(heavy)
print(light)

# print(Book.TYPES)
# book = Book("Harry Potter", "hardcover", 1500)
book = Book.hardcover("Harry Potter", 1500)

# print(book.name)

print(book)