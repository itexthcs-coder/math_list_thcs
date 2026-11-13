import random
from sympy.abc import x
from sympy import expand, latex

lisdang = ['1']
dang = random.choice(lisdang)

if dang == '1':
    c = random.choice([-3, -2, -1, 1, 2, 3])
    m = random.choice([2, 3, 4, 5, 6, 7])
    nhi_thuc = x + c
    da_thuc = expand(nhi_thuc**3)
    
    kq = m + c
    
    da = f'${kq}$'
    s = [
        f'${latex(-2*x + m + c)}$',
        f'${m - c}$',
        f'${latex(2*x + m + c)}$',
        f'${-kq}$'
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    noidungcauhoi = f'Rút gọn biểu thức $P = -x + {m} + \\sqrt[3]{{{latex(da_thuc)}}}$ ta được kết quả là'
    
    da_d = '\\True ' + str(da)
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    loigiai = f'''Ta có ${latex(da_thuc)} = ({latex(nhi_thuc)})^3$.
Do đó: $P = -x + {m} + \\sqrt[3]{{({latex(nhi_thuc)})^3}} = -x + {m} + ({latex(nhi_thuc)}) = {kq}$.'''

content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
print(content)
