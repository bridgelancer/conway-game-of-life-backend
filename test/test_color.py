import pytest

from backend.engine.color import color_mean


def test_one_color_mean():
    color = '#fffffe'
    assert color_mean([color]) == color


minimum = '00'
maximum = 'ff'
average = int((int(minimum, 16) + int(maximum, 16)) / 2)

def test_red_mean():
    assert color_mean([f'#{minimum}0000', f'#ff0000']) == f'#{hex(average)[2:]}0000'


def test_green_mean():
    assert color_mean([f'#00{maximum}00', f'#00{minimum}00']) == f'#00{hex(average)[2:]}00'


def test_green_mean():
    assert color_mean([f'#0000{minimum}', f'#0000{maximum}']) == f'#0000{hex(average)[2:]}'
