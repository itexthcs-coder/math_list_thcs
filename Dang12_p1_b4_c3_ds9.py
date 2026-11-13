import random
from sympy.abc import x
from sympy import latex

lisdang = ['1']
dang = random.choice(lisdang)

if dang == '1':
    tu = random.choice([-5, -3, -2, 2, 3, 4])
    m = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    mau = x - m
    
    da = f'$x \\neq {m}$'
    s = [
        f'$x > {m}$',
        f'$x \\ge {m}$',
        f'$x < {m}$',
        '$x \\in \\mathbb{R}$'
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    noidungcauhoi = f'Điều kiện xác định của căn thức bậc ba $\\sqrt[3]{{\\dfrac{{{tu}}}{{{latex(mau)}}}}}$ là'
    
    da_d = '\\True ' + str(da)
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    loigiai = f'Căn thức bậc ba $\\sqrt[3]{{\\dfrac{{{tu}}}{{{latex(mau)}}}}}$ xác định khi biểu thức dưới dấu căn $\\dfrac{{{tu}}}{{{latex(mau)}}}$ xác định, tức là ${latex(mau)} \\neq 0 \\Leftrightarrow x \\neq {m}$.'

content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
print(content)
