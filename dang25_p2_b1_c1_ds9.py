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


def bt_dang25_p2_b1_c1_ds9(self):
    # Khai báo biến
    x, y = symbols('x y')
    
    # Hàm định dạng tiền tệ có dấu cách ngăn cách hàng nghìn
    def format_money(val):
        return '{:,}'.format(val).replace(',', ' ')
    
    # Hàm định dạng số làm tròn 2 chữ số thập phân dùng dấu phẩy
    def format_round(val):
        d = Decimal(str(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        return str(d).replace('.', ',')
    
    # Dạng bài: Xăng RON 95 giá price_x đồng/lít, Dầu Diesel giá price_y đồng/lít, tổng tiền total_money đồng
    # Mẫu gốc: Xăng 24 000 đ/l, Dầu 20 000 đ/l, tổng 500 000 đ (rút gọn chia 4 000 => 6x + 5y = 125)
    while True:
        u = random.choice([5, 6, 7])
        v = random.choice([4, 5])
        if math.gcd(u, v) == 1 and u != v:
            # Chọn nghiệm nguyên dương thực tế (x_sol, y_sol)
            # u*x + v*y = C_sim
            x_sol = random.choice([5, 10, 15])
            y_sol = random.choice([7, 11, 13])
            C_sim = u * x_sol + v * y_sol
            
            # Chọn hệ số tiền tệ k_m = 4000
            k_m = 4000
            price_x = u * k_m
            price_y = v * k_m
            total_money = C_sim * k_m
            
            # Tìm các nghiệm nguyên dương khác (nếu có)
            all_sol = []
            for xi in range(1, C_sim // u + 1):
                rem = C_sim - u * xi
                if rem > 0 and rem % v == 0:
                    all_sol.append((xi, rem // v))
            if len(all_sol) >= 2:
                break
    
    # Lấy 2 nghiệm: 1 nghiệm cho câu c (cặp số thoả mãn), 1 nghiệm cho câu d (nghiệm nguyên dương)
    pair1 = all_sol[0]
    pair2 = all_sol[1]
    
    # Tính số lít khi chỉ đổ xăng (y = 0 => x = total_money / price_x = C_sim / u)
    lit_x_only = Decimal(str(C_sim)) / Decimal(str(u))
    lit_x_round_str = format_round(lit_x_only)
    
    price_x_str = format_money(price_x)
    price_y_str = format_money(price_y)
    total_money_str = format_money(total_money)
    
    lhs_rutgon = '%sx + %sy' % (u, v)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Một trạm xăng bán hai loại nhiên liệu: Xăng RON 95 giá %s đồng/lít và Dầu Diesel giá %s đồng/lít. Một tài xế đổ $x$ lít xăng RON 95 và $y$ lít dầu Diesel hết tổng cộng %s đồng.''' % (price_x_str, price_y_str, total_money_str))
    
    ############################################################################# Nhận biết #################################################
    # a) Phương trình biểu diễn số tiền thanh toán là u*x + v*y = C_sim
    nb_da_1_d = '\\True Phương trình biểu diễn số tiền thanh toán là $%s = %s$' % (lhs_rutgon, C_sim)
    nb_da_1_s = 'Phương trình biểu diễn số tiền thanh toán là $%sx + %sy = %s$' % (v, u, C_sim)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Số tiền mua xăng RON 95 là $%s x$ (đồng). \\\\ Số tiền mua dầu Diesel là $%s y$ (đồng). \\\\ Tổng số tiền là %s đồng nên ta có phương trình: \\\\ $%s x + %s y = %s$. \\\\ Chia cả hai vế của phương trình cho $%s$, ta được: $%s = %s$.''' % (price_x, price_y, total_money_str, price_x, price_y, total_money, k_m, lhs_rutgon, C_sim))
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################# Thông hiểu #################################################
    # b) Nếu tài xế chỉ đổ xăng RON 95 (y = 0) thì số lít xăng mua được là khoảng lit_x_round_str lít
    lit_x_wrong_str = format_round(lit_x_only + Decimal('1.25'))
    th_da_1_d = '\\True Nếu tài xế chỉ đổ xăng RON 95 ($y = 0$) thì số lít xăng mua được là khoảng %s lít' % (lit_x_round_str)
    th_da_1_s = 'Nếu tài xế chỉ đổ xăng RON 95 ($y = 0$) thì số lít xăng mua được là khoảng %s lít' % (lit_x_wrong_str)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Khi tài xế chỉ đổ xăng RON 95, tức là $y = 0$. \\\\ Thay $y = 0$ vào phương trình $%s = %s$, ta được: \\\\ $%s x + %s \\cdot 0 = %s \\Leftrightarrow %s x = %s \\Leftrightarrow x = \\dfrac{%s}{%s} \\approx %s$ lít.''' % (lhs_rutgon, C_sim, u, v, C_sim, u, C_sim, C_sim, u, lit_x_round_str))
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################# Vận dụng #################################################
    # c) Cặp số (pair1[0]; pair1[1]) thoả mãn phương trình số tiền thanh toán
    pair1_wrong = (pair1[0] + 1, pair1[1])
    vd_da_1_d = '\\True Cặp số $(%s; %s)$ thoả mãn phương trình số tiền thanh toán' % (pair1[0], pair1[1])
    vd_da_1_s = 'Cặp số $(%s; %s)$ thoả mãn phương trình số tiền thanh toán' % (pair1_wrong[0], pair1_wrong[1])
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Thay $x = %s$ và $y = %s$ vào vế trái của phương trình $%s = %s$, ta được: \\\\ %s \\cdot %s + %s \\cdot %s = %s + %s = %s = VP$. \\\\ Do đó, cặp số $(%s; %s)$ thoả mãn phương trình số tiền thanh toán.''' % (pair1[0], pair1[1], lhs_rutgon, C_sim, u, pair1[0], v, pair1[1], u * pair1[0], v * pair1[1], C_sim, pair1[0], pair1[1]))
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################# Vận dụng cao #################################################
    # d) Cặp số (pair2[0]; pair2[1]) là một nghiệm nguyên dương của phương trình
    pair2_wrong = (pair2[0], pair2[1] + 1)
    vdc_da_1_d = '\\True Cặp số $(%s; %s)$ là một nghiệm nguyên dương của phương trình' % (pair2[0], pair2[1])
    vdc_da_1_s = 'Cặp số $(%s; %s)$ là một nghiệm nguyên dương của phương trình' % (pair2_wrong[0], pair2_wrong[1])
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Xét cặp số $(%s; %s)$: \\\\ + Ta thấy $%s > 0$ và $%s > 0$ nên đây là các số nguyên dương. \\\\ + Thay vào phương trình $%s = %s$: $%s \\cdot %s + %s \\cdot %s = %s + %s = %s = VP$. \\\\ Do đó, cặp số $(%s; %s)$ là một nghiệm nguyên dương của phương trình.''' % (pair2[0], pair2[1], pair2[0], pair2[1], lhs_rutgon, C_sim, u, pair2[0], v, pair2[1], u * pair2[0], v * pair2[1], C_sim, pair2[0], pair2[1]))
    
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
