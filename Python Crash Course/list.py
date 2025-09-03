names = ["messi", "neymar", "ronaldo", "suarez"]
print(names)

# Accessing elements 

print(names[1])
print(names[1].title())
print(names[-1])

# Using individual values

message = f"My favourite player is {names[0].title()}"
print(message)

# Modifying elements

names[3] = "hazard"
print(names)

# Adding / removing elements

names.append("pogba") # Adding at lat position
print(names)

names.insert(1, "martinez") # Adding at an index
print(names)

del names[1] # removing at an index (deleting permenently)
print(names)

names.pop() # removing from lat position
print(names)

popped_name = names.pop(0)
print(popped_name)

names.remove("neymar") # removing by value
print(names)