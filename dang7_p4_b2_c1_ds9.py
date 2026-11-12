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


def bt_dang7_p4_b2_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        m1 = random.choice([-2, 1, 2])
        m2 = random.choice([-3, 3])
    
        # Hệ: 2x - y = -3 và -2*m^2*x - 9y = 3*(m + 3)
        a2_m1 = -2 * (m1**2)
        c2_m1 = 3 * (m1 + 3)
        x_m1 = Rational(c2_m1 + 27, a2_m1 - 18)
        y_m1 = 2 * x_m1 + 3
    
        a2_m2 = -2 * (m2**2)
        c2_m2 = 3 * (m2 + 3)
        x_m2 = Rational(c2_m2 + 27, a2_m2 - 18)
        y_m2 = 2 * x_m2 + 3
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hệ phương trình $\\begin{cases} 2x - y = -3 \\\\ -2m^2x - 9y = 3(m + 3) \\end{cases}$ ($m$ là tham số). \\\\
                         a) Giải hệ phương trình khi $m = %s$ và khi $m = %s$. \\\\
                         b) Chứng minh rằng hệ phương trình luôn có nghiệm duy nhất với mọi giá trị thực của $m$.'''
                         % (latex(m1), latex(m2)))
    
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
                   \\item Khi $m = %s$, hệ phương trình trở thành $\\begin{cases} 2x - y = -3 \\\\ %s = %s \\end{cases}$. Giải hệ này ta tìm được nghiệm duy nhất là $(%s; %s)$. \\\\
                   Khi $m = %s$, hệ phương trình trở thành $\\begin{cases} 2x - y = -3 \\\\ %s = %s \\end{cases}$. Giải hệ này ta tìm được nghiệm duy nhất là $(%s; %s)$. \n
                   \\item Từ phương trình thứ nhất ta có $y = 2x + 3$. Thế vào phương trình thứ hai, ta được: \\\\
                   $-2m^2x - 9(2x + 3) = 3(m + 3) \\Leftrightarrow (-2m^2 - 18)x - 27 = 3m + 9 \\Leftrightarrow -2(m^2 + 9)x = 3m + 36$. \\\\
                   Vì $m^2 + 9 > 0$ với mọi $m \\in \\mathbb{R}$ nên $-2(m^2 + 9) \\neq 0$ với mọi $m \\in \\mathbb{R}$. \\\\
                   Do đó phương trình luôn có nghiệm duy nhất $x = -\\frac{3m + 36}{2(m^2 + 9)}$, kéo theo $y = 2x + 3$ cũng xác định duy nhất. \\\\
                   Vậy hệ phương trình luôn có nghiệm duy nhất với mọi giá trị thực của $m$. \n
                   \\end{enumEX} \n'''
                   % (latex(m1), latex(a2_m1 * x - 9 * y), latex(c2_m1), latex(x_m1), latex(y_m1),
                      latex(m2), latex(a2_m2 * x - 9 * y), latex(c2_m2), latex(x_m2), latex(y_m2)))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
