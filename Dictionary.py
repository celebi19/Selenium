thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

# example 1

Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
print(type(Employee))
print("printing Employee data .... ")
print("Name : %s" %Employee["Name"])
print("Age : %d" %Employee["Age"])
print("Salary : %d" %Employee["salary"])
print("Company : %s" %Employee["Company"])

print("Name: %s" %Employee["Name"])

x = Employee["Age"]
print(x)

x = Employee.get("Age") # same results above without using print command.
print(x)

print("Age: %d" %Employee["Age"])
print("Age:" , x)

#Employee["Name"] = input("Name:")
del Employee["Name"]

for x in Employee:
    print(x)   # prints  all keys " Age, Salary, Company. Note that Name was deleted earlier"

for x in Employee:
    print(Employee) # printS 3 times "{'Age': 29, 'salary': 25000, 'Company': 'GOOGLE'}"

for x in Employee:
    print(Employee[x]) # prints all values " 29, 2500, GOOGLE"

for x in Employee.values():
    print(x)   # print all values using values method

for x in Employee.items():
    print(x)  # prints all items using items method



Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
print(Employee) # prints " {'Name': 'John', 'Age': 29, 'salary': 25000, 'Company': 'GOOGLE'} "



# Example 2

Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
Employee["Name"] = "Hakan"
print(Employee)

# Example 3

Employee = {"Name": "John", "Age": 29, "Salary":25000,"Company":"GOOGLE","Name":"Newname"}
for x,y in Employee.items():
    print(x,y) # notice that name is printed "Newname" not John as Newname was assigned later.

