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


def bt_dang13_p2_b1_c1_ds9(self):
    # Khai báo biến
    m, x, y = symbols('m x y')
    
    # Dạng bài: Cho hệ phương trình:
    # pt 1: x + y = m
    # pt 2: x - y = k_diff
    # Mẫu gốc: x + y = m; x - y = 2
    while True:
        k_diff = random.choice([2, 4, 6])
        # Chọn một giá trị m cụ thể (chẵn để nghiệm nguyên đẹp)
        m_val = k_diff + random.choice([2, 4])
        x_val = (m_val + k_diff) // 2
        y_val = (m_val - k_diff) // 2
        if x_val != y_val:
            break
    
    # Nội dung câu hỏi (hệ phương trình viết dạng ngoặc nhọn \begin{cases} ... \end{cases})
    noidungcauhoi = ('''Cho hệ phương trình $\\begin{cases} x + y = m \\\\ x - y = %s \\end{cases}$ với $m$ là tham số.''' % (k_diff))
    
    ############################################################################# Nhận biết #################################################
    # a) Hệ phương trình luôn có nghiệm duy nhất với mọi giá trị của m
    nb_da_1_d = '\\True Hệ phương trình luôn có nghiệm duy nhất với mọi giá trị của $m$'
    nb_da_1_s = 'Hệ phương trình vô nghiệm với mọi giá trị của $m$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Xét định thức của hệ phương trình: $D = 1 \\cdot (-1) - 1 \\cdot 1 = -2 \\ne 0$. \\\\ Vì $D \\ne 0$ không phụ thuộc vào tham số $m$ nên hệ phương trình luôn có nghiệm duy nhất với mọi giá trị của $m$.''')
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################# Thông hiểu #################################################
    # b) Nghiệm của hệ là x = (m + k_diff)/2; y = (m - k_diff)/2
    expr_x_str = '\\dfrac{m + %s}{2}' % (k_diff)
    expr_y_str = '\\dfrac{m - %s}{2}' % (k_diff)
    expr_x_wrong = '\\dfrac{m - %s}{2}' % (k_diff)
    expr_y_wrong = '\\dfrac{m + %s}{2}' % (k_diff)
    
    th_da_1_d = '\\True Nghiệm của hệ là $x = %s; y = %s$' % (expr_x_str, expr_y_str)
    th_da_1_s = 'Nghiệm của hệ là $x = %s; y = %s$' % (expr_x_wrong, expr_y_wrong)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Cộng từng vế hai phương trình của hệ, ta được: \\\\ $(x + y) + (x - y) = m + %s \\Leftrightarrow 2x = m + %s \\Leftrightarrow x = %s$. \\\\ Trừ từng vế hai phương trình của hệ, ta được: \\\\ $(x + y) - (x - y) = m - %s \\Leftrightarrow 2y = m - %s \\Leftrightarrow y = %s$. \\\\ Vậy nghiệm của hệ là $x = %s; y = %s$.''' % (k_diff, k_diff, expr_x_str, k_diff, k_diff, expr_y_str, expr_x_str, expr_y_str))
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################# Vận dụng #################################################
    # c) Để nghiệm của hệ thoả mãn x > 0 và y > 0 thì điều kiện là m > k_diff
    vd_da_1_d = '\\True Để nghiệm của hệ thoả mãn $x > 0$ và $y > 0$ thì điều kiện là $m > %s$' % (k_diff)
    vd_da_1_s = 'Để nghiệm của hệ thoả mãn $x > 0$ và $y > 0$ thì điều kiện là $m > -%s$' % (k_diff)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Để nghiệm thoả mãn $x > 0$ và $y > 0$, ta có hệ điều kiện: \\\\ $\\begin{cases} %s > 0 \\\\ %s > 0 \\end{cases} \\Leftrightarrow \\begin{cases} m + %s > 0 \\\\ m - %s > 0 \\end{cases} \\Leftrightarrow \\begin{cases} m > -%s \\\\ m > %s \\end{cases} \\Leftrightarrow m > %s$. \\\\ Vậy điều kiện cần tìm là $m > %s$.''' % (expr_x_str, expr_y_str, k_diff, k_diff, k_diff, k_diff, k_diff, k_diff))
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################# Vận dụng cao #################################################
    # d) Khi m = m_val, nghiệm của hệ là (x_val; y_val)
    vdc_da_1_d = '\\True Khi $m = %s$, nghiệm của hệ là $(%s; %s)$' % (m_val, x_val, y_val)
    vdc_da_1_s = 'Khi $m = %s$, nghiệm của hệ là $(%s; %s)$' % (m_val, y_val, x_val)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Thay $m = %s$ vào công thức nghiệm của hệ, ta được: \\\\ $x = \\dfrac{%s + %s}{2} = \\dfrac{%s}{2} = %s$, \\\\ $y = \\dfrac{%s - %s}{2} = \\dfrac{%s}{2} = %s$. \\\\ Vậy khi $m = %s$, nghiệm của hệ phương trình là $(%s; %s)$.''' % (m_val, m_val, k_diff, m_val + k_diff, x_val, m_val, k_diff, m_val - k_diff, y_val, m_val, x_val, y_val))
    
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
