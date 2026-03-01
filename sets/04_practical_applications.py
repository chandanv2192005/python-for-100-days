# Practical Applications of Sets in Python

# 1. Deduplication (Removing Duplicates)
# Converting a list to a set automatically removes duplicates.
raw_emails = ["user1@example.com", "user2@example.com", "user1@example.com", "user3@example.com"]
unique_emails = list(set(raw_emails))
print(f"Original: {raw_emails}")
print(f"Unique: {unique_emails}")

# 2. Efficient Membership Testing
# Sets are optimized for O(1) lookups, unlike lists O(n).
banned_users = {"spam_king", "troll_master", "bot_99"}
current_user = "troll_master"

if current_user in banned_users:
    print(f"Access Denied for {current_user}")

# 3. Data Filtering & Comparison
# Comparing two datasets (e.g., active vs. all users).
all_employees = {"Alice", "Bob", "Charlie", "David", "Eve"}
signed_up_for_webinar = {"Alice", "Charlie", "Eve"}

# Find employees who HAVEN'T signed up yet
missing_employees = all_employees.difference(signed_up_for_webinar)
print(f"Employees yet to sign up: {missing_employees}")

# 4. Finding Mutual Interests (Intersection)
user_a_interests = {"coding", "hiking", "gaming", "music"}
user_b_interests = {"music", "cooking", "hiking", "travel"}

common_interests = user_a_interests.intersection(user_b_interests)
print(f"Common Interests: {common_interests}")

# 5. Inventory Management (Symmetric Difference)
# Finding items that are unique to each warehouse
warehouse_a = {"Apples", "Bananas", "Oranges"}
warehouse_b = {"Bananas", "Pears", "Grapes"}

unique_items = warehouse_a.symmetric_difference(warehouse_b)
print(f"Items unique to each warehouse: {unique_items}")
