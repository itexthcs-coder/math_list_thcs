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


def bt_dang2_p4_b1_c1_ds9(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            x_val, y_val = randint(6, 15), randint(6, 15)
            if x_val == y_val: continue
            t0_p = (x_val * y_val * 60) / (x_val + y_val)
            if not t0_p.is_integer(): continue
            t0_p = int(t0_p)
            t1, t2 = randint(2, x_val - 2), randint(2, y_val - 2)
            tu = t1 * y_val + t2 * x_val
            mau = x_val * y_val
            ucln = math.gcd(tu, mau)
            tu, mau = tu // ucln, mau // ucln
            if tu < mau and mau <= 20: break
            
        gio, phut = t0_p // 60, t0_p % 60
        time_str = ""
        if gio > 0: time_str += "%s giờ " % gio
        if phut > 0: time_str += "%s phút" % phut
        time_str = time_str.strip()
        ucln_t0 = math.gcd(t0_p, 60)
        tu_t0, mau_t0 = t0_p // ucln_t0, 60 // ucln_t0
        
        noidungcauhoi = ('''Hai vòi nước cùng chảy vào một bể không có nước thì sau %s sẽ đầy bể. Nếu mở vòi thứ nhất chảy trong $%s$ giờ rồi khóa lại và mở tiếp vòi thứ hai chảy trong $%s$ giờ thì được $\\frac{%s}{%s}$ bể nước. Hỏi nếu chảy riêng một mình thì mỗi vòi sẽ làm đầy bể trong bao lâu?''' % (time_str, t1, t2, tu, mau))
        
        loigiai = ('''Gọi thời gian vòi thứ nhất và vòi thứ hai chảy riêng đầy bể lần lượt là $x$ và $y$ (giờ) ($x, y > 0$).\\\\
    Một giờ vòi thứ nhất chảy được $\\frac{1}{x}$ (bể).\\\\
    Một giờ vòi thứ hai chảy được $\\frac{1}{y}$ (bể).\\\\
    Đổi %s = $\\frac{%s}{%s}$ giờ.\\\\
    Vì hai vòi cùng chảy thì sau $\\frac{%s}{%s}$ giờ đầy bể nên trong $1$ giờ hai vòi chảy được $1 : \\frac{%s}{%s} = \\frac{%s}{%s}$ bể, ta có phương trình: $\\frac{1}{x} + \\frac{1}{y} = \\frac{%s}{%s}$ (1).\\\\
    Mở vòi thứ nhất $%s$ giờ và vòi thứ hai $%s$ giờ thì được $\\frac{%s}{%s}$ bể nên ta có phương trình: $%s \\cdot \\frac{1}{x} + %s \\cdot \\frac{1}{y} = \\frac{%s}{%s}$ (2).\\\\
    Từ (1) và (2) ta có hệ phương trình:\\\\
    $\\begin{cases} \\frac{1}{x} + \\frac{1}{y} = \\frac{%s}{%s} \\\\ %s \\cdot \\frac{1}{x} + %s \\cdot \\frac{1}{y} = \\frac{%s}{%s} \\end{cases}$\\\\
    Đặt $u = \\frac{1}{x}, v = \\frac{1}{y}$, giải hệ ta được $u = \\frac{1}{%s}, v = \\frac{1}{%s}$.\\\\
    Suy ra $x = %s, y = %s$ (thỏa mãn).\\\\
    Vậy nếu chảy riêng, vòi một cần $%s$ giờ, vòi hai cần $%s$ giờ.''' % (time_str, tu_t0, mau_t0, tu_t0, mau_t0, tu_t0, mau_t0, mau_t0, tu_t0, mau_t0, tu_t0, t1, t2, tu, mau, t1, t2, tu, mau, mau_t0, tu_t0, t1, t2, tu, mau, x_val, y_val, x_val, y_val, x_val, y_val))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \\n'
               '\\begin{ex}\\n'+
               str(noidungcauhoi)+
               '\\loigiai{ \\n' +str(loigiai)+'}\\n'
               '\\end{ex}\\n'
               '\\end{minipage} \\n\\n')
    return content
