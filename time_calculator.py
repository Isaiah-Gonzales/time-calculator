def add_time(start, duration, weekday = "placeholder"):
  days = 0
  #check if user included colons in their inputs and an AM or PM in their start time
  if ':' not in start:
    print("ERROR: Please enter a properly formatted start-time 'hh:mm AM' or 'hh:mm PM'")
    return
  if ':' not in duration:
    print("ERROR: Please enter a properly formatted duration 'hh:mm")
    return
  if "PM" not in start:
    if "AM" not in start:
      print("ERROR: Don't forget to enter an 'AM' or 'PM' in your start time")
      return
    
  #remove spaces from inputs
  strippedStart = start.replace(" ", "")
  strippedDuration =duration.replace(" ", "")

  #find position of colon within inputs and AM or PM in start time
  startColonPosition = strippedStart.find(':')
  lenStart = len(strippedStart)
  if "PM" in strippedStart:
    locationAMPM = strippedStart.find('PM')
  if "AM" in strippedStart:
    locationAMPM = strippedStart.find('AM')
  
  durationColonPosition = strippedDuration.find(':')
  
  #define variables for hours and minutes and AMPM  
  hStart = strippedStart[:startColonPosition]
  mStart = strippedStart[startColonPosition+1:locationAMPM]

  hDuration = strippedDuration[:durationColonPosition]
  mDuration = strippedDuration[durationColonPosition+1:len(strippedDuration)]
  
  AMPMStart = strippedStart[locationAMPM:len(strippedStart)]
  
  #check if start time hours and mins are numbers
  if hStart.isdigit() == False:
    print("ERROR: Please enter a properly formatted start-time 'hh:mm AM' or 'hh:mm PM'")
    return
  if mStart.isdigit() == False:
    print("ERROR: Please enter a properly formatted start-time 'hh:mm AM' or 'hh:mm PM'")
    return

  #check if duration hours and mins are numbers
  if hDuration.isdigit() == False:
    print("ERROR: Please enter a properly formatted duration 'hh:mm'")
    return
  if mDuration.isdigit() == False:
    print("ERROR: Please enter a properly formatted duration 'hh:mm'")
    return

  #check if start hours are 12 or less
  if int(hStart) > 12:
    print("ERROR: Invalid hour in start time")
    return
  # check if min are less than 60
  if int(mStart) > 59:
    print("ERROR: Invalid minutes in start time")
    return
  if int(mDuration) > 59:
    print("ERROR: Invalid minutes in duration time")
    return
    
  #Will use a 24-hour time scale, format start hour
  if "AM" in start:
    if hStart == "12":
      hStart = "0"
  if "PM" in start:
    if hStart != "12":
      hStart = str(int(hStart) + 12)

  #Calculate new mins
  if int(mStart) + int(mDuration) < 60:
    newMin = str(int(mStart) + int(mDuration))
    
  if int(mStart) + int(mDuration) == 60:
    newMin = "0"
    hStart = str(int(hStart)+1)
    
  if int(mStart) + int(mDuration) > 60:
    hours = int(((int(mStart)+int(mDuration))/60))
    newMin = str((int(mStart)+int(mDuration))-(60 * hours))
    hStart = str(int(hStart)+hours)  
    
  #calculate new hour and new AMPM
  if int(hStart) + int(hDuration) < 12:
    newHour = str(int(hStart) + int(hDuration))
    newAMPM = AMPMStart
    
  if int(hStart) + int(hDuration) == 12:
    newHour = "12"
    if AMPMStart == "AM":
      newAMPM = "PM"
    if AMPMStart == "PM":
      newAMPM = "AM"
      
  if int(hStart) + int(hDuration) > 12:
    
    days = int((int(hStart)+int(hDuration))/24)
    newHour = str((int(hStart) + int(hDuration))-(24 * days))

  #convert new hour back into 12-hour time
    if int(newHour) < 12:
      newAMPM = "AM"
    
    if int(newHour) >= 12:
      newHour = str(int(newHour) - 12)
      newAMPM = "PM"

    if int(newHour) == 0:
      newHour = "12"

  #formatting, add leading zeroes if necessary

  if len(newMin) < 2:
    newMinList = list(newMin)
    newMinList.insert(0,'0')
    newMin = ''.join(newMinList)  

  
  #create empty containers for weekday and days counter  
  newWeekday = ""
  daysCounter = ""
  
  if type(weekday) is not str:
    print("Please enter a valid weekday")
    return

  if days == 1:
    daysCounter = " (next day)"
  
  if days > 1:
    daysCounter = " (" + str(days) + " days later)"
  
  if weekday != "placeholder":
    weekdays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    weekday = weekday.lower()

    #if user entered an valid weekday, print new weekday. Otherwise, give error message
    if weekday in weekdays:
      if days < 1:
       newWeekday = ", " + weekday.capitalize()
      if days >= 1:
        if weekdays.index(weekday) + days > 6:
          weeks = int((weekdays.index(weekday) + days)/7)
          newWeekday = ", " + weekdays[((weekdays.index(weekday) + days) - (weeks * 7))].capitalize()
        if weekdays.index(weekday) + days <= 6:
          newWeekday = ", " + weekdays[((weekdays.index(weekday) + days))].capitalize()
    else:
      print("Please enter a valid weekday")
      return
  
  newTime = newHour + ":" + newMin + " " + newAMPM + newWeekday + daysCounter
  
  return str(newTime)