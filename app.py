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
        if answer == Question.answer:
            print("Yes")

ask_question(questions)




