import random

lisdang = ['1']
dang = random.choice(lisdang)

if dang == '1':
    bien = random.choice(['a', 'b', 'x', 'm'])
    kieu = random.choice([1, 2])
    
    if kieu == 1:
        da = f'$\\sqrt[3]{{{bien}^3}} = {bien}$'
    else:
        da = f'$(\\sqrt[3]{{{bien}}})^3 = {bien}$'
        
    s = [
        f'$\\sqrt[3]{{{bien}^3}} = |{bien}|$',
        f'$(\\sqrt[3]{{{bien}}})^3 = -{bien}$',
        f'$(\\sqrt[3]{{{bien}}})^3 = {bien}^3$',
        f'$\\sqrt[3]{{{bien}^3}} = {bien}^3$'
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    noidungcauhoi = f'Với mọi số thực ${bien}$, đẳng thức nào sau đây luôn đúng?'
    
    da_d = '\\True ' + str(da)
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    loigiai = f'Từ định nghĩa căn bậc ba, ta có $(\\sqrt[3]{{{bien}}})^3 = \\sqrt[3]{{{bien}^3}} = {bien}$ với mọi số thực ${bien}$.'

content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
print(content)
