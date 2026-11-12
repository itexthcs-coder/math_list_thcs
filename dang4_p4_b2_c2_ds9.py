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


def bt_dang4_p4_b2_c2_ds9(self):
    # Dạng 4: Chứng minh bất đẳng thức phân số bằng tính chất bắc cầu qua số hữu tỉ trung gian
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        nguyen = randint(2, 5)
        le = random.choice([1, 2, 3, 4]) # số thập phân nguyen,le
        tg_val = nguyen + le / 10
        tg_str = f"{nguyen},{le}"
        
        # Chọn m1 chẵn để m1 * tg_val là số nguyên, m2 chia hết cho 10 để m2 * tg_val là số nguyên
        m1 = random.choice([10, 20, 30])
        m2 = random.choice([10, 20, 30])
        while m1 == m2:
            m2 = random.choice([10, 20, 30])
            
        tu1 = int(round(m1 * tg_val)) + 1
        tu2 = int(round(m2 * tg_val)) - 1
        
        g1 = math.gcd(tu1, m1)
        tu1_rg, m1_rg = tu1 // g1, m1 // g1
        g2 = math.gcd(tu2, m2)
        tu2_rg, m2_rg = tu2 // g2, m2 // g2
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Vận dụng tính chất bắc cầu của bất đẳng thức, hãy chứng minh rằng:
                         $$\\dfrac{%d}{%d} > \\dfrac{%d}{%d}.$$'''
                         % (tu1_rg, m1_rg, tu2_rg, m2_rg))
    
        # Nội dung lời giải
        loigiai = ('''Ta chọn số hữu tỉ trung gian là $%s$. \\\\
                   Xét phân số thứ nhất:
                   $$\\dfrac{%d}{%d} = \\dfrac{%d}{%d} = %s + \\dfrac{1}{%d} > %s. \\quad (1)$$
                   Xét phân số thứ hai:
                   $$\\dfrac{%d}{%d} = \\dfrac{%d}{%d} = %s - \\dfrac{1}{%d} < %s. \\quad (2)$$
                   Từ $(1)$ và $(2)$, theo tính chất bắc cầu của bất đẳng thức ta có $\\dfrac{%d}{%d} > %s > \\dfrac{%d}{%d}$, suy ra $\\dfrac{%d}{%d} > \\dfrac{%d}{%d}$.'''
                   % (tg_str, tu1_rg, m1_rg, tu1, m1, tg_str, m1, tg_str,
                      tu2_rg, m2_rg, tu2, m2, tg_str, m2, tg_str,
                      tu1_rg, m1_rg, tg_str, tu2_rg, m2_rg, tu1_rg, m1_rg, tu2_rg, m2_rg))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
    


    return content
