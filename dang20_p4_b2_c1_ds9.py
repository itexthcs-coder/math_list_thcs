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


def bt_dang20_p4_b2_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            s1 = random.choice([20, 24, 25])
            s2 = s1 + random.choice([4, 5])
            x0 = random.choice([8, 10, 12, 15])
            y0 = s2 * (x0 - 1)
            thua = y0 - s1 * x0
            if thua > 0:
                break
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong một kì thi học sinh giỏi, ban tổ chức dự định xếp các thí sinh vào một số phòng thi nhất định. Nếu xếp mỗi phòng $%s\\text{ thí sinh}$ thì còn thừa $%s\\text{ thí sinh}$ chưa có chỗ. Nếu xếp mỗi phòng $%s\\text{ thí sinh}$ thì vừa đủ chỗ cho tất cả thí sinh và còn thừa nguyên $1\\text{ phòng thi}$ không sử dụng đến. Tính số phòng thi dự định ban đầu và tổng số thí sinh tham dự kì thi.'''
                         % (latex(s1), latex(thua), latex(s2)))
    
        # Nội dung lời giải
        loigiai = ('''Gọi $x$ là số phòng thi dự định ban đầu ($x \\in \\mathbb{N}^*; x > 1$) và $y$ là tổng số thí sinh tham dự kì thi ($y \\in \\mathbb{N}^*$). \\\\
                   Nếu xếp mỗi phòng $%s\\text{ thí sinh}$ thì thừa $%s\\text{ thí sinh}$, nên ta có phương trình: $y = %sx + %s$. \\\\
                   Nếu xếp mỗi phòng $%s\\text{ thí sinh}$ thì vừa đủ và thừa nguyên $1\\text{ phòng thi}$ (tức sử dụng $x - 1$ phòng), nên ta có phương trình: $y = %s(x - 1)$. \\\\
                   Ta có hệ phương trình: \\\\
                   $\\begin{cases} y = %sx + %s \\\\ y = %s(x - 1) \\end{cases} \\Leftrightarrow \\begin{cases} %sx - y = -%s \\\\ %sx - y = %s \\end{cases}$. \\\\
                   Trừ từng vế phương trình thứ hai cho phương trình thứ nhất, ta được $%sx = %s$, suy ra $x = %s$ (thỏa mãn điều kiện). \\\\
                   Thay $x = %s$ vào phương trình thứ nhất, ta tìm được $y = %s \\cdot %s + %s = %s$ (thỏa mãn điều kiện). \\\\
                   Vậy ban đầu ban tổ chức dự định có $%s\\text{ phòng thi}$ và có tất cả $%s\\text{ thí sinh}$ tham dự kì thi.'''
                   % (latex(s1), latex(thua), latex(s1), latex(thua),
                      latex(s2), latex(s2),
                      latex(s1), latex(thua), latex(s2),
                      latex(s1), latex(thua), latex(s2), latex(s2),
                      latex(s2 - s1), latex(thua + s2), latex(x0),
                      latex(x0), latex(s1), latex(x0), latex(thua), latex(y0),
                      latex(x0), latex(y0)))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
