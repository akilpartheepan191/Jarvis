import datetime
import time
import keyboard as k
def wait():
  time.sleep(0.8)


def wai(times):
  time.sleep(times)


def open(app_name):
  k.send('windows')
  wait()
  k.write(app_name)
  wait()
  k.send('enter')


def close()
  k.send('ctrl+w')


def switch():
  k.send('alt+tab')


def login():
  open('chrome')
  wait()
  k.send('f6')
  wait()
  k.write('camu.in')
  wai(2)
  k.send('enter')


def telltime():
  hour=int(datetime.datetime.now().hour)
  minute=int(datetime.datetime.now().minute)
  return f'the time is {hour} {minute}'

