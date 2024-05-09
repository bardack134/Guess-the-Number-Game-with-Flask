import random
from flask import Flask

app = Flask(__name__)

#random number between 0 and 9
random_number=random.randint(0,9)
print(random_number)

#home window
@app.route("/")
def hello_world():
    
    #Message displayed to the use
    return "<h1>Guess a number between 0 and 9</h1>"\
            "<img src=\'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnFtOWJwcjMxeXZkcTQ5aGp6ZjExMDgwMm83NXA2aGRjMzNpOWxhaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KGeqA1GqHBP2La5eSn/giphy.gif'/>"


@app.route("/guess/<int:number>")
def guess_number(number):
     
    #if the number enter by the user is correct or low or high
    if number == random_number:
        return "<h1 style='color: green'>Correct</h1>"\
                "<img src=\'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMG9hejRtajdheGltemp3ZzRiZHphdzRwMDVlcTBxamc2a2M5YmlhYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26tknCqiJrBQG6bxC/giphy.gif'/>"
    
    
    elif number > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaHV1eWM0Z2xpOHVsbTk4b3g5aHVkcW12b3lueXkxMHc3ZDB0c3RqbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o6Zt61bk1ts82gdQk/giphy.gif'/>"
        
    elif number < random_number:
        return "<h1 style='color: purple'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjhhZWlvdWxubHZ6M2Nldmk4YjZrd2dianl1YnIxdXZlYzF1cHVndiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VL48WGMDjD64umCEkv/giphy.gif'/>"
        
    


if __name__ == '__main__':
    app.run(debug=True)