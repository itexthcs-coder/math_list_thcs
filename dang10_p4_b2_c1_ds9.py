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


def bt_dang10_p4_b2_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            x0 = random.choice([1, 2, 3])
            y0 = random.choice([1, 2, 3])
            a1 = random.choice([2, 3])
            b1 = random.choice([-2, -1])
            a2 = random.choice([1, 2])
            b2 = random.choice([2, 3])
            k0 = random.choice([2, 3, 4])
            if a1 * b2 - a2 * b1 != 0 and x0 != y0:
                break
    
        c1 = a1 * x0 + b1 * y0
        c2 = a2 * x0 + b2 * y0
        b3 = random.choice([2, 3])
        c3 = (k0 - 1) * x0 + b3 * y0
    
        pt1_str = latex(a1 * x + b1 * y) + '=' + latex(c1)
        pt2_str = latex(a2 * x + b2 * y) + '=' + latex(c2)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Trên mặt phẳng tọa độ $Oxy$, tìm giá trị của tham số $k$ để ba đường thẳng sau đồng quy tại một điểm: \\\\
                         $d_1: %s; \\qquad d_2: %s; \\qquad d_3: (k - 1)x + %sy = %s$.'''
                         % (pt1_str, pt2_str, latex(b3), latex(c3)))
    
        # Nội dung lời giải
        loigiai = ('''Tọa độ giao điểm $M(x; y)$ của hai đường thẳng $d_1$ và $d_2$ là nghiệm của hệ phương trình: \\\\
                   $\\begin{cases} %s \\\\ %s \\end{cases}$. \\\\
                   Giải hệ phương trình trên, ta tìm được $x = %s$ và $y = %s$, suy ra $M(%s; %s)$. \\\\
                   Để ba đường thẳng $d_1, d_2, d_3$ đồng quy thì đường thẳng $d_3$ phải đi qua điểm $M(%s; %s)$. \\\\
                   Thay $x = %s$ và $y = %s$ vào phương trình của $d_3$, ta được: \\\\
                   $(k - 1) \\cdot %s + %s \\cdot %s = %s \\Leftrightarrow %s(k - 1) = %s \\Leftrightarrow k - 1 = %s \\Leftrightarrow k = %s$. \\\\
                   Vậy giá trị tham số cần tìm là $k = %s$.'''
                   % (pt1_str, pt2_str,
                      latex(x0), latex(y0), latex(x0), latex(y0),
                      latex(x0), latex(y0),
                      latex(x0), latex(y0),
                      latex(x0), latex(b3), latex(y0), latex(c3),
                      latex(x0), latex(c3 - b3 * y0), latex(k0 - 1), latex(k0),
                      latex(k0)))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
