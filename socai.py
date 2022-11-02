import pyautogui as pag
import pyperclip as clip
import time
import sys

print("[ 카카오톡 멘션 도배 ]")
print()
print()
mention_target = input("멘션될 상대를 입력하세요 (멘션을 사용하지 않을경우, 아무것도 쓰지 마세요): ")
print()
attack_time = int(input("몇번 도배할건지 입력하세요: "))
print()
attack_message = input("무슨 메시지를 보낼건지 입력하세요: ")
print()
print("도배가 3초 뒤에 시작합니다.\n지금 즉시 카카오톡 채팅창으로 이동하세요!")
time.sleep(3)

print()
print("도배를 시작합니다!")

def mention():
    # mention
    pag.write('@')
    time.sleep(0.01)
    clip.copy(mention_target)
    pag.hotkey("ctrl", "v")
    time.sleep(0.01)
    pag.press('tab')
    time.sleep(0.01)

def send():
    # message
    clip.copy(attack_message)
    pag.hotkey("ctrl", "v")
    time.sleep(0.01)
    pag.press('enter')
    print(i)
    time.sleep(0.01)

try:
    for i in range(attack_time):
        if mention_target != "":
            mention()
            send()
        else:
            send()

    print("도배를 성공적으로 마쳤습니다.")
except Exception:
    print("오류가 발생했습니다!" + Exception)