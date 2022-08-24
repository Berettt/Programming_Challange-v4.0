import pyautogui, keyboard, time
def autoclicker(time_between_clicks=1):

  while True:
    time.sleep(time_between_clicks)
    pyautogui.click()

    if keyboard.is_pressed('/'):
      break

if __name__ == '__main__':
  wait = float(input('Type in time between clicks '))
  time.sleep(1)
  print('autoclicker is active!')
  print('hold "/" to stop')
  autoclicker(wait)