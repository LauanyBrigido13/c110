import time

def countdown_timer(seconds):
    mins = seconds//60
    secs = seconds % 60

    timer = f'{mins}:{secs}'
    print(timer)

user_input = input("Digite o tempo em segundos: ")
seconds = int(user_input)

countdown_timer(seconds)