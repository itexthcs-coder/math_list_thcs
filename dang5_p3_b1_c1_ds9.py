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


def bt_dang5_p3_b1_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Gọi số năm cách đây là t (năm)
        # Tỉ số tuổi bố và con hiện nay là k1 (bố gấp k1 lần con)
        # Tỉ số tuổi bố và con cách đây t năm là k2 (bố gấp k2 lần con, k2 > k1)
        # Hiện nay: B = k1 * C
        # t năm trước: B - t = k2 * (C - t)
        # => k1 * C - t = k2 * C - k2 * t
        # => (k2 - k1) * C = (k2 - 1) * t
        # => C = (k2 - 1) * t / (k2 - k1)
        
        # Chọn ngẫu nhiên k1 và k2 thỏa mãn bài toán thực tế
        k1 = randint(2, 4)       # Tỉ số hiện nay (ví dụ: 2, 3, 4)
        k2 = k1 + randint(1, 3)  # Tỉ số trong quá khứ phải lớn hơn hiện nay
        
        # Để tuổi con C là số nguyên dương:
        # t chia hết cho (k2 - k1) // gcd((k2 - 1), (k2 - k1))
        mau_so = (k2 - k1) // math.gcd(k2 - 1, k2 - k1)
        boi_so = randint(1, 4)
        t = boi_so * mau_so
        
        # Tính tuổi con và tuổi bố hiện nay
        tuoi_con = ((k2 - 1) * t) // (k2 - k1)
        tuoi_bo = k1 * tuoi_con
        
        # Tuổi con và bố cách đây t năm
        tuoi_con_truoc = tuoi_con - t
        tuoi_bo_truoc = tuoi_bo - t
        
        # Chênh lệch hệ số và số hạng tự do
        hieu_k = k2 - k1
        ve_phai = (k2 - 1) * t
        
        # Kết quả cần tìm: tuổi người con năm nay
        kq = tuoi_con
        kq_str = str(kq)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Hiện nay tuổi của bố gấp %s lần tuổi của con. Cách đây %s năm, tuổi của bố gấp %s lần tuổi của con. Hỏi năm nay người con bao nhiêu tuổi?'''
                         %(str(k1),
                           str(t),
                           str(k2)
                         ))
    
        # Nội dung lời giải
        loigiai = ('''Gọi số tuổi hiện nay của người con là $x$ (tuổi, $x > %s$). \\\\
    Vì hiện nay tuổi của bố gấp %s lần tuổi của con nên tuổi hiện nay của người bố là $%s \\cdot x$ (tuổi). \\\\
    Cách đây %s năm: \\\\
    - Tuổi của người con là: $x - %s$ (tuổi). \\\\
    - Tuổi của người bố là: $%s \\cdot x - %s$ (tuổi). \\\\
    Theo đề bài, cách đây %s năm tuổi của bố gấp %s lần tuổi của con nên ta có phương trình: \\\\
    $%s \\cdot x - %s = %s \\cdot (x - %s)$ \\\\
    $\\Leftrightarrow %s \\cdot x - %s = %s \\cdot x - %s$ \\\\
    $\\Leftrightarrow %s \\cdot x - %s \\cdot x = %s - %s$ \\\\
    $\\Leftrightarrow %s \\cdot x = %s \\Leftrightarrow x = %s$. \\\\
    Vậy năm nay người con $%s$ tuổi.'''
                   %(str(t),
                     str(k1), str(k1),
                     str(t),
                     str(t),
                     str(k1), str(t),
                     str(t), str(k2),
                     str(k1), str(t), str(k2), str(t),
                     str(k1), str(t), str(k2), str(k2 * t),
                     str(k2), str(k1), str(k2 * t), str(t),
                     str(hieu_k), str(ve_phai), str(kq_str),
                     str(kq_str)
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
