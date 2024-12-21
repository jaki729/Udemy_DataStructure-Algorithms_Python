# What is Procedural programming?
# Procedural programming is about writing procedures or functions that perform operations on the data
# In procedural programming, the focus of the usage of functions is to provide a procedure that can be called to perform a specific task. 
# The data is exposed to the entire program and can be changed by any function that has access to it.
# Procedural programming follows a top-down approach.
# Procedural programming is also known as inline programming.

# Procedural Programming Concepts:
# 1. Procedure
# 2. Functions are the first-class citizens
# 3. Emphasis on procedure calls
# 4. Global data
# 5. Data is exposed to the entire program
# 6. Follows a top-down approach
# 7. Procedural programming is also known as inline programming 

# What is Object-Oriented Programming?
# Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes in programming.
# It aims to implement real-world entities like inheritance, hiding, polymorphism etc in programming.
# The main aim of OOP is to bind together the data and the functions that operate on them so that no other part of the code can access this data except that function.
# OOP follows a bottom-up approach in program design.
# OOP is a way to develop software that is modular, reusable and easy to maintain.

# OOPs Concepts:
# 1. Class
# 2. Object
# 3. Inheritance
# 4. Polymorphism
# 5. Abstraction
# 6. Encapsulation

# What is a Class?
# A class is a blueprint for the object.
# A class is a user-defined data type, which holds its own data members and member functions, 
# which can be accessed and used by creating an instance of that class.
# A class is like a template or a set of instructions to build a specific type of object.
# A class is defined by using the class keyword, followed by the name of the class and a colon.
# A class is a collection of objects.
# A class is a logical entity.

# What is an Object?
# An object is an instance of a class.
# When a class is defined, no memory is allocated but when it is instantiated (i.e. an object is created) memory is allocated.
# An object is a physical entity.
# An object is created using the constructor of the class. This object will then be called the instance of the class.
# An object is also called an instance of a class and the process of creating this object is called instantiation.
# In simple terms, a class is a blueprint for an object, and an object is an instance of a class.
# An object can be created using the new keyword. When an object is created, 
# memory is allocated and the constructor is called to initialize the object.
# An object is a real-world entity. Inherite properties and behaviors from the class.
# self is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# self keyword is used to access the attributes and methods of the class in python.
# self keyword is an object of the class.

# What is an attribute?
# An attribute is a named property of a class. It has a type. It describes the range of values that that it may hold(variables).
# An attribute is a variable that is bound to a class or an object.
# Attributes are the individual things that differentiate one object from another and determine the appearance, state, or other qualities of that object.
# In the class, an attribute is defined by using variables.
# Attributes are data stored inside a class or instance and represent the state or quality of the class or instance 
# Attributes are used to store information about the state of the object.
# Attributes are the properties of the object.

# What is a Method?
# A method is a group of statements that together performs action and returns the result.
# In OOP, a method is a function that belongs to a class.
# In OOP, methods define the behavior of the object.
# Methods are the functions that are defined in a class.
# Methods are used to define the behavior of an object.
# Methods are called by object name followed by the dot operator then method name.
# Methods are also called as functions. Combination of attributes and methods are called as class members.
# Behavior of the object is defined by methods.

# Example:
class YoutubeChannel:
    def __init__(self, username, subscribers=0, subscription=0):
        self.username = username
        self.subscribers = subscribers
        self.subscription = subscription
    
    def subscribe(self, user):
        self.subscribers += 1
        self.subscription += 1
    
    def unsubscribe(self, user):
        self.subscribers -= 1
        self.subscription -= 1

user1 = YoutubeChannel("John")
user2 = YoutubeChannel("Jane")
user1.subscribe(user2)
user2.subscribe(user1)
print(f"{user1.username} has {user1.subscribers} subscribers and {user1.subscription} subscriptions")
print(f"{user1.username} has subscription: {user1.subscription}")
print(f"{user2.username} has {user2.subscribers} subscribers and {user2.subscription} subscriptions")
print(f"{user2.username} has subscription: {user2.subscription}")
print(f"Total number of subscribers: {user1.subscribers + user2.subscribers}")
print(f"Total number of subscriptions: {user1.subscription + user2.subscription}")