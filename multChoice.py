from question import Question

question_prompts = [
    "Who is the best puppy?\n(a) Oscar\n(b) not Oscar\n\n",
    "What color is Oscar?\n(a) Black\n(b) Tan\n(c) Black and Tan\n\n",
    "How old is Oscar?\n(a) 2\n(b) 3\n(c) 4\n\n"
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b")
]

def runTest(questions):
    score = 0
    for Question in questions:
        answer = input(Question.prompt)
        if answer == Question.answer:
            score += 1
    print("you got " +str(score)+"/"+str(len(questions))+" correct")


runTest(questions)