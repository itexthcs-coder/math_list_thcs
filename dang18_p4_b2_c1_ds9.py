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


def bt_dang18_p4_b2_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            x0 = random.choice([18, 20, 22, 24])
            y0 = random.choice([12, 14, 15, 16])
            dx = random.choice([3, 4, 5])
            dy = random.choice([2, 3, 4])
            if x0 > y0 and x0 > dx and x0 * y0 > (x0 - dx) * (y0 + dy):
                break
    
        nua_cv = x0 + y0
        chu_vi = 2 * nua_cv
        giam_dt = x0 * y0 - (x0 - dx) * (y0 + dy)
        vp_dt = -giam_dt + dx * dy
    
        pt_dt_rg = latex(dy * x - dx * y) + '=' + latex(vp_dt)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một khu vườn hình chữ nhật có chu vi là $%s\\text{ m}$. Nếu tăng chiều rộng thêm $%s\\text{ m}$ và giảm chiều dài đi $%s\\text{ m}$ thì diện tích khu vườn giảm đi $%s\\text{ m}^2$. Tính chiều dài và chiều rộng ban đầu của khu vườn.'''
                         % (latex(chu_vi), latex(dy), latex(dx), latex(giam_dt)))
    
        # Nội dung lời giải
        loigiai = ('''Gọi chiều dài và chiều rộng ban đầu của khu vườn lần lượt là $x\\text{ (m)}$ và $y\\text{ (m)}$ ($x > y > 0; x > %s$). \\\\
                   Nửa chu vi của khu vườn là $x + y = %s : 2 = %s\\text{ (m)}$. \\\\
                   Diện tích ban đầu của khu vườn là $xy\\text{ (m}^2\\text{)}$. Khi tăng chiều rộng thêm $%s\\text{ m}$ và giảm chiều dài đi $%s\\text{ m}$ thì diện tích mới là $(x - %s)(y + %s)\\text{ (m}^2\\text{)}$. \\\\
                   Theo đề bài ta có phương trình: \\\\
                   $(x - %s)(y + %s) = xy - %s \\Leftrightarrow xy + %sx - %sy - %s = xy - %s \\Leftrightarrow %s$. \\\\
                   Từ đó ta có hệ phương trình $\\begin{cases} x + y = %s \\\\ %s \\end{cases}$. \\\\
                   Giải hệ phương trình trên, ta tìm được $x = %s$ và $y = %s$ (thỏa mãn điều kiện). \\\\
                   Vậy chiều dài ban đầu của khu vườn là $%s\\text{ m}$ và chiều rộng ban đầu là $%s\\text{ m}$.'''
                   % (latex(dx), latex(chu_vi), latex(nua_cv),
                      latex(dy), latex(dx), latex(dx), latex(dy),
                      latex(dx), latex(dy), latex(giam_dt), latex(dy), latex(dx), latex(dx * dy), latex(giam_dt), pt_dt_rg,
                      latex(nua_cv), pt_dt_rg,
                      latex(x0), latex(y0),
                      latex(x0), latex(y0)))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
