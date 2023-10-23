import hou

# Define OBJ environment
env = hou.node("/obj")

# Define Planets names
scaffolding_items = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Create Scaffolding
for i, each in enumerate(scaffolding_items):
        item = env.createNode("geo", each)

# Layout children in network view (/obj)
env.layoutChildren()


