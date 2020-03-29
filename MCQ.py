from Question import question

question_prompts = [
    "What color are apples?\n(a) Red\n(b) Purple\n(c) Orange\n\n",
    "What color are oranges?\n(a) Red\n(b) Purple\n(c) Orange\n\n",
    "What color are strawberries?\n(a) Red\n(b) Purple\n(c) Orange\n\n"
]


questions = [
    question(question_prompts[0], "a"),
    question(question_prompts[1], "c"),
    question(question_prompts[2], "a")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)