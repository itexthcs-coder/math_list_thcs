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


def bt_dang21_p2_b1_c1_ds9(self):
    # Khai báo biến
    x, y = symbols('x y')
    
    # Hàm định dạng tiền tệ có dấu cách ngăn cách hàng nghìn
    def format_money(val):
        return '{:,}'.format(val).replace(',', ' ')
    
    # Random dữ liệu bài toán thực tế:
    # Giá vở loại I: price1 (nghìn đồng), Giá vở loại II: price2 (nghìn đồng)
    # Mẫu gốc: loại I 8 000 đồng, loại II 6 000 đồng, tổng 70 000 đồng (rút gọn chia 2000 => 4x + 3y = 35)
    while True:
        u = random.choice([3, 4, 5])
        v = random.choice([2, 3, 5])
        if math.gcd(u, v) == 1 and u != v:
            # Chọn nghiệm nguyên dương thực tế (x0, y0)
            x0 = random.choice([2, 5, 8])
            y0 = random.choice([3, 5, 9])
            c_sim = u * x0 + v * y0
            
            # Thừa số nhân tiền tệ k_m = 1000 hoặc 2000
            k_m = random.choice([1000, 2000])
            price1 = u * k_m
            price2 = v * k_m
            total_money = c_sim * k_m
            
            # Tìm một nghiệm nguyên dương khác (x1, y1) nếu có
            # u*x + v*y = c_sim
            valid_pairs = []
            for xi in range(1, c_sim // u + 1):
                rem = c_sim - u * xi
                if rem > 0 and rem % v == 0:
                    valid_pairs.append((xi, rem // v))
            if len(valid_pairs) >= 2:
                break
    
    # Cặp số thoả mãn thực tế
    pair_true = valid_pairs[0]
    pair_second = valid_pairs[1]
    # Cặp số sai
    pair_wrong = (pair_second[0] + 1, pair_second[1])
    
    price1_str = format_money(price1)
    price2_str = format_money(price2)
    total_money_str = format_money(total_money)
    
    # Phương trình rút gọn: u*x + v*y = c_sim
    pt_rutgon = '%sx + %sy = %s' % (u, v, c_sim)
    pt_full = '%s x + %s y = %s' % (price1_str, price2_str, total_money_str)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Một cửa hàng bán hai loại vở: vở loại I giá %s đồng/quyển và vở loại II giá %s đồng/quyển. Bạn Lan mua $x$ quyển vở loại I và $y$ quyển vở loại II hết đúng %s đồng.''' % (price1_str, price2_str, total_money_str))
    
    ############################################################################# Nhận biết #################################################
    # a) Phương trình biểu thị số tiền Lan mua vở là price1 x + price2 y = total_money (hay u x + v y = c_sim)
    nb_da_1_d = '\\True Phương trình biểu thị số tiền Lan mua vở là $%sx + %sy = %s$ (hay $%s$)' % (price1, price2, total_money, pt_rutgon)
    nb_da_1_s = 'Phương trình biểu thị số tiền Lan mua vở là $%sx + %sy = %s$' % (price2, price1, total_money)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Số tiền mua $x$ quyển vở loại I là $%s x$ (đồng). \\\\ Số tiền mua $y$ quyển vở loại II là $%s y$ (đồng). \\\\ Tổng số tiền là %s đồng nên ta có phương trình: $%sx + %sy = %s$. \\\\ Chia cả hai vế cho $%s$, ta được: $%s$.''' % (price1, price2, total_money_str, price1, price2, total_money, k_m, pt_rutgon))
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################# Thông hiểu #################################################
    # b) Vì x, y là số quyển vở nên x, y phải là các số tự nhiên (x, y \in \mathbb{N}*)
    th_da_1_d = '\\True Vì $x, y$ là số quyển vở nên $x, y$ phải là các số tự nhiên ($x, y \\in \\mathbb{N}^*$)'
    th_da_1_s = 'Vì $x, y$ là số quyển vở nên $x, y$ có thể là các số thực bất kì ($x, y \\in \\mathbb{R}$)'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Do $x$ và $y$ lần lượt biểu thị số quyển vở mà Lan mua nên số quyển vở phải là các số nguyên dương, tức là $x, y \\in \\mathbb{N}^*$.''' )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################# Vận dụng #################################################
    # c) Cặp số (pair_true[0]; pair_true[1]) thoả mãn bài toán thực tế
    vd_da_1_d = '\\True Cặp số $(%s; %s)$ thoả mãn bài toán thực tế' % (pair_true[0], pair_true[1])
    vd_da_1_s = 'Cặp số $(%s; %s)$ không thoả mãn bài toán thực tế' % (pair_true[0], pair_true[1])
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Thay $x = %s$ và $y = %s$ vào phương trình $%s$, ta có: \\\\ %s \\cdot %s + %s \\cdot %s = %s + %s = %s = VP$. \\\\ Vì $%s, %s \\in \\mathbb{N}^*$ nên cặp số $(%s; %s)$ hoàn toàn thoả mãn bài toán thực tế.''' % (pair_true[0], pair_true[1], pt_rutgon, u, pair_true[0], v, pair_true[1], u * pair_true[0], v * pair_true[1], c_sim, pair_true[0], pair_true[1], pair_true[0], pair_true[1]))
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################# Vận dụng cao #################################################
    # d) Lan có thể mua được pair_second[0] quyển loại I và pair_second[1] quyển loại II
    calc_check = u * pair_wrong[0] + v * pair_wrong[1]
    vdc_da_1_d = '\\True Lan có thể mua được %s quyển loại I và %s quyển loại II' % (pair_second[0], pair_second[1])
    vdc_da_1_s = 'Lan có thể mua được %s quyển loại I và %s quyển loại II' % (pair_wrong[0], pair_wrong[1])
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Kiểm tra phương trình $%s$: \\\\ Với %s quyển loại I và %s quyển loại II: \\\\ %s \\cdot %s + %s \\cdot %s = %s + %s = %s = VP$. \\\\ Do đó, Lan có thể mua được %s quyển loại I và %s quyển loại II.''' % (pt_rutgon, pair_second[0], pair_second[1], u, pair_second[0], v, pair_second[1], u * pair_second[0], v * pair_second[1], c_sim, pair_second[0], pair_second[1]))
    
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
