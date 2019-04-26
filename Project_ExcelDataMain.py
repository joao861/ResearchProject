import Project_GUIFunct as pg
import Project_SchedFunct as ps
import pandas as pd
import random

# Import data from excel
#-------------------------------------------------------------------------------------------------------------
courseData = pd.read_excel("CourseList.xlsx") # Imports the excel file "CourseList.xlsx" with the names of the courses
roomData = pd.read_excel("RoomList.xlsx") # Imports the excel file "RoomList.xlsx" with the name of the rooms

meetingDays = pd.read_excel("MeetingTimes.xlsx")
courseDuration = pd.read_excel("CreditDuration.xlsx")
setScheduleData = pd.read_excel("SetSchedule.xlsx")
#-------------------------------------------------------------------------------------------------------------

# Convert excel files to dictionaries or lists
#-------------------------------------------------------------------------------------------------------------
# Lists
courseList = list(dict.fromkeys(courseData['Course'])) # List of courses for the program to search for matches
roomList = list(dict.fromkeys(roomData['Room'])) # List of rooms for the program to search for matches
# Dictionaries
creditsDict = dict(zip(courseData['Course'], courseData['Credits'])) # How many credits a course has
durationDict = dict(zip(courseDuration['Credits'], courseDuration['Duration'])) # How long a course will last according to their credits
# ------------------------------------------------------------------------------------------------------------

# Testing the program
#-------------------------------------------------------------------------------------------------------------

userCourse = pg.setCourse() # Choosing a course
userRoom = pg.setRoom(roomList[random.randrange(100)]) # Choosing a room
my_day = pg.setDays() # Choosing a date. Using default values (current date)
my_day.weekDays()
print(my_day.day)
userDate = pg.setDate().combineDate() # Returns the date as string in MM/DD/YY format
set_time = pg.setTime()
set_time.checkTime(1, 20, 5, 40) # Choosing a time for the meeting
ps.Schedule(set_time.timeStart(), set_time.timeEnd(), my_day.day, userRoom.roomID, userCourse.courseID, userDate.year)
