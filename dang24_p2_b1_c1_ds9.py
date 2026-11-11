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


def bt_dang24_p2_b1_c1_ds9(self):
    # Khai báo biến
    x, y = symbols('x y')
    
    # Hàm định dạng tiền tệ có khoảng trắng cách hàng nghìn
    def format_money(val):
        return '{:,}'.format(val).replace(',', ' ')
    
    # Dạng bài: Mua m kg táo và n kg cam với tổng số tiền total_vnd đồng
    # Gọi x là giá 1 kg táo (nghìn đồng), y là giá 1 kg cam (nghìn đồng)
    # Mẫu gốc: m = 2, n = 3, total_vnd = 150 000 đồng => 2x + 3y = 150
    while True:
        m_kg = random.choice([2, 3, 4])
        n_kg = random.choice([2, 3, 5])
        if math.gcd(m_kg, n_kg) == 1 and m_kg != n_kg:
            # Chọn cặp nghiệm nguyên dương đẹp (x_sol, y_sol) tính bằng nghìn đồng
            # Ví dụ giá cam y_sol, giá táo x_sol
            x_sol = random.choice([25, 30, 35, 40])
            y_sol = random.choice([20, 25, 30, 35])
            total_k = m_kg * x_sol + n_kg * y_sol
            total_vnd = total_k * 1000
            
            # Chọn một mức giá cam khác y_test để kiểm tra câu c
            y_test = random.choice([15, 20, 25])
            if (total_k - n_kg * y_test) % m_kg == 0 and y_test != y_sol:
                x_test = (total_k - n_kg * y_test) // m_kg
                if x_test > 0:
                    break
    
    total_vnd_str = format_money(total_vnd)
    lhs_str = '%sx + %sy' % (m_kg, n_kg)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Một người đi siêu thị mua %s kg táo và %s kg cam với tổng số tiền %s đồng. Gọi giá $1$ kg táo là $x$ (nghìn đồng) và giá $1$ kg cam là $y$ (nghìn đồng).''' % (m_kg, n_kg, total_vnd_str))
    
    ############################################################################# Nhận biết #################################################
    # a) Phương trình biểu thị số tiền mua hàng là mx + ny = total_k
    nb_da_1_d = '\\True Phương trình biểu thị số tiền mua hàng là $%s = %s$' % (lhs_str, total_k)
    nb_da_1_s = 'Phương trình biểu thị số tiền mua hàng là $%s = %s$' % (lhs_str, total_vnd)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Vì đơn vị của $x$ và $y$ là nghìn đồng nên đổi tổng số tiền mua hàng: %s đồng $= %s$ nghìn đồng. \\\\ Số tiền mua táo là $%s x$ (nghìn đồng), số tiền mua cam là $%s y$ (nghìn đồng). \\\\ Ta có phương trình biểu thị số tiền mua hàng là: $%s = %s$.''' % (total_vnd_str, total_k, m_kg, n_kg, lhs_str, total_k))
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################# Thông hiểu #################################################
    # b) Cặp số (x_sol; y_sol) là một nghiệm của phương trình
    x_wrong = x_sol + 5
    th_da_1_d = '\\True Cặp số $(%s; %s)$ là một nghiệm của phương trình' % (x_sol, y_sol)
    th_da_1_s = 'Cặp số $(%s; %s)$ là một nghiệm của phương trình' % (x_wrong, y_sol)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Thay $x = %s$ và $y = %s$ vào vế trái của phương trình, ta được: \\\\ $%s \\cdot %s + %s \\cdot %s = %s + %s = %s = VP$. \\\\ Do đó, cặp số $(%s; %s)$ là một nghiệm của phương trình.''' % (x_sol, y_sol, m_kg, x_sol, n_kg, y_sol, m_kg * x_sol, n_kg * y_sol, total_k, x_sol, y_sol))
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################# Vận dụng #################################################
    # c) Nếu giá cam là y_test nghìn đồng/kg thì giá táo tương ứng là x_test nghìn đồng/kg
    x_test_wrong = x_test + 10
    vd_da_1_d = '\\True Nếu giá cam là %s nghìn đồng/kg thì giá táo tương ứng là %s nghìn đồng/kg' % (y_test, x_test)
    vd_da_1_s = 'Nếu giá cam là %s nghìn đồng/kg thì giá táo tương ứng là %s nghìn đồng/kg' % (y_test, x_test_wrong)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Nếu giá cam là $y = %s$ (nghìn đồng/kg), thay vào phương trình $%s = %s$, ta được: \\\\ $%s x + %s \\cdot %s = %s \\Leftrightarrow %s x + %s = %s \\Leftrightarrow %s x = %s \\Leftrightarrow x = %s$. \\\\ Vậy giá táo tương ứng là %s nghìn đồng/kg.''' % (y_test, lhs_str, total_k, m_kg, n_kg, y_test, total_k, m_kg, n_kg * y_test, total_k, m_kg, total_k - n_kg * y_test, x_test, x_test))
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################# Vận dụng cao #################################################
    # d) Điểm biểu diễn tập nghiệm của phương trình trên góc phần tư thứ nhất của hệ trục Oxy là một đoạn thẳng giới hạn bởi trục toạ độ
    vdc_da_1_d = '\\True Điểm biểu diễn tập nghiệm của phương trình trên góc phần tư thứ nhất của hệ trục $Oxy$ là một đoạn thẳng giới hạn bởi trục toạ độ'
    vdc_da_1_s = 'Điểm biểu diễn tập nghiệm của phương trình trên góc phần tư thứ nhất của hệ trục $Oxy$ là một đường thẳng kéo dài vô hạn về hai phía'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Trong bài toán thực tế, giá tiền của cam và táo không thể âm ($x \\ge 0$ và $y \\ge 0$). \\\\ Đường thẳng $%s = %s$ cắt hai trục toạ độ tại hai điểm $A\\left(%s; 0\\right)$ và $B\\left(0; %s\\right)$. \\\\ Vì $x \\ge 0$ và $y \\ge 0$ nên phần biểu diễn các nghiệm thực tế trên góc phần tư thứ nhất chính là đoạn thẳng $AB$ nối hai giao điểm trên các trục toạ độ.''' % (lhs_str, total_k, latex(Rational(total_k, m_kg)), latex(Rational(total_k, n_kg))))
    
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
