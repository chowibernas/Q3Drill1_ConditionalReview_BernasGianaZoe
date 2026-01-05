from pyscript import document, display 

#Input Grades
def solving_av(e): 
    
    #this line of code avoids the results from stacking
    document.getElementById("invalid").innerHTML = " "
    document.getElementById("status").innerHTML = " "
    document.getElementById("score").innerHTML = " "

    # these variables converts the user's input into floats 
    grade1 = float(document.getElementById("input1").value)
    grade2 = float(document.getElementById("input2").value)

    # this code is used for validation which ensures that the user inputs a valid number that satisfies the code below.
    if not (1 <= grade1 <= 100) or not (1 <= grade2 <= 100):
        display("⚠️ Please put valid numbers.", target="invalid")
        return

    # this variable computes the average
    result = (grade1 + grade2)/2

    # this code displays the output
    display(f"Your average is: {result}", target="score")
   
    # here is the if and else statements that ensures that the condition is met
    if result >= 75:
        display("Great job. You passed!", target="status")

    else:
        display("You failed. Try using other study methods that suits your style.", target="status")

        



