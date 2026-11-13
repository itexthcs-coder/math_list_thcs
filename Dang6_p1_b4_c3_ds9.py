import random

lisdang = ['1']
dang = random.choice(lisdang)

if dang == '1':
    dau = random.choice([1, -1])
    k_int = random.choice([1, 2, 3, 4, 5, 11, 12])
    k_val = dau * k_int / 10.0
    a_val = round(k_val**3, 3)
    
    k_str = str(k_val).replace('.', ',')
    a_str = str(a_val).replace('.', ',')
    
    da = f'${k_str}$'
    
    nhieu1 = str(-k_val).replace('.', ',')
    nhieu2 = str(round(dau * k_int / 100.0, 2)).replace('.', ',')
    nhieu3 = str(dau * k_int)
    nhieu4 = str(round(dau * (k_int + 1) / 10.0, 1)).replace('.', ',')
    
    s = list(set([f'${nhieu1}$', f'${nhieu2}$', f'${nhieu3}$', f'${nhieu4}$']) - {da})
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    noidungcauhoi = f'Giá trị của $\\sqrt[3]{{{a_str}}}$ bằng'
    
    da_d = '\\True ' + str(da)
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    if dau == -1:
        loigiai = f'Vì $({k_str})^3 = {a_str}$ nên $\\sqrt[3]{{{a_str}}} = {k_str}$.'
    else:
        loigiai = f'Vì ${k_str}^3 = {a_str}$ nên $\\sqrt[3]{{{a_str}}} = {k_str}$.'

content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
print(content)
