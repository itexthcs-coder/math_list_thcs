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


def bt_dang6_p4_b3_c1_ds9(self):
    def fmt_dec(val):
        if val == int(val):
            return str(int(val))
        return str(round(val, 2)).replace('.', '{,}')
    
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x0 = random.randint(15, 25) * 100
        y0 = random.randint(12, 22) * 100
        while x0 == y0:
            y0 = random.randint(12, 22) * 100
    
        p1 = random.choice([10, 12, 15, 18])
        p2 = random.choice([i for i in [10, 12, 15, 20] if i != p1])
    
        tong_ngoai = x0 + y0
        x_nay = int(x0 * (100 + p1) // 100)
        y_nay = int(y0 * (100 + p2) // 100)
        tong_nay = x_nay + y_nay
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Năm ngoái, hai đơn vị sản xuất nông nghiệp thu hoạch được $%s\\text{ tấn}$ thóc. Năm nay, hai đơn vị thu hoạch được $%s\\text{ tấn}$ thóc. Hỏi năm nay, mỗi đơn vị thu hoạch được bao nhiêu tấn thóc, biết rằng năm nay, đơn vị thứ nhất làm vượt mức $%s\\%%$, đơn vị thứ hai làm vượt mức $%s\\%%$ so với năm ngoái?'''
                         % (tong_ngoai, tong_nay, p1, p2))
    
        # Nội dung lời giải
        loigiai = ('''\\begin{itemize}
                        \\item Gọi số thóc năm ngoái của đơn vị thứ nhất là $x$ (tấn) và của đơn vị thứ hai là $y$ (tấn). Điều kiện: $x > 0$ và $y > 0$.\\\\
                        Năm ngoái hai đơn vị thu hoạch được $%s\\text{ tấn}$ thóc nên ta có phương trình:
                        $$x + y = %s. \\quad (1)$$
                        Năm nay, đơn vị thứ nhất vượt mức $%s\\%%$ nên thu hoạch được $%sx$ (tấn); đơn vị thứ hai vượt mức $%s\\%%$ nên thu hoạch được $%sy$ (tấn).\\\\
                        Tổng số thóc năm nay của hai đơn vị là $%s\\text{ tấn}$ nên ta có phương trình:
                        $$%sx + %sy = %s. \\quad (2)$$
                        Từ $(1)$ và $(2)$, ta có hệ phương trình:
                        $$\\begin{cases} x + y = %s \\\\ %sx + %sy = %s. \\end{cases}$$
                        \\item Giải hệ phương trình:\\\\
                        Từ $(1)$ rút $y = %s - x$ thế vào $(2)$, ta tìm được $x = %s$ và $y = %s$.
                        \\item Các giá trị $x = %s$ và $y = %s$ thỏa mãn điều kiện của ẩn.\\\\
                        Vậy năm nay:\\\\
                        Đơn vị thứ nhất thu hoạch được $%s \\cdot %s = %s\\text{ (tấn thóc)}$.\\\\
                        Đơn vị thứ hai thu hoạch được $%s \\cdot %s = %s\\text{ (tấn thóc)}$.
                    \\end{itemize}'''
                   % (tong_ngoai, tong_ngoai,
                      p1, fmt_dec(1 + p1/100), p2, fmt_dec(1 + p2/100),
                      tong_nay, fmt_dec(1 + p1/100), fmt_dec(1 + p2/100), tong_nay,
                      tong_ngoai, fmt_dec(1 + p1/100), fmt_dec(1 + p2/100), tong_nay,
                      tong_ngoai, x0, y0,
                      x0, y0,
                      fmt_dec(1 + p1/100), x0, x_nay,
                      fmt_dec(1 + p2/100), y0, y_nay))
    
    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    

    return content
