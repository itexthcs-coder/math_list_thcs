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


def bt_dang14_p1_b1_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Hàm tạo một phương trình bậc nhất hai ẩn ax + by = c
        def tao_pt(a_val, b_val, c_val):
            if a_val == 1:
                str_a = 'x'
            elif a_val == -1:
                str_a = '-x'
            elif a_val == 0:
                str_a = '0x'
            else:
                str_a = '%sx' % a_val
    
            abs_b = abs(b_val)
            str_b = 'y' if abs_b == 1 else '%sy' % abs_b
            dau_b = '+' if b_val >= 0 else '-'
            if a_val == 0:
                if b_val == 1:
                    return '0x + y = %s' % c_val
                elif b_val == -1:
                    return '0x - y = %s' % c_val
                else:
                    return '0x %s %s = %s' % (dau_b, str_b, c_val)
    
            return '%s %s %s = %s' % (str_a, dau_b, str_b, c_val)
    
        # 1. Hệ KHÔNG phải là hệ hai phương trình bậc nhất hai ẩn (chứa phương trình 0x + 0y = c)
        c_sai1 = random.choice([3, 4, 5, 6, 7])
        c_sai2 = random.choice([1, 2, 3, 5])
        pt_k1 = 'x + y = %s' % c_sai1
        pt_k2 = '0x + 0y = %s' % c_sai2
        he_khong_phai = '\\{ %s;\\, %s \\}' % (pt_k1, pt_k2)
    
        # 2. Các hệ đúng (là hệ hai phương trình bậc nhất hai ẩn):
        # Hệ 1: dạng ax + by = c; dx + ey = f thông thường
        a1, b1, c1 = 3, -1, 2
        a2, b2, c2 = 1, 2, 7
        c1 = random.choice([2, 3, 4, 5])
        c2 = random.choice([5, 6, 7, 8])
        he_dung1 = '\\{ %s;\\, %s \\}' % (tao_pt(a1, b1, c1), tao_pt(a2, b2, c2))
    
        # Hệ 2: các hệ số nguyên nhỏ
        a3, b3 = random.choice([(2, 1), (3, 1), (1, 2)])
        a4, b4 = random.choice([(1, -1), (2, -1), (1, -2)])
        c3 = random.choice([0, 1, 2, 3])
        c4 = random.choice([3, 4, 5, 6])
        he_dung2 = '\\{ %s;\\, %s \\}' % (tao_pt(a3, b3, c3), tao_pt(a4, b4, c4))
    
        # Hệ 3: dạng đặc biệt có chứa hệ số 0 ở mỗi phương trình: {0x + y = m; x + 0y = n}
        m_val = random.choice([-3, -2, -1, 1, 2, 3])
        n_val = random.choice([-3, -2, -1, 1, 2, 3])
        he_dung3 = '\\{ 0x + y = %s;\\, x + 0y = %s \\}' % (m_val, n_val)
    
        # Các đáp án trắc nghiệm
        du = ['$%s$' % he_khong_phai]
        da = random.choice(du)
    
        s = [
            '$%s$' % he_dung1,
            '$%s$' % he_dung2,
            '$%s$' % he_dung3
        ]
    
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
    
        # Câu hỏi
        noidungcauhoi = ('''Hệ phương trình nào sau đây KHÔNG phải là hệ hai phương trình bậc nhất hai ẩn?''')
    
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Nội dung lời giải
        loigiai = ('''Hệ hai phương trình bậc nhất hai ẩn $x$ và $y$ là hệ gồm hai phương trình bậc nhất hai ẩn.\\\\
    Trong đó, phương trình bậc nhất hai ẩn có dạng $ax + by = c$ với $a^2 + b^2 \\neq 0$ (nghĩa là $a$ và $b$ không đồng thời bằng $0$).\\\\
    - Hệ $%s$ chứa phương trình $%s$ có cả hai hệ số $a = 0$ và $b = 0$ ($a^2 + b^2 = 0$) nên không phải là phương trình bậc nhất hai ẩn. Do đó hệ này không phải là hệ hai phương trình bậc nhất hai ẩn.\\\\
    - Các hệ $%s$, $%s$ và $%s$ đều gồm hai phương trình bậc nhất hai ẩn nên là hệ hai phương trình bậc nhất hai ẩn.'''
                   % (he_khong_phai, pt_k2, he_dung1, he_dung2, he_dung3))
    
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
