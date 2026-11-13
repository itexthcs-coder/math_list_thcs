import random
from sympy.abc import x
from sympy import latex

lisdang = ['1']
dang = random.choice(lisdang)

if dang == '1':
    a = random.randint(2, 7)
    b = random.choice([-5, -3, -1, 1, 3, 5])
    bt = a*x + b
    
    da = f'$\\sqrt[3]{{{latex(bt)}}}$'
    s = [
        f'$\\sqrt{{{latex(bt)}}}$',
        f'$3\\sqrt{{{latex(bt)}}}$',
        f'$({latex(bt)})^3$',
        f'$\\dfrac{{1}}{{3}}({latex(bt)})$'
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    noidungcauhoi = 'Trong các biểu thức sau, biểu thức nào là căn thức bậc ba?'
    
    da_d = '\\True ' + str(da)
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    loigiai = f'Căn thức bậc ba là biểu thức có dạng $\\sqrt[3]{{A}}$, trong đó $A$ là một biểu thức đại số. Do đó $\\sqrt[3]{{{latex(bt)}}}$ là căn thức bậc ba.'

content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
print(content)
