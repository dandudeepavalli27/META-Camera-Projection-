# SESSION 8 – Camera Projection (Pinhole Camera Model)

# Step 1: Input values
f = 600   # focal length
X = 3     # horizontal coordinate
Z = 6     # depth

# Step 2: Apply projection formula
u = (f * X) / Z

# Step 3: Display result
print("Projected pixel coordinate u =", u, "pixels")

print("\nProgram Executed Successfully")
