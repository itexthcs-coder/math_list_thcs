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


def bt_dang5_p1_b1_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Tạo ngẫu nhiên cặp số (x0; y0)
        x0 = random.choice([i for i in range(-5, 6) if i != 0])
        y0 = random.choice([i for i in range(-5, 6) if i != 0])
    
        # Hàm định dạng vế trái của phương trình ax + by
        def format_vt(a_val, b_val):
            if a_val == 1:
                str_a = 'x'
            elif a_val == -1:
                str_a = '-x'
            else:
                str_a = '%sx' % a_val
    
            dau_b = '+' if b_val > 0 else '-'
            abs_b = abs(b_val)
            str_b = 'y' if abs_b == 1 else '%sy' % abs_b
            return '%s %s %s' % (str_a, dau_b, str_b)
    
        # Hàm tính chuỗi thay thế từng bước vào vế trái
        def format_the_so(a_val, b_val, u, v):
            str_u = '%s' % u if u >= 0 else '(%s)' % u
            str_v = '%s' % v if v >= 0 else '(%s)' % v
            dau_b = '+' if b_val > 0 else '-'
            abs_b = abs(b_val)
            return '%s \\cdot %s %s %s \\cdot %s' % (a_val, str_u, dau_b, abs_b, str_v)
    
        # Tạo 3 phương trình nhận (x0, y0) là nghiệm (3 phương án sai của bài toán)
        ds_he_so = [
            (3, 1),
            (1, -2),
            (2, 3),
            (1, 1),
            (2, -1),
            (-1, 2),
            (3, -2),
            (1, 3)
        ]
        random.shuffle(ds_he_so)
    
        # Chọn 3 cặp hệ số (a, b) cho các phương trình nhận (x0, y0) là nghiệm
        a_dung1, b_dung1 = ds_he_so[0]
        c_dung1 = a_dung1 * x0 + b_dung1 * y0
        pt_nhan1 = '%s = %s' % (format_vt(a_dung1, b_dung1), c_dung1)
    
        a_dung2, b_dung2 = ds_he_so[1]
        c_dung2 = a_dung2 * x0 + b_dung2 * y0
        pt_nhan2 = '%s = %s' % (format_vt(a_dung2, b_dung2), c_dung2)
    
        a_dung3, b_dung3 = ds_he_so[2]
        c_dung3 = a_dung3 * x0 + b_dung3 * y0
        pt_nhan3 = '%s = %s' % (format_vt(a_dung3, b_dung3), c_dung3)
    
        # Tạo 1 phương trình KHÔNG nhận (x0, y0) là nghiệm (Đáp án đúng của câu hỏi)
        a_sai, b_sai = ds_he_so[3]
        vt_sai = a_sai * x0 + b_sai * y0
        # Chọn c_sai khác vt_sai
        sai_lech = random.choice([-3, -2, -1, 1, 2, 3])
        c_sai = vt_sai + sai_lech
        pt_khong_nhan = '%s = %s' % (format_vt(a_sai, b_sai), c_sai)
    
        # Đáp án đúng của câu trắc nghiệm
        du = ['$%s$' % pt_khong_nhan]
        da = random.choice(du)
    
        # Các đáp án nhiễu
        s = [
            '$%s$' % pt_nhan1,
            '$%s$' % pt_nhan2,
            '$%s$' % pt_nhan3
        ]
    
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
    
        # Câu hỏi
        noidungcauhoi = ('''Cặp số $(%s;\\, %s)$ KHÔNG là nghiệm của phương trình nào sau đây?''' % (x0, y0))
    
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Nội dung lời giải
        loigiai = ('''Thay $x = %s$ và $y = %s$ vào từng phương trình:\\\\
    - Với phương trình $%s$: $VT = %s = %s = %s = VP$, nên $(%s;\\, %s)$ là nghiệm của phương trình.\\\\
    - Với phương trình $%s$: $VT = %s = %s = %s = VP$, nên $(%s;\\, %s)$ là nghiệm của phương trình.\\\\
    - Với phương trình $%s$: $VT = %s = %s = %s = VP$, nên $(%s;\\, %s)$ là nghiệm của phương trình.\\\\
    - Với phương trình $%s$: $VT = %s = %s = %s \\neq %s = VP$, nên $(%s;\\, %s)$ không là nghiệm của phương trình.\\\\
    Vậy cặp số $(%s;\\, %s)$ không là nghiệm của phương trình $%s$.'''
                   % (x0, y0,
                      pt_nhan1, format_the_so(a_dung1, b_dung1, x0, y0), c_dung1, c_dung1, x0, y0,
                      pt_nhan2, format_the_so(a_dung2, b_dung2, x0, y0), c_dung2, c_dung2, x0, y0,
                      pt_nhan3, format_the_so(a_dung3, b_dung3, x0, y0), c_dung3, c_dung3, x0, y0,
                      pt_khong_nhan, format_the_so(a_sai, b_sai, x0, y0), vt_sai, vt_sai, c_sai, x0, y0,
                      x0, y0, pt_khong_nhan))
    
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
