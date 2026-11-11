import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang26_p2_b1_c1_ds9(self):
    # Khai báo biến
    x, y = symbols('x y')
    
    # Hàm định dạng số có khoảng trắng ngăn cách hàng nghìn
    def format_num(val):
        return '{:,}'.format(val).replace(',', ' ')
    
    # Dạng bài toán thực tế: Xe tải chở hai mặt hàng gồm các thùng hàng loại A và loại B
    # Mẫu gốc: loại A nặng 20 kg/thùng, loại B nặng 30 kg/thùng, tổng 120 thùng, nặng 3 tấn (3000 kg)
    # Rút gọn phương trình khối lượng: chia cho 10 => 2x + 3y = 300
    while True:
        wA = random.choice([20, 25, 30])
        wB = random.choice([30, 40, 50])
        if wA != wB:
            # Chọn số thùng loại A (x0) và loại B (y0) nguyên dương đẹp
            x0 = random.choice([50, 60, 70, 80])
            y0 = random.choice([40, 50, 60, 70])
            if x0 != y0:
                total_boxes = x0 + y0
                total_kg = wA * x0 + wB * y0
                # Tổng khối lượng tính theo tấn (phải là số nguyên hoặc thập phân đẹp)
                ton_val = total_kg / 1000
                if ton_val.is_integer():
                    ton_str = '%s tấn' % (int(ton_val))
                else:
                    ton_str = '%s tấn' % (str(ton_val).replace('.', ','))
                
                # Ước chung để rút gọn phương trình khối lượng
                gcd_val = math.gcd(wA, wB)
                gcd_val = math.gcd(gcd_val, total_kg)
                uA = wA // gcd_val
                vB = wB // gcd_val
                c_mass = total_kg // gcd_val
                break
    
    total_kg_str = format_num(total_kg)
    pt_mass_rutgon = '%sx + %sy = %s' % (uA, vB, c_mass)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Một xe tải chở hai mặt hàng gồm các thùng hàng loại A (nặng %s kg/thùng) và loại B (nặng %s kg/thùng). Xe chở tổng cộng %s thùng hàng với tổng khối lượng đúng %s (%s kg).''' % (wA, wB, total_boxes, ton_str, total_kg_str))
    
    ############################################################################# Nhận biết #################################################
    # a) Gọi x, y lần lượt là số thùng hàng loại A và loại B thì ta có hệ: { x + y = total_boxes; wA*x + wB*y = total_kg }
    # Đề yêu cầu hệ viết dạng ngoặc nhọn
    nb_da_1_d = '\\True Gọi $x, y$ lần lượt là số thùng hàng loại A và loại B thì ta có hệ: $\\begin{cases} x + y = %s \\\\ %sx + %sy = %s \\end{cases}$' % (total_boxes, wA, wB, total_kg)
    nb_da_1_s = 'Gọi $x, y$ lần lượt là số thùng hàng loại A và loại B thì ta có hệ: $\\begin{cases} x + y = %s \\\\ %sx + %sy = %s \\end{cases}$' % (total_boxes, wB, wA, total_kg)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Gọi số thùng hàng loại A là $x$ và số thùng hàng loại B là $y$ ($x, y \\in \\mathbb{N}^*$). \\\\ Vì tổng số thùng hàng là %s thùng nên ta có: $x + y = %s$. \\\\ Tổng khối lượng các thùng hàng là %s kg nên ta có: $%sx + %sy = %s$. \\\\ Ta có hệ phương trình: $\\begin{cases} x + y = %s \\\\ %sx + %sy = %s \\end{cases}$.''' % (total_boxes, total_boxes, total_kg_str, wA, wB, total_kg, total_boxes, wA, wB, total_kg))
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################# Thông hiểu #################################################
    # b) Phương trình khối lượng tương đương với pt_mass_rutgon
    c_mass_wrong = c_mass + random.choice([10, -10, 20])
    th_da_1_d = '\\True Phương trình khối lượng tương đương với $%s$' % (pt_mass_rutgon)
    th_da_1_s = 'Phương trình khối lượng tương đương với $%sx + %sy = %s$' % (uA, vB, c_mass_wrong)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Phương trình khối lượng là $%sx + %sy = %s$. \\\\ Chia cả hai vế của phương trình cho $%s$, ta được phương trình tương đương: $%s$.''' % (wA, wB, total_kg, gcd_val, pt_mass_rutgon))
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################# Vận dụng #################################################
    # c) Số thùng hàng loại A là x_equal thùng và loại B là y_equal thùng (mẫu gốc: lấy 60 và 60 là sai vì x0 != y0)
    half_box = total_boxes // 2
    vd_da_1_d = '\\True Số thùng hàng loại A là %s thùng và loại B là %s thùng' % (x0, y0)
    vd_da_1_s = 'Số thùng hàng loại A là %s thùng và loại B là %s thùng' % (half_box, total_boxes - half_box)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Giải hệ phương trình $\\begin{cases} x + y = %s \\\\ %sx + %sy = %s \\end{cases}$: \\\\ Nhân hai vế của phương trình thứ nhất với $%s$, ta có: $\\begin{cases} %sx + %sy = %s \\\\ %sx + %sy = %s \\end{cases}$. \\\\ Trừ từng vế hai phương trình, ta được: \\\\ $(%s - %s)x = %s - %s \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$. \\\\ Thay $x = %s$ vào phương trình $x + y = %s$, ta được: $y = %s - %s = %s$. \\\\ Vậy số thùng hàng loại A là %s thùng và loại B là %s thùng.''' % (total_boxes, uA, vB, c_mass, vB, vB, vB, vB * total_boxes, uA, vB, c_mass, vB, uA, vB * total_boxes, c_mass, vB - uA, vB * total_boxes - c_mass, x0, x0, total_boxes, total_boxes, x0, y0, x0, y0))
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################# Vận dụng cao #################################################
    # d) Cặp số (x0; y0) là nghiệm của hệ phương trình mô tả bài toán
    vdc_da_1_d = '\\True Cặp số $(%s; %s)$ là nghiệm của hệ phương trình mô tả bài toán' % (x0, y0)
    vdc_da_1_s = 'Cặp số $(%s; %s)$ là nghiệm của hệ phương trình mô tả bài toán' % (y0, x0)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Từ kết quả giải hệ phương trình ở trên, ta tìm được $x = %s$ và $y = %s$. \\\\ Do đó, cặp số $(%s; %s)$ chính là nghiệm của hệ phương trình mô tả bài toán.''' % (x0, y0, x0, y0))
    
    list_vdc_2 = [loigiai_vdc_1]
    
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)
    
    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
    
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
    
        if 1 <= true_count <= 3:
            break
    
    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    
    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)
    
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(shuffled_answers_nb[0]) + '}\n'
               '{' + str(shuffled_answers_th[0]) + '}\n'
               '{' + str(shuffled_answers_vd[0]) + '}\n'
               '{' + str(shuffled_answers_vdc[0]) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
               '\\item ' + str(shuffled_solutions_th[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
