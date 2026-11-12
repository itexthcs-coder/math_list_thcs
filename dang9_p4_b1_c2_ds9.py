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


def bt_dang9_p4_b1_c2_ds9(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        x = symbols('x')
        while True:
            a = random.choice([1, 2, 3, 4])
            b = random.choice([2, 3, 4, 5])
            if a != b:
                break
    
        # (x + m)/(x - a) + (x - b)/x = 2
        # Khử mẫu: x(x + m) + (x - b)(x - a) = 2x(x - a)
        # <=> (m + a - b)x = -a*b
        heso_m = a - b
        dau_heso = f"+ {heso_m}" if heso_m > 0 else f"- {abs(heso_m)}"
        vp_so = -a * b
        m_cam1 = b - a
        m_cam2 = -a
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho phương trình $\\dfrac{x + m}{x - %s} + \\dfrac{x - %s}{x} = 2$. Tìm tất cả các giá trị của tham số $m$ để phương trình đã cho có nghiệm duy nhất.'''
                         %(latex(a), latex(b)))
    
        # Nội dung lời giải
        loigiai = ('''Điều kiện xác định: $x \\neq 0$ và $x \\neq %s$. \\\\
                   Quy đồng mẫu hai vế với mẫu thức chung $x(x - %s)$ rồi khử mẫu, ta được: \\\\
                   $x(x + m) + (x - %s)(x - %s) = 2x(x - %s)$ \\\\
                   $x^2 + mx + x^2 - %sx + %s = 2x^2 - %sx$ \\\\
                   $(m %s)x = %s$. \\\\
                   Để phương trình đã cho có nghiệm duy nhất thì phương trình bậc nhất $(m %s)x = %s$ phải có nghiệm duy nhất $x$ thoả mãn điều kiện xác định $x \\neq 0$ và $x \\neq %s$: \\\\
                   $\\bullet$ Điều kiện có nghiệm duy nhất: $m %s \\neq 0$, suy ra $m \\neq %s$. Khi đó nghiệm là $x = \\dfrac{%s}{m %s}$. \\\\
                   $\\bullet$ Điều kiện $x \\neq 0$: $\\dfrac{%s}{m %s} \\neq 0$ (luôn đúng vì $%s \\neq 0$). \\\\
                   $\\bullet$ Điều kiện $x \\neq %s$: $\\dfrac{%s}{m %s} \\neq %s$, suy ra $%s \\neq %s(m %s)$ hay $m \\neq %s$. \\\\
                   Vậy với $m \\neq %s$ và $m \\neq %s$ thì phương trình đã cho có nghiệm duy nhất.'''
                   %(latex(a),
                     latex(a),
                     latex(b), latex(a), latex(a),
                     latex(a + b), latex(a*b), latex(2*a),
                     dau_heso, latex(vp_so),
                     dau_heso, latex(vp_so), latex(a),
                     dau_heso, latex(m_cam1), latex(vp_so), dau_heso,
                     latex(vp_so), dau_heso, latex(vp_so),
                     latex(a), latex(vp_so), dau_heso, latex(a), latex(vp_so), latex(a), dau_heso, latex(m_cam2),
                     latex(m_cam1), latex(m_cam2)))
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
