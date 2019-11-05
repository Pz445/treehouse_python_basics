TICKET_PRICE = 10

SERVICE_CHARGE = 2

tickets_remaining = 100

def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining > 0:
    print("There are {} tickets remaining for this event.".format(tickets_remaining))
    username = input("What is your name?  ")
    try:
        tickets_needed = int(input("Hello {}, how many tickets do you need for this event?  ".format(username)))
        if tickets_needed > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue. {}. Please try again".format(err))
    else:
        total_price = calculate_price(tickets_needed)
        print("The total cost for your tickets is ${}".format(total_price))
        confirmation = input("Do you wish to order {} tickets for ${} now?\nPlease enter Y or N  ".format(tickets_needed, total_price))
        if confirmation.lower() == 'y':
            print("Sold! Thank you for your purchase {}.".format(username))
            tickets_remaining -= tickets_needed
        else:
            print("Thank you for your interest {}!".format(username))

print("All sold out!")