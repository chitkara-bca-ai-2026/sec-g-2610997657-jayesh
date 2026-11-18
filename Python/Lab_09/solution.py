# Lab 09 - Festival Decoration Designer
# Generate different patterns using nested loops

n = int(input("Enter the number of rows: "))

# Pattern 1: Star Triangle (Right-Angled)
print("Pattern 1: Star Triangle")
print("------------------------------")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == i:
            print("*", end="")
        else:
            print("*", end=" ")
    print()

print()

# Pattern 2: Number Triangle
print("Pattern 2: Number Triangle")
print("------------------------------")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == i:
            print(j, end="")
        else:
            print(j, end=" ")
    print()

print()

# Pattern 3: Inverted Star Triangle
print("Pattern 3: Inverted Star Triangle")
print("------------------------------")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        if j == i:
            print("*", end="")
        else:
            print("*", end=" ")
    print()

print()

# Pattern 4: Pyramid (Centered Triangle)
print("Pattern 4: Pyramid")
print("------------------------------")
for i in range(1, n + 1):
    # number of stars in each row = 2*i - 1
    stars = 2 * i - 1
    # spaces before stars for centering
    spaces = n - i
    # Print leading spaces
    print("  " * spaces, end="")
    # Print stars with spaces between them
    for j in range(1, stars + 1):
        if j == stars:
            print("*", end="")
        else:
            print("*", end=" ")
    print()
