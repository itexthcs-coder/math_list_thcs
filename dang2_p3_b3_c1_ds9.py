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


def bt_dang2_p3_b3_c1_ds9(self):
    def fmt_gio_phut(phut):
        h = phut // 60
        m = phut % 60
        if h == 0:
            return f"{m}\\text{{ phút}}"
        elif m == 0:
            return f"{h}\\text{{ giờ}}"
        return f"{h}\\text{{ giờ }} {m}\\text{{ phút}}"
    
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        v_tai = random.choice([42, 45, 48, 51, 54])
        dv = random.choice([12, 15, 18])
        v_khach = v_tai + dv
    
        t_truoc_phut = random.choice([60, 80, 100])
        t_chung_phut = random.choice([40, 60])
    
        t_khach_tong_phut = t_truoc_phut + t_chung_phut
        t_khach_gio = Rational(t_khach_tong_phut, 60)
        t_tai_gio = Rational(t_chung_phut, 60)
        S_tong = int(v_tai * t_tai_gio + v_khach * t_khach_gio)
    
        kq_str = str(v_tai)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một chiếc xe khách đi từ Thành phố Hồ Chí Minh đến Cần Thơ, quãng đường dài $%s\\text{ km}$. Sau khi xe khách xuất phát $%s$, một chiếc xe tải bắt đầu đi từ Cần Thơ về Thành phố Hồ Chí Minh trên cùng một tuyến đường và gặp xe khách sau đó $%s$. Biết rằng mỗi giờ xe khách đi nhanh hơn xe tải $%s\\text{ km}$. Tính vận tốc (đơn vị: $\\text{km/h}$) của xe tải.''' % (S_tong, fmt_gio_phut(t_truoc_phut), fmt_gio_phut(t_chung_phut), dv))
    
        # Nội dung lời giải
        loigiai = ('''Gọi $x\\text{ (km/h)}$ là vận tốc của xe tải và $y\\text{ (km/h)}$ là vận tốc của xe khách ($x > 0, y > 0$). \\\\
                   Mỗi giờ xe khách đi nhanh hơn xe tải $%s\\text{ km}$ nên ta có phương trình $y - x = %s$. \\\\
                   Tính đến lúc gặp nhau, xe tải đi trong $%s = %s\\text{ giờ}$ và xe khách đi trong $%s + %s = %s = %s\\text{ giờ}$. \\\\
                   Vì hai xe đi ngược chiều gặp nhau nên tổng quãng đường hai xe đi được bằng $%s\\text{ km}$, ta có hệ phương trình:
                   $$\\begin{cases} y - x = %s \\\\ %sx + %sy = %s. \\end{cases}$$
                   Giải hệ phương trình trên, ta được $x = %s$ và $y = %s$ (thỏa mãn). \\\\
                   Vậy vận tốc của xe tải là $%s\\text{ km/h}$.'''
                   % (dv, dv,
                      fmt_gio_phut(t_chung_phut), latex(t_tai_gio),
                      fmt_gio_phut(t_truoc_phut), fmt_gio_phut(t_chung_phut), fmt_gio_phut(t_khach_tong_phut), latex(t_khach_gio),
                      S_tong, dv, latex(t_tai_gio), latex(t_khach_gio), S_tong,
                      v_tai, v_khach, v_tai))
    
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
    
    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
