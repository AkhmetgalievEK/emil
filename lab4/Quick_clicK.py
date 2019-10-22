from tkinter import *
from random import randint, choice
import time
import math


WIDTH = 620
HEIGHT = 400
figure_size = [30, 40, 50, 60]
figure_color = ["red", "orange", "yellow", "green", "blue"]


class Ball():
    def __init__(self):
        self.R = choice(figure_size)
        self.x = randint(self.R, WIDTH - self.R)
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx = randint(1, 3)
        self.dy = randint(1, 3)
        self.ball_id = game_window.create_oval(self.x - self.R,
                                               self.y - self.R,
                                               self.x + self.R,
                                               self.y + self.R, 
                                               fill = choice(figure_color)
        )

    def move(self):
        if self.x + self.R >= WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R >= HEIGHT or self.y - self.R <= 0:
            self.dy = -self.dy
        self.x += self.dx
        self.y += self.dy

    def show(self):
        game_window.move(self.ball_id, self.dx, self.dy)


class Square():
    def __init__(self):
        self.half_a = choice(figure_size)
        self.x = randint(self.half_a, WIDTH - self.half_a)
        self.y0 = randint(self.half_a, HEIGHT - self.half_a)
        self.y = self.y0 + self.half_a * math.cos(0.05 * self.x)
        self.dx = 3
        self.dy = 0
        self.square_id = game_window.create_rectangle(self.x - self.half_a,
                                                      self.y - self.half_a,
                                                      self.x + self.half_a,
                                                      self.y + self.half_a, 
                                                      fill = choice(figure_color)
        )

    def move(self):
        if self.x + self.half_a >= WIDTH or self.x - self.half_a <= 0:
            self.dx = -self.dx
        self.x += self.dx
        old_y = self.y
        self.y = self.y0 + self.half_a * math.cos(0.05 * self.x)
        self.dy = self.y - old_y

    def show(self):
        game_window.move(self.square_id, self.dx, self.dy)


def update_window():
    for ball in balls:
        ball.move()
        ball.show()
    for square in squares:
        square.move()
        square.show()
    main_window.after(10, update_window)


def time_flow():
    if play_time['text'] > "0":
        play_time['text'] = str(int(play_time['text']) - 1)
        main_window.after(1000, time_flow)
    else:
        global button_is_pressed
        button_is_pressed = False
        call()


button_is_pressed = False
def game_begin(event):
    global button_is_pressed
    button_is_pressed = True
    game_button.place_forget()
    play_time['text'] = "11"
    time_flow()
    score['text'] = "0"


def delete_ball(ball):
    i = 0
    for ball_i in balls:
        if ball == ball_i:
            del balls[i]
        i += 1


def delete_square(square):
    i = 0
    for square_i in squares:
        if square == square_i:
            del squares[i]
        i += 1


players_list = []
def update_list():
    global players_list
    players_list.append(int(score['text']))
    players_list.sort()   

    with open('file.txt', 'w') as f:
        f.write("All results: ")
        i = players_list[0]
        for i in players_list:
            f.write(str(i) + " ")
        f.write("\nThe best of resutls: " + str(i))


def call():
    global game_button
    game_button = Button(main_window,
                         background = "blue",
                         activebackground = "red",
                         font = "Arial 40",
                         text = "Играть eщё"
    )
    game_button.place(relx = 0.5, rely = 0.5, anchor = S)
    update_list()
    time.sleep(2)
    game_button.bind('<Button-1>', game_begin)


def hit_check(event):
    if button_is_pressed:
        for ball in balls:
            if (event.x - ball.x) ** 2 + (event.y - ball.y) ** 2 <= ball.R ** 2:
                game_window.delete(ball.ball_id)
                delete_ball(ball)
                balls.append(Ball())
                score['text'] = (int(score['text']) + 3)
        for square in squares:
            if abs(event.x - square.x) <= square.half_a and \
                abs(event.y - square.y) <= square.half_a:
                game_window.delete(square.square_id)
                delete_square(square)
                squares.append(Square())
                score['text'] = (int(score['text']) + 5)


def main():
    global main_window, game_window, game_button, play_time, balls, score, squares
    main_window = Tk()

    game_window = Canvas(main_window, 
                         width = WIDTH, 
                         height = HEIGHT,
                         background = "white"
    )
    game_window.pack()

    game_button = Button(main_window,
                         background = "blue",
                         activebackground = "red",
                         font = "Arial 40",
                         text = "Играть"
    )
    game_button.place(relx = 0.5, rely = 0.5, anchor = S)

    play_time = Label(main_window,
                      width = 3,
                      background = "white",
                      font = "Arial 40",
                      foreground = "black",
                      justify = CENTER,
                      text = "10" 
    )
    play_time.pack(side = LEFT, fill = BOTH)

    instruction = Label(main_window,
                        background = "white",
                        font = "Arial 12",
                        foreground = "black",
                        justify = CENTER,
                        text = "Инструкция к игре Quick_clicK\n" + \
                               "За 10с вы должны набрать наибольшее количество очков\n" + \
                               "Попадание по 1 кругу - 3 балла\n" + \
                               "Попадание по 1 квадрату - 5 баллов\n" + \
                               "Возможно одновременное попадание"
    )
    instruction.pack(side = LEFT, fill = BOTH)

    score = Label(main_window,
                  width = 3,
                  background = "white",
                  font = "Arial 40",
                  foreground = "black",
                  justify = CENTER,
                  text = "0" 
    )
    score.pack(side = LEFT, fill = BOTH)


    balls = [Ball() for i in range(5)]
    squares = [Square() for i in range(5)]
    update_window()

    game_button.bind('<Button-1>', game_begin)   
    game_window.bind('<Button-1>', hit_check)


    main_window.mainloop()


if __name__ == "__main__":
    main()


