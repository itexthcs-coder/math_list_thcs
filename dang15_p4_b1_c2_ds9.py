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


def bt_dang15_p4_b1_c2_ds9(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        x = symbols('x')
        bo_so = random.choice([
            (150, 90, 15, 30, 45),
            (180, 108, 18, 36, 54),
            (210, 120, 15, 45, 60),
            (140, 80, 15, 30, 45)
        ])
        s_ab, s_oto, chenh_v, v_xm, v_oto = bo_so
        s_xm = s_ab - s_oto
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Quãng đường $AB$ dài $%s\\text{ km}$. Một ô tô đi từ $A$ đến $B$, cùng lúc đó một xe máy đi từ $B$ về $A$. Hai xe gặp nhau tại một điểm cách $A$ là $%s\\text{ km}$. Biết vận tốc của ô tô lớn hơn vận tốc của xe máy là $%s\\text{ km/h}$. Tính vận tốc của mỗi xe.'''
                         %(latex(s_ab), latex(s_oto), latex(chenh_v)))
    
        # Nội dung lời giải
        loigiai = ('''Gọi $x\\text{ (km/h)}$ là vận tốc của xe máy ($x > 0$), khi đó vận tốc của ô tô là $(x + %s)\\text{ km/h}$. \\\\
                   Đến lúc gặp nhau, ô tô đi được quãng đường là $%s\\text{ km}$ và xe máy đi được quãng đường là $%s - %s = %s\\text{ (km)}$. \\\\
                   Thời gian ô tô đi đến lúc gặp nhau là $\\dfrac{%s}{x + %s}$ (giờ) và thời gian xe máy đi là $\\dfrac{%s}{x}$ (giờ). \\\\
                   Vì hai xe khởi hành cùng một lúc nên thời gian đi đến lúc gặp nhau của hai xe bằng nhau, ta có phương trình: \\\\
                   $\\dfrac{%s}{x + %s} = \\dfrac{%s}{x}$. \\\\
                   Quy đồng mẫu hai vế với mẫu thức chung $x(x + %s)$ rồi khử mẫu, ta được: \\\\
                   $%sx = %s(x + %s)$ \\\\
                   $%sx = %sx + %s$ \\\\
                   $%sx = %s$ \\\\
                   $x = %s$ (thoả mãn). \\\\
                   Vậy vận tốc của xe máy là $%s\\text{ km/h}$ và vận tốc của ô tô là $%s + %s = %s\\text{ km/h}$.'''
                   %(latex(chenh_v),
                     latex(s_oto), latex(s_ab), latex(s_oto), latex(s_xm),
                     latex(s_oto), latex(chenh_v), latex(s_xm),
                     latex(s_oto), latex(chenh_v), latex(s_xm),
                     latex(chenh_v),
                     latex(s_oto), latex(s_xm), latex(chenh_v),
                     latex(s_oto), latex(s_xm), latex(s_xm * chenh_v),
                     latex(s_oto - s_xm), latex(s_xm * chenh_v),
                     latex(v_xm),
                     latex(v_xm), latex(v_xm), latex(chenh_v), latex(v_oto)))
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
