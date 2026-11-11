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


def bt_dang1_p2_b1_c1_ds9(self):
    # Khai báo biến
    x, y = symbols('x y')
    
    # Hàm phụ trợ format số thập phân hoặc phân số
    def format_dec(val):
        if float(val).is_integer():
            return str(int(val))
        val_float = float(val)
        # làm tròn 2 chữ số thập phân nếu cần
        s = str(round(val_float, 2)).replace('.', ',')
        return s
    
    # Random hệ số a, b, c cho phương trình ax + by = c
    # Mẫu gốc: 3x - 2y = 6
    # a, b khác 0, c khác 0
    while True:
        a_val = random.choice([2, 3, 4, 5])
        b_val = random.choice([-5, -4, -3, -2, 2, 3, 4, 5])
        # Chọn nghiệm nguyên đẹp (x0, 0) và (0, y0)
        # y = 0 => ax = c => c chia hết cho a
        # x = 0 => by = c => c chia hết cho b
        k = random.choice([1, 2, 3])
        # lcm(a, |b|)
        lcm_ab = math.lcm(abs(a_val), abs(b_val))
        c_val = lcm_ab * k * random.choice([1, -1])
        if c_val != 0:
            break
    
    # Phương trình: a*x + b*y = c
    # Biểu diễn phương trình
    pt_expr = a_val * x + b_val * y
    
    # Nghiệm cắt Ox: x0 = c/a, y = 0
    x_ox = c_val // a_val
    # Nghiệm cắt Oy: x = 0, y0 = c/b
    y_oy = c_val // b_val
    
    # Rút y theo x: y = (c - ax) / b = (-a/b) x + (c/b)
    slope = Rational(-a_val, b_val)
    intercept = Rational(c_val, b_val)
    
    # Chuỗi biểu diễn y theo x
    y_expr = slope * x + intercept
    y_str_true = latex(y_expr)
    
    # Chuỗi hiển thị phương trình gốc
    # Ví dụ 3x - 2y = 6
    lhs_str = latex(pt_expr)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho phương trình bậc nhất hai ẩn $%s = %s$.''' % (lhs_str, c_val))
    
    ############################################################################# Nhận biết #################################################
    # a) Cặp số (x_ox; 0) là một nghiệm của phương trình.
    # Đúng: (x_ox, 0)
    # Sai: (x_ox + 1, 0) hoặc đảo thành (0, x_ox)
    nb_da_1_d = '\\True Cặp số $(%s; 0)$ là một nghiệm của phương trình' % (x_ox)
    nb_da_1_s = 'Cặp số $(%s; 0)$ là một nghiệm của phương trình' % (x_ox + 1)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Thay $x = %s$ và $y = 0$ vào vế trái phương trình, ta được: $%s \\cdot (%s) + (%s) \\cdot 0 = %s = VP$. \\\\ Do đó, cặp số $(%s; 0)$ là một nghiệm của phương trình.''' % (x_ox, a_val, x_ox, b_val, a_val * x_ox, x_ox))
    
    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################# Thông hiểu #################################################
    # b) Cặp số (0; y_wrong) là một nghiệm của phương trình.
    # Trong ảnh gốc: Cặp số (0; 3) là một nghiệm của phương trình (Sai vì nghiệm đúng là (0; -3))
    # Đúng: (0, y_oy)
    # Sai: (0, -y_oy)
    th_da_1_d = '\\True Cặp số $(0; %s)$ là một nghiệm của phương trình' % (y_oy)
    th_da_1_s = 'Cặp số $(0; %s)$ là một nghiệm của phương trình' % (-y_oy if y_oy != 0 else 1)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Thay $x = 0$ vào phương trình ta được: $%s \\cdot 0 + (%s)y = %s \\Leftrightarrow %sy = %s \\Leftrightarrow y = %s$. \\\\ Do đó cặp số $(0; %s)$ là nghiệm của phương trình, còn $(0; %s)$ không phải là nghiệm.''' % (a_val, b_val, c_val, b_val, c_val, y_oy, y_oy, -y_oy if y_oy != 0 else 1))
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################# Vận dụng #################################################
    # c) Phương trình có nghiệm tổng quát là (x; mx + n) với x \in \mathbb{R} tuỳ ý.
    # Đúng: y = slope*x + intercept
    # Sai: đổi dấu hệ số góc hoặc sai hệ số tự do
    slope_wrong = -slope
    y_expr_wrong = slope_wrong * x + intercept
    
    vd_da_1_d = '\\True Phương trình có nghiệm tổng quát là $(x; %s)$ với $x \\in \\mathbb{R}$ tuỳ ý' % (y_str_true)
    vd_da_1_s = 'Phương trình có nghiệm tổng quát là $(x; %s)$ với $x \\in \\mathbb{R}$ tuỳ ý' % (latex(y_expr_wrong))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Ta có: $%s = %s \\Leftrightarrow %sy = %s - %sx \\Leftrightarrow y = %s$. \\\\ Vậy nghiệm tổng quát của phương trình là $(x; %s)$ với $x \\in \\mathbb{R}$ tuỳ ý.''' % (lhs_str, c_val, b_val, c_val, a_val, y_str_true, y_str_true))
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################# Vận dụng cao #################################################
    # d) Đường thẳng biểu diễn tập nghiệm của phương trình cắt trục tung tại điểm (0; y_oy).
    # Đúng: (0; y_oy)
    # Sai: (y_oy; 0) hoặc (0; -y_oy)
    vdc_da_1_d = '\\True Đường thẳng biểu diễn tập nghiệm của phương trình cắt trục tung tại điểm $(0; %s)$' % (y_oy)
    vdc_da_1_s = 'Đường thẳng biểu diễn tập nghiệm của phương trình cắt trục tung tại điểm $(%s; 0)$' % (y_oy)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Giao điểm của đường thẳng biểu diễn tập nghiệm với trục tung có hoành độ $x = 0$. \\\\ Thay $x = 0$ vào phương trình $%s = %s$, ta được $y = %s$. \\\\ Vậy đường thẳng cắt trục tung tại điểm $(0; %s)$.''' % (lhs_str, c_val, y_oy, y_oy))
    
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
