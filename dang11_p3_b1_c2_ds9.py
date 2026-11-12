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


def bt_dang11_p3_b1_c2_ds9(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        x = symbols('x')
        x_ans = random.choice([1, 2, 3, 4])
        c_trong = random.choice([12, 14, 15, 16, 18])
        c_ngoai = c_trong + 2 * x_ans
        dt_trong = c_trong**2
        gioi_han = Rational(c_ngoai, 2)
        gioi_han_str = str(float(gioi_han)).replace('.', ',') if c_ngoai % 2 != 0 else str(c_ngoai // 2)
        kq_str = str(x_ans)
    
        hinh_ve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (3.6,0);
    \\coordinate (C) at (3.6,3.6);
    \\coordinate (D) at (0,3.6);
    \\coordinate (E) at (0.7,0.7);
    \\coordinate (F) at (2.9,0.7);
    \\coordinate (G) at (2.9,2.9);
    \\coordinate (H) at (0.7,2.9);
    \\coordinate (M) at (2.9,1.8);
    \\coordinate (N) at (3.6,1.8);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
    \\draw[line width=1pt] (E)--(F)--(G)--(H)--cycle;
    \\draw[line width=1pt, <->] (M)--(N);
    \\fill (A) circle (1pt);
    \\fill (B) circle (1pt);
    \\fill (C) circle (1pt);
    \\fill (D) circle (1pt);
    \\fill (E) circle (1pt);
    \\fill (F) circle (1pt);
    \\fill (G) circle (1pt);
    \\fill (H) circle (1pt);
    \\node[above] at (1.8,3.6) {$%s$};
    \\node[below] at (3.25,1.8) {$x$};
    \\end{tikzpicture}
    \\end{center}''' % (latex(c_ngoai)))
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong một khu vườn hình vuông có cạnh bằng $%s\\text{ m}$ người ta làm một lối đi xung quanh vườn có bề rộng không đổi là $x\\text{ (m)}$ ($x > 0$) như hình vẽ. Để diện tích phần đất trồng trọt còn lại ở giữa là $%s\\text{ m}^2$ thì bề rộng $x$ của lối đi bằng bao nhiêu mét? %s'''
                         %(latex(c_ngoai), latex(dt_trong), hinh_ve))
    
        # Nội dung lời giải
        loigiai = ('''Vì bề rộng lối đi là $x\\text{ (m)}$ ($0 < x < %s$) nên phần đất hình vuông còn lại có cạnh là $(%s - 2x)\\text{ m}$. \\\\
                   Theo đề bài, diện tích phần đất còn lại là $%s\\text{ m}^2$ nên ta có phương trình: \\\\
                   $(%s - 2x)^2 = %s$ \\\\
                   $(%s - 2x)^2 - %s^2 = 0$ \\\\
                   $(%s - 2x - %s)(%s - 2x + %s) = 0$ \\\\
                   $(%s - 2x)(%s - 2x) = 0$. \\\\
                   Giải hai phương trình $%s - 2x = 0$ và $%s - 2x = 0$, ta được $x = %s$ (thoả mãn) hoặc $x = %s$ (loại). \\\\
                   Vậy bề rộng $x$ của lối đi bằng $%s\\text{ m}$.'''
                   %(gioi_han_str, latex(c_ngoai),
                     latex(dt_trong),
                     latex(c_ngoai), latex(dt_trong),
                     latex(c_ngoai), latex(c_trong),
                     latex(c_ngoai), latex(c_trong), latex(c_ngoai), latex(c_trong),
                     latex(c_ngoai - c_trong), latex(c_ngoai + c_trong),
                     latex(c_ngoai - c_trong), latex(c_ngoai + c_trong), latex(x_ans), latex(c_ngoai - x_ans),
                     kq_str))
    
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(str(kq_str))
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
