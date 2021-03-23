class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


        ## -- str method - you wanna turn your object into a string or print(str(bob))

    # def __str__(self): ## use when you want to turn your object into a string (print easy to read string for users)
    #     #return "hello"
    #     return f"Person {self.name}, {self.age} years old."


        ## -- repr method - is used to print out an unambiguous representetion of an object - user for recreate an object if you were
        ## a programmer looking at that output

        ## user just one of them in your code

    def __repr__(self): ## return a string that allows us to recreate the original object very easily
        return f"<Person('{self.name}', {self.age} years old.)>" ## <> tell programmers that read this string here
        ## that we printing out an object


bob = Person("Bob", 35)
print(bob)  # Not the nicest thing to read! ## $ <__main__.Person object at 0x7fbf730f9ee0> 

## Person() == Person.__init__()
bob.__repr__()