# class Dog:

#     def __init__(self, name, breed, owner):
#         self.name = name
#         self.breed = breed
#         self.owner = owner

#     def bark(self):
#         print('whoof')


# class Owner:
#     def __init__(self, name, address, contact_number):
#         self.name = name
#         self.address = address
#         self.phone_number = contact_number



# class Person:
#     def  __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"my name is {self.name} and I am {self.age} years old. " )


# person = Person("alice", 30)
# person.greet()

# owner1 = Owner("Dany", "sfdf", "88-99")

# dog1 = Dog("Bruce", "ROTT", owner1)
# dog2 = Dog("Scott", "Something", owner1)

# print(dog1.name, dog2.name)

                                                    
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
    

user1 = User('dantheman', "dAan@gmail.com", "123")

print(user1.email)
# print(user1.set_email("harshit@mal.com"))
user1.email = 'harshit@mal.com'
print(user1.email)

# user2 = User('batman', )"bat@gmail.com", "abc")
# print(user1.clean_email())


