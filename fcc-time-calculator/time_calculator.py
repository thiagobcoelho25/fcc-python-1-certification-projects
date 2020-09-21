def add_time(start, duration,day = False):
  CONSTANT_DAYS = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]

  initHours = start.replace(":"," ").split()
  initMins = int(initHours[1])
  formatTime = initHours[2]
  initHours = int(initHours[0])

  durationTime = duration.split(":")

  durationTime[0] = int(durationTime[0])
  durationTime[1] = int(durationTime[1])
  days = 0
  
  #Change to 24:00 Format-Time
  if formatTime == "PM":
    initHours = initHours + 12

  #Sum minutes from Start and Duration
  if initMins + durationTime[1] >= 60:
    initHours = initHours + (initMins + durationTime[1])//60
    initMins = (initMins + durationTime[1])%60
    durationTime[1] = 0
    if initHours >= 24:
      days = days + initHours//24
      initHours = initHours%24
  else:
    initMins = initMins + durationTime[1]
    durationTime[1] = 0
  
  #Transform duration from hours to days
  if durationTime[0] >= 24:
    days = days + durationTime[0]//24
    initHours = initHours + durationTime[0]%24
    if initHours >= 24:
      days = days + initHours//24
      initHours = initHours%24
  elif durationTime[0] + initHours >=24:
    days = days + (durationTime[0] + initHours)//24
    initHours = (durationTime[0] + initHours)%24
  else:
    initHours = durationTime[0] + initHours

  #Change to 12:00 AM/PM Format-Time
  if initHours > 12:
    initHours = initHours - 12
    formatTime = "PM"
  elif initHours == 12:
    formatTime = "PM"
  elif initHours == 0:
    initHours = 12
    formatTime = "AM"
  else:
    formatTime = "AM"

  #Convert minutes from < 10 for ex: 8 -> '08'
  if initMins < 10:
    initMins = "0"+str(initMins)
  else:
    initMins = str(initMins)

  #If pass more than one day or 3 argument is True
  if not day == False:
    i = CONSTANT_DAYS.index(day.lower()) + 1
    if i + days > 7:
      i = (i+days)%7
    else:
      i = i + days
    if days == 0:
      return str(initHours) + ":" +initMins + " " + formatTime+", "+CONSTANT_DAYS[i-1].title()
    elif days == 1:
      return str(initHours) + ":" +initMins + " " + formatTime+", "+CONSTANT_DAYS[i-1].title()+" (next day)"
    else:
      return str(initHours) + ":" +initMins + " " + formatTime+", "+CONSTANT_DAYS[i-1].title()+f" ({days} days later)"
  else:
    if days == 0:
      return str(initHours) + ":" +initMins + " " + formatTime
    elif days == 1:
      return str(initHours) + ":" +initMins + " " + formatTime+" (next day)"
    else:
      return str(initHours) + ":" +initMins + " " + formatTime+f" ({days} days later)"
      

