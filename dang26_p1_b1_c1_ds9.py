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


def bt_dang26_p1_b1_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Random toạ độ giao điểm với trục hoành x0 và giao điểm với trục tung y0 (khác 0)
        x0 = random.choice([2, 3, 4, 5, -2, -3, -4, -5])
        y0 = random.choice([2, 3, 4, 5, -2, -3, -4, -5])
    
        # Thiết lập phương trình đường thẳng qua (x0; 0) và (0; y0): y0*x + x0*y = x0*y0
        a = y0
        b = x0
        c = x0 * y0
    
        # Rút gọn hệ số nếu có ước chung lớn nhất
        ucln = math.gcd(math.gcd(abs(a), abs(b)), abs(c))
        a = a // ucln
        b = b // ucln
        c = c // ucln
    
        # Đảm bảo hệ số a dương
        if a < 0:
            a = -a
            b = -b
            c = -c
    
        # Định dạng chuỗi phương trình ax + by = c
        dau_b = '+' if b > 0 else '-'
        abs_b = abs(b)
        str_b = 'y' if abs_b == 1 else '%sy' % abs_b
        if a == 1:
            str_a = 'x'
        elif a == -1:
            str_a = '-x'
        else:
            str_a = '%sx' % a
        pt_d = '%s %s %s = %s' % (str_a, dau_b, str_b, c)
    
        # Đáp án đúng: giao điểm với trục hoành Ox là (x0; 0)
        da_dung = '$(%s;\\, 0)$' % x0
    
        # Các đáp án gây nhiễu
        s1 = '$(0;\\, %s)$' % y0        # Giao điểm với trục tung Oy
        s2 = '$(%s;\\, 0)$' % (-x0)      # Sai dấu hoành độ giao điểm
        s3 = '$(0;\\, %s)$' % (-y0)      # Sai dấu tung độ giao điểm
    
        tap_sai = list(set([s1, s2, s3]) - {da_dung})
        while len(tap_sai) < 3:
            tap_sai.append('$(0;\\, %s)$' % x0)
            tap_sai = list(set(tap_sai) - {da_dung})
    
        random.shuffle(tap_sai)
    
        du = [da_dung]
        da = random.choice(du)
    
        das1 = tap_sai[0]
        das2 = tap_sai[1]
        das3 = tap_sai[2]
    
        # Câu hỏi
        noidungcauhoi = ('''Giao điểm của đường thẳng $d: %s$ với trục hoành $Ox$ có toạ độ là:''' % pt_d)
    
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Nội dung lời giải
        loigiai = ('''Giao điểm của đường thẳng $d$ với trục hoành $Ox$ có tung độ $y = 0$.\\\\
    Thay $y = 0$ vào phương trình đường thẳng $d: %s$, ta được:\\\\
    $%s %s %s \\cdot 0 = %s$\\\\
    $\\Leftrightarrow %s = %s \\Leftrightarrow x = %s$.\\\\
    Vậy toạ độ giao điểm của đường thẳng $d$ với trục hoành $Ox$ là $(%s;\\, 0)$.'''
                   % (pt_d,
                      str_a, dau_b, abs_b, c,
                      str_a, c, x0,
                      x0))
    
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
