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


def bt_dang4_p1_b1_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Tạo ngẫu nhiên hệ số a, b của phương trình ax + by = c
        a = random.choice([2, 3, 4, 5])
        b = random.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    
        # Chọn nghiệm đúng (x0, y0)
        x0 = random.randint(-5, 6)
        y0 = random.randint(-5, 6)
        c = a * x0 + b * y0
    
        # Thiết lập chuỗi phương trình ax + by = c
        dau_b = '+' if b > 0 else '-'
        abs_b = abs(b)
        str_b = 'y' if abs_b == 1 else '%sy' % abs_b
        if a == 1:
            str_a = 'x'
        elif a == -1:
            str_a = '-x'
        else:
            str_a = '%sx' % a
        pt = '%s %s %s = %s' % (str_a, dau_b, str_b, c)
    
        # Đáp án đúng
        da_dung = '$(%s;\\, %s)$' % (x0, y0)
    
        # Sinh các cặp số sai (nhiễu)
        cac_cap_sai = []
        # Ứng viên 1: Đổi vị trí x, y nếu không bằng c
        if a * y0 + b * x0 != c and (y0, x0) != (x0, y0):
            cac_cap_sai.append((y0, x0))
        # Ứng viên 2: Đổi dấu
        if a * (-x0) + b * y0 != c:
            cac_cap_sai.append((-x0, y0))
        if a * x0 + b * (-y0) != c:
            cac_cap_sai.append((x0, -y0))
        if a * (-x0) + b * (-y0) != c:
            cac_cap_sai.append((-x0, -y0))
    
        # Bổ sung các cặp ngẫu nhiên khác
        for dx in [-2, -1, 1, 2, 3]:
            for dy in [-2, -1, 1, 2, 3]:
                xi = x0 + dx
                yi = y0 + dy
                if a * xi + b * yi != c:
                    cac_cap_sai.append((xi, yi))
    
        # Loại bỏ trùng lặp
        cac_cap_sai = list(dict.fromkeys(cac_cap_sai))
        random.shuffle(cac_cap_sai)
    
        # Lấy 3 cặp sai
        s1_pair = cac_cap_sai[0]
        s2_pair = cac_cap_sai[1]
        s3_pair = cac_cap_sai[2]
    
        du = [da_dung]
        da = random.choice(du)
    
        s = [
            '$(%s;\\, %s)$' % (s1_pair[0], s1_pair[1]),
            '$(%s;\\, %s)$' % (s2_pair[0], s2_pair[1]),
            '$(%s;\\, %s)$' % (s3_pair[0], s3_pair[1])
        ]
    
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
    
        # Câu hỏi
        noidungcauhoi = ('''Cặp số nào sau đây là một nghiệm của phương trình $%s$?''' % pt)
    
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Tính toán từng trường hợp để viết lời giải chi tiết
        def bieu_thuc_vt(u, v):
            # Tính chuỗi biểu thức thế vào vế trái
            str_u = '%s' % u if u >= 0 else '(%s)' % u
            str_v = '%s' % v if v >= 0 else '(%s)' % v
            return '%s \\cdot %s %s %s \\cdot %s' % (a, str_u, dau_b, abs_b, str_v)
    
        vt_dung = a * x0 + b * y0
        vt_s1 = a * s1_pair[0] + b * s1_pair[1]
        vt_s2 = a * s2_pair[0] + b * s2_pair[1]
        vt_s3 = a * s3_pair[0] + b * s3_pair[1]
    
        # Nội dung lời giải
        loigiai = ('''Thay lần lượt các cặp số $(x; y)$ vào vế trái của phương trình $%s$, ta có:\\\\
    - Với cặp số $(%s;\\, %s)$: $VT = %s = %s = %s = VP$, do đó $(%s;\\, %s)$ là một nghiệm của phương trình.\\\\
    - Với cặp số $(%s;\\, %s)$: $VT = %s = %s \\neq %s = VP$, do đó $(%s;\\, %s)$ không là nghiệm.\\\\
    - Với cặp số $(%s;\\, %s)$: $VT = %s = %s \\neq %s = VP$, do đó $(%s;\\, %s)$ không là nghiệm.\\\\
    - Với cặp số $(%s;\\, %s)$: $VT = %s = %s \\neq %s = VP$, do đó $(%s;\\, %s)$ không là nghiệm.'''
                   % (pt,
                      x0, y0, bieu_thuc_vt(x0, y0), vt_dung, c, x0, y0,
                      s1_pair[0], s1_pair[1], bieu_thuc_vt(s1_pair[0], s1_pair[1]), vt_s1, c, s1_pair[0], s1_pair[1],
                      s2_pair[0], s2_pair[1], bieu_thuc_vt(s2_pair[0], s2_pair[1]), vt_s2, c, s2_pair[0], s2_pair[1],
                      s3_pair[0], s3_pair[1], bieu_thuc_vt(s3_pair[0], s3_pair[1]), vt_s3, c, s3_pair[0], s3_pair[1]))
    
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
