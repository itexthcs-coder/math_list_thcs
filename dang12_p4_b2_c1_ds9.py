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


def bt_dang12_p4_b2_c1_ds9(self):
    # Khai báo biến
    def fmt_tp(val):
        return str(val).replace('.', ',')
    
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = random.choice([
            (20, 5, 10, 1.5, 1500),   # x = 500, y = 1000
            (20, 5, 10, 3, 3000),     # x = 1000, y = 2000
            (25, 10, 15, 2.4, 2400),  # x = 800, y = 1600
            (30, 15, 20, 1.8, 1800)   # x = 600, y = 1200
        ])
        c1, c2, chh, V_lit, V_ml = bo_so
        hcl_nc = (chh * V_ml) // 100
        x0 = V_ml // 3
        y0 = 2 * x0
    
        hs1_tp = fmt_tp(c1 / 100)
        hs2_tp = fmt_tp(c2 / 100)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Tính số mililít dung dịch acid $\\text{HCl}$ nồng độ $%s\\%%$ và số mililít dung dịch acid $\\text{HCl}$ nồng độ $%s\\%%$ cần dùng để pha chế $%s\\text{ lít}$ dung dịch acid $\\text{HCl}$ nồng độ $%s\\%%$.'''
                         % (latex(c1), latex(c2), fmt_tp(V_lit), latex(chh)))
    
        # Nội dung lời giải
        loigiai = ('''Đổi $%s\\text{ lít} = %s\\text{ ml}$. \\\\
                   Gọi $x\\text{ (ml)}$ là số mililít dung dịch acid $\\text{HCl}$ nồng độ $%s\\%%$ và $y\\text{ (ml)}$ là số mililít dung dịch acid $\\text{HCl}$ nồng độ $%s\\%%$ cần lấy ($x, y > 0$). \\\\
                   Thể tích dung dịch acid $\\text{HCl } %s\\%%$ nhận được sau khi trộn lẫn là $x + y = %s\\text{ (ml)}$. \\\\
                   Tổng số mililít acid $\\text{HCl}$ nguyên chất có trong hai dung dịch là $%sx + %sy = %s \\cdot %s\\%% = %s\\text{ (ml)}$. \\\\
                   Ta có hệ phương trình $\\begin{cases} x + y = %s \\\\ %sx + %sy = %s \\end{cases}$. \\\\
                   Giải hệ phương trình trên, ta tìm được $x = %s$ và $y = %s$ (thỏa mãn điều kiện). \\\\
                   Vậy cần dùng $%s\\text{ ml}$ dung dịch acid $\\text{HCl}$ nồng độ $%s\\%%$ và $%s\\text{ ml}$ dung dịch acid $\\text{HCl}$ nồng độ $%s\\%%$.'''
                   % (fmt_tp(V_lit), latex(V_ml),
                      latex(c1), latex(c2),
                      latex(chh), latex(V_ml),
                      hs1_tp, hs2_tp, latex(V_ml), latex(chh), latex(hcl_nc),
                      latex(V_ml), hs1_tp, hs2_tp, latex(hcl_nc),
                      latex(x0), latex(y0),
                      latex(x0), latex(c1), latex(y0), latex(c2)))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
