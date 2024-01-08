print("Welcome computer Quiz")

playing = input("Are you want to play?")

if playing=="yes":
  print("Lets start")

else:
  print("okay,next time")

score=0

answer=input("Whats your name?")
if answer.lower()=="mukta":
  print("Correct!")
  score +=2

else:
  print("Incorrect")

  
answer=input("What is your country name?")
if answer.lower()=="bangladesh":
    print("Correct!")
    score +=1

else:
    print("Incorrect")

    
answer=input("Whats your mother name?")
if answer.lower()=="sharmin":
      print("Correct!")
      score +=1

else:
      print("Incorrect")

      
answer=input("Whats your father name?")
if answer.upper()=="Mozzem":
        print("Correct!")
        score +=1

else:
        print("Incorrect")

print("your score is " + str(score) + " question")

print("you got " + str((score/4)*100)+"%.")