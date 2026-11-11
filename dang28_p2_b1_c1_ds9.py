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


def bt_dang28_p2_b1_c1_ds9(self):
    # Khai báo biến
    x, y = symbols('x y')
    
    # Hàm định dạng số thập phân dùng dấu phẩy
    def format_dec(val):
        val_float = float(val)
        if val_float.is_integer():
            return str(int(val_float))
        return str(val_float).replace('.', ',')
    
    # Dạng bài: Sản xuất hai loại áo:
    # Áo ngắn tay cần a_cloth m vải/áo, áo dài tay cần b_cloth m vải/áo.
    # Định mức dùng vừa hết total_cloth m vải để may x áo ngắn tay và y áo dài tay.
    # Mẫu gốc: a_cloth = 1.2 m, b_cloth = 1.5 m, total_cloth = 300 m
    # 1.2x + 1.5y = 300  <=>  4x + 5y = 1000
    
    while True:
        # Chọn hệ số rút gọn u, v nguyên tố cùng nhau (u < v)
        u_val = random.choice([3, 4, 5])
        v_val = random.choice([4, 5, 6])
        if math.gcd(u_val, v_val) == 1 and u_val < v_val:
            # Chọn factor thập phân k_scale để tạo ra số thập phân đẹp: 0.3 hoặc 0.25
            k_scale = random.choice([0.3, 0.25, 0.4])
            a_cloth = round(u_val * k_scale, 2)
            b_cloth = round(v_val * k_scale, 2)
            
            # Chọn số áo tối đa khi chỉ may áo ngắn tay (y = 0): x_max nguyên đẹp
            # total_cloth = a_cloth * x_max
            x_max = random.choice([200, 250, 300, 400])
            total_cloth = int(round(a_cloth * x_max))
            
            # Phương trình rút gọn: u_val * x + v_val * y = C_simp
            # 10 * a_cloth = u_val * (10 * k_scale)
            # Nhân cả hai vế với 10 (nếu k_scale = 0.3, 0.4) hoặc 100
            # Cụ thể: (a_cloth / gcd) * x + (b_cloth / gcd) * y = total_cloth / gcd
            # u_val * x + v_val * y = C_simp với C_simp = total_cloth / k_scale
            C_simp = int(round(total_cloth / k_scale))
            
            # Tìm các nghiệm nguyên dương thực tế (x > 0, y > 0)
            valid_pairs = []
            for xi in range(10, x_max, 10):
                rem = C_simp - u_val * xi
                if rem > 0 and rem % v_val == 0:
                    yi = rem // v_val
                    valid_pairs.append((xi, yi))
            
            if len(valid_pairs) >= 3:
                break
    
    # Lấy 2 nghiệm nguyên dương thoả mãn thực tế
    pair1 = valid_pairs[0]
    pair2 = valid_pairs[1]
    
    # Cặp số sai (không thoả mãn)
    pair_wrong = (pair1[0], pair1[1] + 10)
    
    a_cloth_str = format_dec(a_cloth)
    b_cloth_str = format_dec(b_cloth)
    total_cloth_str = format_dec(total_cloth)
    
    # Biểu thức phương trình
    pt_dec_str = '%sx + %sy = %s' % (a_cloth_str, b_cloth_str, total_cloth_str)
    pt_simp_str = '%sx + %sy = %s' % (u_val, v_val, C_simp)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Một công ty may sản xuất hai loại áo: áo sơ mi ngắn tay cần %s m vải/áo và áo sơ mi dài tay cần %s m vải/áo. Phân xưởng được giao định mức dùng vừa hết %s m vải để may $x$ áo ngắn tay và $y$ áo dài tay.''' % (a_cloth_str, b_cloth_str, total_cloth_str))
    
    ############################################################################# Nhận biết #################################################
    # a) Mối quan hệ giữa số áo may được là pt_dec_str (hay pt_simp_str)
    nb_da_1_d = '\\True Mối quan hệ giữa số áo may được là $%s$ (hay $%s$)' % (pt_dec_str, pt_simp_str)
    nb_da_1_s = 'Mối quan hệ giữa số áo may được là $%sx + %sy = %s$ (hay $%s$)' % (b_cloth_str, a_cloth_str, total_cloth_str, pt_simp_str)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Số mét vải dùng để may $x$ áo sơ mi ngắn tay là $%s x$ (m). \\\\ Số mét vải dùng để may $y$ áo sơ mi dài tay là $%s y$ (m). \\\\ Vì tổng lượng vải sử dụng là %s m nên ta có phương trình: $%s$. \\\\ Chia cả hai vế của phương trình cho %s, ta được phương trình rút gọn: $%s$.''' % (a_cloth_str, b_cloth_str, total_cloth_str, pt_dec_str, format_dec(k_scale), pt_simp_str))
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################# Thông hiểu #################################################
    # b) Nếu chỉ may áo cộc tay (ngắn tay) thì may được tối đa x_max chiếc áo
    x_max_wrong = x_max + random.choice([20, -20, 50])
    th_da_1_d = '\\True Nếu chỉ may áo cộc tay thì may được tối đa %s chiếc áo' % (x_max)
    th_da_1_s = 'Nếu chỉ may áo cộc tay thì may được tối đa %s chiếc áo' % (x_max_wrong)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Nếu chỉ may áo cộc tay (ngắn tay), tức là không may áo dài tay ($y = 0$). \\\\ Thay $y = 0$ vào phương trình $%s$, ta được: \\\\ $%s x = %s \\Leftrightarrow x = %s : %s = %s$. \\\\ Do đó, nếu chỉ may áo cộc tay thì phân xưởng may được tối đa %s chiếc áo.''' % (pt_dec_str, a_cloth_str, total_cloth_str, total_cloth_str, a_cloth_str, x_max, x_max))
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################# Vận dụng #################################################
    # c) Cặp số x = pair1[0] và y = pair1[1] thoả mãn bài toán thực tế
    vd_da_1_d = '\\True Cặp số $x = %s$ và $y = %s$ thoả mãn bài toán thực tế' % (pair1[0], pair1[1])
    vd_da_1_s = 'Cặp số $x = %s$ và $y = %s$ thoả mãn bài toán thực tế' % (pair_wrong[0], pair_wrong[1])
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Thay $x = %s$ và $y = %s$ vào vế trái của phương trình $%s$, ta có: \\\\ %s \\cdot %s + %s \\cdot %s = %s + %s = %s = VP$. \\\\ Do $%s, %s \\in \\mathbb{N}^*$ nên cặp số $x = %s$ và $y = %s$ hoàn toàn thoả mãn bài toán thực tế.''' % (pair1[0], pair1[1], pt_simp_str, u_val, pair1[0], v_val, pair1[1], u_val * pair1[0], v_val * pair1[1], C_simp, pair1[0], pair1[1], pair1[0], pair1[1]))
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################# Vận dụng cao #################################################
    # d) Cặp số x = pair2[0] và y = pair2[1] thoả mãn bài toán thực tế
    pair2_wrong = (pair2[1], pair2[0])
    vdc_da_1_d = '\\True Cặp số $x = %s$ và $y = %s$ thoả mãn bài toán thực tế' % (pair2[0], pair2[1])
    vdc_da_1_s = 'Cặp số $x = %s$ và $y = %s$ thoả mãn bài toán thực tế' % (pair2_wrong[0], pair2_wrong[1])
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Thay $x = %s$ và $y = %s$ vào vế trái phương trình $%s$: \\\\ %s \\cdot %s + %s \\cdot %s = %s + %s = %s = VP$. \\\\ Vì $%s, %s \\in \\mathbb{N}^*$ nên cặp số $x = %s$ và $y = %s$ cũng là một phương án sản xuất thoả mãn bài toán thực tế.''' % (pair2[0], pair2[1], pt_simp_str, u_val, pair2[0], v_val, pair2[1], u_val * pair2[0], v_val * pair2[1], C_simp, pair2[0], pair2[1], pair2[0], pair2[1]))
    
    list_vdc_2 = [loigiai_vdc_1]
    
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)
    
    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
    
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
    
        if 1 <= true_count <= 3:
            break
    
    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    
    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)
    
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
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
