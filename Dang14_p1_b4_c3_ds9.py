import random
from sympy.abc import x
from sympy import latex

lisdang = ['1']
dang = random.choice(lisdang)

if dang == '1':
    k = random.randint(2, 5)
    a = random.randint(2, 5)
    x0 = -random.randint(2, 10)
    b = -(k**3) - a*x0
    bt = a*x + b
    
    da = f'$-{k}$'
    s = [
        f'${k}$',
        f'$-{k**3}$',
        f'$-{k+1}$',
        f'$-{k-1}$' if k > 2 else '$-6$'
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    noidungcauhoi = f'Tại $x = {x0}$, giá trị của căn thức $\\sqrt[3]{{{latex(bt)}}}$ bằng'
    
    da_d = '\\True ' + str(da)
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    b_str = f'+ {b}' if b >= 0 else f'- {-b}'
    loigiai = f'Thay $x = {x0}$ vào căn thức đã cho, ta được: $\\sqrt[3]{{{a} \\cdot ({x0}) {b_str}}} = \\sqrt[3]{{-{k**3}}} = \\sqrt[3]{{(-{k})^3}} = -{k}$.'

content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
print(content)
