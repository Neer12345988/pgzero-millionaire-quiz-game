import pgzrun

WIDTH = 870
HEIGHT = 650
TITLE = "Speed Maths"

marquee_box = Rect(0, 0, 880, 80)
score_box = Rect(0, 0, 150, 50)
timer_box = Rect(0, 0, 150, 150)
question_box = Rect(0, 0, 650, 150)
answer_box1 = Rect(0, 0, 300, 150)
answer_box2 = Rect(0, 0, 300, 150)
answer_box3 = Rect(0, 0, 300, 150)
answer_box4 = Rect(0, 0, 300, 150)
skip_box = Rect(0, 0, 150, 330)

marquee_box.move_ip(0, 0)
score_box.move_ip(700, 50)
timer_box.move_ip(700, 100)
question_box.move_ip(20, 100)
answer_box1.move_ip(20, 270)
answer_box2.move_ip(370, 270)
answer_box3.move_ip(20, 450)
answer_box4.move_ip(370, 450)
skip_box.move_ip(700, 270)

score = 0
question_file_name = "questions.txt"
time = 10
marquee_text = ""

game_over = False

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
questions = []

question_count = 0
question_index = 0

def draw():
    global marquee_text
    
    screen.clear()
    screen.fill("#0EE0AF")
    screen.draw.filled_rect(marquee_box, "#0EE0AF")
    screen.draw.filled_rect(score_box, "#00ff00")
    screen.draw.filled_rect(timer_box, "#00ff00")
    screen.draw.filled_rect(question_box, "#0000FF")
    screen.draw.filled_rect(skip_box, "#F40A0A")

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box, "#0b6174")

    marquee_text = f"Welcome to the Speed Maths Test! You are on question {question_index} of {question_count}."

    screen.draw.textbox(marquee_text, marquee_box, color = "#ff3700")
    screen.draw.textbox(f"Score: {score}", score_box, color = "#F1F109")
    screen.draw.textbox(str(time), timer_box, color = "white", shadow = (0.5, 0.5), scolor = "grey")
    screen.draw.textbox("Skip", skip_box, color = "#000000", angle = -90)
    screen.draw.textbox("Hello World", question_box, color = "#1bfe2a", shadow = (0.3, 0.3), scolor = "#16f934")
    for answer_box in answer_boxes:
        screen.draw.textbox("Hello World", answer_box, color = "#f767ce")

def update():
    move_marquee()

def move_marquee():
    marquee_box.x -= 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def read_question_file():
    global question_count, questions
    q_file = open(question_file_name, "r")
    for question in q_file:
        questions.append(question)
        question_count += 1
    q_file.close()

pgzrun.go()