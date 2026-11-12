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


def bt_dang20_p3_b3_c1_ds9(self):
    def fmt_dec(val):
        if val == int(val):
            return str(int(val))
        return str(round(val, 2)).replace('.', '{,}')
    
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cases = [
            (4, 4, 6, 2.5, 44, 14),  # cách đây 4 năm: 40 = 4*10; sau 6 năm: 50 = 2.5*20
            (5, 4, 5, 2.5, 45, 15),  # cách đây 5 năm: 40 = 4*10; sau 5 năm: 50 = 2.5*20
            (3, 4, 7, 2.5, 43, 13),  # cách đây 3 năm: 40 = 4*10; sau 7 năm: 50 = 2.5*20
            (6, 5, 4, 3, 46, 14)     # cách đây 6 năm: 40 = 5*8; sau 4 năm: 50 = 3*18? Không: 42 = 3*14 => x=38, y=10 (32=4*8, 42=3*14)
        ]
        # Kiểm tra lại bộ 4: nếu y0 = 10, x0 = 38 => cách đây 4 năm: 34 != 5*6. Dùng 4 bộ chuẩn xác:
        valid_cases = [
            (4, 4, 6, 2.5, 44, 14),
            (5, 4, 5, 2.5, 45, 15),
            (3, 4, 7, 2.5, 43, 13),
            (4, 5, 6, 2.5, 34, 10)   # cách đây 4 năm: 30 = 5*6; sau 6 năm: 40 = 2.5*16
        ]
        t_truoc, k_truoc, t_sau, k_sau, x0, y0 = random.choice(valid_cases)
        tong_tuoi = x0 + y0
        kq_str = str(tong_tuoi)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cách đây $%s\\text{ năm}$, tuổi của mẹ gấp $%s$ lần tuổi của con. Sau $%s\\text{ năm}$ nữa (tính từ hiện nay), tuổi của mẹ chỉ còn gấp $%s$ lần tuổi của con. Tính tổng số tuổi của hai mẹ con hiện nay.''' % (t_truoc, k_truoc, t_sau, fmt_dec(k_sau)))
    
        # Nội dung lời giải
        loigiai = ('''Gọi $x$ (tuổi) và $y$ (tuổi) lần lượt là tuổi của mẹ và tuổi của con hiện nay ($x > y > %s$). \\\\
                   Ta lập được hệ phương trình:
                   $$\\begin{cases} x - %s = %s(y - %s) \\\\ x + %s = %s(y + %s) \\end{cases} \\Leftrightarrow \\begin{cases} x - %sy = %s \\\\ x - %sy = %s. \\end{cases}$$
                   Giải hệ phương trình trên, ta được $x = %s$ và $y = %s$ (thỏa mãn). \\\\
                   Vậy tổng số tuổi của hai mẹ con hiện nay là $%s + %s = %s\\text{ (tuổi)}$.'''
                   % (t_truoc,
                      t_truoc, k_truoc, t_truoc,
                      t_sau, fmt_dec(k_sau), t_sau,
                      k_truoc, t_truoc - k_truoc * t_truoc,
                      fmt_dec(k_sau), int(k_sau * t_sau - t_sau),
                      x0, y0, x0, y0, tong_tuoi))
    
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
    
    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
