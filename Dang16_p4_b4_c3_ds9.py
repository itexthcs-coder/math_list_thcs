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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D


def bt_Dang16_p4_b4_c3_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        canh_uoc = random.choice([8, 9, 10])
        the_tich = canh_uoc**3 + random.choice([1, 2, 3])
        don_gia = random.choice([110, 120, 130, 150])
        val = the_tich**(1/3)
        canh_2 = str(Decimal(float(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
        dien_tich_dm2 = 5 * (canh_uoc**2)
        dien_tich_m2_str = str(dien_tich_dm2 / 100).replace('.', ',')
        tien_nghin = int(round((dien_tich_dm2 / 100) * don_gia))

        noidungcauhoi = ('''Một người thợ gò hàn cần làm một thùng tôn hình lập phương không nắp có sức chứa $%s\text{ dm}^3$. \\
        a) Hãy ước lượng chiều dài cạnh của thùng tôn (làm tròn đến chữ số thập phân thứ hai). \\
        b) Biết giá tôn là $%s\,000\text{ đồng/m}^2$, hãy tính số tiền tôn tối thiểu để làm chiếc thùng đó (làm tròn đến hàng nghìn đồng).'''
                         % (the_tich, don_gia))

        loigiai = ('''\\begin{enumEX}[a)]{1} \n
        \\item Gọi $a$ ($\text{dm}$, $a > 0$) là độ dài cạnh thùng tôn. Ta có $a^3 = %s \Rightarrow a = \sqrt[3]{%s} \approx %s \approx %s\text{ (dm)}$. \n
        \\item Diện tích tôn cần dùng cho $5$ mặt của thùng là $S = 5 \cdot a^2 \approx 5 \cdot %s^2 = %s\text{ (dm}^2\text{)} = %s\text{ (m}^2\text{)}$. \\
        Số tiền mua tôn tối thiểu là: $%s \times %s\,000 = %s\,000\text{ (đồng)}$. \n
        \\end{enumEX} \n'''
                   % (the_tich, the_tich, str(round(val, 5)).replace('.', ','), canh_2,
                      canh_uoc, dien_tich_dm2, dien_tich_m2_str,
                      dien_tich_m2_str, don_gia, tien_nghin))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
