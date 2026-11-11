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


def bt_dang1_p4_b1_c1_ds9(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            x_val = randint(30, 80)
            y_val = randint(30, 80)
            a1 = random.choice([1.2, 1.5, 1.8])
            b1 = random.choice([2.0, 2.2, 2.5])
            a2 = random.choice([1.5, 2.0, 2.5])
            b2 = random.choice([1.0, 1.5])
            c1 = a1 * x_val + b1 * y_val
            c2 = a2 * x_val + b2 * y_val
            if c1.is_integer() and c2.is_integer():
                c1, c2 = int(c1), int(c2)
                break
                
        a1_s = str(a1).replace('.', ',')
        b1_s = str(b1).replace('.', ',')
        a2_s = str(a2).replace('.', ',')
        b2_s = str(b2).replace('.', ',')
        
        noidungcauhoi = ('''Một phân xưởng may dự kiến sản xuất áo sơ mi và quần âu. Để may $1$ chiếc áo sơ mi cần %s mét vải và %s giờ công; để may $1$ chiếc quần âu cần %s mét vải và %s giờ công. Trong một tuần, xưởng sử dụng hết %s mét vải và %s giờ công. Tính số lượng áo sơ mi và quần âu xưởng đã may được.''' % (a1_s, a2_s, b1_s, b2_s, c1, c2))
        
        loigiai = ('''Gọi số lượng áo sơ mi và quần âu xưởng may được lần lượt là $x$ và $y$ (chiếc) ($x, y \\in \\mathbb{N}^*$).\\\\
    Số mét vải để may $x$ áo sơ mi là $%s x$ (m).\\\\
    Số mét vải để may $y$ quần âu là $%s y$ (m).\\\\
    Vì xưởng sử dụng hết $%s$ mét vải nên ta có phương trình: $%s x + %s y = %s$ (1).\\\\
    Số giờ công để may $x$ áo sơ mi là $%s x$ (giờ).\\\\
    Số giờ công để may $y$ quần âu là $%s y$ (giờ).\\\\
    Vì xưởng sử dụng hết $%s$ giờ công nên ta có phương trình: $%s x + %s y = %s$ (2).\\\\
    Từ (1) và (2), ta có hệ phương trình:\\\\
    $\\begin{cases} %s x + %s y = %s \\\\ %s x + %s y = %s \\end{cases}$\\\\
    Giải hệ phương trình, ta được $x = %s$, $y = %s$ (thỏa mãn điều kiện).\\\\
    Vậy xưởng đã may được $%s$ áo sơ mi và $%s$ quần âu.''' % (a1_s, b1_s, c1, a1_s, b1_s, c1, a2_s, b2_s, c2, a2_s, b2_s, c2, a1_s, b1_s, c1, a2_s, b2_s, c2, x_val, y_val, x_val, y_val))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \\n'
               '\\begin{ex}\\n'+
               str(noidungcauhoi)+
               '\\loigiai{ \\n' +str(loigiai)+'}\\n'
               '\\end{ex}\\n'
               '\\end{minipage} \\n\\n')
    return content
