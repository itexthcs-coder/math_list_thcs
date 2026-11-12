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


def bt_dang20_p4_b1_c2_ds9(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        x = symbols('x')
        bo_so = random.choice([
            (2, "2", 24, Rational(8, 5), "1,6", Rational(3, 2), "1,5", Rational(1, 2), "0,5", Rational(128, 5), "25,6", Rational(19, 2), "9,5"),
            (2, "2", 18, 2, "2", Rational(3, 2), "1,5", Rational(1, 2), "0,5", 20, "20", Rational(13, 2), "6,5"),
            (Rational(5, 2), "2,5", 28, 2, "2", Rational(3, 2), "1,5", 1, "1", 30, "30", Rational(33, 2), "16,5"),
            (2, "2", 22, 2, "2", Rational(8, 5), "1,6", Rational(2, 5), "0,4", 24, "24", Rational(32, 5), "6,4")
        ])
        h_coc, h_coc_str, ac_val, ce_val, ce_str, ef_val, ef_str, dh_val, dh_str, fk_val, fk_str, x_ans, x_ans_str = bo_so
        ti_so = Rational(dh_val, ce_val)
    
        hinh_ve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (0,3.2);
    \\coordinate (C) at (3.2,0);
    \\coordinate (D) at (3.2,1.2);
    \\coordinate (E) at (4.5,0);
    \\coordinate (F) at (4.5,0.65);
    \\coordinate (H) at (3.2,0.65);
    \\coordinate (K) at (0,0.65);
    \\draw[line width=1pt] (A)--(B)--(F)--(E)--cycle;
    \\draw[line width=1pt] (C)--(D);
    \\draw[line width=1pt, dashed] (K)--(F);
    \\fill (A) circle (1pt) node[below] {$A$};
    \\fill (B) circle (1pt) node[above] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[above right] {$D$};
    \\fill (E) circle (1pt) node[below] {$E$};
    \\fill (F) circle (1pt) node[right] {$F$};
    \\fill (H) circle (1pt) node[below left] {$H$};
    \\fill (K) circle (1pt) node[left] {$K$};
    \\node[below] at (1.6,0) {$%s\\text{ m}$};
    \\node[below] at (3.85,0) {$%s\\text{ m}$};
    \\node[right] at (4.5,0.32) {$%s\\text{ m}$};
    \\node[left] at (3.2,0.95) {$%s\\text{ m}$};
    \\end{tikzpicture}
    \\end{center}''' % (latex(ac_val), ce_str, ef_str, h_coc_str))
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Để đo chiều cao của một toà nhà cao tầng $AB$, người ta đặt một chiếc cọc $CD$ cao $%s\\text{ m}$ thẳng đứng cách chân toà nhà một khoảng $AC = %s\\text{ m}$. Một người đứng lùi ra xa cọc một khoảng $CE = %s\\text{ m}$ (sao cho $A, C, E$ thẳng hàng) thì nhìn thấy đỉnh cọc $D$ và đỉnh toà nhà $B$ thẳng hàng với mắt người quan sát. Biết khoảng cách từ mắt người đó đến mặt đất là $EF = %s\\text{ m}$ (như hình vẽ). Tính chiều cao $AB$ của toà nhà. %s'''
                         %(h_coc_str, latex(ac_val), ce_str, ef_str, hinh_ve))
    
        # Nội dung lời giải
        loigiai = ('''Kẻ đường thẳng qua $F$ song song với mặt đất $EA$, cắt $CD$ tại $H$ và cắt $AB$ tại $K$. \\\\
                   Ta có các tứ giác $EFHC$ và $EHKA$ là hình chữ nhật nên $CH = AK = EF = %s\\text{ m}$, $FH = CE = %s\\text{ m}$ và $FK = AE = %s + %s = %s\\text{ (m)}$. \\\\
                   Độ dài đoạn thẳng $DH$ là $DH = CD - CH = %s - %s = %s\\text{ (m)}$. \\\\
                   Gọi $x\\text{ (m)}$ là chiều cao $AB$ của toà nhà ($x > %s$), suy ra $BK = x - %s\\text{ (m)}$. \\\\
                   Vì $DH // BK$ (cùng vuông góc với $FK$), áp dụng định lí Thalès trong tam giác $BFK$, ta có: \\\\
                   $\\dfrac{DH}{BK} = \\dfrac{FH}{FK}$ hay $\\dfrac{%s}{x - %s} = \\dfrac{%s}{%s} = %s$. \\\\
                   Quy đồng mẫu hai vế với mẫu thức chung $%s(x - %s)$ rồi khử mẫu, ta được: \\\\
                   $x - %s = %s \\cdot %s$, suy ra $x = %s\\text{ (m)}$ (thoả mãn). \\\\
                   Vậy chiều cao của toà nhà là $%s\\text{ m}$.'''
                   %(ef_str, ce_str, latex(ac_val), ce_str, fk_str,
                     h_coc_str, ef_str, dh_str,
                     h_coc_str, ef_str,
                     dh_str, ef_str, ce_str, fk_str, latex(ti_so),
                     latex(ti_so.q), ef_str,
                     ef_str, dh_str, latex(ti_so.q), x_ans_str,
                     x_ans_str))
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
