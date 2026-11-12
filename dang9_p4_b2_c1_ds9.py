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


def bt_dang9_p4_b2_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            a_val = random.choice([-2, -1, 1, 2])
            b_val = random.choice([-3, -2, -1, 1, 2, 3])
            xA = random.choice([-3, -2, -1])
            xB = random.choice([1, 2, 3])
            xM = random.choice([2, 3, 4])
            if a_val != 0 and b_val != 0 and xM != xB:
                break
    
        yA = a_val * xA + b_val
        yB = a_val * xB + b_val
        yM = a_val * xM + b_val
    
        # Đường thẳng d2: p*x + q*y = r đi qua M(xM; yM)
        p = random.choice([2, 3])
        q = random.choice([2, 3])
        while p * 1 + q * a_val == 0:
            q = random.choice([2, 3])
        r = p * xM + q * yM
    
        a_sym, b_sym = symbols('a b')
        ptA_str = latex(xA * a_sym + b_sym) + '=' + latex(yA)
        ptB_str = latex(xB * a_sym + b_sym) + '=' + latex(yB)
        dt1_str = latex(a_val * x + b_val)
        dt2_str = latex(p * x + q * y) + '=' + latex(r)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Tìm hai số $a$ và $b$ để đường thẳng $d_1: y = ax + b$ đi qua hai điểm $A(%s; %s)$ và $B(%s; %s)$. Sau đó, tìm tọa độ giao điểm $M$ của đường thẳng $d_1$ vừa tìm được với đường thẳng $d_2: %s$.'''
                         % (latex(xA), latex(yA), latex(xB), latex(yB), dt2_str))
    
        # Nội dung lời giải
        loigiai = ('''Vì đường thẳng $d_1: y = ax + b$ đi qua điểm $A(%s; %s)$ và điểm $B(%s; %s)$ nên ta có hệ phương trình: \\\\
                   $\\begin{cases} %s \\\\ %s \\end{cases}$. \\\\
                   Trừ từng vế hai phương trình của hệ, ta được $(%s)a = %s$, suy ra $a = %s$. \\\\
                   Thay $a = %s$ vào phương trình thứ hai, ta tìm được $b = %s$. Do đó $d_1: y = %s$. \\\\
                   Tọa độ giao điểm $M(x; y)$ của $d_1$ và $d_2$ là nghiệm của hệ phương trình: \\\\
                   $\\begin{cases} y = %s \\\\ %s \\end{cases}$. \\\\
                   Thế $y = %s$ vào phương trình thứ hai, ta được $%sx + %s(%s) = %s$, suy ra $x = %s$ và $y = %s$. \\\\
                   Vậy giao điểm cần tìm là $M(%s; %s)$.'''
                   % (latex(xA), latex(yA), latex(xB), latex(yB),
                      ptA_str, ptB_str,
                      latex(xB - xA), latex(yB - yA), latex(a_val),
                      latex(a_val), latex(b_val), dt1_str,
                      dt1_str, dt2_str,
                      dt1_str, latex(p), latex(q), dt1_str, latex(r), latex(xM), latex(yM),
                      latex(xM), latex(yM)))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
