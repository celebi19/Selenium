
class User:
    def __init__(self,full_name, birthday):

       self.name = full_name
       self.birthday = birthday

user =  User("Dave Bowman", "19710315")
print(user.name)
print(user.birthday)
print(user.name + " " + user.birthday)








