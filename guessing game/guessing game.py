from questio import question

question_prompts = [
     "what is the colour of a mango?\n(a) red\n(b)orange\n(c)pink\n(d)green \n\n",
     "what is 2+2?\n(a)4\n(b)5\n(c)2\n(d)7 \n\n",
     "when is afternoon start?\n(a)12.am/\n(b)12.pm\n(c)4pm\n(d)1pm\n\n"
]

questions = [
    question(question_prompts[0],"b"),
    question(question_prompts[1],"a"),
    question(question_prompts[2],"b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1

        print(" You got" + str(score) + "/" + str(len(questions)) + "correct")
run_test(questions)
