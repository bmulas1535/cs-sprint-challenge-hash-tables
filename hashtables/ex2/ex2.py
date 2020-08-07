#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Totally overthought this one, btw
    # Each ticket has a start and a stop.
    # Put the tickets in a dictionary with the start as the key, 
    # and the stop as the value.
    tickets_dict = {ticket.source : ticket.destination for ticket in tickets}
    # Base start value is always NONE, so create a variable to track our start points
    start = "NONE"
    # Create a list to hold our path
    route = list()
    # Make n number of iterations, where n is the same length as the list of tickets.
    for _i in range(length):
        ## Pull the key with the start location as defined from the variable we set
        destination = tickets_dict[start]
        ## append this destination to the path
        route.append(destination)
        ## Update the start location to the current destination for the next
        ## iteration
        start = destination
    return route
