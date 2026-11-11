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


def bt_dang14_p2_b1_c1_ds9(self):
    # Khai báo biến
    x, y = symbols('x y')
    
    # Hàm phụ trợ format số thập phân dùng dấu phẩy
    def format_dec(val):
        val_float = float(val)
        if val_float.is_integer():
            return str(int(val_float))
        return str(round(val_float, 2)).replace('.', ',')
    
    # Bộ ba số Pythagore (u, v, w) với u^2 + v^2 = w^2 để AB luôn nguyên đẹp
    pythagorean_triples = [
        (4, 3, 5),
        (3, 4, 5),
        (8, 6, 10),
        (6, 8, 10),
        (12, 5, 13),
        (5, 12, 13)
    ]
    
    # Random bộ ba số
    u_val, v_val, w_val = random.choice(pythagorean_triples)
    
    # Đường thẳng đi qua A(u_val; 0) và B(0; -v_val):
    # Phương trình đoạn chắn: x / u_val - y / v_val = 1 <=> v_val * x - u_val * y = u_val * v_val
    a_val = v_val
    b_val = u_val
    c_val = u_val * v_val
    
    # Toạ độ điểm A trên Ox: (u_val, 0)
    x_A = u_val
    # Toạ độ điểm B trên Oy: (0, -v_val)
    y_B = -v_val
    # Độ dài AB = w_val
    len_AB = w_val
    
    # Chọn điểm C(x_C; y_C) thuộc đường thẳng d
    # Lấy x_C = u_val / 2 => y_C = -v_val / 2
    x_C = Rational(u_val, 2)
    y_C = Rational(a_val * x_C - c_val, b_val)
    x_C_str = format_dec(x_C)
    y_C_str = format_dec(y_C)
    
    lhs_str = '%sx - %sy' % (a_val, b_val)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Xét đường thẳng $d$ biểu diễn tập nghiệm của phương trình $%s = %s$.''' % (lhs_str, c_val))
    
    ############################################################################# Nhận biết #################################################
    # a) Đường thẳng d đi qua điểm A(x_A; 0) trên trục Ox
    x_A_wrong = x_A + random.choice([1, -1])
    nb_da_1_d = '\\True Đường thẳng $d$ đi qua điểm $A(%s; 0)$ trên trục $Ox$' % (x_A)
    nb_da_1_s = 'Đường thẳng $d$ đi qua điểm $A(%s; 0)$ trên trục $Ox$' % (x_A_wrong)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Giao điểm của đường thẳng $d$ với trục hoành $Ox$ có tung độ $y = 0$. \\\\ Thay $y = 0$ vào phương trình $%s = %s$, ta được: \\\\ $%sx - %s \\cdot 0 = %s \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$. \\\\ Do đó, đường thẳng $d$ đi qua điểm $A(%s; 0)$ trên trục $Ox$.''' % (lhs_str, c_val, a_val, b_val, c_val, a_val, c_val, x_A, x_A))
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################# Thông hiểu #################################################
    # b) Đường thẳng d đi qua điểm B(0; y_B) trên trục Oy
    y_B_wrong = abs(y_B)
    th_da_1_d = '\\True Đường thẳng $d$ đi qua điểm $B(0; %s)$ trên trục $Oy$' % (y_B)
    th_da_1_s = 'Đường thẳng $d$ đi qua điểm $B(0; %s)$ trên trục $Oy$' % (y_B_wrong)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Giao điểm của đường thẳng $d$ với trục tung $Oy$ có hoành độ $x = 0$. \\\\ Thay $x = 0$ vào phương trình $%s = %s$, ta được: \\\\ $%s \\cdot 0 - %sy = %s \\Leftrightarrow -%sy = %s \\Leftrightarrow y = %s$. \\\\ Do đó, đường thẳng $d$ đi qua điểm $B(0; %s)$ trên trục $Oy$.''' % (lhs_str, c_val, a_val, b_val, c_val, b_val, c_val, y_B, y_B))
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################# Vận dụng #################################################
    # c) Độ dài đoạn thẳng AB nối hai giao điểm với các trục toạ độ bằng len_AB
    len_AB_wrong = len_AB + random.choice([1, 2])
    vd_da_1_d = '\\True Độ dài đoạn thẳng $AB$ nối hai giao điểm với các trục toạ độ bằng $%s$' % (len_AB)
    vd_da_1_s = 'Độ dài đoạn thẳng $AB$ nối hai giao điểm với các trục toạ độ bằng $%s$' % (len_AB_wrong)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Hai giao điểm của $d$ với các trục toạ độ là $A(%s; 0)$ và $B(0; %s)$. \\\\ Ta có $OA = |%s| = %s$ và $OB = |%s| = %s$. \\\\ Tam giác $OAB$ vuông tại $O$, áp dụng định lý Pythagore ta có: \\\\ $AB = \\sqrt{OA^2 + OB^2} = \\sqrt{%s^2 + (%s)^2} = \\sqrt{%s + %s} = \\sqrt{%s} = %s$. \\\\ Vậy độ dài đoạn thẳng $AB$ bằng $%s$.''' % (x_A, y_B, x_A, x_A, y_B, abs(y_B), x_A, y_B, x_A**2, y_B**2, x_A**2 + y_B**2, len_AB, len_AB))
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################# Vận dụng cao #################################################
    # d) Điểm C(x_C; y_C) thuộc đường thẳng d
    vdc_da_1_d = '\\True Điểm $C(%s; %s)$ thuộc đường thẳng $d$' % (x_C_str, y_C_str)
    vdc_da_1_s = 'Điểm $C(%s; %s)$ không thuộc đường thẳng $d$' % (x_C_str, y_C_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Thay toạ độ điểm $C(%s; %s)$ vào vế trái của phương trình đường thẳng $d$, ta được: \\\\ $%s \\cdot %s - %s \\cdot (%s) = %s - (%s) = %s = VP$. \\\\ Do đó, điểm $C(%s; %s)$ thuộc đường thẳng $d$.''' % (x_C_str, y_C_str, a_val, x_C_str, b_val, y_C_str, format_dec(a_val * x_C), format_dec(b_val * y_C), c_val, x_C_str, y_C_str))
    
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
