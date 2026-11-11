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


def bt_dang6_p3_b1_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Nồng độ c1 < c2 (đơn vị %)
        # Dung dịch cần pha có khối lượng m (gam), nồng độ c% (c1 < c < c2)
        # Gọi khối lượng dung dịch c2% là x (gam), dung dịch c1% là m - x (gam)
        # Lượng muối: x * c2/100 + (m - x) * c1/100 = m * c/100
        # => x * (c2 - c1) = m * (c - c1)
        # => x = m * (c - c1) / (c2 - c1)
        
        # Chọn c1 và c2 là các số tròn chục hoặc bội số của 5
        c1 = randint(1, 3) * 5       # ví dụ: 5, 10, 15
        c2 = c1 + randint(2, 5) * 5  # ví dụ: c1 + 10, 15, 20...
        
        # Để nghiệm x nguyên đẹp, ta chọn x trước, sau đó tính m và c
        # Chọn x (khối lượng dung dịch c2%) và y (khối lượng dung dịch c1%)
        x_dd = randint(3, 15) * 10
        y_dd = randint(3, 15) * 10
        m_dd = x_dd + y_dd
        
        # Tính khối lượng muối nguyên chất
        muoi1 = (y_dd * c1) // 100
        muoi2 = (x_dd * c2) // 100
        tong_muoi = (y_dd * c1 + x_dd * c2) / 100
        
        # Đảm bảo c là số nguyên thỏa mãn:
        # (y_dd * c1 + x_dd * c2) % m_dd == 0
        # Để chắc chắn, ta chọn trực tiếp c nguyên sao cho x nguyên:
        c_diff = c2 - c1
        # Chọn ngẫu nhiên k sao cho 0 < k < c_diff
        k = randint(1, c_diff - 1)
        c_target = c1 + k
        
        # Để x = m * k / c_diff nguyên, m_dd chia hết cho c_diff / gcd(k, c_diff)
        ucln = math.gcd(k, c_diff)
        mau = c_diff // ucln
        m_dd = mau * randint(10, 30)
        x_dd = (m_dd * k) // c_diff
        y_dd = m_dd - x_dd
        
        # Tính lượng muối
        muoi_tong = (m_dd * c_target) / 100
        muoi_tong_str = str(muoi_tong).replace('.', ',') if muoi_tong % 1 != 0 else str(int(muoi_tong))
        
        # Kết quả cần tìm: khối lượng dung dịch c2%
        kq = x_dd
        kq_str = str(kq)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong phòng thí nghiệm, một học sinh cần pha chế %s gam dung dịch nước muối có nồng độ %s\\%%. Học sinh này có sẵn hai chai dung dịch muối nồng độ %s\\%% và %s\\%%. Hỏi cần lấy bao nhiêu gam dung dịch %s\\%% để pha trộn?'''
                         %(str(m_dd),
                           str(c_target),
                           str(c1),
                           str(c2),
                           str(c2)
                         ))
    
        # Nội dung lời giải
        loigiai = ('''Khối lượng muối nguyên chất cần có trong $%s$ gam dung dịch muối nồng độ $%s\\%%$ là: \\\\
    $%s \\cdot %s\\%% = %s$ (gam). \\\\
    Gọi khối lượng dung dịch muối nồng độ $%s\\%%$ cần lấy là $x$ (gam, $0 < x < %s$). \\\\
    Khối lượng dung dịch muối nồng độ $%s\\%%$ cần lấy là: \\\\
    $%s - x$ (gam). \\\\
    Lượng muối nguyên chất có trong $x$ gam dung dịch nồng độ $%s\\%%$ là: \\\\
    $x \\cdot %s\\%% = %s \\cdot x$ (gam). \\\\
    Lượng muối nguyên chất có trong $%s - x$ gam dung dịch nồng độ $%s\\%%$ là: \\\\
    $(%s - x) \\cdot %s\\%% = %s \\cdot (%s - x)$ (gam). \\\\
    Theo đề bài, tổng khối lượng muối trong hai dung dịch đem trộn bằng lượng muối có trong dung dịch mới, nên ta có phương trình: \\\\
    $%s \\cdot x + %s \\cdot (%s - x) = %s$ \\\\
    $\\Leftrightarrow %s \\cdot x + %s - %s \\cdot x = %s$ \\\\
    $\\Leftrightarrow %s \\cdot x = %s \\Leftrightarrow x = %s$. \\\\
    Vậy cần lấy $%s$ gam dung dịch nồng độ $%s\\%%$ để pha trộn.'''
                   %(str(m_dd), str(c_target),
                     str(m_dd), str(c_target), str(muoi_tong_str),
                     str(c2), str(m_dd),
                     str(c1),
                     str(m_dd),
                     str(c2),
                     str(c2), str(Rational(c2, 100)),
                     str(m_dd), str(c1),
                     str(m_dd), str(c1), str(Rational(c1, 100)), str(m_dd),
                     str(Rational(c2, 100)), str(Rational(c1, 100)), str(m_dd), str(muoi_tong_str),
                     str(Rational(c2, 100)), str(Rational(c1 * m_dd, 100)), str(Rational(c1, 100)), str(muoi_tong_str),
                     str(Rational(c2 - c1, 100)), str(Rational(m_dd * c_target - c1 * m_dd, 100)), str(kq_str),
                     str(kq_str), str(c2)
                   ))
    
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(str(kq_str))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n' +
               '\\end{minipage} \n\n')
    return content
