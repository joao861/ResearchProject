import re
import datetime
import pandas as pd

#-------------------------------------------------------------------------------------------------------------
# Classes:
### setCourse.- Stores the user course
### setRoom.- Stores the user room
### setDate.- Stores the month and year when a meeting will take place
### setDays.- Stores the days a meeting will take place
### setTime.- Stores the time a meeting starts, and ends
#-------------------------------------------------------------------------------------------------------------

class setCourse:
    #-----------------------------------------------------------------------------------------------------------------------
    # The 'setCourse' class has to methods. The first one will keep the course that the user would want to separate a room for.
    # The second method is a search engine that will allow the user to conduct a search of all the courses availible, and then choose one of them
    #-----------------------------------------------------------------------------------------------------------------------
    def __init__(self, courseID):
        self.courseID = courseID # <----- Defines the user course though input. Modify it to take input from the GUI as a command
        return
    
    def searchCourse(self):
        courseMatches = [] # Stores any matches to the user's input
        if self.courseID in courseList:
            print(self.courseID) # <----- Shows the course the user was looking for. Modify it to show it in the GUI rather than in the Shell
        else:
            for i in range(len(courseList)):
                check_room = re.search(self.courseID, courseList[i]) # Finds courses that start with what the user has input
                if check_room is not None:
                    courseMatches.append(courseList[i]) # Adds possible courses that the user may be looking for
            for j in range(len(courseMatches)):
                print(courseMatches[j]) # <----- Shows the course Suggestions to the user. Modify it to show it in the GUI rather than in the Shell
        return
    
class setRoom:
    #-----------------------------------------------------------------------------------------------------------------------
    # The 'setRoom' stores the room that the user wants to assign a meeting to.
    # This class also has a search engine that the user can use to find the name of the rooms availible
    #-----------------------------------------------------------------------------------------------------------------------
    def __init__(self, roomID):
        self.roomID = roomID # <---- Defines the user room thorugh input. Modify it to take input from the GUI as a command
        return      
        
    def searchRoom(self):
        roomMatches = []
        if self.roomID in roomList:
            print(self.roomID) # <---- Shows the room the user was looking for. Modify it to show it in the GUI rather than in the Shell
        else:
            for i in range(len(roomList)):
                check_room = re.search(self.roomID, roomList[i]) # Finds courses that start with what the user has input
                if check_room is not None:
                    roomMatches.append(roomList[i]) # Adds possible courses that the user may be looking for
            for j in range(len(roomMatches)):
                print(roomMatches[j]) # <---- Shows the course Suggestions to the user. Modify it to show it in the GUI rather than in the Shell
        return
    
class setDate:
    #-----------------------------------------------------------------------------------------------------------------------
    # The 'setDate' class stores the month and year that the user wants their meeting to take place.
    # The defaul values of month and year will be the current date.
    #-----------------------------------------------------------------------------------------------------------------------
    def __init__(self, month = datetime.datetime.now().strftime("%m"), year = datetime.datetime.now().strftime("%Y")): # <---- Get values of day, month, year from the user as inputs from GUI
        self.month = month
        self.year = year
        return
    
    def combineDate(self):
        convertDate = str(self.month + "/" + self.year) # Joins month, day, and year
        date = datetime.datetime.strptime(convertDate, "%m/%Y") # Converts the previous date to a MM/DD/YYYY format
        return date

