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


def bt_Dang18_p4_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        v0 = random.choice([15, 16, 18, 20, 25])
        m0 = random.choice([2.5, 3.2, 4.0, 5.0])
        E0 = (m0 * (v0**2)) / 2
        s_m0 = str(m0).replace('.', ',')
        s_E0 = str(round(E0, 2)).rstrip('0').rstrip(',').replace('.', ',')

        ti_so_v = random.choice([2, 3, 4])
        k_m = random.choice([2, 3])
        k_E = (ti_so_v**2) * k_m

        # Nội dung câu hỏi
        noidungcauhoi = ('''Vận tốc $v$ ($\text{m/s}$) của một vật đang bay được cho bởi công thức $v = \sqrt{\dfrac{2E}{m}}$, trong đó $E$ là động năng của vật (tính bằng Joule, kí hiệu là $\text{J}$) và $m$ ($\text{kg}$) là khối lượng của vật.\\
                         a) Tính vận tốc bay của một vật khi biết vật đó có khối lượng $%s\text{ kg}$ và động năng $%s\text{ J}$.\\
                         b) Một vật thứ hai có khối lượng gấp $%s$ lần vật thứ nhất nhưng có động năng gấp $%s$ lần vật thứ nhất. Hỏi vận tốc của vật thứ hai gấp bao nhiêu lần vận tốc của vật thứ nhất?'''
                         % (s_m0, s_E0, latex(k_m), latex(k_E)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
                      \item Thay $m = %s\text{ kg}$ và $E = %s\text{ J}$ vào công thức, ta được:
                      $$v = \sqrt{\dfrac{2 \cdot %s}{%s}} = \sqrt{%s} = %s\text{ (m/s)}.$$
                      \item Gọi $m_1, E_1, v_1$ và $m_2, E_2, v_2$ lần lượt là khối lượng, động năng và vận tốc của vật thứ nhất và vật thứ hai. Theo đề bài, ta có $m_2 = %sm_1$ và $E_2 = %sE_1$. Tỉ số vận tốc của hai vật là:
                      $$\dfrac{v_2}{v_1} = \dfrac{\sqrt{\dfrac{2E_2}{m_2}}}{\sqrt{\dfrac{2E_1}{m_1}}} = \sqrt{\dfrac{2 \cdot %sE_1}{%sm_1} : \dfrac{2E_1}{m_1}} = \sqrt{%s} = %s.$$
                      Vậy vận tốc của vật thứ hai gấp $%s$ lần vận tốc của vật thứ nhất.
                      \\end{enumEX}'''
                   % (s_m0, s_E0, s_E0, s_m0, latex(v0**2), latex(v0),
                      latex(k_m), latex(k_E), latex(k_E), latex(k_m), latex(ti_so_v**2), latex(ti_so_v), latex(ti_so_v)))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
