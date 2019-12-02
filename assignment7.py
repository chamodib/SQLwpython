#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!pip install pyodbc  
print("Hello there! Welcome :)")
import pyodbc
import datetime


conn = pyodbc.connect('driver={SQL Server};Server="";Trusted_Connection=yes;')

cur = conn.cursor()

# to validate the connection
cur.execute('SELECT username,password from ""')


loop = 1

while loop == 1:
    print(("\nEnter 1 to SEARCH for Listings , 2 for BOOKING a Listings or 3 to REVIEW a Listing \n"))
    cus_input = input ("Enter 1, 2 or 3: ")
    
    # Searching 
    if cus_input == "1":
            
        print("\nPlease provide following information: \n")
        
        cus_price = input ("Enter 1 to Filter Prices [Min -> Max], Enter 2 to Filter Prices [Max -> Min]: ")
        cus_rooms = input ("Enter the number of bedrooms you look for: ")
        cus_start = input ("Enter the start date: ")
        cus_end = input ("Enter the end date: ")
        
        #Counting days needed
        from datetime import datetime
        stdate = datetime.fromisoformat(cus_start)
        endate = datetime.fromisoformat(cus_end)
        dcount = (endate - stdate).days
        #print(dcount)

        print("\n")
        
        # Filter for ASC prices
        if cus_price == "1":
            
            SQLCommand = ("SELECT listing_id, number_of_bedrooms,  MAX(price), name, SUBSTRING(description,1,25)FROM Calendar INNER JOIN Listings ON Calendar.listing_id = Listings.id WHERE number_of_bedrooms = ? AND date >= ? AND date <= ? AND available = 1 AND (SELECT Count(listing_id) FROM Calendar WHERE date>= ? AND date <= ? AND available = 1 AND Calendar.listing_id = Listings.id AND number_of_bedrooms = ? ) >= ? GROUP BY listing_id, name, description, number_of_bedrooms ORDER BY MAX(price) ASC")  
            values = [cus_rooms, cus_start, cus_end, cus_start, cus_end, cus_rooms, dcount+1]
            cur.execute(SQLCommand, values)
            results = cur.fetchone()
            
            #If no results are found
            if results is None:
                print("\nNo results are found for your criteria\n")
            else:
                while results:
                    print(str(results[0]) + "  |  " + str(results[1])  + "  |  " +  str(results[2]) + "  |  " +  str(results[3]) + "  |  " +  str(results[4]))
                    print()
                    results = cur.fetchone()
 
            results = cur.fetchone()  

        # Filter for DESC prices
        elif cus_price == "2":
            
            SQLCommand = ("SELECT listing_id, number_of_bedrooms,  MAX(price), name, SUBSTRING(description,1,25)FROM Calendar INNER JOIN Listings ON Calendar.listing_id = Listings.id WHERE number_of_bedrooms = ? AND date >= ? AND date <= ? AND available = 1 AND (SELECT Count(listing_id) FROM Calendar WHERE date>= ? AND date <= ? AND available = 1 AND Calendar.listing_id = Listings.id AND number_of_bedrooms = ? ) >= ? GROUP BY listing_id, name, description, number_of_bedrooms ORDER BY MAX(price) DESC") 
            values = [cus_rooms, cus_start, cus_end, cus_start, cus_end, cus_rooms, dcount+1]
            cur.execute(SQLCommand, values)
            results = cur.fetchone()
            
            #If no results are found
            if results is None:
                print("\nNo results are found for your criteria\n")
            else:
                while results:
                    print(str(results[0]) + "  |  " + str(results[1])  + "  |  " +  str(results[2]) + "  |  " +  str(results[3]) + "  |  " +  str(results[4]))
                    print()
                    results = cur.fetchone()
            conn.commit()
            
        #If no price filtering specified - show in random order    
        elif cus_price == "":
            
            SQLCommand = ("SELECT listing_id, number_of_bedrooms,  MAX(price), name, SUBSTRING(description,1,25)FROM Calendar INNER JOIN Listings ON Calendar.listing_id = Listings.id WHERE number_of_bedrooms = ? AND date >= ? AND date <= ? AND available = 1 AND (SELECT Count(listing_id) FROM Calendar WHERE date>= ? AND date <= ? AND available = 1 AND Calendar.listing_id = Listings.id AND number_of_bedrooms = ? ) >= ? GROUP BY listing_id, name, description, number_of_bedrooms ORDER BY MAX(price) ASC")  
            values = [cus_rooms, cus_start, cus_end, cus_start, cus_end, cus_rooms, dcount+1]
            cur.execute(SQLCommand, values)
            results = cur.fetchone()
            
            
            #If no results are found
            if results is None:
                print("\nNo results are found for your criteria\n")
            else:
                while results:
                    print(str(results[0]) + "  |  " + str(results[1])  + "  |  " +  str(results[2]) + "  |  " +  str(results[3]) + "  |  " +  str(results[4]))
                    print()
                    results = cur.fetchone()
            #results = cur.fetchone()  
                        
        #If entered a random number    
        else:
            print ("\nInvalid input for pricing filter. Please Enter 1 for Min and Enter 2 for Max\n")
       
    
    # Book Listing
    elif cus_input == "2":
        
        #Getting user input
        print("\nTo make a Booking, enter following information\n")
        cus_input_listing = input ("Enter the listing id: ")
        cus_input_name = input ("Enter your name: ")
        cus_input_from = input ("Enter the start date (format year-month-date): ")
        cus_input_to = input ("Enter the end date (format year-month-date): ")
        cus_input_guest = input ("Enter the number of guests: ")
        
        #Getting maximum ID to create new one
        SQLCommand0 = ("SELECT MAX(id) FROM Bookings")
        cur.execute(SQLCommand0)
        results = cur.fetchone()
        
        #If table is empty, start with 0 and add 1
        max_id = results[0]
        if max_id is None:
            max_id = 0
        new_id = max_id +1
        
        #Add a booking given user input
        SQLCommand = ("INSERT INTO Bookings (id, listing_id, guest_name, stay_from, stay_to, number_of_guests) VALUES (?,?,?,?,?,?)")
        values = [new_id, cus_input_listing,cus_input_name, cus_input_from,cus_input_to,cus_input_guest ]
        cur.execute(SQLCommand, values)
        conn.commit() 
        
        #Show the bookings 
        SQLCommand1 = ("SELECT * FROM Bookings WHERE id = ?")
        cur.execute(SQLCommand1, new_id)
        results = cur.fetchone()
        #SQLCommand2 = ("SELECT * FROM Calendar WHERE listing_id = 6606")
        #cur.execute(SQLCommand2)
        
            
        #If no results are found
        if results is None:
            print("\nNo results are found for your criteria\n")
        else:
            while results:
                print(results)
                results = cur.fetchone()
            
        
        
    # Reviwe Listing
    elif cus_input == "3":
        print("\nTo write a review, please provide the following information\n")
        
        #Show their booked list
        cus_input0 = input ("\nEnter your name: ")
        SQLCommand = ("SELECT id, listing_id, stay_from, stay_to FROM Bookings WHERE guest_name = ?")
        cur.execute(SQLCommand, cus_input0)
        results = cur.fetchone()
        
        #Print the results
        if results is None:
            print("\nNo bookings are found for your name \n")
        else:
            while results:
                print(results)
                results = cur.fetchone()
        
            #Take customer input
            cus_input1 = input ("\nEnter the Listing ID: ")
            cus_input2 =input ("\nEnter Booking ID: ")
            cus_input3 = input ("\nEnter your review: ")
            cus_input4 = input ("Enter today's date: ")
        

        #A combined trigger (name + date)
        #SQLCommand00 = ("CREATE TRIGGER add_review ON Reviews INSTEAD OF INSERT AS BEGIN IF (SELECT COUNT (*) FROM INSERTED, Bookings WHERE (INSERTED.listing_id = Bookings.listing_id) AND (INSERTED.guest_name= Bookings.guest_name) AND (GETDATE() > Bookings.stay_to)) > 0 BEGIN INSERT INTO Reviews(listing_id, id, comments,guest_name) SELECT * FROM INSERTED END ELSE BEGIN RAISERROR ('Can only review the listing after the stay', 10, 1) ROLLBACK TRANSACTION END END")
        #cur.execute(SQLCommand00)
        
            #Find max id to create a new id
            SQLCommand2 = ("SELECT MAX(id) FROM Reviews")
            cur.execute(SQLCommand2)
            results = cur.fetchone()

            max_id = results[0]
            if max_id is None:
                max_id = 0
            new_id = max_id +1
        
            # Try catch the error when trigger is initiated
            try:
                SQLCommand1 = ("INSERT INTO Reviews (listing_id, id, comments, guest_name) VALUES (?,?,?,?)")
                values = [cus_input1, new_id, cus_input3, cus_input0]
                cur.execute(SQLCommand1, values)
                conn.commit()
            except Exception as e:
                print("\nCan only review the listing after the stay and if you did not book it")
            
            SQLCommand2 = ("SELECT * FROM Reviews WHERE id = ?")
            cur.execute(SQLCommand2, new_id)
            results = cur.fetchone()

            #Print out your review
            if results is None:
                print("Your review wasn't recorded.\n")
            else:
                print("\nYour review was successfully recorded. See below. \n")
                while results:
                    print(results)
                    results = cur.fetchone()
             
    # Invalid
    else:
        print("\nInvalid input. Enter 1 to SEARCH for Listings , 2 for BOOKING a 2Listings or 3 to REVIEW a Listing \n")

    
conn.close()









# 

# ### 
