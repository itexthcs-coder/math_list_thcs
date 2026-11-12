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


def bt_dang6_p4_b1_c2_ds9(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        x = symbols('x')
        a = random.choice([1, 2, 3])
        b = random.choice([2, 3, 4])
        c = b + 1
        k = random.choice([4, 6, 8])
        # (x^2 + 2ax)/(x^2 + 2ax + b) - k/(x^2 + 2ax + b + 1) = 1
        # Đặt t = x^2 + 2ax + b => (t - b)/t - k/(t + 1) = 1
        # Khử mẫu: (t - b)(t + 1) - kt = t(t + 1) <=> (-b - k)t - b = 0 => t = -b/(b + k) < 0 (loại vì t >= b - a^2)
        while b - a**2 < 1:
            b += 2
        c = b + 1
        tu1 = x**2 + 2*a*x
        mau1 = x**2 + 2*a*x + b
        mau2 = x**2 + 2*a*x + c
        t_nghiem = Rational(-b, b + k)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Giải phương trình: $\\dfrac{%s}{%s} - \\dfrac{%s}{%s} = 1$.'''
                         %(latex(tu1), latex(mau1), latex(k), latex(mau2)))
    
        # Nội dung lời giải
        loigiai = ('''Ta có $%s = (x + %s)^2 + %s > 0$ và $%s = (x + %s)^2 + %s > 0$ với mọi $x \\in \\mathbb{R}$ nên phương trình xác định với mọi $x$. \\\\
                   Đặt $t = %s$ ($t \\ge %s$), khi đó $%s = t - %s$ và $%s = t + 1$. Phương trình trở thành: \\\\
                   $\\dfrac{t - %s}{t} - \\dfrac{%s}{t + 1} = 1$ (ĐKXĐ: $t \\neq 0$ và $t \\neq -1$). \\\\
                   Quy đồng mẫu hai vế với mẫu thức chung $t(t + 1)$ rồi khử mẫu, ta được: \\\\
                   $(t - %s)(t + 1) - %st = t(t + 1)$ \\\\
                   $t^2 + (1 - %s)t - %s - %st = t^2 + t$ \\\\
                   $-%st = %s$ \\\\
                   $t = %s$. \\\\
                   Giá trị $t = %s$ không thoả mãn điều kiện $t \\ge %s$. \\\\
                   Vậy phương trình đã cho vô nghiệm ($S = \\emptyset$).'''
                   %(latex(mau1), latex(a), latex(b - a**2), latex(mau2), latex(a), latex(c - a**2),
                     latex(mau1), latex(b - a**2), latex(tu1), latex(b), latex(mau2),
                     latex(b), latex(k),
                     latex(b), latex(k),
                     latex(b), latex(b), latex(k),
                     latex(b + k), latex(b),
                     latex(t_nghiem),
                     latex(t_nghiem), latex(b - a**2)))
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
