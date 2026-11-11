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


def bt_dang22_p1_b1_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Random giá trị hằng số k trong (m - k) hoặc (m + k)
        k = random.choice([1, 2, 3, 4, 5])
        dau_k = random.choice(['-', '+'])
        
        # Random hệ số b khác 0 và hệ số c
        b = random.choice([2, 3, 4, 5, -2, -3, -4, -5])
        c = random.choice([i for i in range(-9, 10) if i != 0])
        
        # Định dạng vế trái: (m - k)x + by hoặc (m + k)x + by
        dau_b = '+' if b > 0 else '-'
        abs_b = abs(b)
        str_b = 'y' if abs_b == 1 else '%sy' % abs_b
        pt = '(m %s %s)x %s %s = %s' % (dau_k, k, dau_b, str_b, c)
    
        # Nghiệm m_val khiến hệ số của x bằng 0
        m_val = k if dau_k == '-' else -k
    
        # Do hệ số b khác 0 nên với mọi m, phương trình luôn có ít nhất một hệ số khác 0 (b khác 0)
        # Vì vậy phương trình luôn là phương trình bậc nhất hai ẩn với mọi m thuộc R
        da_dung = 'Với mọi $m \\in \\mathbb{R}$'
    
        # Các đáp án gây nhiễu
        s1 = '$m \\neq %s$' % m_val
        s2 = '$m = %s$' % m_val
        s3 = '$m \\neq 0$'
    
        du = [da_dung]
        da = random.choice(du)
    
        s = [s1, s2, s3]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
    
        # Câu hỏi
        noidungcauhoi = ('''Tìm điều kiện của tham số $m$ để phương trình $%s$ là phương trình bậc nhất hai ẩn:''' % pt)
    
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Nội dung lời giải
        loigiai = ('''Phương trình dạng $Ax + By = C$ là phương trình bậc nhất hai ẩn khi và chỉ khi $A$ và $B$ không đồng thời bằng $0$ ($A^2 + B^2 \\neq 0$).\\\\
    Xét phương trình $%s$, ta có:\\\\
    Hệ số của $x$ là $A = m %s %s$.\\\\
    Hệ số của $y$ là $B = %s \\neq 0$.\\\\
    Vì hệ số $B = %s \\neq 0$ luôn thoả mãn với mọi $m \\in \\mathbb{R}$ nên phương trình đã cho luôn là phương trình bậc nhất hai ẩn với mọi $m \\in \\mathbb{R}$.'''
                   % (pt, dau_k, k, b, b))
    
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
