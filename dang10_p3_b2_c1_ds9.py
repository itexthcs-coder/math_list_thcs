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


def bt_dang10_p3_b2_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Chọn nghiệm (x0; y0) trước sao cho x0 - p != 0 và y0 + q != 0
        p = random.choice([1, 2])
        q = random.choice([1, 2])
        u_mau = random.choice([2, 3])   # x0 - p = u_mau => u = 1/u_mau
        v_mau = random.choice([1, 2])   # y0 + q = v_mau => v = 1/v_mau
        x0 = p + u_mau
        y0 = v_mau - q
    
        a1 = u_mau * random.choice([1, 2])
        b1 = v_mau * random.choice([2, 3])
        a2 = u_mau * random.choice([2, 3])
        b2 = v_mau * random.choice([1, 2])
    
        c1 = a1 // u_mau + b1 // v_mau
        c2 = a2 // u_mau - b2 // v_mau
        kq = x0 * y0
        kq_str = str(kq).replace('.', ',')
    
        u_sym, v_sym = symbols('u v')
        pt1_uv = latex(a1 * u_sym + b1 * v_sym) + '=' + latex(c1)
        pt2_uv = latex(a2 * u_sym - b2 * v_sym) + '=' + latex(c2)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Biết hệ phương trình $\\begin{cases} \\frac{%s}{x - %s} + \\frac{%s}{y + %s} = %s \\\\ \\frac{%s}{x - %s} - \\frac{%s}{y + %s} = %s \\end{cases}$ ($x \\neq %s; y \\neq -%s$) có nghiệm duy nhất là $(x_0; y_0)$. Tính tích $x_0 \\cdot y_0$.'''
                         % (latex(a1), latex(p), latex(b1), latex(q), latex(c1),
                            latex(a2), latex(p), latex(b2), latex(q), latex(c2),
                            latex(p), latex(q)))
    
        # Nội dung lời giải
        loigiai = ('''Đặt $u = \\frac{1}{x - %s}$ và $v = \\frac{1}{y + %s}$, hệ phương trình đã cho trở thành: \\\\
                   $\\begin{cases} %s \\\\ %s \\end{cases}$. \\\\
                   Giải hệ phương trình trên bằng phương pháp cộng đại số, ta tìm được $u = %s$ và $v = %s$. \\\\
                   Từ đó suy ra $\\begin{cases} x_0 - %s = %s \\\\ y_0 + %s = %s \\end{cases} \\Leftrightarrow \\begin{cases} x_0 = %s \\\\ y_0 = %s \\end{cases}$ (thỏa mãn điều kiện). \\\\
                   Vậy $x_0 \\cdot y_0 = %s \\cdot (%s) = %s$.'''
                   % (latex(p), latex(q),
                      pt1_uv, pt2_uv,
                      latex(Rational(1, u_mau)), latex(Rational(1, v_mau)),
                      latex(p), latex(u_mau), latex(q), latex(v_mau),
                      latex(x0), latex(y0),
                      latex(x0), latex(y0), latex(kq)))
    
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
