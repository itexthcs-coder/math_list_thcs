import random
from sympy import sqrt, latex

lisdang = ['1']
dang = random.choice(lisdang)

if dang == '1':
    n = random.choice([2, 3, 5, 6, 7])
    c = random.choice([-3, -2, -1, 1, 2, 3])
    bt_trong = sqrt(n) + c
    
    da = f'${c}$'
    s = [
        f'${-c}$',
        f'$2\\sqrt{{{n}}} + {c}$' if c > 0 else f'$2\\sqrt{{{n}}} - {-c}$',
        '$0$',
        f'${n + c}$'
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    noidungcauhoi = f'Giá trị của biểu thức $(\\sqrt[3]{{{latex(bt_trong)}}})^3 - \\sqrt{{{n}}}$ bằng'
    
    da_d = '\\True ' + str(da)
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    c_str = f'+ {c}' if c > 0 else f'- {-c}'
    loigiai = f'Áp dụng $(\\sqrt[3]{{A}})^3 = A$, ta có: $(\\sqrt[3]{{{latex(bt_trong)}}})^3 - \\sqrt{{{n}}} = \\sqrt{{{n}}} {c_str} - \\sqrt{{{n}}} = {c}$.'

content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
print(content)
