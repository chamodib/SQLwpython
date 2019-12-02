# SQLwpython
This is a Python program written to search and insert data into a database based in SQL Server. The database consists of AirBnB data, contained within 4 tables: Listings, Bookings, Reviews and Calendar. 
(The database is secured and cannot be accessed by anyone outside)

The program is created based on the following assignment:

Search Listings
1. This function allows the user to search for a suitable listing the satisfies certain criteria.
2. A user should be able to set the following filters as their search criteria: minimum and
maximum price, number of bedrooms, and start and end date.
3. After the search is complete, a list of search results must be shown to the user. The list
must include the following information for each listing: id, name, first 25 characters of
description, number of bedrooms, price. The results can be shown on the terminal or in a
GUI.
4. If the search result is empty, an appropriate message should be shown to the user.

Book Listing
1. A user must be able to select a listing from the results of the function Search Listings and
book it. This can be done by entering the listing’s id in a terminal or by clicking at a listing
in a GUI.
2. All the booking information should be recorded in the Booking table.
3. When a listing is booked, the Calendar table needs to be updated as well. This should
happen by the first trigger you wrote for assignment 4.

Write Review
1. A user should be able to write a review of a listing after his stay in that listing.
2. To write a review, a user must enter their name and the program should show all the
bookings of that user. Then the user can select one of their bookings and write a review of
that listing.
3. The following information should be asked from the user who wants to write a review:
user’s name, current date, review text.
4. The program should allow a review only if the given date is after the stay_to attribute of
the related booking record. You need to make sure that the triggers you implemented in
assignment 4 are working properly with your application program. If any error happened
in a trigger, your program should print the trigger’s error message and let the user know
that the review was not stored. 


Some important points regarding the code:  
1. The database has all the data from CSV files and triggers for booking and reviewing implemented. 
2. Everything loops back to the main user prompt asking them to choose to search, book or review listings. Although you can book or review thing directly, it is recommended to ALWAYS search listings before booking or reviewing to reduce errors.   
3. Although error handling is written in, some things were not handled. For example, entering a different type of variable (string) instead of a (int). It will throw an error and shut down program. However you CAN leave things blank. More information is provided in sections below. 
4. The connection doesn’t close until the user closes the window. It’s programmed to loop until then. 
5. If no results are found, a message will be printed.  
