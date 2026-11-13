import random
from sympy.abc import x
from sympy import expand, latex

lisdang = ['1']
dang = random.choice(lisdang)

if dang == '1':
    c = random.choice([-3, -2, -1, 1, 2, 3])
    nhi_thuc = x + c
    da_thuc = expand(nhi_thuc**3)
    
    da = f'${latex(nhi_thuc)}$'
    s = [
        f'$|{latex(nhi_thuc)}|$',
        f'${latex(x - c)}$',
        f'$({latex(nhi_thuc)})^3$',
        f'${latex(-x - c)}$'
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    noidungcauhoi = f'Biểu thức $\\sqrt[3]{{{latex(da_thuc)}}}$ bằng biểu thức nào sau đây với mọi $x \\in \\mathbb{{R}}$?'
    
    da_d = '\\True ' + str(da)
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    loigiai = f'Ta có ${latex(da_thuc)} = ({latex(nhi_thuc)})^3$. Do đó $\\sqrt[3]{{{latex(da_thuc)}}} = \\sqrt[3]{{({latex(nhi_thuc)})^3}} = {latex(nhi_thuc)}$.'

content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
print(content)
