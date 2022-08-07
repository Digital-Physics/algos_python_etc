# https://www.pythonmorsels.com/pointers/
print("In Python, variables are pointers to objects")
print("Some objects like Lists are mutable, others like Ints and Tuples are not")
print("Mutation vs. Assignment")
print("Mutations change objects; Assignment changes variables and the objects they point to")
print("Objects don't contain objects; they point to objects")
print("Data structures like dictionaries and lists contain pointers to objects, not objects themselves")
print("Think of a set of variable names, and a set of objects")
print("re-assigning variables updates the mapping/arrows from first set to the second set")
print("mutation of an object updates one of the objects in the second set without changing the variable mapping to the objects")

a = [1, 2, 3]
b = a
b.append(42)
print("a and b point to the same object; neither a nor b was ever overwritten/redefined/rebound/re-assigned")
print("the object they still both point to was mutated")
print(a, b)
print()

a = [1, 2, 3]
b = a
a = a + [42]
print("a and b are different; (re)assignment of a variable to new object took place; not a mutation of the object a pointed to")
print(a, b)
print()

a = [1,2,3]
b = a
a = [42]
print("a and b are different again; one variable was reassigned to a new object, so now a and b point to different objects")
print(a, b)
print()

print("rule to avoid errors (and reliance on deep copy):")
print("it is ok to set one variable equal to another (so they both point to same obj) if one of the variables will later be re-assigned")
print("it is also ok if you want the two variables to change in tandem when the object they point to is mutated")
print("if a variable is reassigned, the 2 vars/pointers will point to different objects after that point")
print("note: appending is mutating a list object")
print("note: popping is mutating a list object")
print("note: concatenation would involve reassigning a variable/pointer to a new concatenated object")
