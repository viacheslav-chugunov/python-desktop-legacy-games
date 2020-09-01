from win32api import GetSystemMetrics


RESOLUTION = (GetSystemMetrics(0), GetSystemMetrics(1))

WINDOW_SETUP = {
    'title': 'Pong',
    'fullscreen': True,
}

BEATER = {
    'speed': 8,
    'hp': 5,
}

BALL = {
    'speed': 12,
}

HEAL = {
    'speed': 1,
}
