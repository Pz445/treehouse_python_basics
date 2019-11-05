TICKET_PRICE = 10

tickets_remaining = 100  

# Run all code until tickets run out
while tickets_remaining > 0:

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

    # Prompt confirm order.  Y/N
    confirmation = input("Do you wish to order {} tickets for ${} now?\nPlease enter Y or N  ".format(tickets_needed, total_price))
    confirmation = confirmation.lower()
    # If yes
    if confirmation == 'y':
        # print SOLD! to confirm purchase
        print("Sold! Thank you for your purchase {}.".format(username))
        # reduce remaining ticket count
        tickets_remaining -= tickets_needed
    # otherwise Thank them by name
    else:
        print("Thank you for your interest {}!".format(username))

# Notify user tickets sold out
print("All sold out!")