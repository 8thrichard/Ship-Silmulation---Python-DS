# Ship-Silmulation---Python-DS
- Assignment Requirements;
- The Chaos Cruise Ship simulation!

The rules:
passengers /staff start in a mixed up line arriving at different times to board the ship
passengers / staff have reservations but need room assignments
passengers with GREEN passes get rooms on A deck - total rooms = 20
passengers with BLUE passes get rooms on B deck - total rooms = 100
passengers with ORANGE passes get rooms on C deck - total rooms = 200
passengers with RED passes are STAFF and get assigned rooms on D deck - total rooms = 500
passengers accumulate in the line all mixed up and your program needs to process / simulate each passenger as they come onboard the ship
you determine the data structure, but choose wisely. 
the following data structure rules must be met by your code:
passenger/ staff line FIFO
each passenger / staff room data structure LIFO (remove the room once it's used to avoid duplication of rooms
check and verify availability, don't overflow the data structures - make sure each passenger has their own appropriate room - VERIFY!
the line will contain 820 individual seeking rooms (the ship is full), make sure each passenger is processed before the ship leaves
simulate this line with random generation, but control it to make sure correct number of passengers get on the correct decks
simulations printout should include:
Passenger name, pass color, new room assignment, deck number (as the line simulation is moving forward)  Add sleep time to slow it down.
Final output of the program should be a room manifest with duplicates checked in a table format (use tabulate library to give it a good clean look)  All passengers must have their own room with no surprises :).
