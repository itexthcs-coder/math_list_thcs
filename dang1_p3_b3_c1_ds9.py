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


def bt_dang1_p3_b3_c1_ds9(self):
    def fmt_dec(val):
        if val == int(val):
            return str(int(val))
        return str(round(val, 2)).replace('.', '{,}')
    
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        v_cu = random.randint(6, 18)
        v_zn = random.randint(4, 15)
        V_tong = v_cu + v_zn
        m_cu = round(8.9 * v_cu, 1)
        m_zn = 7 * v_zn
        M_tong = round(m_cu + m_zn, 1)
    
        kq_str = str(int(m_cu)) if m_cu == int(m_cu) else str(m_cu).replace('.', ',')
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một vật có khối lượng $%s\\text{ g}$ và thể tích $%s\\text{ cm}^3$ là hợp kim của đồng và kẽm. Biết rằng $1\\text{ cm}^3$ đồng nặng $8{,}9\\text{ g}$ và $1\\text{ cm}^3$ kẽm nặng $7\\text{ g}$. Hỏi trong vật hợp kim đó có bao nhiêu gam đồng?''' % (fmt_dec(M_tong), V_tong))
    
        # Nội dung lời giải
        loigiai = ('''Gọi $x\\text{ (g)}$ là khối lượng đồng và $y\\text{ (g)}$ là khối lượng kẽm có trong vật ($x > 0, y > 0$). \\\\
                   Khối lượng của vật là $%s\\text{ g}$ nên ta có phương trình $x + y = %s$. \\\\
                   Thể tích của đồng là $\\dfrac{x}{8{,}9}\\text{ (cm}^3)$, thể tích của kẽm là $\\dfrac{y}{7}\\text{ (cm}^3)$ và tổng thể tích của vật là $%s\\text{ cm}^3$ nên ta có phương trình $\\dfrac{x}{8{,}9} + \\dfrac{y}{7} = %s$. \\\\
                   Ta có hệ phương trình: $\\begin{cases} x + y = %s \\\\ \\dfrac{x}{8{,}9} + \\dfrac{y}{7} = %s. \\end{cases}$ \\\\
                   Giải hệ phương trình trên, ta được $x = %s$ và $y = %s$ (thỏa mãn điều kiện). \\\\
                   Vậy trong vật hợp kim đó có $%s\\text{ g}$ đồng.'''
                   % (fmt_dec(M_tong), fmt_dec(M_tong),
                      V_tong, V_tong,
                      fmt_dec(M_tong), V_tong,
                      fmt_dec(m_cu), fmt_dec(m_zn),
                      fmt_dec(m_cu)))
    
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
    
    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
