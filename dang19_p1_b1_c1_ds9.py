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


def bt_dang19_p1_b1_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Random hệ số a1, b1, c1 cho d1: a1*x + b1*y = c1
        a1 = random.choice([1, 2, 3])
        b1 = random.choice([1, 2, 3, -1, -2, -3])
        c1 = random.choice([1, 2, 3, 4, 5])
    
        # Chọn tỉ số nhân k (k != 0, k != 1) để d1 song song d2
        k = random.choice([2, 3, -2, -3])
        a2 = k * a1
        b2 = k * b1
        # c2 != k * c1 để hai đường thẳng song song (không trùng nhau)
        sai_lech = random.choice([1, -1, 2, -2, 3])
        c2 = k * c1 + sai_lech
    
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
    
        pt_d1 = '%s = %s' % (format_vt(a1, b1), c1)
        pt_d2 = '%s = %s' % (format_vt(a2, b2), c2)
    
        # Đáp án đúng
        da_dung = 'Song song với nhau'
    
        # Các đáp án gây nhiễu
        s1 = 'Trùng nhau'
        s2 = 'Cắt nhau tại một điểm duy nhất'
        s3 = 'Vuông góc với nhau'
    
        du = [da_dung]
        da = random.choice(du)
    
        s = [s1, s2, s3]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
    
        # Câu hỏi
        noidungcauhoi = ('''Đồ thị hai đường thẳng $d_1: %s$ và $d_2: %s$ có vị trí tương đối là:''' % (pt_d1, pt_d2))
    
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Viết tỉ số phân số hiển thị
        phan_so_a = '\\frac{%s}{%s}' % (a1, a2)
        phan_so_b = '\\frac{%s}{%s}' % (b1, b2)
        phan_so_c = '\\frac{%s}{%s}' % (c1, c2)
    
        # Nội dung lời giải
        loigiai = ('''Xét hai đường thẳng $d_1: %s$ và $d_2: %s$.\\\\
    Ta có các tỉ số:\\\\
    $%s = %s$ và $%s \\neq %s$, suy ra $%s = %s \\neq %s$.\\\\
    Do đó, hai đường thẳng $d_1$ và $d_2$ song song với nhau ($d_1 // d_2$).'''
                   % (pt_d1, pt_d2,
                      phan_so_a, phan_so_b, phan_so_a, phan_so_c,
                      phan_so_a, phan_so_b, phan_so_c))
    
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
