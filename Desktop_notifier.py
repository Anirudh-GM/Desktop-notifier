from plyer import notification
import time
import sys

def desktop_notifier(title, message):
    notification.notify(title=title,
        message=message,
        timeout=10)

def water_reminder():
    x=int(input("Enter time in seconds for repeating water reminder:"))
    y=int(input("Enter how many times to be remembered:"))
    for i in range(y):
        title = "Reminder"
        message = "Drink water"
        time.sleep(x)
        desktop_notifier(title, message)
        
def screen_reminder():
    x=int(input("Enter time in seconds for repeating screen time reminder:"))
    y=int(input("Enter how many times to be remembered:"))
    for i in range(y):
        title = "Reminder"
        message = "Take a break"
        time.sleep(x)
        desktop_notifier(title, message)
        
def other_reminder():
    x=int(input("Enter time in seconds for repeating reminder:"))
    y=int(input("Enter how many times to be remembered:"))
    z=input("Enter the message to remember:")
    for i in range(y):
        title = "Reminder"
        message = z
        time.sleep(x)
        desktop_notifier(title, message)
    
def choice_display():
    print('''Type of reminders available -
          1. Water reminder
          2. Screen time reminder
          3. Other reminder
          Press 4 for exit''')
    choice=int(input("\nEnter the number of the choice from the above list:"))
    choice_selected(choice)

def choice_selected(choice):
   if choice==1:
       water_reminder()
       
   elif choice==2:
       screen_reminder()
            
   elif choice==3:
       other_reminder()
       
   elif choice==4:
       sys.exit(0)

   else:
        print("\nEnter a choice between 1 to 4\n")
        choice_display()
        
if __name__ == "__main__":
    choice_display()