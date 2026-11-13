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


def bt_Dang20_p4_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([4, 5, 6])
        d = k**2
        heso_can = Decimal(str(2.8 * k)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        v_ms = float(heso_can) * math.sqrt(2)
        v_ms_round = Decimal(str(v_ms)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        v_kmh_round = Decimal(str(v_ms * 3.6)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

        s_heso_can = str(heso_can).rstrip('0').rstrip('.').replace('.', ',')
        s_v_ms = str(v_ms_round).replace('.', ',')
        s_v_kmh = str(v_kmh_round).replace('.', ',')
        v_gioihan = 60
        ketluan = "đã vi phạm" if float(v_kmh_round) > v_gioihan else "không vi phạm"

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong điều tra tai nạn giao thông, cảnh sát ước tính tốc độ $v$ ($\text{m/s}$) của một chiếc ô tô ngay trước khi phanh gấp thông qua độ dài vết trượt bánh xe $d$ ($\text{m}$) trên mặt đường bằng công thức: $v = \sqrt{2\mu g d}$, trong đó $\mu$ là hệ số ma sát giữa lốp xe và mặt đường, $g = 9,8\text{ m/s}^2$ là gia tốc trọng trường.\\
                         a) Trên một đoạn đường khô ráo có hệ số ma sát $\mu = 0,8$, cảnh sát đo được vết trượt phanh của một ô tô dài $d = %s\text{ m}$. Hãy tính tốc độ của ô tô ngay trước khi phanh (theo đơn vị $\text{m/s}$ và đổi ra $\text{km/h}$, làm tròn đến hàng phần mười).\\
                         b) Đoạn đường trên quy định tốc độ tối đa cho phép là $%s\text{ km/h}$. Hỏi người lái xe có vi phạm quy định tốc độ không?'''
                         % (latex(d), latex(v_gioihan)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
                      \item Thay $\mu = 0,8$; $g = 9,8$ và $d = %s$ vào công thức, ta được:
                      $$v = \sqrt{2 \cdot 0,8 \cdot 9,8 \cdot %s} = \sqrt{7,84 \cdot %s} = \sqrt{7,84} \cdot \sqrt{%s} = 2,8 \cdot %s\sqrt{2} = %s\sqrt{2} \approx %s\text{ (m/s)}.$$
                      Đổi sang đơn vị $\text{km/h}$: $v \approx %s \cdot 3,6 \approx %s\text{ (km/h)}$.
                      \item So sánh với tốc độ tối đa cho phép là $%s\text{ km/h}$, ta thấy tốc độ ước tính của ô tô là $%s\text{ km/h}$ nên người lái xe %s quy định tốc độ.
                      \\end{enumEX}'''
                   % (latex(d), latex(d), latex(2 * d), latex(2 * d), latex(k), s_heso_can, s_v_ms,
                      s_v_ms, s_v_kmh, latex(v_gioihan), s_v_kmh, ketluan))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
