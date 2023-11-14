# Author: Ryan Rinvil

# list of 4 colors and store it as a variable.
colors = ["red", "blue", "green", "yellow"]

# method to add 3 more colors to the list in a single statement.
colors.extend(["orange", "purple", "pink"])

# different method to add one additional color to the list.
colors.append("brown")

# method to insert a new color at index 3.
colors.insert(3, "violet")

# copy of the list.
colors_copy = colors.copy()

# method to remove one element from the copy of the list.
colors_copy.pop(2)  # Removes the element at index 2, which is "green"
