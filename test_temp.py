import pytest
from temp_main import Time_equals

def test_time_equal():
    test_cases = [
        # 00
        ((-1, 0, 5), 'Fora de horario'),
        ((0, 0, 5), 'Horario 00'),
        ((1, 0, 5), 'Dif 5minutes'),
        ((4, 0, 5), 'Dif 5minutes'),
        ((5, 0, 5), 'Dif 5minutes'),
        ((6, 0, 5), 'Fora de horario'),
        # 01
        ((0, 1, 6), 'Fora de horario'),
        ((1, 1, 6), 'Horario 01'),
        ((2, 1, 6), 'Dif 5minutes'),
        ((5, 1, 6), 'Dif 5minutes'),
        ((6, 1, 6), 'Dif 5minutes'),
        ((7, 1, 6), 'Fora de horario'),
        # 02
        ((1, 2, 7), 'Fora de horario'),
        ((2, 2, 7), 'Horario 02'),
        ((3, 2, 7), 'Dif 5minutes'),
        ((6, 2, 7), 'Dif 5minutes'),
        ((7, 2, 7), 'Dif 5minutes'),
        ((8, 2, 7), 'Fora de horario'),
        # 03
        ((2, 3, 8), 'Fora de horario'),
        ((3, 3, 8), 'Horario 03'),
        ((4, 3, 8), 'Dif 5minutes'),
        ((7, 3, 8), 'Dif 5minutes'),
        ((8, 3, 8), 'Dif 5minutes'),
        ((9, 3, 8), 'Fora de horario'),
        # 04
        ((3, 4, 9), 'Fora de horario'),
        ((4, 4, 9), 'Horario 04'),
        ((5, 4, 9), 'Dif 5minutes'),
        ((8, 4, 9), 'Dif 5minutes'),
        ((9, 4, 9), 'Dif 5minutes'),
        ((10, 4, 9), 'Fora de horario'),
        # 05
        ((4, 5, 10), 'Fora de horario'),
        ((5, 5, 10), 'Horario 05'),
        ((6, 5, 10), 'Dif 5minutes'),
        ((9, 5, 10), 'Dif 5minutes'),
        ((10, 5, 10), 'Dif 5minutes'),
        ((11, 5, 10), 'Fora de horario'),
        # 06
        ((5, 6, 11), 'Fora de horario'),
        ((6, 6, 11), 'Horario 06'),
        ((7, 6, 11), 'Dif 5minutes'),
        ((10, 6, 11), 'Dif 5minutes'),
        ((11, 6, 11), 'Dif 5minutes'),
        ((12, 6, 11), 'Fora de horario'),
        # 07
        ((6, 7, 12), 'Fora de horario'),
        ((7, 7, 12), 'Horario 07'),
        ((8, 7, 12), 'Dif 5minutes'),
        ((11, 7, 12), 'Dif 5minutes'),
        ((12, 7, 12), 'Dif 5minutes'),
        ((13, 7, 12), 'Fora de horario'),
        # 08
        ((7, 8, 13), 'Fora de horario'),
        ((8, 8, 13), 'Horario 08'),
        ((9, 8, 13), 'Dif 5minutes'),
        ((12, 8, 13), 'Dif 5minutes'),
        ((13, 8, 13), 'Dif 5minutes'),
        ((14, 8, 13), 'Fora de horario'),
        # 09
        ((8, 9, 14), 'Fora de horario'),
        ((9, 9, 14), 'Horario 09'),
        ((10, 9, 14), 'Dif 5minutes'),
        ((13, 9, 14), 'Dif 5minutes'),
        ((14, 9, 14), 'Dif 5minutes'),
        ((15, 9, 14), 'Fora de horario'),
        # 10
        ((9, 10, 15), 'Fora de horario'),
        ((10, 10, 15), 'Horario 10'),
        ((11, 10, 15), 'Dif 5minutes'),
        ((14, 10, 15), 'Dif 5minutes'),
        ((15, 10, 15), 'Dif 5minutes'),
        ((16, 10, 15), 'Fora de horario'),
        # 11
        ((10, 11, 16), 'Fora de horario'),
        ((11, 11, 16), 'Horario 11'),
        ((12, 11, 16), 'Dif 5minutes'),
        ((15, 11, 16), 'Dif 5minutes'),
        ((16, 11, 16), 'Dif 5minutes'),
        ((17, 11, 16), 'Fora de horario'),
        # 12
        ((11, 12, 17), 'Fora de horario'),
        ((12, 12, 17), 'Horario 12'),
        ((13, 12, 17), 'Dif 5minutes'),
        ((16, 12, 17), 'Dif 5minutes'),
        ((17, 12, 17), 'Dif 5minutes'),
        ((18, 12, 17), 'Fora de horario'),
        # 13
        ((12, 13, 18), 'Fora de horario'),
        ((13, 13, 18), 'Horario 13'),
        ((14, 13, 18), 'Dif 5minutes'),
        ((17, 13, 18), 'Dif 5minutes'),
        ((18, 13, 18), 'Dif 5minutes'),
        ((19, 13, 18), 'Fora de horario'),
        # 14
        ((13, 14, 19), 'Fora de horario'),
        ((14, 14, 19), 'Horario 14'),
        ((15, 14, 19), 'Dif 5minutes'),
        ((18, 14, 19), 'Dif 5minutes'),
        ((19, 14, 19), 'Dif 5minutes'),
        ((20, 14, 19), 'Fora de horario'),
        # 15
        ((14, 15, 20), 'Fora de horario'),
        ((15, 15, 20), 'Horario 15'),
        ((16, 15, 20), 'Dif 5minutes'),
        ((19, 15, 20), 'Dif 5minutes'),
        ((20, 15, 20), 'Dif 5minutes'),
        ((21, 15, 20), 'Fora de horario'),
        # 16
        ((15, 16, 21), 'Fora de horario'),
        ((16, 16, 21), 'Horario 16'),
        ((17, 16, 21), 'Dif 5minutes'),
        ((20, 16, 21), 'Dif 5minutes'),
        ((21, 16, 21), 'Dif 5minutes'),
        ((22, 16, 21), 'Fora de horario'),
        # 17
        ((16, 17, 22), 'Fora de horario'),
        ((17, 17, 22), 'Horario 17'),
        ((18, 17, 22), 'Dif 5minutes'),
        ((21, 17, 22), 'Dif 5minutes'),
        ((22, 17, 22), 'Dif 5minutes'),
        ((23, 17, 22), 'Fora de horario'),
        # 18
        ((17, 18, 23), 'Fora de horario'),
        ((18, 18, 23), 'Horario 18'),
        ((19, 18, 23), 'Dif 5minutes'),
        ((22, 18, 23), 'Dif 5minutes'),
        ((23, 18, 23), 'Dif 5minutes'),
        ((24, 18, 23), 'Fora de horario'),
        # 19
        ((18, 19, 24), 'Fora de horario'),
        ((19, 19, 24), 'Horario 19'),
        ((20, 19, 24), 'Dif 5minutes'),
        ((23, 19, 24), 'Dif 5minutes'),
        ((24, 19, 24), 'Dif 5minutes'),
        ((25, 19, 24), 'Fora de horario'),
        # 20
        ((19, 20, 25), 'Fora de horario'),
        ((20, 20, 25), 'Horario 20'),
        ((22, 20, 25), 'Dif 5minutes'),
        ((24, 20, 25), 'Dif 5minutes'),
        ((25, 20, 25), 'Dif 5minutes'),
        ((26, 20, 25), 'Fora de horario'),
        # 21
        ((20, 21, 26), 'Fora de horario'),
        ((21, 21, 26), 'Horario 21'),
        ((22, 21, 26), 'Dif 5minutes'),
        ((25, 21, 26), 'Dif 5minutes'),
        ((26, 21, 26), 'Dif 5minutes'),
        ((27, 21, 26), 'Fora de horario'),
        # 22
        ((21, 22, 27), 'Fora de horario'),
        ((22, 22, 27), 'Horario 22'),
        ((23, 22, 27), 'Dif 5minutes'),
        ((26, 22, 27), 'Dif 5minutes'),
        ((27, 22, 27), 'Dif 5minutes'),
        ((28, 22, 27), 'Fora de horario'),
        # 23
        ((22, 23, 28), 'Fora de horario'),
        ((23, 23, 28), 'Horario 23'),
        ((24, 23, 28), 'Dif 5minutes'),
        ((27, 23, 28), 'Dif 5minutes'),
        ((28, 23, 28), 'Dif 5minutes'),
        ((29, 23, 28), 'Fora de horario'),
    ]

    for inputs, expected_output in test_cases:
        time = Time_equals()
        time.catch_minutes = lambda: inputs[0]
        time.catch_hours = lambda: inputs[1]
        time.diff_5minutes = lambda: inputs[2]
        assert time.time_equal() == expected_output
