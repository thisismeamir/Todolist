import datetime as dt
def Init():
     with open('./database.txt', 'r') as file:
          datalive = []
          for line in file:
               line = line.split("-")
               # ['[x]','2.3.13.','asdasdas']
               data = {
                    'condition': line[0],
                    'date': line[1],
                    'description': line[2]
               }  
               datalive.append(data)   
          print(datalive)          
               


def main():
     Init()
     while True:
          userInput = input("What to do now? ")

          if userInput == 'new':
               inpu
          elif userInput == 'delete':
               pass
          
          elif userInput == 'exit':
               
               break
          

if __name__ == '__main__':
     main()