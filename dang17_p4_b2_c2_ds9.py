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


def bt_dang17_p4_b2_c2_ds9(self):
    # Dạng 17: Bài toán quy đổi nhiệt độ môi trường và điều kiện hoạt động của thiết bị điện tử
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        c_lo = random.choice([-15, -10, -5, 0])
        c_hi = random.choice([35, 40, 45, 50])
        f_lo = int(round(1.8 * c_lo + 32))
        f_hi = int(round(1.8 * c_hi + 32))
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một loại thiết bị cảm biến công nghiệp hoạt động ổn định khi nhiệt độ môi trường $F$ (tính theo độ Fahrenheit) nằm trong khoảng từ $%d^\\circ\\text{F}$ đến $%d^\\circ\\text{F}$ ($%d \\le F \\le %d$). Biết công thức liên hệ giữa nhiệt độ Fahrenheit ($F$) và nhiệt độ Celsius ($C$) là $F = 1,8C + 32$. Hãy tìm khoảng nhiệt độ hoạt động ổn định của thiết bị này theo đơn vị độ Celsius ($^\\circ\\text{C}$).'''
                         % (f_lo, f_hi, f_lo, f_hi))
    
        # Nội dung lời giải
        loigiai = ('''Thay $F = 1,8C + 32$ vào điều kiện $%d \\le F \\le %d$ ta được bất đẳng thức kép:
                   $$%d \\le 1,8C + 32 \\le %d.$$
                   Cộng cả ba vế của bất đẳng thức trên với $-32$ ta được:
                   $$%d - 32 \\le 1,8C \\le %d - 32 \\iff %d \\le 1,8C \\le %d.$$
                   Nhân cả ba vế của bất đẳng thức trên với số dương $\\dfrac{1}{1,8} > 0$ ta được:
                   $$\\dfrac{%d}{1,8} \\le C \\le \\dfrac{%d}{1,8} \\iff %d \\le C \\le %d.$$
                   Vậy thiết bị cảm biến hoạt động ổn định trong khoảng nhiệt độ từ $%d^\\circ\\text{C}$ đến $%d^\\circ\\text{C}$.'''
                   % (f_lo, f_hi, f_lo, f_hi, f_lo, f_hi, f_lo - 32, f_hi - 32,
                      f_lo - 32, f_hi - 32, c_lo, c_hi, c_lo, c_hi))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')


    return content
