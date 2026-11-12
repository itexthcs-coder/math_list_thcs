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


def bt_dang3_p3_b2_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        m1 = random.choice([3, 5, 7, 9])
        m2 = random.choice([2, 4, 5, 7])
        while m1 == m2:
            m2 = random.choice([2, 4, 5, 7])
    
        u0 = random.choice([1, 2, 3])
        v0 = random.choice([-3, -2, -1])
        x0 = m1 * u0
        y0 = m2 * v0
    
        a1 = random.choice([2, 3, 4])
        b1 = random.choice([-3, -2])
        a2 = random.choice([1, 2, 3])
        b2 = random.choice([2, 3, 4])
        while a1 * b2 - a2 * b1 == 0:
            b2 = random.choice([2, 3, 4])
    
        c1 = a1 * u0 + b1 * v0
        c2 = a2 * u0 + b2 * v0
        kq = x0 + 2 * y0
        kq_str = str(kq).replace('.', ',')
    
        pt1_str = latex(Rational(a1, m1) * x + Rational(b1, m2) * y) + '=' + latex(c1)
        pt2_str = latex(Rational(a2, m1) * x + Rational(b2, m2) * y) + '=' + latex(c2)
    
        u_sym, v_sym = symbols('u v')
        pt1_uv = latex(a1 * u_sym + b1 * v_sym) + '=' + latex(c1)
        pt2_uv = latex(a2 * u_sym + b2 * v_sym) + '=' + latex(c2)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Hệ phương trình $\\begin{cases} %s \\\\ %s \\end{cases}$ có nghiệm duy nhất là $(x_0; y_0)$. Giá trị của biểu thức $M = x_0 + 2y_0$ bằng bao nhiêu?'''
                         % (pt1_str, pt2_str))
    
        # Nội dung lời giải
        loigiai = ('''Đặt $u = \\frac{x}{%s}$ và $v = \\frac{y}{%s}$, hệ phương trình đã cho trở thành: \\\\
                   $\\begin{cases} %s \\\\ %s \\end{cases}$. \\\\
                   Giải hệ phương trình trên, ta tìm được $u = %s$ và $v = %s$. \\\\
                   Suy ra $x_0 = %s \\cdot %s = %s$ và $y_0 = %s \\cdot (%s) = %s$. \\\\
                   Vậy $M = x_0 + 2y_0 = %s + 2 \\cdot (%s) = %s$.'''
                   % (latex(m1), latex(m2),
                      pt1_uv, pt2_uv,
                      latex(u0), latex(v0),
                      latex(m1), latex(u0), latex(x0),
                      latex(m2), latex(v0), latex(y0),
                      latex(x0), latex(y0), latex(kq)))
    
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
