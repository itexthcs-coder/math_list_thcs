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


def bt_Dang3_p1_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        goc = random.choice(['\\alpha', '\\beta', 'x', 'B'])
        cap_dung = random.choice([
            (f'$\\sin(90^\\circ - {goc}) = \\cos {goc}$', 'hai góc phụ nhau thì $\\sin$ góc này bằng $\\cos$ góc kia'),
            (f'$\\cos(90^\\circ - {goc}) = \\sin {goc}$', 'hai góc phụ nhau thì $\\cos$ góc này bằng $\\sin$ góc kia'),
            (f'$\\tan(90^\\circ - {goc}) = \\cot {goc}$', 'hai góc phụ nhau thì $\\tan$ góc này bằng $\\cot$ góc kia'),
            (f'$\\cot(90^\\circ - {goc}) = \\tan {goc}$', 'hai góc phụ nhau thì $\\cot$ góc này bằng $\\tan$ góc kia')
        ])
        da, ly_do = cap_dung

        s = [
            f'$\\tan(90^\\circ - {goc}) = \\cos {goc}$',
            f'$\\cot(90^\\circ - {goc}) = 1 - \\tan {goc}$',
            f'$\\cos(90^\\circ - {goc}) = \\cot {goc}$',
            f'$\\sin(90^\\circ - {goc}) = \\sin {goc}$',
            f'$\\tan(90^\\circ - {goc}) = \\sin {goc}$'
        ]
        if da in s:
            s.remove(da)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        hinh_tikz = f'''
\\begin{{center}}
\\begin{{tikzpicture}}[scale=0.8]
\\coordinate (A) at (0,0);
\\coordinate (B) at (4,0);
\\coordinate (C) at (0,2.5);
\\draw[thick] (A) -- (B) -- (C) -- cycle;
\\draw (A) rectangle ++(0.3,0.3);
\\draw (3.3,0) arc (180:148:0.7) node[midway, left] {{${goc}$}};
\\draw (0,1.8) arc (270:328:0.7) node[midway, below right] {{$90^\\circ-{goc}$}};
\\end{{tikzpicture}}
\\end{{center}}'''

        noidungcauhoi = f'''Với mọi góc nhọn ${goc}$, hệ thức nào sau đây luôn \\textbf{{đúng}}?{hinh_tikz}'''

        da_d = '\\True ' + str(da)
        da_s1, da_s2, da_s3 = str(das1), str(das2), str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = f'''Theo tính chất tỉ số lượng giác của hai góc phụ nhau: {ly_do}.\\\\
Do đó {da} là khẳng định đúng.'''

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
