from datetime import date

today = date.today()
datalive = []
def dateArrange(text:str):
     text = text.split(".")
     text[0] = int(text[0])
     text[1] = int(text[1])
     text[2] = int(text[2])
     return date(text[0], text[1], text[2])





def Init():
     with open('./database.txt', 'r') as file:
          global datalive 
          i = 1
          for line in file:
               if line != '\n':
                    line = line.split("-")
                    # ['[x]','2.3.13.','asdasdas']
                    
                    data = {'no': i,
                         'condition': line[0],
                         'date': line[1],
                         'description': line[2]
                    } 
                    
                    i +=1
                    datalive.append(data)   
               else:
                    continue
     return datalive

def refresh():
     i = 1
     for data in datalive:
          data['no'] = i
          i += 1



def main():
     global datalive, today
     Init()
     while True:
          i = 0
          for item in datalive:
               i +=1
               print(f"--{item['no']}-{item['condition']}-{today - dateArrange(item['date'])}:{item['description']}")
               
          
          userInput = input("What to do now? ")
          

          if 'new' in userInput:     
               userInput = userInput.split("-")
               date = userInput[1]
               description = userInput[2]
               data ={
                    'condition': "[]",
                    'date': date,
                    'description': description
               }  
               datalive.append(data)
               refresh()
               
          elif 'delete' in userInput:
               userInputdel = userInput.split("-")[1]
               while userInputdel.isalpha():
                    userInputdel = input("what do you want to delete? ")
          
               i = int(userInputdel)    
               datalive.pop(i - 1)        
               refresh()
                     
          elif 'check' in userInput:
               userInputcheck = userInput.split("-")[1]
               while userInputcheck.isalpha():
                    userInputcheck = input("what do you want to delete? ")
          
               i = int(userInputcheck)   
               datalive[i-1]['condition'] = '[x]'
          
          elif 'edit' in userInput:
               userInput = userInput.split("-")
               date = userInput[2]
               description = userInput[3]
               data ={
                    'condition': "[]",
                    'date': date,
                    'description': description
               }  
               userInedit = userInput[1]
               while userInedit.isalpha():
                    userInedit = input("what do you want to change? ")
               i = int(userInedit)   
               
               datalive[i-1] = data
               refresh()
          
          elif userInput == 'exit':
               save = open("database.txt","w")
               for item in datalive:
                    line = f"{item['condition']}-{item['date']}-{item['description']}\n"
                    save.write(line)
               break
          
# edit-3-12312.12.-asdasdasda
if __name__ == '__main__':
     main()