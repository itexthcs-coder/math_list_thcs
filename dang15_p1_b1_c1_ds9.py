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


def bt_dang15_p1_b1_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Tạo ngẫu nhiên nghiệm (x0, y0)
        x0 = random.choice([1, 2, 3, 4, -1, -2, -3])
        y0 = random.choice([1, 2, 3, 4, -1, -2, -3])
    
        # Hàm định dạng vế trái ax + by
        def format_vt(a_val, b_val):
            if a_val == 1:
                str_a = 'x'
            elif a_val == -1:
                str_a = '-x'
            else:
                str_a = '%sx' % a_val
    
            abs_b = abs(b_val)
            str_b = 'y' if abs_b == 1 else '%sy' % abs_b
            dau_b = '+' if b_val > 0 else '-'
            return '%s %s %s' % (str_a, dau_b, str_b)
    
        # Hàm viết chuỗi thay số
        def format_the_so(a_val, b_val, u, v):
            str_u = '%s' % u if u >= 0 else '(%s)' % u
            str_v = '%s' % v if v >= 0 else '(%s)' % v
            dau_b = '+' if b_val > 0 else '-'
            abs_b = abs(b_val)
            if a_val == 1:
                part_a = '%s' % str_u
            elif a_val == -1:
                part_a = '-(%s)' % str_u if u < 0 else '-%s' % str_u
            else:
                part_a = '%s \\cdot %s' % (a_val, str_u)
    
            if abs_b == 1:
                part_b = '%s' % str_v
            else:
                part_b = '%s \\cdot %s' % (abs_b, str_v)
            return '%s %s %s' % (part_a, dau_b, part_b)
    
        # Chọn các cặp hệ số (a, b) khác nhau
        tap_he_so = [
            (1, 1),
            (2, -1),
            (1, -1),
            (1, 2),
            (3, -1),
            (2, 1),
            (1, 3),
            (-1, 2)
        ]
        random.shuffle(tap_he_so)
    
        # Hệ 1: HỆ ĐÚNG (cả hai phương trình đều nhận (x0, y0) là nghiệm)
        a1, b1 = tap_he_so[0]
        c1 = a1 * x0 + b1 * y0
        a2, b2 = tap_he_so[1]
        c2 = a2 * x0 + b2 * y0
        pt1_dung = '%s = %s' % (format_vt(a1, b1), c1)
        pt2_dung = '%s = %s' % (format_vt(a2, b2), c2)
        he_dung = '\\{ %s;\\, %s \\}' % (pt1_dung, pt2_dung)
    
        # Hệ 2: Phương trình 1 đúng, phương trình 2 sai
        a3, b3 = tap_he_so[2]
        c3 = a3 * x0 + b3 * y0
        a4, b4 = tap_he_so[3]
        sai_lech1 = random.choice([-2, -1, 1, 2])
        c4 = a4 * x0 + b4 * y0 + sai_lech1
        pt1_sai1 = '%s = %s' % (format_vt(a3, b3), c3)
        pt2_sai1 = '%s = %s' % (format_vt(a4, b4), c4)
        he_sai1 = '\\{ %s;\\, %s \\}' % (pt1_sai1, pt2_sai1)
    
        # Hệ 3: Phương trình 1 sai, phương trình 2 đúng
        a5, b5 = tap_he_so[4]
        sai_lech2 = random.choice([-3, -2, 2, 3])
        c5 = a5 * x0 + b5 * y0 + sai_lech2
        a6, b6 = tap_he_so[5]
        c6 = a6 * x0 + b6 * y0
        pt1_sai2 = '%s = %s' % (format_vt(a5, b5), c5)
        pt2_sai2 = '%s = %s' % (format_vt(a6, b6), c6)
        he_sai2 = '\\{ %s;\\, %s \\}' % (pt1_sai2, pt2_sai2)
    
        # Hệ 4: Cả hai phương trình đều sai
        a7, b7 = tap_he_so[6]
        c7 = a7 * x0 + b7 * y0 + random.choice([-2, -1, 1, 2])
        a8, b8 = tap_he_so[7]
        c8 = a8 * x0 + b8 * y0 + random.choice([-2, -1, 1, 2])
        pt1_sai3 = '%s = %s' % (format_vt(a7, b7), c7)
        pt2_sai3 = '%s = %s' % (format_vt(a8, b8), c8)
        he_sai3 = '\\{ %s;\\, %s \\}' % (pt1_sai3, pt2_sai3)
    
        # Các đáp án trắc nghiệm
        du = ['$%s$' % he_dung]
        da = random.choice(du)
    
        s = [
            '$%s$' % he_sai1,
            '$%s$' % he_sai2,
            '$%s$' % he_sai3
        ]
    
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
    
        # Câu hỏi
        noidungcauhoi = ('''Cặp số $(%s;\\, %s)$ là nghiệm của hệ phương trình nào sau đây?''' % (x0, y0))
    
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Lời giải chi tiết
        loigiai = ('''Thay $x = %s$ và $y = %s$ vào từng hệ phương trình:\\\\
    - Xét hệ $%s$:\\\\
    Phương trình thứ nhất: $VT = %s = %s = VP$.\\\\
    Phương trình thứ hai: $VT = %s = %s = VP$.\\\\
    Do đó, cặp số $(%s;\\, %s)$ là nghiệm của cả hai phương trình nên là nghiệm của hệ $%s$.\\\\
    - Xét hệ $%s$:\\\\
    Phương trình thứ hai có $VT = %s = %s \\neq %s = VP$ nên cặp số $(%s;\\, %s)$ không là nghiệm của hệ.\\\\
    - Xét hệ $%s$:\\\\
    Phương trình thứ nhất có $VT = %s = %s \\neq %s = VP$ nên cặp số $(%s;\\, %s)$ không là nghiệm của hệ.\\\\
    - Xét hệ $%s$:\\\\
    Phương trình thứ nhất có $VT = %s = %s \\neq %s = VP$ nên cặp số $(%s;\\, %s)$ không là nghiệm của hệ.'''
                   % (x0, y0,
                      he_dung,
                      format_the_so(a1, b1, x0, y0), c1,
                      format_the_so(a2, b2, x0, y0), c2,
                      x0, y0, he_dung,
                      he_sai1,
                      format_the_so(a4, b4, x0, y0), a4 * x0 + b4 * y0, c4, x0, y0,
                      he_sai2,
                      format_the_so(a5, b5, x0, y0), a5 * x0 + b5 * y0, c5, x0, y0,
                      he_sai3,
                      format_the_so(a7, b7, x0, y0), a7 * x0 + b7 * y0, c7, x0, y0))
    
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
