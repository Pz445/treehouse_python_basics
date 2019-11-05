TICKET_PRICE = 10

tickets_remaining = 100  

# Output how many tickets are remaining
print("There are {} tickets remaining for this event.".format(tickets_remaining))

# Gather the user's name and assign it to a new variable
username = input("What is your name?  ")

# Prompt the user by name and ask how many tickets they would like
tickets_needed = int(input("Hello {}, how many tickets do you need for this event?  ".format(username)))

# Calculate the price (number of tickets * ticket price) and assign to variable
total_price = tickets_needed * TICKET_PRICE

# Output price to the screen
print("The total cost for your tickets is ${}".format(total_price))