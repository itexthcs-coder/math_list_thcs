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


def bt_dang3_p4_b1_c1_ds9(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            x_val, y_val = randint(40, 60), randint(30, 45)
            if x_val <= y_val: continue
            t1 = random.choice([1.5, 2.0, 2.5])
            S = t1 * (x_val + y_val)
            if not S.is_integer(): continue
            S = int(S)
            t2, t3 = random.choice([0.5, 1.0, 1.5]), random.choice([1.0, 1.5, 2.0])
            if (t2 + t3) * x_val + t3 * y_val == S: break
            
        t1_s = str(t1).replace('.', ',') if t1 != int(t1) else str(int(t1))
        t2_s = str(t2).replace('.', ',') if t2 != int(t2) else str(int(t2))
        t3_s = str(t3).replace('.', ',') if t3 != int(t3) else str(int(t3))
        t23_s = str(t2+t3).replace('.', ',') if (t2+t3) != int(t2+t3) else str(int(t2+t3))
        
        noidungcauhoi = ('''Hai thành phố A và B cách nhau $%s$ km. Một ô tô đi từ A đến B và một xe máy đi từ B về A, hai xe khởi hành cùng một lúc và gặp nhau sau $%s$ giờ. Nếu ô tô khởi hành trước xe máy $%s$ giờ thì hai xe gặp nhau sau khi xe máy đi được $%s$ giờ. Tính vận tốc của mỗi xe.''' % (S, t1_s, t2_s, t3_s))
        
        loigiai = ('''Gọi vận tốc của ô tô là $x$ (km/h) và vận tốc của xe máy là $y$ (km/h) ($x > y > 0$).\\\\
    Hai xe khởi hành cùng lúc và đi ngược chiều, gặp nhau sau $%s$ giờ nên tổng quãng đường hai xe đi được là khoảng cách AB:\\\\
    $%s x + %s y = %s$ (1).\\\\
    Nếu ô tô đi trước $%s$ giờ, xe máy đi $%s$ giờ thì gặp nhau, nghĩa là ô tô đã đi tất cả $%s + %s = %s$ giờ. Khi đó ta có phương trình:\\\\
    $%s x + %s y = %s$ (2).\\\\
    Từ (1) và (2) ta có hệ phương trình:\\\\
    $\\begin{cases} %s x + %s y = %s \\\\ %s x + %s y = %s \\end{cases}$\\\\
    Giải hệ phương trình ta được $x = %s$, $y = %s$ (thỏa mãn).\\\\
    Vậy vận tốc ô tô là $%s$ km/h, vận tốc xe máy là $%s$ km/h.''' % (t1_s, t1_s, t1_s, S, t2_s, t3_s, t2_s, t3_s, t23_s, t23_s, t3_s, S, t1_s, t1_s, S, t23_s, t3_s, S, x_val, y_val, x_val, y_val))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \\n'
               '\\begin{ex}\\n'+
               str(noidungcauhoi)+
               '\\loigiai{ \\n' +str(loigiai)+'}\\n'
               '\\end{ex}\\n'
               '\\end{minipage} \\n\\n')
    return content
