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


def bt_dang4_p3_b1_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # t1: thời gian xuôi dòng (giờ), t2: thời gian ngược dòng (giờ)
        # v_nuoc: vận tốc dòng nước (km/h)
        # Vận tốc thực của ca nô là v:
        # Quãng đường: s = (v + v_nuoc) * t1 = (v - v_nuoc) * t2
        # => v * (t2 - t1) = v_nuoc * (t1 + t2)
        # => v = v_nuoc * (t1 + t2) / (t2 - t1)
        
        # Để nghiệm v nguyên đẹp, chọn t1, t2 sao cho (t2 - t1) là ước của (t1 + t2) hoặc v_nuoc chia hết
        t1 = randint(2, 4)
        t2 = t1 + randint(1, 2)
        
        # Chọn v_nuoc sao cho v nguyên dương
        # v_nuoc chia hết cho (t2 - t1) / gcd(t1 + t2, t2 - t1)
        hieu_t = t2 - t1
        tong_t = t1 + t2
        ucln = math.gcd(tong_t, hieu_t)
        mau_so = hieu_t // ucln
        
        he_so = randint(1, 4)
        v_nuoc = he_so * mau_so
        
        v = (v_nuoc * tong_t) // hieu_t
        
        # Kết quả cần tìm: vận tốc thực của ca nô
        kq = v
        kq_str = str(kq)
        
        # Các bước tính toán trung gian phục vụ lời giải chi tiết
        hai_lan_v_nuoc = 2 * v_nuoc
        v_lech = hai_lan_v_nuoc
        tich_v_lech_t1 = v_lech * t1
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một ca nô đi xuôi dòng mất %s giờ và đi ngược dòng mất %s giờ cho cùng một quãng đường sông. Biết vận tốc của dòng nước là %s\\text{ km/h}. Hỏi vận tốc thực của ca nô (khi nước yên lặng) là bao nhiêu km/h?'''
                         %(str(t1),
                           str(t2),
                           str(v_nuoc)
                         ))
    
        # Nội dung lời giải
        loigiai = ('''Vận tốc ca nô khi xuôi dòng bằng vận tốc thực cộng với vận tốc dòng nước. \\\\
    Vận tốc ca nô khi ngược dòng bằng vận tốc thực trừ đi vận tốc dòng nước. \\\\
    Do đó, hiệu vận tốc khi xuôi dòng và ngược dòng bằng $2$ lần vận tốc dòng nước, tức là: \\\\
    $%s \\cdot 2 = %s\\text{ (km/h)}$. \\\\
    Gọi $v\\text{ (km/h)}$ là vận tốc thực của ca nô ($v > %s$). \\\\
    Vận tốc khi xuôi dòng là $v + %s\\text{ (km/h)}$. \\\\
    Vận tốc khi ngược dòng là $v - %s\\text{ (km/h)}$. \\\\
    Vì quãng đường đi xuôi dòng và ngược dòng là như nhau nên ta có phương trình: \\\\
    $%s \\cdot (v + %s) = %s \\cdot (v - %s)$ \\\\
    $\\Leftrightarrow %s \\cdot v + %s = %s \\cdot v - %s$ \\\\
    $\\Leftrightarrow %s \\cdot v - %s \\cdot v = %s + %s$ \\\\
    $\\Leftrightarrow %s \\cdot v = %s \\Leftrightarrow v = %s\\text{ (km/h)}$. \\\\
    Vậy vận tốc thực của ca nô là $%s\\text{ km/h}$.'''
                   %(str(v_nuoc), str(hai_lan_v_nuoc),
                     str(v_nuoc),
                     str(v_nuoc),
                     str(v_nuoc),
                     str(t1), str(v_nuoc), str(t2), str(v_nuoc),
                     str(t1), str(t1 * v_nuoc), str(t2), str(t2 * v_nuoc),
                     str(t2), str(t1), str(t1 * v_nuoc), str(t2 * v_nuoc),
                     str(hieu_t), str(t1 * v_nuoc + t2 * v_nuoc), str(kq_str),
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
