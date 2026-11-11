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


def bt_dang15_p3_b1_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Giá tiền 1 kg Robusta (gia_ro) và 1 kg Arabica (gia_ar) tính theo nghìn đồng
        # gia_ro < gia_ar
        gia_ro = randint(50, 75)
        gia_ar = gia_ro + randint(20, 45)
        
        # Khối lượng từng loại cà phê cần trộn (kg)
        m_ro = randint(15, 40)
        m_ar = randint(15, 40)
        
        # Tổng khối lượng cà phê trộn
        tong_m = m_ro + m_ar
        
        # Tổng giá trị tiền (nghìn đồng)
        tong_tien = m_ro * gia_ro + m_ar * gia_ar
        
        # Đảm bảo giá trung bình mỗi kg là số nguyên
        while tong_tien % tong_m != 0:
            m_ro = randint(15, 40)
            m_ar = randint(15, 40)
            tong_m = m_ro + m_ar
            tong_tien = m_ro * gia_ro + m_ar * gia_ar
            
        gia_tb = tong_tien // tong_m
        
        # Giả sử cả tong_m kg đều là cà phê Arabica
        tien_neu_toan_ar = tong_m * gia_ar
        # Số tiền chênh lệch so với thực tế
        chenh_lech_tien = tien_neu_toan_ar - tong_tien
        # Mỗi kg Arabica đắt hơn mỗi kg Robusta số tiền là
        chenh_lech_gia = gia_ar - gia_ro
        
        # Kết quả cần tìm: số kg cà phê Robusta
        kq = m_ro
        kq_str = str(kq)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một cửa hàng muốn tạo ra %s kg cà phê trộn có giá %s nghìn đồng/kg bằng cách trộn cà phê Robusta (giá %s nghìn đồng/kg) và cà phê Arabica (giá %s nghìn đồng/kg). Hỏi cửa hàng cần sử dụng bao nhiêu kg cà phê Robusta?'''
                         %(str(tong_m),
                           str(gia_tb),
                           str(gia_ro),
                           str(gia_ar)
                         ))
    
        # Nội dung lời giải
        loigiai = ('''Tổng số tiền để mua $%s\\text{ kg}$ cà phê trộn là: \\\\
    $%s \\cdot %s = %s$ (nghìn đồng). \\\\
    Giả sử cả $%s\\text{ kg}$ cà phê đều là cà phê Arabica thì tổng số tiền phải trả là: \\\\
    $%s \\cdot %s = %s$ (nghìn đồng). \\\\
    Số tiền theo giả thiết nhiều hơn số tiền thực tế là: \\\\
    $%s - %s = %s$ (nghìn đồng). \\\\
    Mỗi ki-lô-gam cà phê Arabica đắt hơn mỗi ki-lô-gam cà phê Robusta số tiền là: \\\\
    $%s - %s = %s$ (nghìn đồng). \\\\
    Cửa hàng cần sử dụng số ki-lô-gam cà phê Robusta là: \\\\
    $%s : %s = %s\\text{ (kg)}$. \\\\
    Vậy cửa hàng cần sử dụng $%s\\text{ kg}$ cà phê Robusta.'''
                   %(str(tong_m),
                     str(tong_m), str(gia_tb), str(tong_tien),
                     str(tong_m),
                     str(tong_m), str(gia_ar), str(tien_neu_toan_ar),
                     str(tien_neu_toan_ar), str(tong_tien), str(chenh_lech_tien),
                     str(gia_ar), str(gia_ro), str(chenh_lech_gia),
                     str(chenh_lech_tien), str(chenh_lech_gia), str(kq_str),
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
