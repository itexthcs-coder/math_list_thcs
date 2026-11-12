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


def bt_dang20_p3_b2_c2_ds9(self):
    # Dạng 20: Bài toán phân chia thưởng theo KPI kinh doanh
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        luong_cb = random.choice([7000, 7500, 8000]) # nghìn đồng
        thuong_sp = random.choice([150, 180, 200])   # nghìn đồng
        so_sp = randint(18, 35)
        le = random.choice([0, 50, 100])
        muc_tieu = luong_cb + thuong_sp * (so_sp - 1) + (thuong_sp if le == 0 else le)
        can_thuong = muc_tieu - luong_cb
        kq = so_sp
        kq_str = str(kq)
    
        def fmt_t(nghin):
            return f"{nghin * 1000:,}".replace(",", "\\,")
    
        noidungcauhoi = ('''Một nhân viên kinh doanh có mức lương cơ bản là $%s$ đồng/tháng. Ngoài ra, cứ bán được mỗi sản phẩm vượt chỉ tiêu thì nhân viên được thưởng thêm $%s$ đồng. Để tổng thu nhập trong tháng đạt ít nhất $%s$ đồng, nhân viên đó cần bán vượt chỉ tiêu ít nhất bao nhiêu sản phẩm?''' % (fmt_t(luong_cb), fmt_t(thuong_sp), fmt_t(muc_tieu)))
    
        loigiai = ('''Gọi $x$ ($x \\in \\mathbb{N}^*$) là số sản phẩm bán vượt chỉ tiêu. \\\\
                   Tổng thu nhập trong tháng của nhân viên là $%s + %sx$ (đồng). \\\\
                   Để tổng thu nhập đạt ít nhất $%s$ đồng, ta có bất đẳng thức: \\\\
                   $%s + %sx \\ge %s$ \\\\
                   $%sx \\ge %s$ (cộng hai vế với $-%s$) \\\\
                   $x \\ge \\dfrac{%d}{%d}$ (nhân hai vế với $\\dfrac{1}{%s} > 0$). \\\\
                   Vì $x \\in \\mathbb{N}^*$ và $\\dfrac{%d}{%d} %s$ nên nhân viên đó cần bán vượt chỉ tiêu ít nhất $%d$ sản phẩm.'''
                   % (fmt_t(luong_cb), fmt_t(thuong_sp), fmt_t(muc_tieu), fmt_t(luong_cb), fmt_t(thuong_sp), fmt_t(muc_tieu),
                      fmt_t(thuong_sp), fmt_t(can_thuong), fmt_t(luong_cb), can_thuong, thuong_sp, fmt_t(thuong_sp),
                      can_thuong, thuong_sp, f"= {so_sp}" if le == 0 else f"\\approx {round(can_thuong/thuong_sp, 2)}", kq))
    
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
    

    return content
