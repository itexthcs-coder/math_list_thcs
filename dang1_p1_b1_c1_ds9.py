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


def bt_dang1_p1_b1_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Tạo phương trình bậc nhất 2 ẩn dạng đúng: ax + by = c (a khác 0 hoặc b khác 0)
        a1 = random.choice([i for i in range(-9, 10) if i != 0])
        b1 = random.choice([i for i in range(-9, 10) if i != 0])
        c1 = random.choice([i for i in range(-15, 16) if i != 0])
    
        dau_b = '+' if b1 > 0 else '-'
        abs_b1 = abs(b1)
        str_b1 = 'y' if abs_b1 == 1 else '%sy' % abs_b1
        if a1 == 1:
            str_a1 = 'x'
        elif a1 == -1:
            str_a1 = '-x'
        else:
            str_a1 = '%sx' % a1
        pt_dung = '%s %s %s = %s' % (str_a1, dau_b, str_b1, c1)
    
        # Các phương án nhiễu (sai)
        # Loại 1: Bậc 2 ở x hoặc y (ví dụ: 2x^2 + 3y = 5)
        a2 = random.choice([2, 3, 4, 5])
        b2 = random.choice([2, 3, 5, 7])
        c2 = random.choice([3, 5, 7, 9])
        pt_sai1 = '%sx^2 + %sy = %s' % (a2, b2, c2)
    
        # Loại 2: Cả 2 hệ số a = 0 và b = 0 (0x + 0y = c với c khác 0)
        c3 = random.choice([2, 3, 4, 5, 6, 7])
        pt_sai2 = '0x + 0y = %s' % c3
    
        # Loại 3: Phương trình bậc nhất 3 ẩn x, y, z (x + y - z = 0 hoặc tương tự)
        pt_sai3 = 'x + y - z = 0'
    
        # Các đáp án trắc nghiệm
        du = ['$%s$' % pt_dung]
        da = random.choice(du)
    
        s = [
            '$%s$' % pt_sai1,
            '$%s$' % pt_sai2,
            '$%s$' % pt_sai3
        ]
    
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
    
        # Câu hỏi
        noidungcauhoi = ('''Trong các hệ thức sau, hệ thức nào là phương trình bậc nhất hai ẩn $x$ và $y$?''')
    
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Nội dung lời giải
        loigiai = ('''Phương trình bậc nhất hai ẩn $x$ và $y$ là hệ thức dạng $ax + by = c$, trong đó $a, b, c$ là các số đã biết ($a \\neq 0$ hoặc $b \\neq 0$).\\\\
    - Hệ thức $%s$ có dạng $ax + by = c$ với $a = %s \\neq 0$ và $b = %s \\neq 0$ nên là phương trình bậc nhất hai ẩn $x$ và $y$.\\\\
    - Hệ thức $%s$ chứa $x^2$ nên không là phương trình bậc nhất hai ẩn.\\\\
    - Hệ thức $%s$ có hệ số của cả $x$ và $y$ đều bằng $0$ ($a = 0, b = 0$) nên không là phương trình bậc nhất hai ẩn.\\\\
    - Hệ thức $%s$ chứa ba ẩn $x, y, z$ nên không là phương trình bậc nhất hai ẩn $x$ và $y$.'''
                   % (pt_dung, a1, b1, pt_sai1, pt_sai2, pt_sai3))
    
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
