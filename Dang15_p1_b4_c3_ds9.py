import random
from sympy import sqrt, latex

lisdang = ['1']
dang = random.choice(lisdang)

if dang == '1':
    n = random.choice([2, 3, 5, 6, 7])
    m = 1 if n in [2, 3] else 2
    
    bt = m - sqrt(n)
    bt_doi = sqrt(n) - m
    
    da = f'${latex(bt)}$'
    s = [
        f'${latex(bt_doi)}$',
        f'${m} + \\sqrt{{{n}}}$',
        f'$-{m} - \\sqrt{{{n}}}$',
        f'${m - n}$'
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    noidungcauhoi = f'Rút gọn biểu thức $\\sqrt[3]{{({latex(bt)})^3}}$ ta được kết quả là'
    
    da_d = '\\True ' + str(da)
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    loigiai = f'Áp dụng hằng đẳng thức $\\sqrt[3]{{A^3}} = A$ với mọi số thực $A$, ta có: $\\sqrt[3]{{({latex(bt)})^3}} = {latex(bt)}$.'

content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
print(content)
