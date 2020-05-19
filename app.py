from Questions import Question
questionsP =[
"What is color is grass? \n(a)Green \n(b)Red\n(c)Blue",
"What is color is a bananna? \n(a)Green \n(b)Yellow\n(c)Blue"
]

questions = [
    Question(questionsP[0],"a"),
    Question(questionsP[1],"b"),
]
def ask_question(questions):
    for i in questions:
        answer = input(i.prompt +" ")
        if answer == i.answer:
            print("Yes That is right")

ask_question(questions)




