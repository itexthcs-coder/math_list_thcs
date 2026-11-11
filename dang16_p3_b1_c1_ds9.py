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


def bt_dang16_p3_b1_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Mệnh giá 2 loại tiền (nghìn đồng)
        menh_gia_1 = 50
        menh_gia_2 = 100
        
        # Số tờ tiền loại 50 nghìn đồng và loại 100 nghìn đồng
        to_50 = randint(5, 25)
        to_100 = randint(5, 25)
        
        tong_to = to_50 + to_100
        tong_tien = to_50 * menh_gia_1 + to_100 * menh_gia_2
        
        # Giả sử tất cả đều là tờ 50 nghìn đồng
        tien_neu_toan_50 = tong_to * menh_gia_1
        # Số tiền chênh lệch
        chenh_lech_tien = tong_tien - tien_neu_toan_50
        # Chênh lệch mỗi tờ
        chenh_lech_menh_gia = menh_gia_2 - menh_gia_1
        
        # Kết quả cần tìm: số tờ 100 nghìn đồng
        kq = to_100
        kq_str = str(kq)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một người đi rút tiền tại ATM được trả %s tờ tiền gồm hai mệnh giá %s nghìn đồng và %s nghìn đồng. Tổng số tiền rút là %s nghìn đồng. Hỏi máy ATM đã nhả ra bao nhiêu tờ %s nghìn đồng?'''
                         %(str(tong_to),
                           str(menh_gia_1),
                           str(menh_gia_2),
                           str(tong_tien),
                           str(menh_gia_2)
                         ))
    
        # Nội dung lời giải
        loigiai = ('''Giả sử tất cả $%s$ tờ tiền đều có mệnh giá $%s$ nghìn đồng thì tổng số tiền rút được là: \\\\
    $%s \\cdot %s = %s$ (nghìn đồng). \\\\
    Số tiền thực tế nhiều hơn số tiền theo giả thiết là: \\\\
    $%s - %s = %s$ (nghìn đồng). \\\\
    Mỗi tờ tiền mệnh giá $%s$ nghìn đồng nhiều hơn mỗi tờ tiền mệnh giá $%s$ nghìn đồng số tiền là: \\\\
    $%s - %s = %s$ (nghìn đồng). \\\\
    Số tờ tiền mệnh giá $%s$ nghìn đồng là: \\\\
    $%s : %s = %s$ (tờ). \\\\
    Vậy máy ATM đã nhả ra $%s$ tờ $%s$ nghìn đồng.'''
                   %(str(tong_to), str(menh_gia_1),
                     str(tong_to), str(menh_gia_1), str(tien_neu_toan_50),
                     str(tong_tien), str(tien_neu_toan_50), str(chenh_lech_tien),
                     str(menh_gia_2), str(menh_gia_1),
                     str(menh_gia_2), str(menh_gia_1), str(chenh_lech_menh_gia),
                     str(menh_gia_2),
                     str(chenh_lech_tien), str(chenh_lech_menh_gia), str(kq_str),
                     str(kq_str), str(menh_gia_2)
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
