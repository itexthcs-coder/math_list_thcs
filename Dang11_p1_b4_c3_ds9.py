import random
from sympy.abc import x
from sympy import Rational, latex

lisdang = ['1']
dang = random.choice(lisdang)

if dang == '1':
    a = random.choice([-4, -3, -2, 2, 3, 4, 5])
    b = random.choice([-5, -3, -1, 1, 2, 4])
    bt = a*x + b
    nghiem = Rational(-b, a)
    
    da = 'Mọi số thực $x \\in \\mathbb{R}$'
    s = [
        f'$x \\ge {latex(nghiem)}$',
        f'$x > {latex(nghiem)}$',
        f'$x \\le {latex(nghiem)}$',
        f'$x \\neq {latex(nghiem)}$'
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    noidungcauhoi = f'Căn thức bậc ba $\\sqrt[3]{{{latex(bt)}}}$ xác định với những giá trị nào của $x$?'
    
    da_d = '\\True ' + str(da)
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    loigiai = f'Vì mọi số thực đều có căn bậc ba và đa thức ${latex(bt)}$ xác định với mọi $x \\in \\mathbb{{R}}$ nên $\\sqrt[3]{{{latex(bt)}}}$ xác định với mọi số thực $x \\in \\mathbb{{R}}$.'

content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
print(content)
