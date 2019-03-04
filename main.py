"""
This program imports a file and creates a list of State objects with attributes. The program can also sort and display data from the list.
Author: Nicole Newsom
Version: 1/25/19
Email: n01029978@ospreys.unf.edu
"""
import stateClass

def menu(listOfStates):
  """
  Presents the options avaiable to the user. Executes other functions based
  on user input. 
  """
  while(True):
    print("Please select an option below:\n\t 1. Print a State Report.\n\t 2.Sort by state name.\n\t 3.Sort by population. \n\t 4.Find and print a given state.\n\t 5.Quit")

    option = input()

    if option>=1 and option<=5:
      if option == 1:
      #print("Printed report")
        printReport(listOfStates)
 

      elif option == 2:
      #print("Sorted by state name")
        sortByName(listOfStates, 0, 49)
    
      elif option == 3:
     # print("Sorted by state population")
        sortByPopulation(listOfStates)
    
      elif option == 4:
      #print("State Selected")
        selectState(listOfStates)
    
      else:
       print"Quitting"
       break
    else:
      print"Invalid option. Try again."
      

def printReport(myList):
  print("State Name".ljust(15) + "Capital".ljust(15) + "Abbreviation".ljust(15) + "Population".ljust(12) + "Region".ljust(16) + "Number of House Seats")
  print("".ljust(94, '-'))
  for item in myList:
    print(str(item))
  
def sortByName(myList, low, high):
  myList.sort(key=lambda x: x.name, reverse=False)
  #if low < high:
   # pivotIndex = partition(myList, low, high)
    #sortByName(myList, low, pivotIndex-1)
    #sortByName(myList, pivotIndex+1, high)

def partition(myList, first, last):
  i = first - 1
  pivot = myList[last]

  for x in range(first, last):
    if myList[last].__gt__(pivot):
      i = i+1
  myList[i+1],myList[last] = myList[last],myList[i+1]
  return (i+1)

def selectState(myList):
  state = raw_input("Enter the name of a state: ")

  if myList[0].getName() is "Alabama":
    targetIndex = binarySearch(myList, state)

    if targetIndex >=0:
      printSingleState(myList, targetIndex)
    else:
      return
  else:
    i=0
    for item in myList:
        if item.getName() == state:
          printSingleState(myList, i)
        i = i + 1
  


def printSingleState(myList, index):
  #prints report of a single state
  print("State Name: " + myList[index].getName())
  print("Capital City: " + myList[index].getCapital())
  print("Abbreviation: " + myList[index].getAbbr())
  print("Population: " + myList[index].getPopulation())
  print("Region: " + myList[index].getRegion())
  print("Number of House Seats: " + myList[index].getSeats())

def binarySearch(myList, target):
  start = 0  #need case for if not found
  end = len(myList) - 1

  while start <=end:
    midIndex = (start + end)/2
    middle = myList[midIndex].getName() 

    if middle > target:
      end = midIndex - 1
    elif middle < target:
      start = midIndex + 1
    elif middle is target:
      return midIndex
    else:
      retry = raw_input("Not found. Type a different name or type 'cancel' to go back to the menu: ")

      if retry is not "cancel":
        binarySearch(myList, retry)
      else:
        return -5

def maxPopulation(myList):
  greatest = myList[0].population
  for i in range(1,len(myList) - 1):
    if myList[i].population > greatest:
      greatest = myList[i].population
  return greatest
     


def sortByPopulation(myList):
  max1 = maxPopulation(myList)

  exp = 1

  while max1/exp > 0:
    countSort(myList, exp)
    exp *= 10

def countSort(arr, xp):
  n = len(arr)

  output = [0] *n

  counted = [0] * (10)

  for i in range (0, n):
    index = (arr[i].population/xp)
    counted [(index)%10] += 1

  for i in range(1, 10):
    counted[i] += counted[i - 1]

  i = n-1

  while i>=0:
    index = (arr[i].population/xp)
    output[counted[(index)%10] - 1] = arr[i]
    counted[ (index) %10] -= 1
    i-=1

  i = 0
  for i in range(0, len(arr)):
    arr[i] = output[i]
  
def main():
  #create list here
  fileName = raw_input("Enter the name of a file: ")
  

  usa = []
  while(True):
    try:
     f = open(fileName, "r")
    except IOError:
      answer = raw_input("Cannot find file. Try again? y/n")
      if answer == "y":
        fileName = raw_input("Enter the name of a file: ")
      else:
        quit()
        break
    else:
      break


  firstLine = f.readline()
  #print(firstLine)
  while True:
    line = f.readline()
    usa.append(line)
    if not line: break

 # print(usa[0])
  f.close()

  i = 0
  for x in usa:
    usa[i] = usa[i].split(",")
    i+=1

  

  myCountry = []#empty list of State objects

  j = 0
  while j < 50:
    myCountry.append(stateClass.State(usa[j][0], usa[j][1], usa[j][2], int(usa[j][3]), usa[j][4], usa[j][5]))
    j+=1
  #print(myCountry[0])
  menu(myCountry)

main()