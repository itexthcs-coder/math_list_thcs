import random

lisdang = ['1']
dang = random.choice(lisdang)

if dang == '1':
    ds_so = [3.25, 12, 45, 2.1, -18, -28, 0.35, 15.4, -7.2]
    so = random.choice(ds_so)
    
    if so >= 0:
        val = so**(1/3)
    else:
        val = -((-so)**(1/3))
        
    kq_tron = round(val, 2)
    
    while abs(round(val, 3) * 1000 % 10 - 5) == 0:
        so = random.choice(ds_so)
        val = so**(1/3) if so >= 0 else -((-so)**(1/3))
        kq_tron = round(val, 2)
        
    so_str = str(so).replace('.', ',')
    val_9_str = f'{val:.9f}'.rstrip('0').rstrip('.').replace('.', ',')
    kq_str = f'{kq_tron:.2f}'.replace('.', ',')
    
    nhieu1 = f'{kq_tron + 0.01:.2f}'.replace('.', ',')
    nhieu2 = f'{kq_tron - 0.01:.2f}'.replace('.', ',')
    nhieu3 = f'{round(val, 3):.3f}'.replace('.', ',')
    nhieu4 = f'{round(val, 1):.1f}'.replace('.', ',')
    
    da = f'${kq_str}$'
    s = list(set([f'${nhieu1}$', f'${nhieu2}$', f'${nhieu3}$', f'${nhieu4}$']) - {da})
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    noidungcauhoi = f'Sử dụng máy tính cầm tay tính $\\sqrt[3]{{{so_str}}}$ và làm tròn kết quả đến chữ số thập phân thứ hai, ta được'
    
    da_d = '\\True ' + str(da)
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    loigiai = f'Sử dụng máy tính cầm tay, ta tính được $\\sqrt[3]{{{so_str}}} \\approx {val_9_str}$. Làm tròn kết quả đến chữ số thập phân thứ hai ta được ${kq_str}$.'

content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
print(content)
