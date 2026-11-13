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


def bt_Dang2_p1_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        tam_giac = random.choice([
            ('D', 'E', 'F'),
            ('A', 'B', 'C'),
            ('H', 'I', 'K')
        ])
        D, E, F = tam_giac
        chon = random.choice([1, 2])

        if chon == 1:
            canh_tinh = f'{D}{E}'
            du = [f'${D}{F}\cdot \tan {F}$', f'${D}{F}\cdot \cot {E}$']
            da = random.choice(du)
            s = [
                f'${D}{F}\cdot \tan {E}$',
                f'${D}{F}\cdot \sin {F}$',
                f'${E}{F}\cdot \tan {F}$',
                f'${D}{F}\cdot \cos {E}$',
                f'${E}{F}\cdot \cot {E}$'
            ]
            gt = f'${D}{E} = {D}{F}\cdot \tan {F} = {D}{F}\cdot \cot {E}$'
        else:
            canh_tinh = f'{D}{F}'
            du = [f'${D}{E}\cdot \tan {E}$', f'${D}{E}\cdot \cot {F}$']
            da = random.choice(du)
            s = [
                f'${D}{E}\cdot \tan {F}$',
                f'${D}{E}\cdot \sin {E}$',
                f'${E}{F}\cdot \tan {E}$',
                f'${D}{E}\cdot \cos {F}$',
                f'${E}{F}\cdot \cot {F}$'
            ]
            gt = f'${D}{F} = {D}{E}\cdot \tan {E} = {D}{E}\cdot \cot {F}$'

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        hinh_tikz = f'''
\\begin{{center}}
\\begin{{tikzpicture}}[scale=0.8]
\\coordinate ({D}) at (0,0);
\\coordinate ({E}) at (3.8,0);
\\coordinate ({F}) at (0,2.5);
\\draw[thick] ({D}) -- ({E}) -- ({F}) -- cycle;
\\draw ({D}) rectangle ++(0.3,0.3);
\\node[below left] at ({D}) {{${D}$}};
\\node[below right] at ({E}) {{${E}$}};
\\node[above left] at ({F}) {{${F}$}};
\\end{{tikzpicture}}
\\end{{center}}'''

        noidungcauhoi = f'''Cho tam giác ${D}{E}{F}$ vuông tại ${D}$ (như hình vẽ). Cạnh góc vuông ${canh_tinh}$ bằng biểu thức nào sau đây?{hinh_tikz}'''

        da_d = '\\True ' + str(da)
        da_s1, da_s2, da_s3 = str(das1), str(das2), str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = f'''Theo Định lí 2: Trong tam giác vuông, mỗi cạnh góc vuông bằng cạnh góc vuông kia nhân với $\\tan$ góc đối hoặc nhân với $\\cot$ góc kề.\\\\
Xét tam giác ${D}{E}{F}$ vuông tại ${D}$, ta có: {gt}.\\\\
Vậy chọn đáp án {da}.'''

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
