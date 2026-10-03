import turtle
import random
import time

# Konfigurasi Layar
wn = turtle.Screen()
wn.title("Catch the Ball - Python Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Buat Keranjang (Player)
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("blue")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Buat Bola (Item yang jatuh)
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 260)

# Teks Skor & Nyawa di Layar
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Variabel Game
initial_speed = -1.5
ball.dy = initial_speed
score = 0
lives = 3

# Fungsi Pembaruan Teks Tampilan
def update_display():
    pen.clear()
    pen.write(f"Skor: {score}  Nyawa: {lives}", align="center", font=("Courier", 18, "normal"))

update_display()

# Fungsi Gerakan Kiri & Kanan
def paddle_right():
    x = paddle.xcor()
    if x < 240:
        paddle.setx(x + 30)

def paddle_left():
    x = paddle.xcor()
    if x > -240:
        paddle.setx(x - 30)

# Hubungkan Keyboard
wn.listen()
wn.onkeypress(paddle_right, "Right")
wn.onkeypress(paddle_left, "Left")
wn.onkeypress(paddle_right, "d")
wn.onkeypress(paddle_left, "a")

# Main Loop Game
while True:
    wn.update()

    # Gerakkan Bola ke Bawah
    ball.sety(ball.ycor() + ball.dy)

    # Cek Tabrakan dengan Keranjang (Lebih akurat & longgar)
    # Jika bola menyentuh area horizontal keranjang DAN berada di ketinggian atas keranjang
    if (paddle.xcor() - 55 < ball.xcor() < paddle.xcor() + 55) and (-245 <= ball.ycor() <= -235):
        score += 1
        ball.goto(random.randint(-240, 240), 260)
        # Penambahan kecepatan sangat landai
        if ball.dy > -4.0: 
            ball.dy -= 0.15 
        update_display()

    # Cek jika bola jatuh melewati keranjang (Bawah) - Gagal
    elif ball.ycor() < -280:
        lives -= 1
        ball.goto(random.randint(-240, 240), 260)
        ball.dy = initial_speed  # Kembalikan kecepatan ke awal saat luput
        update_display()
        
        # Game Over & Mulai Ulang Otomatis
        if lives <= 0:
            pen.goto(0, 0)
            pen.write("GAME OVER!\nMulai Ulang...", align="center", font=("Courier", 22, "bold"))
            wn.update()
            time.sleep(3)  # Jeda 3 detik sebelum restart
            
            # Reset Statistik Game
            score = 0
            lives = 3
            ball.dy = initial_speed
            ball.goto(random.randint(-240, 240), 260)
            pen.goto(0, 260)
            update_display()

    time.sleep(0.01)