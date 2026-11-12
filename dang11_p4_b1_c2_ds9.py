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


def bt_dang11_p4_b1_c2_ds9(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        x = symbols('x')
        x_ans = random.choice([1, 2, 3])
        dai_trong = random.choice([14, 16, 18])
        rong_trong = random.choice([8, 10, 12])
        dai_ngoai = dai_trong + 2 * x_ans
        rong_ngoai = rong_trong + 2 * x_ans
        dt_trong = dai_trong * rong_trong
        gioi_han = Rational(rong_ngoai, 2)
        gioi_han_str = str(float(gioi_han)).replace('.', ',') if rong_ngoai % 2 != 0 else str(rong_ngoai // 2)
        pt_rutgon = expand((dai_ngoai//2 - x)*(rong_ngoai//2 - x) - dt_trong//4)
        x_loai = (dai_ngoai + rong_ngoai)//2 - x_ans
    
        hinh_ve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (4.6,0);
    \\coordinate (C) at (4.6,3.2);
    \\coordinate (D) at (0,3.2);
    \\coordinate (E) at (0.6,0.6);
    \\coordinate (F) at (4.0,0.6);
    \\coordinate (G) at (4.0,2.6);
    \\coordinate (H) at (0.6,2.6);
    \\coordinate (M) at (4.0,1.6);
    \\coordinate (N) at (4.6,1.6);
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
    \\node[above] at (2.3,3.2) {$%s\\text{ m}$};
    \\node[right] at (4.6,1.6) {$%s\\text{ m}$};
    \\node[below] at (4.3,1.6) {$x$};
    \\end{tikzpicture}
    \\end{center}''' % (latex(dai_ngoai), latex(rong_ngoai)))
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một mảnh vườn hình chữ nhật có chiều dài $%s\\text{ m}$ và chiều rộng $%s\\text{ m}$. Người ta làm một lối đi xung quanh vườn có bề rộng không đổi là $x\\text{ (m)}$ ($x > 0$) như hình vẽ. Phần đất còn lại ở giữa dùng để trồng rau có diện tích là $%s\\text{ m}^2$. Tính bề rộng $x$ của lối đi. %s'''
                         %(latex(dai_ngoai), latex(rong_ngoai), latex(dt_trong), hinh_ve))
    
        # Nội dung lời giải
        loigiai = ('''Điều kiện của bề rộng lối đi là $0 < x < %s$. \\\\
                   Vì làm lối đi xung quanh rộng $x\\text{ (m)}$ nên phần đất hình chữ nhật dùng để trồng rau có chiều dài là $(%s - 2x)\\text{ m}$ và chiều rộng là $(%s - 2x)\\text{ m}$. \\\\
                   Theo đề bài, diện tích phần đất trồng rau là $%s\\text{ m}^2$ nên ta có phương trình: \\\\
                   $(%s - 2x)(%s - 2x) = %s$ \\\\
                   $4(%s - x)(%s - x) = %s$ \\\\
                   $%s = 0$ \\\\
                   $(x - %s)(x - %s) = 0$. \\\\
                   Giải hai phương trình $x - %s = 0$ và $x - %s = 0$, ta tìm được $x = %s$ (thoả mãn) hoặc $x = %s$ (loại). \\\\
                   Vậy bề rộng $x$ của lối đi là $%s\\text{ m}$.'''
                   %(gioi_han_str,
                     latex(dai_ngoai), latex(rong_ngoai),
                     latex(dt_trong),
                     latex(dai_ngoai), latex(rong_ngoai), latex(dt_trong),
                     latex(dai_ngoai//2), latex(rong_ngoai//2), latex(dt_trong),
                     latex(pt_rutgon),
                     latex(x_ans), latex(x_loai),
                     latex(x_ans), latex(x_loai), latex(x_ans), latex(x_loai),
                     latex(x_ans)))
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
