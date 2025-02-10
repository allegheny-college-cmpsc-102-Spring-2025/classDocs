import random

## Generate some random data

# Function to generate a random phone number
def generate_phone_number():
    return f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
# end of generate_phone_number()

# Function to generate a random email address
def generate_email():
    domains = ["gmail.com", 
               "yahoo.com", 
               "hotmail.com", 
               "example.com"]
    return f"{random.choice(domains)}"
# end of generate_email()

# List of random names_list
names_list = ["Alice", 
              "Bob", 
              "Charlie", 
              "David", 
              "Eve"]

# Creating the dictionary from which we select names_list
contacts = {}
for name in names_list:
    phone_number = generate_phone_number()
    email_address = f"{name.lower()}_{random.randint(1, 100)}@{generate_email()}"
    contacts[name] = [phone_number, email_address]

    
# Displaying the dictionary
print(f" My Contacts:\n   {contacts}")

###

# Randomly selecting a name
thisName = random.choice(names_list)
number = contacts[thisName][0]
email = contacts[thisName][1]

print("\n And the winner is ... \n")
print(f" Name: {thisName}")
print(f"   number: {number}")
print(f"   email: {email}")
