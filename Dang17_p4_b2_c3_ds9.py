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


def bt_Dang17_p4_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tv_inch = random.choice([40, 45, 50, 55, 60])
        rong_inch = tv_inch * 3 // 5
        dai_inch = tv_inch * 4 // 5
        rong_cm = Decimal(str(rong_inch * 2.54)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        dai_cm = Decimal(str(dai_inch * 2.54)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        s_rong_cm = str(rong_cm).replace('.', ',')
        s_dai_cm = str(dai_cm).replace('.', ',')

        tu_rong = int(dai_cm) + 5
        tu_cao = int(rong_cm) - 5

        # Nội dung câu hỏi
        noidungcauhoi = ('''Kích thước màn hình ti vi hình chữ nhật được xác định bởi độ dài đường chéo. Một loại ti vi có tỉ lệ hai cạnh màn hình là $4 : 3$.\\
                         a) Gọi $x$ ($\text{inch}$) là chiều rộng của màn hình ti vi ($x > 0$). Viết công thức tính độ dài đường chéo $d$ ($\text{inch}$) của màn hình ti vi theo $x$.\\
                         b) Tính chiều rộng và chiều dài (theo centimét, làm tròn đến hàng phần mười) của màn hình ti vi loại $%s\text{ inch}$, biết $1\text{ inch} \approx 2,54\text{ cm}$.\\
                         c) Một gia đình muốn đặt chiếc ti vi $%s\text{ inch}$ này vào một hộc tủ hình chữ nhật có chiều rộng $%s\text{ cm}$ và chiều cao $%s\text{ cm}$. Hỏi chiếc ti vi có đặt vừa vào hộc tủ đó không? Vì sao?'''
                         % (latex(tv_inch), latex(tv_inch), latex(tu_rong), latex(tu_cao)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
                      \item Vì tỉ lệ hai cạnh màn hình là $4 : 3$ nên chiều dài của màn hình ti vi là $\dfrac{4}{3}x$ ($\text{inch}$). Áp dụng định lí Pythagore, độ dài đường chéo của màn hình ti vi là:
                      $$d = \sqrt{x^2 + \left(\dfrac{4}{3}x\right)^2} = \sqrt{\dfrac{25}{9}x^2} = \dfrac{5}{3}x \text{ (inch)}.$$
                      \item Với ti vi loại $%s\text{ inch}$, ta có $\dfrac{5}{3}x = %s \Leftrightarrow x = %s$ ($\text{inch}$), suy ra chiều dài màn hình là $\dfrac{4}{3} \cdot %s = %s$ ($\text{inch}$).
                      Đổi sang đơn vị centimét:
                      \begin{itemize}
                      \item Chiều rộng màn hình: $%s \cdot 2,54 \approx %s\text{ (cm)}$.
                      \item Chiều dài màn hình: $%s \cdot 2,54 \approx %s\text{ (cm)}$.
                      \end{itemize}
                      \item Vì chiều dài ti vi ($%s\text{ cm}$) nhỏ hơn chiều rộng hộc tủ ($%s\text{ cm}$), nhưng chiều rộng (chiều cao) ti vi ($%s\text{ cm}$) lại lớn hơn chiều cao hộc tủ ($%s\text{ cm}$) nên chiếc ti vi không đặt vừa vào hộc tủ đó.
                      \\end{enumEX}'''
                   % (latex(tv_inch), latex(tv_inch), latex(rong_inch), latex(rong_inch), latex(dai_inch),
                      latex(rong_inch), s_rong_cm, latex(dai_inch), s_dai_cm,
                      s_dai_cm, latex(tu_rong), s_rong_cm, latex(tu_cao)))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
