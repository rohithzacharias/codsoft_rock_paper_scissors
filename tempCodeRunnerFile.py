import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import pygame
import os
from PIL import Image, ImageTk

# Initialize Pygame Mixer
pygame.init()
pygame.mixer.init()

# Function to play sound
def play_sound(file):
    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, file)
    pygame.mixer.music.load(full_path)
    pygame.mixer.music.play()

# Main Window
root = tk.Tk()
root.title("Rock Paper Scissors - CodSoft Task 4")
root.geometry("400x550")
root.resizable(False, False)
root.configure(bg="#2c3e50")

# Ask for User Name
user_name = simpledialog.askstring("Player Name", "Enter your name:")
if not user_name:
    user_name = "Player"

# Ask for Target Score
while True:
    try:
        target_score = simpledialog.askinteger("Target Score", f"Enter target score to win, {user_name}:")
        if target_score and target_score > 0:
            break
    except:
        continue

# Load Images
base_dir = os.path.dirname(__file__)
rock_img = ImageTk.PhotoImage(Image.open(os.path.join(base_dir, "rock.png")).resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open(os.path.join(base_dir, "paper.png")).resize((100, 100)))
scissors_img = ImageTk.PhotoImage(Image.open(os.path.join(base_dir, "scissors.png")).resize((100, 100)))

# Game Variables
choices = ["Rock", "Paper", "Scissors"]
player_score = 0
computer_score = 0

# Game Logic
def play(choice):
    global player_score, computer_score

    computer_choice = random.choice(choices)

    if choice == computer_choice:
        result = "It's a Tie! 😐"
        result_label.config(text=result)
        player_choice_label.config(text=f"{user_name}: {choice}")
        computer_choice_label.config(text=f"Computer: {computer_choice}")
        return

    win = (choice == "Rock" and computer_choice == "Scissors") or \
          (choice == "Paper" and computer_choice == "Rock") or \
          (choice == "Scissors" and computer_choice == "Paper")

    if win:
        result = "You Win! 🎉"
        player_score += 1
        play_sound("win.wav")
    else:
        result = "Computer Wins! 😔"
        computer_score += 1
        play_sound("lose.wav")

    # Update UI
    player_choice_label.config(text=f"{user_name}: {choice}")
    computer_choice_label.config(text=f"Computer: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score - {user_name}: {player_score} | Computer: {computer_score}")

    check_winner()

# Check if someone reached target score
def check_winner():
    if player_score >= target_score:
        messagebox.showinfo("Game Over", f"{user_name.upper()} WON THE MATCH! 🏆")
        root.destroy()
    elif computer_score >= target_score:
        messagebox.showinfo("Game Over", "SYSTEM WON THE MATCH! 💻")
        root.destroy()

# GUI Elements
title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="#2c3e50", fg="white")
title.pack(pady=10)

# Image Buttons
button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, image=rock_img, command=lambda: play("Rock"), bg="#2c3e50", bd=0)
paper_button = tk.Button(button_frame, image=paper_img, command=lambda: play("Paper"), bg="#2c3e50", bd=0)
scissors_button = tk.Button(button_frame, image=scissors_img, command=lambda: play("Scissors"), bg="#2c3e50", bd=0)

rock_button.grid(row=0, column=0, padx=10)
paper_button.grid(row=0, column=1, padx=10)
scissors_button.grid(row=0, column=2, padx=10)

# Labels
player_choice_label = tk.Label(root, text=f"{user_name}: ", font=("Arial", 14), bg="#2c3e50", fg="white")
player_choice_label.pack(pady=10)

computer_choice_label = tk.Label(root, text="Computer: ", font=("Arial", 14), bg="#2c3e50", fg="white")
computer_choice_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#2c3e50", fg="yellow")
result_label.pack(pady=10)

score_label = tk.Label(root, text=f"Score - {user_name}: 0 | Computer: 0", font=("Arial", 13), bg="#2c3e50", fg="white")
score_label.pack(pady=15)

# Run the App
root.mainloop()