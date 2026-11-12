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


def bt_dang8_p4_b2_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([2, 3, 4])
    
        # Hệ: mx + y = k*m và x + my = m + k - 1
        # Rút y = k*m - m*x => x + m*(k*m - m*x) = m + k - 1 => (1 - m^2)x = -k*m^2 + m + k - 1 = (1 - m)(k*m + k - 1)
        # Hoặc chọn hệ chuẩn: mx + y = 2m và x + my = m + 1 => (m^2 - 1)x = m^2 - 1 => x = 1, y = m
        # Biến thể có nhân tử: mx + y = 3m và x + my = m + 2 => (m^2 - 1)x = 2(m^2 - 1) => x = 2, y = m
        c0 = random.choice([2, 3, 4])
        m_sym = symbols('m')
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hệ phương trình $\\begin{cases} mx + y = %sm \\\\ x + my = m + %s \\end{cases}$ ($m$ là tham số). Tìm điều kiện của $m$ để hệ phương trình có nghiệm duy nhất $(x; y)$, khi đó chứng minh rằng nếu $m \\in \\mathbb{Z}$ thì $x, y$ cũng là các số nguyên.'''
                         % (latex(c0), latex(c0 - 1)))
    
        # Nội dung lời giải
        loigiai = ('''Từ phương trình thứ nhất ta có $y = %sm - mx$. Thế vào phương trình thứ hai, ta được: \\\\
                   $x + m(%sm - mx) = m + %s \\Leftrightarrow (1 - m^2)x = -%sm^2 + m + %s \\Leftrightarrow (m^2 - 1)x = %s(m^2 - 1) - (m - 1)$?'''
                   % (latex(c0), latex(c0), latex(c0 - 1), latex(c0), latex(c0 - 1), latex(c0)))
        # Kiểm tra lại đại số chính xác: x + m*(c0*m - m*x) = m + c0 - 1 => (1 - m^2)x = -c0*m^2 + m + c0 - 1 = (1 - m)(c0*m + c0 - 1)
        # Với m != 1: (1 + m)x = c0*m + c0 - 1 => x = c0 - 1/(m+1)!
        # Rất đẹp! Giải điều kiện nguyên: x = c0 - 1/(m+1) nguyên <=> m + 1 in {-1; 1} <=> m in {-2; 0} (với m != +-1 => m in {-2; 0})!
        noidungcauhoi = ('''Cho hệ phương trình $\\begin{cases} mx + y = %sm \\\\ x + my = m + %s \\end{cases}$ ($m$ là tham số). Tìm các giá trị nguyên của $m$ để hệ phương trình có nghiệm duy nhất $(x; y)$ sao cho $x$ và $y$ đều là các số nguyên.'''
                         % (latex(c0), latex(c0 - 1)))
    
        loigiai = ('''Từ phương trình thứ nhất ta có $y = %sm - mx$. Thế vào phương trình thứ hai, ta được: \\\\
                   $x + m(%sm - mx) = m + %s \\Leftrightarrow (1 - m^2)x = -%sm^2 + m + %s \\Leftrightarrow (1 - m)(1 + m)x = (1 - m)(%sm + %s)$. \\\\
                   Để hệ phương trình có nghiệm duy nhất thì $(1 - m)(1 + m) \\neq 0 \\Leftrightarrow m \\neq \\pm 1$. \\\\
                   Khi đó $x = \\frac{%sm + %s}{m + 1} = %s - \\frac{1}{m + 1}$, và $y = %sm - m\\left(%s - \\frac{1}{m + 1}\\right) = \\frac{m}{m + 1} = 1 - \\frac{1}{m + 1}$. \\\\
                   Với $m \\in \\mathbb{Z}$ ($m \\neq \\pm 1$), để $x$ và $y$ đều là số nguyên thì $m + 1$ phải là ước của $1$, tức là $m + 1 \\in \\{-1; 1\\} \\Leftrightarrow m \\in \\{-2; 0\\}$ (thỏa mãn $m \\neq \\pm 1$). \\\\
                   Vậy các giá trị nguyên của $m$ cần tìm là $m \\in \\{-2; 0\\}$.'''
                   % (latex(c0), latex(c0), latex(c0 - 1), latex(c0), latex(c0 - 1), latex(c0), latex(c0 - 1),
                      latex(c0), latex(c0 - 1), latex(c0),
                      latex(c0), latex(c0)))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
