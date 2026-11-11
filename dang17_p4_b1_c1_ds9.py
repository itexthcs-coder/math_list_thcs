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


def bt_dang17_p4_b1_c1_ds9(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            x_val = random.choice([300, 400, 500, 600, 700])
            y_val = 1000 - x_val
            pA, pB = random.choice([70, 75, 80, 85]), random.choice([50, 55, 60, 65])
            t_dung = pA * x_val / 100 + pB * y_val / 100
            if t_dung.is_integer():
                t_dung = int(t_dung)
                break
                
        noidungcauhoi = ('''Tại một trạm y tế, số lượng vaccine loại A và loại B được dự trữ để tiêm cho trẻ em. Tổng số liều là $1000$ liều. Tuần qua, trạm đã sử dụng $%s\\%%$ số liều loại A và $%s\\%%$ số liều loại B, tổng cộng là $%s$ liều đã tiêm. Tính số liều mỗi loại vaccine lúc ban đầu.''' % (pA, pB, t_dung))
        
        loigiai = ('''Gọi số liều vaccine loại A và loại B lúc ban đầu lần lượt là $x$ và $y$ (liều) ($x, y \\in \\mathbb{N}^*$, $x, y < 1000$).\\\\
    Tổng số liều dự trữ là $1000$ nên ta có phương trình: $x + y = 1000$ (1).\\\\
    Số liều vaccine loại A đã sử dụng là: $\\frac{%s}{100}x = %s x$ (liều).\\\\
    Số liều vaccine loại B đã sử dụng là: $\\frac{%s}{100}y = %s y$ (liều).\\\\
    Tổng số liều đã tiêm là $%s$ liều nên ta có phương trình: $%s x + %s y = %s$ (2).\\\\
    Từ (1) và (2) ta có hệ phương trình:\\\\
    $\\begin{cases} x + y = 1000 \\\\ %s x + %s y = %s \\end{cases}$\\\\
    Giải hệ phương trình, ta được $x = %s$, $y = %s$ (thỏa mãn).\\\\
    Vậy lúc đầu có $%s$ liều loại A và $%s$ liều loại B.''' % (pA, str(pA/100).replace('.', ','), pB, str(pB/100).replace('.', ','), t_dung, str(pA/100).replace('.', ','), str(pB/100).replace('.', ','), t_dung, str(pA/100).replace('.', ','), str(pB/100).replace('.', ','), t_dung, x_val, y_val, x_val, y_val))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \\n'
               '\\begin{ex}\\n'+
               str(noidungcauhoi)+
               '\\loigiai{ \\n' +str(loigiai)+'}\\n'
               '\\end{ex}\\n'
               '\\end{minipage} \\n\\n')
    return content
