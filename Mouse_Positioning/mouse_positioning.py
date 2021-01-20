import pyautogui as p
import PySimpleGUI as psgui

layout = psgui.Multiline(
    f'x={p.position()[0]}\ny={p.position()[1]}', size=(11, 2))
window_layout = [[layout]]

window = psgui.Window(
    'Mouse position',
    layout=window_layout,
    location=(p.size().width, p.size().height),
    keep_on_top=True)

while True:
    event, values = window.read(timeout=100)
    if event == psgui.WIN_CLOSED or event == 'Exit':
        break
    layout.update(value=f'x={p.position()[0]}\ny={p.position()[1]}')
