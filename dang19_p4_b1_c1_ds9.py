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


def bt_dang19_p4_b1_c1_ds9(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        x_val, y_val = randint(40, 80), randint(60, 100)
        a1, b1 = random.choice([(3, 1), (4, 1), (4, 2)])
        a2, b2 = random.choice([(1, 1), (2, 1), (1, 2)])
        if a1 * b2 == a2 * b1:
            a1, b1, a2, b2 = 4, 1, 2, 1
        c1, c2 = a1 * x_val + b1 * y_val, a2 * x_val + b2 * y_val
        
        noidungcauhoi = ('''Một xưởng gỗ sản xuất bàn và ghế. Để đóng $1$ cái bàn cần $%s$ giờ máy cắt và $%s$ giờ thợ mộc; để đóng $1$ cái ghế cần $%s$ giờ máy cắt và $%s$ giờ thợ mộc. Xưởng có tối đa $%s$ giờ máy cắt và $%s$ giờ thợ mộc mỗi tháng. Nếu tận dụng hết công suất, xưởng sẽ đóng được bao nhiêu bàn và bao nhiêu ghế?''' % (a1, a2, b1, b2, c1, c2))
        
        loigiai = ('''Gọi số bàn và số ghế xưởng đóng được lần lượt là $x$ và $y$ (cái) ($x, y \\in \\mathbb{N}^*$).\\\\
    Số giờ máy cắt để đóng $x$ cái bàn là $%s x$ (giờ) và để đóng $y$ cái ghế là $%s y$ (giờ). Vì tổng thời gian máy cắt là $%s$ giờ nên: $%s x + %s y = %s$ (1).\\\\
    Số giờ thợ mộc để đóng $x$ cái bàn là $%s x$ (giờ) và để đóng $y$ cái ghế là $%s y$ (giờ). Vì tổng thời gian thợ mộc là $%s$ giờ nên: $%s x + %s y = %s$ (2).\\\\
    Từ (1) và (2) ta có hệ phương trình:\\\\
    $\\begin{cases} %s x + %s y = %s \\\\ %s x + %s y = %s \\end{cases}$\\\\
    Giải hệ phương trình, ta được $x = %s$, $y = %s$ (thỏa mãn).\\\\
    Vậy xưởng đóng được $%s$ bàn và $%s$ ghế.''' % (a1, b1, c1, a1, b1, c1, a2, b2, c2, a2, b2, c2, a1, b1, c1, a2, b2, c2, x_val, y_val, x_val, y_val))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \\n'
               '\\begin{ex}\\n'+
               str(noidungcauhoi)+
               '\\loigiai{ \\n' +str(loigiai)+'}\\n'
               '\\end{ex}\\n'
               '\\end{minipage} \\n\\n')
    return content
