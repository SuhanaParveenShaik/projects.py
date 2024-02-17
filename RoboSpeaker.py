import os

if __name__ == '__main__':
    print("welcome to Robospeaker 1.1 created by suhana parveen")
    while True:
      x= input("enter what you want me to speak: ")
      if x == "q":
        os.system("You have exited")
        break

    #in mac terminal by using say"" command the text can be read by the voice
    command = f"say{x}"
    #os.system() automatically runs the command
    os.system(command)