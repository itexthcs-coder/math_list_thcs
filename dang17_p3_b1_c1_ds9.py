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


def bt_dang17_p3_b1_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Giá bán lẻ của 1 bánh burger (x) và 1 phần khoai tây chiên (y) tính theo nghìn đồng
        gia_burger = randint(35, 60)
        gia_khoai = randint(20, gia_burger - 5)
        
        # Số lượng burger và khoai trong từng combo
        b1 = 2
        k1 = 1
        b2 = 1
        k2 = 2
        
        # Giá bán của combo 1 và combo 2 (nghìn đồng)
        gia_cb1 = b1 * gia_burger + k1 * gia_khoai
        gia_cb2 = b2 * gia_burger + k2 * gia_khoai
        
        # Nhân đôi combo 1:
        # 2 combo 1 gồm: 4 burger + 2 khoai tây chiên
        gia_cb1_gap_doi = 2 * gia_cb1
        so_burger_cb1_gap_doi = 2 * b1
        
        # Trừ đi combo 2:
        # (4 burger + 2 khoai) - (1 burger + 2 khoai) = 3 burger
        chenh_lech_burger = so_burger_cb1_gap_doi - b2
        chenh_lech_tien = gia_cb1_gap_doi - gia_cb2
        
        # Kết quả cần tìm: giá bán lẻ của 1 chiếc bánh burger
        kq = gia_burger
        kq_str = str(kq)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Tại một quán ăn nhanh, combo 1 gồm %s bánh burger và %s phần khoai tây chiên có giá %s nghìn đồng. Combo 2 gồm %s bánh burger và %s phần khoai tây chiên có giá %s nghìn đồng. Hỏi giá bán lẻ của $1$ chiếc bánh burger là bao nhiêu nghìn đồng?'''
                         %(str(b1), str(k1), str(gia_cb1),
                           str(b2), str(k2), str(gia_cb2)
                         ))
    
        # Nội dung lời giải
        loigiai = ('''Nếu mua $2$ combo 1 thì gồm có: \\\\
    $%s \\cdot 2 = %s$ (bánh burger) và $%s \\cdot 2 = %s$ (phần khoai tây chiên). \\\\
    Số tiền mua $2$ combo 1 là: \\\\
    $%s \\cdot 2 = %s$ (nghìn đồng). \\\\
    Combo 2 gồm có $%s$ bánh burger và $%s$ phần khoai tây chiên có giá $%s$ nghìn đồng. \\\\
    Do số phần khoai tây chiên ở $2$ combo 1 và combo 2 là như nhau (đều là $%s$ phần), nên $2$ combo 1 nhiều hơn combo 2 số bánh burger là: \\\\
    $%s - %s = %s$ (bánh burger). \\\\
    Số tiền chênh lệch giữa $2$ combo 1 và combo 2 là: \\\\
    $%s - %s = %s$ (nghìn đồng). \\\\
    Giá bán lẻ của $1$ chiếc bánh burger là: \\\\
    $%s : %s = %s$ (nghìn đồng). \\\\
    Vậy giá bán lẻ của $1$ chiếc bánh burger là $%s$ nghìn đồng.'''
                   %(str(b1), str(so_burger_cb1_gap_doi), str(k1), str(2 * k1),
                     str(gia_cb1), str(gia_cb1_gap_doi),
                     str(b2), str(k2), str(gia_cb2),
                     str(k2),
                     str(so_burger_cb1_gap_doi), str(b2), str(chenh_lech_burger),
                     str(gia_cb1_gap_doi), str(gia_cb2), str(chenh_lech_tien),
                     str(chenh_lech_tien), str(chenh_lech_burger), str(kq_str),
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
