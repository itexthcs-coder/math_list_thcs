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


def bt_dang17_p1_b3_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        while True:
            a1 = random.choice([2, 3, 4])
            b1 = random.choice([-3, -2, 2, 3])
            a2 = random.choice([i for i in range(2, 5) if i != a1])
            b2 = random.choice([-1, 1])
            if a1 * b2 - a2 * b1 != 0:
                break
                
        u0 = random.choice([2, 3, 4, 5])
        v0 = random.choice([1, 2, 3, 4])
        x0 = Rational(1, u0)
        y0 = Rational(1, v0)
        
        c1 = a1 * u0 + b1 * v0
        c2 = a2 * u0 + b2 * v0
        
        pt1 = f"\\frac{{{a1}}}{{x}} {'+' if b1 > 0 else '-'} \\frac{{{abs(b1)}}}{{y}} = {c1}"
        pt2 = f"\\frac{{{a2}}}{{x}} {'+' if b2 > 0 else '-'} \\frac{{1}}{{y}} = {c2}"
        
        du = [f'$\\left({latex(x0)}; {latex(y0)}\\right)$']
        da = random.choice(du)
        
        s = [
            f'$\\left({u0}; {v0}\\right)$',
            f'$\\left({latex(y0)}; {latex(x0)}\\right)$',
            f'$\\left({latex(-x0)}; {latex(y0)}\\right)$',
            f'$\\left({latex(Rational(1, u0 + 1))}; {latex(y0)}\\right)$'
        ]
        s = list(dict.fromkeys([item for item in s if item != da]))
        
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
        
        noidungcauhoi = ('''Cho hệ phương trình $\\begin{cases} %s \\\\ %s \\end{cases}$ với điều kiện $x \\ne 0, y \\ne 0$. Nghiệm $(x; y)$ của hệ phương trình là''' % (pt1, pt2))
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ('''Đặt $u = \\frac{1}{x}$ và $v = \\frac{1}{y}$, ta có hệ phương trình bậc nhất hai ẩn:
                    $$\\begin{cases} %su %s %sv = %s \\\\ %su %s v = %s. \\end{cases}$$
                    Giải hệ trên, ta được $u = %s$ và $v = %s$.\\\\
                    Do đó $\\frac{1}{x} = %s \\Rightarrow x = %s$ và $\\frac{1}{y} = %s \\Rightarrow y = %s$ (thỏa mãn điều kiện).\\\\
                    Vậy nghiệm của hệ phương trình là $\\left(%s; %s\\right)$.'''
                   % (a1, '+' if b1 > 0 else '-', abs(b1), c1,
                      a2, '+' if b2 > 0 else '-', c2,
                      u0, v0, u0, latex(x0), v0, latex(y0), latex(x0), latex(y0)))
    
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\choice \n' '{'+str(list_1[1])+'}\n' '{'+str(list_1[2])+'}\n' '{'+str(list_1[3])+'}\n' '{'+str(list_1[0])+'}\n' '\\loigiai{'+str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
