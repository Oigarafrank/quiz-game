quiz= input ("do you want to play? ")
if quiz != "yes":
    quit()
def run():

    answer = input("what does CPU stand for? ")
    score = 0
    if answer == "central processing unit":
        print ("correct")
        score += 1
    else:
        print ("incorrect")

    answer = input("what does GPU stand for? ")

    if answer == "graphical processing unit":
        print ("correct")
        score += 1
    else:
        print ("incorrect")

    answer = input("what does RAM stand for? ")

    if answer == "random access memory":
        print ("correct")
        score += 1
    else:
        print ("incorrect")

    answer = input("what does LU stand for? ")

    if answer == "logical unit":
        print ("correct")
        score += 1
    else:
        print ("incorrect")


    print("you have attempted " + str(score)+" questions correctly")
    print("your score is " + str((score/4)*100)+"%")

    replay =input("do you want to play again? ")
    if replay == "yes":
        run()
    else:
        quit()
run()