Month = int(input("Enter the month in the numeric form:"))
Day = int(input("Enter the day in nemric form:"))
Year = int(input("Enter the year as two numerical digits:"))
if Month >= 13 or 0:
  print("Error: Invalid Month Input")
elif Day >= 33:
  print("Error: Invalid Day Input")  
elif Year < 10 or Year >= 100:
  print("Error:Invalid Year Input")
else:
  print( "The date is",Month,('/'),Day,('/'),Year)
  print("Success: Comgratulations! you entered the correct date.")  
