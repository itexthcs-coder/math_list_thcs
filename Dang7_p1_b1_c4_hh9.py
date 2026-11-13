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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D

def bt_Dang7_p1_b1_c4_hh9(self):
    def round_vn(val, digits):
        fmt = '0.' + '0' * digits if digits > 0 else '0'
        d = Decimal(str(val)).quantize(Decimal(fmt), rounding=ROUND_HALF_UP)
        return str(d).replace('.', ',')

    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        d = randint(15, 75)
        m = random.choice([0, 12, 15, 18, 24, 30, 36, 42, 45, 54])
        rad = math.radians(d + m / 60.0)
        ham = random.choice(['sin', 'cos', 'tan', 'cot'])
        if ham == 'sin':
            val = math.sin(rad)
        elif ham == 'cos':
            val = math.cos(rad)
        elif ham == 'tan':
            val = math.tan(rad)
        else:
            val = 1.0 / math.tan(rad)
            
        goc_str = '%d^{\\circ}' % d if m == 0 else '%d^{\\circ}%d\'' % (d, m)
        kq_str = round_vn(val, 3)
        
        da = '$%s$' % kq_str
        s = [
            '$%s$' % round_vn(val + 0.012, 3),
            '$%s$' % round_vn(abs(val - 0.015), 3),
            '$%s$' % round_vn(val + 0.024, 3)
        ]
        das1 = s[0]
        das2 = s[1]
        das3 = s[2]
        
        # Câu hỏi
        noidungcauhoi = ('''Sử dụng máy tính cầm tay, tính $\\%s %s$ (làm tròn kết quả đến chữ số thập phân thứ ba) ta được'''
                         % (ham, goc_str))
        
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        # Nội dung lời giải
        if ham == 'cot':
            loigiai = ('''Sử dụng máy tính cầm tay, ta tính $\\cot %s = \\dfrac{1}{\\tan %s} \\approx %s$. \\\\
            Làm tròn kết quả đến chữ số thập phân thứ ba ta được $%s$.'''
                       % (goc_str, goc_str, round_vn(val, 6), kq_str))
        else:
            loigiai = ('''Sử dụng máy tính cầm tay, ta tính được $\\%s %s \\approx %s$. \\\\
            Làm tròn kết quả đến chữ số thập phân thứ ba ta được $%s$.'''
                       % (ham, goc_str, round_vn(val, 6), kq_str))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n'
               '{' + str(list_1[1]) + '}\n'
               '{' + str(list_1[2]) + '}\n'
               '{' + str(list_1[3]) + '}\n'
               '{' + str(list_1[0]) + '}\n'
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
