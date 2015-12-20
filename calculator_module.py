#!/usr/bin/python
import signal
from engine import Utilities
from engine import TextWriter
from engine import SystemState

signal.signal(signal.SIGINT, Utilities.GracefulExit)

def Init():
  SystemState.pressed_buttons = ''
  SystemState.pressed_button = None

def Process():
  button = str(SystemState.pressed_button)
  pygame = SystemState.pygame
  screen = SystemState.screen
  screen_mode = SystemState.screen_mode

  try:
    if button == 'delete':
      SystemState.pressed_buttons = SystemState.pressed_buttons[:-1]
    elif button == 'plus':
      SystemState.pressed_buttons = SystemState.pressed_buttons + '+'
    elif button == 'minus':
      SystemState.pressed_buttons = SystemState.pressed_buttons + '-'
    elif button == 'multiply':
      SystemState.pressed_buttons = SystemState.pressed_buttons + '*'
    elif button == 'divide':
      SystemState.pressed_buttons = SystemState.pressed_buttons + '/'
    elif button == 'equals' and len(SystemState.pressed_buttons) > 0:
      SystemState.pressed_buttons = str(eval(SystemState.pressed_buttons))
    elif button == 'point':
      SystemState.pressed_buttons = SystemState.pressed_buttons + '.'
    elif button == 'right_parentheses':
      SystemState.pressed_buttons = SystemState.pressed_buttons + '('
    elif button == 'left_parentheses':
      SystemState.pressed_buttons = SystemState.pressed_buttons + ')'
    elif button == 'alt':
      print 'alt'
    else:
      SystemState.pressed_buttons = SystemState.pressed_buttons + str(button)

    TextWriter.Write(
        state=SystemState,
        text=SystemState.pressed_buttons,
        text_type='top'
    )
  except:
    TextWriter.Write(
        state=SystemState,
        text="ERROR",
        text_type='top',
        color=(255, 0, 0)
    )
