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


def bt_dang20_p3_b1_c2_ds9(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        x = symbols('x')
        bo_so = random.choice([
            (Rational(8, 5), "1,6", 14, 2, Rational(64, 5), "12,8"),
            (Rational(3, 2), "1,5", 16, 2, Rational(27, 2), "13,5"),
            (Rational(9, 5), "1,8", 12, 3, 9, "9"),
            (Rational(7, 5), "1,4", 18, 2, 14, "14")
        ])
        h_coc, h_coc_str, kc_coc, bong_coc, h_thap, kq_str = bo_so
        tong_bong = kc_coc + bong_coc
    
        hinh_ve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (0,2.8);
    \\coordinate (C) at (4.5,0);
    \\coordinate (D) at (3.0,0);
    \\coordinate (E) at (3.0,0.93);
    \\draw[line width=1pt] (A)--(B)--(C)--cycle;
    \\draw[line width=1pt] (D)--(E);
    \\fill (A) circle (1pt) node[below] {$A$};
    \\fill (B) circle (1pt) node[above] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[below] {$D$};
    \\fill (E) circle (1pt) node[above right] {$E$};
    \\node[left] at (0,1.4) {$x\\text{ m}$};
    \\node[left] at (3.0,0.45) {$%s\\text{ m}$};
    \\node[below] at (1.5,0) {$%s\\text{ m}$};
    \\node[below] at (3.75,0) {$%s\\text{ m}$};
    \\end{tikzpicture}
    \\end{center}''' % (h_coc_str, latex(kc_coc), latex(bong_coc)))
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một chiếc cọc $DE$ cao $%s\\text{ m}$ cắm thẳng đứng trên mặt đất, cách chân một toà tháp $AB$ một khoảng $AD = %s\\text{ m}$. Tại một thời điểm nắng chiếu, bóng của đỉnh cọc và bóng của đỉnh toà tháp trùng nhau tại điểm $C$ trên mặt đất cách chân cọc $CD = %s\\text{ m}$ (như hình vẽ). Tính chiều cao $x$ của toà tháp (đơn vị: mét). %s'''
                         %(h_coc_str, latex(kc_coc), latex(bong_coc), hinh_ve))
    
        # Nội dung lời giải
        loigiai = ('''Gọi $x\\text{ (m)}$ là chiều cao $AB$ của toà tháp ($x > 0$). \\\\
                   Khoảng cách từ điểm bóng trùng nhau $C$ đến chân tháp $A$ là $AC = AD + DC = %s + %s = %s\\text{ (m)}$. \\\\
                   Vì $DE // AB$ (cùng vuông góc với mặt đất $AC$), áp dụng định lí Thalès trong tam giác $ABC$, ta có: \\\\
                   $\\dfrac{DE}{AB} = \\dfrac{CD}{CA}$ hay $\\dfrac{%s}{x} = \\dfrac{%s}{%s}$. \\\\
                   Quy đồng mẫu hai vế với mẫu thức chung $%sx$ và khử mẫu, ta được: \\\\
                   $%s \\cdot %s = %sx$, suy ra $x = %s\\text{ (m)}$ (thoả mãn). \\\\
                   Vậy chiều cao của toà tháp là $%s\\text{ m}$.'''
                   %(latex(kc_coc), latex(bong_coc), latex(tong_bong),
                     h_coc_str, latex(bong_coc), latex(tong_bong),
                     latex(tong_bong),
                     h_coc_str, latex(tong_bong), latex(bong_coc), kq_str,
                     kq_str))
    
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(str(kq_str))
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
