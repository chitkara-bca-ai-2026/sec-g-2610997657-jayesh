# Lab 14 - Library Book Collection
# Using tuples for book records and sets for categories

# Initial book records as list of tuples
books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering")
]

# Extract unique categories from initial books into a set
library_categories = set()
for book in books:
    library_categories.add(book[3])

# Student wishlist set
student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}

print("=" * 50)
print("   LIBRARY BOOK COLLECTION SYSTEM")
print("=" * 50)

while True:
    print("\n--- Menu ---")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        # View all books - unpack tuples
        print("\n--- Cataloged Books ---")
        for i, (title, author, year, category) in enumerate(books, 1):
            print(f"{i}. '{title}' by {author} ({year}) - Category: {category}")
        print(f"\nTotal books: {len(books)}")

    elif choice == "2":
        # Add a new book record as tuple
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")
        category = input("Enter category: ")
        new_book = (title, author, year, category)
        books.append(new_book)
        library_categories.add(category)
        print(f"Book '{title}' has been added to the collection.")

    elif choice == "3":
        # View unique library categories
        print("\n--- Unique Library Categories ---")
        for cat in sorted(library_categories):
            print(f"  - {cat}")
        print(f"\nTotal unique categories: {len(library_categories)}")

    elif choice == "4":
        # Add category to student wishlist
        category = input("Enter category to add to wishlist: ")
        student_wishlist.add(category)
        print(f"'{category}' has been added to the student wishlist.")

    elif choice == "5":
        # Category gap analysis using set operations
        print("\n--- Category Gap Analysis ---")

        # Categories in both library and wishlist
        common = library_categories.intersection(student_wishlist)
        print(f"\nCategories available in Library AND in Wishlist: {sorted(common)}")

        # Categories in wishlist but not in library
        missing = student_wishlist.difference(library_categories)
        print(f"Categories in Wishlist but NOT in Library: {sorted(missing)}")

        # All categories combined
        all_categories = library_categories.union(student_wishlist)
        print(f"All categories (Library + Wishlist): {sorted(all_categories)}")

    elif choice == "6":
        print("\nThank you for using the Library Book Collection System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
