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


def bt_dang12_p3_b1_c2_ds9(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        x = symbols('x')
        x_ans = random.choice([2, 3, 4])
        canh_nha = random.choice([10, 11, 12, 13])
        chenh = random.choice([2, 3])
        rong = canh_nha + x_ans
        dai = rong + chenh
        dt_nha = canh_nha**2
        x_loai = rong + canh_nha
        kq_str = str(x_ans)
    
        hinh_ve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (4.2,0);
    \\coordinate (C) at (4.2,3.4);
    \\coordinate (D) at (0,3.4);
    \\coordinate (E) at (3.0,0);
    \\coordinate (F) at (3.0,2.7);
    \\coordinate (G) at (0,2.7);
    \\coordinate (P1) at (-0.3,2.7);
    \\coordinate (P2) at (-0.3,3.4);
    \\coordinate (Q1) at (3.0,-0.3);
    \\coordinate (Q2) at (4.2,-0.3);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
    \\draw[line width=1pt] (E)--(F)--(G);
    \\draw[line width=1pt, <->] (P1)--(P2);
    \\draw[line width=1pt, <->] (Q1)--(Q2);
    \\fill (A) circle (1pt);
    \\fill (B) circle (1pt);
    \\fill (C) circle (1pt);
    \\fill (D) circle (1pt);
    \\fill (E) circle (1pt);
    \\fill (F) circle (1pt);
    \\fill (G) circle (1pt);
    \\node[above] at (2.1,3.4) {$%s$};
    \\node[right] at (4.2,1.7) {$%s$};
    \\node[left] at (-0.3,3.05) {$x$};
    \\node[below] at (3.6,-0.3) {$x + %s$};
    \\node at (1.5,1.35) {Nhà};
    \\node at (2.5,3.05) {Sân vườn};
    \\end{tikzpicture}
    \\end{center}''' % (latex(dai), latex(rong), latex(chenh)))
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Bác Bình có một mảnh đất hình chữ nhật chiều dài $%s\\text{ m}$ và chiều rộng $%s\\text{ m}$. Bác dành một phần đất làm sân vườn bao quanh hai cạnh với bề rộng lần lượt là $x\\text{ (m)}$ và $(x + %s)\\text{ (m)}$ như hình vẽ, phần còn lại xây nhà có diện tích $%s\\text{ m}^2$. Hỏi $x$ bằng bao nhiêu mét? %s'''
                         %(latex(dai), latex(rong), latex(chenh), latex(dt_nha), hinh_ve))
    
        # Nội dung lời giải
        loigiai = ('''Điều kiện: $0 < x < %s$. \\\\
                   Chiều dài phần đất làm nhà là $%s - (x + %s) = %s - x$ (mét) và chiều rộng là $(%s - x)\\text{ m}$. \\\\
                   Vì diện tích phần đất làm nhà là $%s\\text{ m}^2$ nên ta có phương trình: \\\\
                   $(%s - x)^2 = %s$ \\\\
                   $(%s - x)^2 - %s^2 = 0$ \\\\
                   $(%s - x - %s)(%s - x + %s) = 0$ \\\\
                   $(%s - x)(%s - x) = 0$. \\\\
                   Giải hai phương trình trên ta tìm được $x = %s$ (thoả mãn) hoặc $x = %s$ (loại). \\\\
                   Vậy $x = %s\\text{ m}$.'''
                   %(latex(rong),
                     latex(dai), latex(chenh), latex(rong), latex(rong),
                     latex(dt_nha),
                     latex(rong), latex(dt_nha),
                     latex(rong), latex(canh_nha),
                     latex(rong), latex(canh_nha), latex(rong), latex(canh_nha),
                     latex(rong - canh_nha), latex(rong + canh_nha),
                     latex(x_ans), latex(x_loai),
                     kq_str))
    
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(str(kq_str))
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
