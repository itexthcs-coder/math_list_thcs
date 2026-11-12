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


def bt_dang16_p3_b6_c2_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x = symbols('x')
        # Tổng 4 bài TX (hệ số 1): tong_tx; GK (hệ số 2): gk; CK (hệ số 3): x. Tổng hệ số = 9.
        # Mục tiêu TB >= 8.0 <=> tong_tx + 2*gk + 3x >= 72
        tong_tx = randint(32, 36)
        gk = random.choice([8.0, 8.5, 9.0])
        da_co = tong_tx + 2*gk
        while (72 - da_co) % 3 == 0:
            tong_tx += 1
            da_co = tong_tx + 2*gk
        x_min = (72 - da_co) / 3
        # Làm tròn lên đến 1 chữ số thập phân để đảm bảo >= 8.0
        kq = math.ceil(x_min * 10) / 10
        kq_str = str(kq).replace('.', ',')
    
        noidungcauhoi = ('''Điểm tổng kết môn Toán của bạn Hà được tính theo công thức: trung bình cộng của $4$ bài kiểm tra thường xuyên (hệ số $1$), $1$ bài kiểm tra giữa kì (hệ số $2$) và $1$ bài kiểm tra cuối kì (hệ số $3$). Hiện tại, tổng điểm $4$ bài thường xuyên của Hà là $%s$ điểm và điểm giữa kì là $%s$ điểm. Hỏi bài kiểm tra cuối kì bạn Hà cần đạt ít nhất bao nhiêu điểm (làm tròn đến chữ số thập phân thứ nhất) để điểm tổng kết môn Toán đạt từ $8,0$ trở lên?'''
                         % (tong_tx, str(gk).replace('.', ',')))
    
        loigiai = ('''Gọi $x$ ($0 \\le x \\le 10$) là điểm bài kiểm tra cuối kì của bạn Hà. Tổng số hệ số là $4 + 2 + 3 = 9$.\\\\
        Điểm tổng kết môn Toán của Hà là $\\dfrac{%s + %s \\cdot 2 + 3x}{9} = \\dfrac{%s + 3x}{9}$.\\\\
        Để điểm tổng kết đạt từ $8,0$ trở lên, ta có bất phương trình:
        $$\\dfrac{%s + 3x}{9} \\ge 8,0 \\Leftrightarrow %s + 3x \\ge 72 \\Leftrightarrow 3x \\ge %s \\Leftrightarrow x \\ge %.3f.$$
        Làm tròn kết quả đến chữ số thập phân thứ nhất sao cho đảm bảo điều kiện, bạn Hà cần đạt ít nhất $%s$ điểm.'''
                   % (tong_tx, str(gk).replace('.', ','), str(da_co).replace('.', ','),
                      str(da_co).replace('.', ','), str(da_co).replace('.', ','),
                      str(round(72 - da_co, 1)).replace('.', ','), x_min, kq_str))
    
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
    
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
