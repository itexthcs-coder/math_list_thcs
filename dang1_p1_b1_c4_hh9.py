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

def bt_dang1_p1_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tencanh = [('AB', 'BC', 'AC'), ('MN', 'NP', 'MP'), ('DE', 'EF', 'DF')]
        A, B, C = random.choice(tencanh)
        
        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (0,0);\n'
            '\\coordinate (B) at (4,0);\n'
            '\\coordinate (C) at (0,3);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle;\n'
            '\\draw[line width=1pt] (0,0.3)--(0.3,0.3)--(0.3,0);\n'
            '\\fill (A) circle (1pt) node[below left] {$%s$};\n'
            '\\fill (B) circle (1pt) node[below right] {$%s$};\n'
            '\\fill (C) circle (1pt) node[above left] {$%s$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        ) % (A[0], A[1], B[1])
        
        c_ke = A
        c_huyen = B
        c_doi = C
        goc_xet = A[1]
        dinh_vuong = A[0]
        
        loai = random.choice(['sin', 'cos', 'tan', 'cot'])
        if loai == 'sin':
            da = '$\\sin %s = \\dfrac{%s}{%s}$' % (goc_xet, c_doi, c_huyen)
            s = [
                '$\\sin %s = \\dfrac{%s}{%s}$' % (goc_xet, c_ke, c_huyen),
                '$\\sin %s = \\dfrac{%s}{%s}$' % (goc_xet, c_doi, c_ke),
                '$\\sin %s = \\dfrac{%s}{%s}$' % (goc_xet, c_ke, c_doi),
                '$\\sin %s = \\dfrac{%s}{%s}$' % (goc_xet, c_huyen, c_doi)
            ]
            ct = '\\sin %s = \\dfrac{\\text{cạnh đối}}{\\text{cạnh huyền}} = \\dfrac{%s}{%s}' % (goc_xet, c_doi, c_huyen)
        elif loai == 'cos':
            da = '$\\cos %s = \\dfrac{%s}{%s}$' % (goc_xet, c_ke, c_huyen)
            s = [
                '$\\cos %s = \\dfrac{%s}{%s}$' % (goc_xet, c_doi, c_huyen),
                '$\\cos %s = \\dfrac{%s}{%s}$' % (goc_xet, c_ke, c_doi),
                '$\\cos %s = \\dfrac{%s}{%s}$' % (goc_xet, c_doi, c_ke),
                '$\\cos %s = \\dfrac{%s}{%s}$' % (goc_xet, c_huyen, c_ke)
            ]
            ct = '\\cos %s = \\dfrac{\\text{cạnh kề}}{\\text{cạnh huyền}} = \\dfrac{%s}{%s}' % (goc_xet, c_ke, c_huyen)
        elif loai == 'tan':
            da = '$\\tan %s = \\dfrac{%s}{%s}$' % (goc_xet, c_doi, c_ke)
            s = [
                '$\\tan %s = \\dfrac{%s}{%s}$' % (goc_xet, c_ke, c_doi),
                '$\\tan %s = \\dfrac{%s}{%s}$' % (goc_xet, c_doi, c_huyen),
                '$\\tan %s = \\dfrac{%s}{%s}$' % (goc_xet, c_ke, c_huyen),
                '$\\tan %s = \\dfrac{%s}{%s}$' % (goc_xet, c_huyen, c_ke)
            ]
            ct = '\\tan %s = \\dfrac{\\text{cạnh đối}}{\\text{cạnh kề}} = \\dfrac{%s}{%s}' % (goc_xet, c_doi, c_ke)
        else:
            da = '$\\cot %s = \\dfrac{%s}{%s}$' % (goc_xet, c_ke, c_doi)
            s = [
                '$\\cot %s = \\dfrac{%s}{%s}$' % (goc_xet, c_doi, c_ke),
                '$\\cot %s = \\dfrac{%s}{%s}$' % (goc_xet, c_ke, c_huyen),
                '$\\cot %s = \\dfrac{%s}{%s}$' % (goc_xet, c_doi, c_huyen),
                '$\\cot %s = \\dfrac{%s}{%s}$' % (goc_xet, c_huyen, c_doi)
            ]
            ct = '\\cot %s = \\dfrac{\\text{cạnh kề}}{\\text{cạnh đối}} = \\dfrac{%s}{%s}' % (goc_xet, c_ke, c_doi)
            
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
        
        # Câu hỏi
        noidungcauhoi = ('''Cho tam giác $%s%s%s$ vuông tại $%s$ như hình vẽ dưới đây. Hệ thức nào sau đây là đúng? %s'''
                         % (dinh_vuong, goc_xet, B[1], dinh_vuong, hinh_ve))
        
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        # Nội dung lời giải
        loigiai = ('''Xét tam giác $%s%s%s$ vuông tại $%s$, đối với góc nhọn $%s$ ta có cạnh đối là $%s$, cạnh kề là $%s$ và cạnh huyền là $%s$. \\\\
        Theo định nghĩa tỉ số lượng giác của góc nhọn, ta có: $%s$.'''
                   % (dinh_vuong, goc_xet, B[1], dinh_vuong, goc_xet, c_doi, c_ke, c_huyen, ct))
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