class setDays:
    #------------------------------------------------------------
    # 'setDays' stores the days a meeting will take place on
    #------------------------------------------------------------
    def __init__(self):
        self.day = "" # This variable will be a string containing all the days the user will want a meeting to occur
        return
                
    def weekDays(self, day = datetime.datetime.now().strftime("%A"),
                 m = False, t= False, w = False, th = False,
                 f = False, s = False, sun = False): # <---- Change m,t,w,th,f,s,sun values to 'True' if the user wants a meeting that day
        #-------------------------------------------------------------------------------------------------------------
        # If the user wants to input a date rather than choosing a day, change the value of 'day' to the user's value
        # m,t,w,th,f,s,sun represent the days of the week. Turn them to true to add them as a meeting day
        #-------------------------------------------------------------------------------------------------------------
        if m or t or w or th or f or s or sun:
            if m:
                self.day += "Monday "
            if t:
                self.day += "Tuesday "
            if w:
                self.day += "Wednesday "
            if th:
                self.day += "Thursday "
            if f:
                self.day += "Friday "
            if s:
                self.day += "Saturday "
            if sun:
                self.day += "Sunday"
        else:
            self.day += day # THe default value for the day is the current day
            
class setTime:
    #-------------------------------------------------------------------------------------------------------------
    # This class stores the time a meeting starts and ends
    #-------------------------------------------------------------------------------------------------------------
    def __init__(self): # <----- What time does the user want the meeting to start, and end
        #--------------------
        self.startHours = None
        self.startMin = None
        #--------------------
        self.endHours = None
        self.endMin = None
        return
        
    def checkTime(self, startHours, startMin, endHours, endMin, start_PM = False, end_PM = False):
        #-------------------------------------------------------------------------------------------------------------
        # This method checks the user's input in order to avoid any conflicts
        # Get values from the user in hours
        #-------------------------------------------------------------------------------------------------------------
        if ((startHours <= 12) and (endHours <= 12)) and (startHours != 0) and (endHours != 0): # The time format can only be between 0 and 12
            if (startHours <= endHours):
                if (start_PM is False): # Checks if the course is in the afternoon
                    self.startHours = startHours # Sets the hours for a course to start
                else :
                    self.startHours = startHours + 12 # If the course is in the afternoon, the program will add 12 hours
                
                if (end_PM is False): # Checks if the course is in the afternoon
                    self.endHours = endHours # Sets the hours for a course to end
                else :
                    self.endHours = endHours + 12 # If the course is in the afternoon, the program will add 12 hours
            else :
                print("Conflicting time")
                return # <----- There should be a way for the GUI to ask the user for a different time input
        else :
            print("Conflicting time")
            return # <----- There should be a way for the GUI to ask the user for a different time format
        #-------------------------------------------------------------------------------------------------------------
        # Get values from the user in minutes
        #-------------------------------------------------------------------------------------------------------------
        if (startMin < 60) and (endMin < 60): # The minutes can not be higher than 60
            if (startHours == endHours):
                if (startMin < endMin):
                    self.startMin = startMin
                    self.endMin = endMin
                else :
                    print("Conflicting time")
                    return # <----- There should be a way for the GUI to ask the user for a different minute span input no higher than 60
            elif (startMin < endMin):
                self.startMin = startMin
                self.endMin = endMin
            else :
                print("Conflicting time")
                return # <----- There should be a way for the GUI to ask the user for a different minute span input no higher than 60
        else :
            print("Conflicting time")
            return # <----- There should be a way for the GUI to ask the user for a different minute span input no higher than 60
        #-------------------------------------------------------------------------------------------------------------
        return
              
    def timeStart(self):
        #-------------------------------------------------------------------------------------------------------------
        # This method will convert the user input for the start time of the course into a string with format HH:MM
        #-------------------------------------------------------------------------------------------------------------
        convertStart = str(str(self.startHours) + ":" + str(self.startMin))
        startTime = datetime.datetime.strptime(convertStart, "%H:%M").time()
        return startTime # <---- Returns the starting time with format HH:MM
    
    def timeEnd(self):
        #-------------------------------------------------------------------------------------------------------------
        # This method will convert the user input for the ending time of the course into a string with format HH:MM
        #-------------------------------------------------------------------------------------------------------------
        convertEnd =  str(str(self.endHours) + ":" + str(self.endMin))
        endTime = datetime.datetime.strptime(convertEnd, "%H:%M").time()
        return endTime # <---- Returns the finishing time with format HH:MM
