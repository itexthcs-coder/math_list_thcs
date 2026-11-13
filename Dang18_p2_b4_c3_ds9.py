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


def bt_Dang18_p2_b4_c3_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        canh = random.choice([5, 6, 7])
        dung_tich = canh**3
        muc_nuoc = canh - 2
        luong_nuoc = (canh**2) * muc_nuoc
        canh_gap_doi = f"{round((2 * dung_tich)**(1/3), 2):.2f}".replace('.', ',')

        noidungcauhoi = f"Một gia đình đặt làm một bể cá bằng kính dạng hình lập phương có dung tích tối đa là ${dung_tich}\\text{{ lít}}$ (biết $1\\text{{ lít}} = 1\\text{{ dm}}^3$)."

        nb_da_1_d = f"\\True Thể tích của bể cá tính theo đơn vị đề-xi-mét khối là ${dung_tich}\\text{{ dm}}^3$."
        nb_da_1_s = f"Thể tích của bể cá tính theo đơn vị đề-xi-mét khối là ${dung_tich * 10}\\text{{ dm}}^3$."
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = f"Vì $1\\text{{ lít}} = 1\\text{{ dm}}^3$ nên dung tích ${dung_tich}\\text{{ lít}}$ tương ứng với thể tích ${dung_tich}\\text{{ dm}}^3$."

        th_da_1_d = f"\\True Độ dài cạnh bên trong của bể cá là ${canh}\\text{{ dm}}$."
        th_da_1_s = f"Độ dài cạnh bên trong của bể cá là ${canh + 3}\\text{{ dm}}$."
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = f"Độ dài cạnh bên trong của bể cá là $\\sqrt[3]{{{dung_tich}}} = {canh}\\text{{ dm}}$."

        vd_da_1_d = f"\\True Nếu đổ nước vào bể sao cho mực nước cao ${muc_nuoc}\\text{{ dm}}$ thì lượng nước trong bể là ${luong_nuoc}\\text{{ lít}}$."
        vd_da_1_s = f"Nếu đổ nước vào bể sao cho mực nước cao ${muc_nuoc}\\text{{ dm}}$ thì lượng nước trong bể là ${canh * muc_nuoc}\\text{{ lít}}$."
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = f"Lượng nước trong bể có dạng hình hộp chữ nhật với thể tích $V = {canh} \\times {canh} \\times {muc_nuoc} = {luong_nuoc}\\text{{ dm}}^3 = {luong_nuoc}\\text{{ lít}}$."

        vdc_da_1_d = f"\\True Để bể chứa được gấp đôi lượng nước tối đa ban đầu (${2*dung_tich}\\text{{ lít}}$) mà vẫn giữ nguyên dạng hình lập phương thì độ dài cạnh bể mới khoảng ${canh_gap_doi}\\text{{ dm}}$."
        vdc_da_1_s = f"Để bể chứa được gấp đôi lượng nước tối đa ban đầu (${2*dung_tich}\\text{{ lít}}$) mà vẫn giữ nguyên dạng hình lập phương thì độ dài cạnh bể phải tăng gấp đôi lên ${2*canh}\\text{{ dm}}$."
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = f"Độ dài cạnh bể mới là $\\sqrt[3]{{{2*dung_tich}}} \\approx {canh_gap_doi}\\text{{ dm}}$ (nếu tăng cạnh gấp đôi thì thể tích tăng $2^3 = 8$ lần)."

        def count_true_answers(answers):
            return sum('\\True' in ans for ans in answers)

        while True:
            nb_da_1 = random.choice(list_nb_da_1)
            th_da_1 = random.choice(list_th_da_1)
            vd_da_1 = random.choice(list_vd_da_1)
            vdc_da_1 = random.choice(list_vdc_da_1)
            answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            if 1 <= count_true_answers(answers) <= 3:
                break

        combined_nb = list(zip([nb_da_1], [loigiai_nb_1]))
        combined_th = list(zip([th_da_1], [loigiai_th_1]))
        combined_vd = list(zip([vd_da_1], [loigiai_vd_1]))
        combined_vdc = list(zip([vdc_da_1], [loigiai_vdc_1]))

        shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
        shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
        shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
        shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(shuffled_answers_nb[0]) + '}\n'
               '{' + str(shuffled_answers_th[0]) + '}\n'
               '{' + str(shuffled_answers_vd[0]) + '}\n'
               '{' + str(shuffled_answers_vdc[0]) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
               '\\item ' + str(shuffled_solutions_th[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
