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


def bt_dang27_p1_b1_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
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
    
        # 1. HỆ ĐÚNG: Có nghiệm duy nhất (a1*b2 - a2*b1 != 0)
        # Ví dụ: x - y = c1_dung; x + y = c2_dung
        c1_dung = random.choice([0, 1, 2, 3])
        c2_dung = random.choice([4, 5, 6, 8])
        pt1_dung = 'x - y = %s' % c1_dung
        pt2_dung = 'x + y = %s' % c2_dung
        he_dung = '\\begin{cases} %s \\\\ %s \\end{cases}' % (pt1_dung, pt2_dung)
    
        # 2. HỆ SAI 1: Vô nghiệm (hai vế trái giống hệt nhau, vế phải khác nhau: x + y = c1_s1; x + y = c2_s1)
        c1_s1 = random.choice([1, 2, 3])
        c2_s1 = c1_s1 + random.choice([1, 2, 3])
        pt1_s1 = 'x + y = %s' % c1_s1
        pt2_s1 = 'x + y = %s' % c2_s1
        he_sai1 = '\\begin{cases} %s \\\\ %s \\end{cases}' % (pt1_s1, pt2_s1)
    
        # 3. HỆ SAI 2: Vô số nghiệm (tỉ số các hệ số bằng nhau: a1*x - y = c1_s2; 2*a1*x - 2*y = 2*c1_s2)
        a_s2 = random.choice([2, 3])
        c1_s2 = random.choice([2, 3, 4])
        pt1_s2 = '%sx - y = %s' % (a_s2, c1_s2)
        pt2_s2 = '%sx - 2y = %s' % (2 * a_s2, 2 * c1_s2)
        he_sai2 = '\\begin{cases} %s \\\\ %s \\end{cases}' % (pt1_s2, pt2_s2)
    
        # 4. HỆ SAI 3: Vô nghiệm (song song với nhau: a3*x + b3*y = c1_s3; a3*x + b3*y = c2_s3)
        a_s3 = random.choice([2, 3])
        b_s3 = random.choice([2, 3])
        c1_s3 = random.choice([1, 2])
        c2_s3 = random.choice([5, 7])
        vt_s3 = format_vt(a_s3, b_s3)
        pt1_s3 = '%s = %s' % (vt_s3, c1_s3)
        pt2_s3 = '%s = %s' % (vt_s3, c2_s3)
        he_sai3 = '\\begin{cases} %s \\\\ %s \\end{cases}' % (pt1_s3, pt2_s3)
    
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
        noidungcauhoi = ('''Hệ phương trình nào sau đây có nghiệm duy nhất?''')
    
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Nội dung lời giải
        loigiai = ('''Hệ phương trình bậc nhất hai ẩn $\\begin{cases} a_1x + b_1y = c_1 \\\\ a_2x + b_2y = c_2 \\end{cases}$ có nghiệm duy nhất khi và chỉ khi hai đường thẳng biểu diễn tập nghiệm của hai phương trình cắt nhau, tức là $\\frac{a_1}{a_2} \\neq \\frac{b_1}{b_2}$.\\\\
    - Xét hệ $%s$: Ta có $\\frac{1}{1} \\neq \\frac{-1}{1}$ (vì $1 \\neq -1$) nên hệ phương trình có nghiệm duy nhất.\\\\
    - Xét hệ $%s$: Ta có $\\frac{1}{1} = \\frac{1}{1} \\neq \\frac{%s}{%s}$ nên hệ vô nghiệm.\\\\
    - Xét hệ $%s$: Ta có $\\frac{%s}{%s} = \\frac{-1}{-2} = \\frac{%s}{%s} = \\frac{1}{2}$ nên hệ có vô số nghiệm.\\\\
    - Xét hệ $%s$: Ta có $\\frac{%s}{%s} = \\frac{%s}{%s} = 1 \\neq \\frac{%s}{%s}$ nên hệ vô nghiệm.\\\\
    Vậy hệ phương trình có nghiệm duy nhất là $%s$.'''
                   % (he_dung,
                      he_sai1, c1_s1, c2_s1,
                      he_sai2, a_s2, 2 * a_s2, c1_s2, 2 * c1_s2,
                      he_sai3, a_s3, a_s3, b_s3, b_s3, c1_s3, c2_s3,
                      he_dung))
    
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
