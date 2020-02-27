from typing import List


def get_padded_hex(color_val: int) -> str:
    return hex(color_val)[2:].zfill(2)


def color_mean(rgb_lst: List[str]) -> str:
    """Compute the arithmetic mean for colors. The RGB component of each string would be
    extracted and the mean would be taken.

    Each element in `rgb_list` should be of the format '#ff00aa'. An assertion error
    would be raised for incorrect format.
    """

    total_r: int = 0
    total_g: int = 0
    total_b: int = 0

    for rgb_str in rgb_lst:
        assert rgb_str[0] == '#'
        assert len(rgb_str) == 7

        r, g, b = int(rgb_str[1:3], 16), int(rgb_str[3:5], 16), int(rgb_str[5:7], 16)
        total_r += r
        total_g += g
        total_b += b

    assert total_r < 256
    assert total_g < 256
    assert total_b < 256

    lst_length: int = len(rgb_lst)
    mean_r: int = int(total_r / lst_length)
    mean_g: int = int(total_g / lst_length)
    mean_b: int = int(total_b / lst_length)

    # still need to format string to pad 0 for integer case
    return f'#{get_padded_hex(mean_r)}{get_padded_hex(mean_g)}{get_padded_hex(mean_b)}'
