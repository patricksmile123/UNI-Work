nice_list = ["Alice", "Mark", "Hannah", "Vic", "Bob", "Charlie"]
naughty_list = ["Colin", "Monica", "Sophie", "Dani", "Eve", "Mallory", "Trudy"]

# import random
# combine nice list and naughty list to create general list
# create a for loop which makes a variable with the rand.randint inside it so it keeps changing
# take the rand int variable as the index for general list.
# If name is in nice_list print name + nice message else print name + nasty message

import random

general_list = ["Alice", "Mark", "Hannah", "Vic", "Bob", "Charlie","Colin", "Monica", "Sophie", "Dani", "Eve", "Mallory", "Trudy" ]
for name in general_list:
    index_number = random.randint(range(len(general_list))
    