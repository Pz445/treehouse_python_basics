TICKET_PRICE = 10

tickets_remaining = 100

while tickets_remaining > 0:
    print("There are {} tickets remaining for this event.".format(tickets_remaining))
    username = input("What is your name?  ")
    # Expect and handle a ValueError
    try:
        tickets_needed = int(input("Hello {}, how many tickets do you need for this event?  ".format(username)))
        # Raise Value Error if request is for more than available
        if tickets_needed > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        # Include error text
        print("Oh no, we ran into an issue. {}. Please try again".format(err))
    else:
        total_price = tickets_needed * TICKET_PRICE
        print("The total cost for your tickets is ${}".format(total_price))
        confirmation = input("Do you wish to order {} tickets for ${} now?\nPlease enter Y or N  ".format(tickets_needed, total_price))
        if confirmation.lower() == 'y':
            print("Sold! Thank you for your purchase {}.".format(username))
            tickets_remaining -= tickets_needed
        else:
            print("Thank you for your interest {}!".format(username))

print("All sold out!")