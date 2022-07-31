# coding:utf-8
# Learn to(pygame):http://m.biancheng.net/pygame/ https://www.pygame.org/docs/ https://zhuanlan.zhihu.com/p/421407064
# Learn to(sqlite3):https://www.runoob.com/sqlite/sqlite-select.html https://www.runoob.com/sqlite/sqlite-order-by.html


def main_UI():
    # pygame.init()
    # print("["+str(time.time())+"][INFO/pygame] 初始化成功")
    #
    # size = width, height = 1000, 1000
    # screen = pygame.display.set_mode(size, pygame.NOFRAME)
    # print("["+str(time.time())+"][INFO/pygame] 窗口显示成功")
    #
    # screen.fill((255, 255, 255))
    # print("["+str(time.time())+"][INFO/pygame] 屏幕填充成功")
    #
    # f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 50)
    # print("["+str(time.time())+"][INFO/pygame] 字体导入成功")
    #
    # # pygame.time.Clock()
    #
    # while True:
    #     if ui_mode == "main_not_login":
    #         text01 = f.render("登录", True, (100, 100, 100), (0, 0, 0))
    #         textRect01 = text01.get_rect()
    #         textRect01.center = (400, 500)  # 350,475 450,520
    #         screen.blit(text01, textRect01)
    #
    #         text02 = f.render("注册", True, (100, 100, 100), (0, 0, 0))
    #         textRect02 = text01.get_rect()
    #         textRect02.center = (600, 500)  # 550,475 650,520
    #         screen.blit(text02, textRect02)
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             conn.close()
    #             print("["+str(time.time())+"][INFO/sqlite3] 数据库连接已断开")
    #             time.sleep(1)
    #             pygame.quit()
    #             print("["+str(time.time())+"][INFO/pygame] 程序已退出")
    #             sys.exit()
    #         if event.type == pygame.MOUSEMOTION and ui_mode == "main_not_login":
    #             print(event.pos)
    #
    #     pygame.display.flip()

    from PyQt5.QtCore import QCoreApplication
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtWidgets import QMessageBox
    from ui_main_not_login import Ui_MainWindow as ui_main_not_login
    from ui_main_about import Ui_Dialog as ui_main_about
    from ui_main_reg import Ui_Dialog as ui_main_reg
    from ui_main_login import Ui_Dialog as ui_main_login
    from ui_login_guest_main import Ui_Dialog as ui_login_guest_main
    from ui_login_user_main import Ui_Dialog as ui_login_user_main
    import datetime
    import random

    g_u_a_TOKEN = []
    for i in range(3):
        g_u_a_TOKEN.append((str(round(random.random()**(random.random()/random.random()), 10)*10**10).split("."))[0])
    token_file = open("Inside_USERS_TOKEN.txt", "w+", buffering=-1, encoding="utf-8")
    for i in range(3):
        token_file.write("guest " if i == 0 else "")
        token_file.write("user  " if i == 1 else "")
        token_file.write("admin " if i == 2 else "")
        token_file.write(str(g_u_a_TOKEN[i])+"\n")
    token_file.close()

    sql_create_books_table = """ CREATE TABLE IF NOT EXISTS books(
book_name TEXT NOT NULL,
book_uuid TEXT PRIMARY KEY NOT NULL,
book_writer TEXT NOT NULL,
book_page INTEGER NOT NULL,
book_insert_time REAL NOT NULL,
book_index BLOB,
book_read_count INTEGER,
book_read_time TEXT,
book_sort TEXT,
book_count_all INTEGER NOT NULL,
book_count_last INTEGER
);"""

    crud_create_table(sql_create_books_table)

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users(
user_name TEXT NOT NULL,
user_uuid TEXT PRIMARY KEY NOT NULL,
user_reg_time TEXT NOT NULL,
user_read_count INTEGER,
user_read_time INTEGER,
user_email TEXT,
user_illegal INTEGER,
user_remake BLOB,
user_level INTEGER NOT NULL,
user_psw TEXT NOT NULL
);"""

    crud_create_table(sql_create_users_table)

    sql_create_logs_table = """ CREATE TABLE IF NOT EXISTS logs(
log_data_borrow TEXT,
log_data_return TEXT,
log_uuid TEXT PRIMARY KEY NOT NULL,
log_user_uuid INTEGER NOT NULL,
log_book_uuid INTEGER,
log_remake BLOB,
log_mode INTEGER NOT NULL
);"""

    crud_create_table(sql_create_logs_table)

    sql_create_max_uuid_table = """ CREATE TABLE IF NOT EXISTS max_uuid(
max_users_uuid TEXT NOT NULL,
max_books_uuid TEXT NOT NULL,
max_logs_uuid TEXT NOT NULL
);"""

    crud_create_table(sql_create_max_uuid_table)

    crud_create_table("""CREATE UNIQUE INDEX IF NOT EXISTS books_index_uuid ON books(book_uuid)""")
    crud_create_table("""CREATE UNIQUE INDEX IF NOT EXISTS users_index_uuid ON users(user_uuid)""")
    crud_create_table("""CREATE UNIQUE INDEX IF NOT EXISTS logs_index_uuid ON logs(log_uuid)""")

    if not crud_read_all_data("max_uuid", "*"):
        crud_create_data("max_uuid", ("0000000001", "0000000001", "0000000001"), 3)

    class UiMainNotLogin(QtWidgets.QMainWindow, ui_main_not_login):
        def __init__(self):
            QtWidgets.QMainWindow.__init__(self)
            ui_main_not_login.__init__(self)
            self.setupUi(self)
            self.setFixedSize(self.size())
            self.title = self.setWindowTitle("图书馆查阅系统")
            self.connect_object()

        def connect_object(self):
            self.about_link_button.clicked.connect(self.about_window)
            self.reg_button.clicked.connect(self.reg_window)
            self.check_update_link_button.clicked.connect(self.check_update)
            self.login_button.clicked.connect(self.login_window)

        def about_window(self):
            pop_window = AboutWindow()
            pop_window.exec()

        def reg_window(self):
            QMessageBox.warning(self, "***提示***", "\t填写规范：\t\t\n"
                                                  "用户名 [必填]：只能由英文、数字、下划线组成且>2位 <15位 开头只能为英文\n"
                                                  "密码 [必填]： 只能由英文、数字、下划线组成且>5位（纯数字）>3位 <19位 开头不能有英文\n"
                                                  "邮箱 [选填]\n"
                                                  "最后一个 [必填]：只能输入 我是真人 这四个字", QMessageBox.Ok)
            pop_window = RegWindow()
            pop_window.exec()

        def login_window(self):
            pop_window = LoginWindow()
            pop_window.exec()

        def check_update(self):
            QMessageBox.warning(self, "错误", "暂无此功能", QMessageBox.No)

    class AboutWindow(QtWidgets.QDialog, ui_main_about):
        def __init__(self):
            QtWidgets.QMainWindow.__init__(self)
            ui_main_about.__init__(self)
            self.setupUi(self)
            self.setFixedSize(self.size())
            self.title = self.setWindowTitle("关于")

    class RegWindow(QtWidgets.QDialog, ui_main_reg):
        def __init__(self):
            QtWidgets.QMainWindow.__init__(self)
            ui_main_reg.__init__(self)
            self.setupUi(self)
            self.setFixedSize(self.size())
            self.title = self.setWindowTitle("注册")
            self.connect_object()

        def closeEvent(self, event):
            a = QMessageBox.question(self, "退出", "你确定要退出吗？\n（未注册的内容将丢失）", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if a == QMessageBox.Yes:
                #QCoreApplication.instance().quit()
                event.accept()
            else:
                event.ignore()

        def connect_object(self):
            self.no_pushButton.clicked.connect(self.no_bottom)
            self.yes_pushButton.clicked.connect(self.yes_bottom)

        def no_bottom(self):
            self.user_email_input.clear()
            self.user_name_input.clear()
            self.user_not_robot_input.clear()
            self.user_psw_agent_input.clear()
            self.user_password_input.clear()

        def yes_bottom(self):
            user_name = self.user_name_input.text()
            user_psw = self.user_password_input.text()
            user_psw_agent = self.user_psw_agent_input.text()
            user_email = self.user_email_input.text()
            user_vcode = self.user_not_robot_input.text()

            temp = user_email.partition("@")

            if user_vcode != "我是真人":
                QMessageBox.information(self, "输入错误", "验证码错误", QMessageBox.Ok)
            elif user_name == "admin" or user_name == "user" or user_name == "guest":
                QMessageBox.information(self, "输入重复", "内置用户名不可使用", QMessageBox.Ok)
            elif user_psw != user_psw_agent:
                QMessageBox.information(self, "输入错误", "密码不一致", QMessageBox.Ok)
            # elif user_psw.isspace():
            #     QMessageBox.information(self, "密码不规范", "密码不能全为空格", QMessageBox.Ok)
            elif user_psw.isdigit() and len(user_psw) <= 4:
                QMessageBox.information(self, "密码不规范", "纯数字可以\n但至少要5位", QMessageBox.Ok)
            elif len(user_name) < 3 or len(user_name) > 15:
                QMessageBox.information(self, "用户名不规范", "用户名大于2位且小于15位", QMessageBox.Ok)
            # elif " " in user_name:
            #     QMessageBox.information(self, "用户名不规范", "用户名不能有空格", QMessageBox.Ok)
            elif user_email != '' and (temp[0] == '' or temp[1] == '' or temp[2] == ''):
                QMessageBox.information(self, "邮箱不规范", '邮箱没有"@"或"@"前后无内容', QMessageBox.Ok)
            elif len(user_email) > 50:
                QMessageBox.information(self, "邮箱不规范", "谁家邮箱名有这么长？？", QMessageBox.Ok)
            elif user_psw == '':
                QMessageBox.information(self, "密码为空", "密码为空", QMessageBox.Ok)
            elif len(user_psw) > 18 or len(user_psw) < 4:
                QMessageBox.information(self, "密码不规范", "密码要小于19位\n大于3位（有字母）", QMessageBox.Ok)
            elif not user_psw.replace("_", "1").isalnum():
                QMessageBox.information(self, "密码不规范", "密码只能由英文、数字、下划线组成")
            elif user_psw.startswith("_"):
                QMessageBox.information(self, "密码不规范", '密码开头不能有"_"')
            # elif user_psw[0].isdigit():
            #     QMessageBox.information(self, "密码不规范", "密码开头不能有数字")
            elif not user_name.replace("_", "1").isalnum():
                QMessageBox.information(self, "用户名不规范", "用户名只能由英文、数字、下划线组成")
            elif user_name.startswith("_"):
                QMessageBox.information(self, "用户名不规范", '用户名开头不能有"_"')
            elif user_name[0].isdigit():
                QMessageBox.information(self, "用户名不规范", "用户名开头不能有数字")

            else:
                temp_data = crud_read_data_where('''users''', """user_name = '%s'""" % user_name, '''user_name''')
                if temp_data is not None:
                    if not temp_data:
                        temp = crud_read_all_data("max_uuid", "max_users_uuid")
                        a = QMessageBox.question(self, "恭喜", "用户名没被占用\n现在可以立即注册",
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                        if a == QMessageBox.Yes:
                            time1 = datetime.datetime.now()
                            time2 = str(time1.year) + "_" + str(time1.month) + "_" + str(time1.day) + "_" + str(
                                time1.hour) + "_" + str(time1.minute) + "_" + str(time1.second)
                            print(temp_data)  # debug
                            print(time2)  # debug
                            print(temp)  # debug

                            if temp[0][0] == "0000000001":
                                crud_create_data("users", (user_name, "0000000001", time2, 0, 0, user_email, 0, "", 1,
                                                           user_psw), 10)
                                crud_update_data("max_uuid", "max_users_uuid = '0000000002'", "")
                                QMessageBox.information(self, "注册", "注册成功")
                            else:
                                temp2 = int(temp[0][0].lstrip("0"))
                                print(temp2)  # debug 未加1，去0

                                temp4 = temp2 + 1
                                print(temp4)  # debug 加1，去0

                                temp3 = str(temp2).rjust(10, "0")
                                print(temp3)  # debug 未加1，补全

                                temp5 = str(temp4).rjust(10,"0")
                                print(temp5)  # debug 加1，补全

                                crud_create_data("users", (user_name, temp3, time2, 0, 0, user_email, 0, "", 1,
                                                           user_psw), 10)
                                crud_update_data("max_uuid", "max_users_uuid = '%s'" % temp5, "")
                                QMessageBox.information(self, "注册", "注册成功")
                            temp = None
                            temp2 = None
                            temp3 = None
                            temp4 = None
                            temp5 = None

                            time1 = None
                            time2 = None
                    else:
                        QMessageBox.information(self, "注册失败", "用户名已被使用", QMessageBox.Ok)

            user_email = None
            user_psw = None
            user_psw_agent = None
            user_vcode = None
            user_name = None
            temp = (None, None, None)
            temp_data = None

    class LoginWindow(QtWidgets.QDialog, ui_main_login):
        def __init__(self):
            QtWidgets.QMainWindow.__init__(self)
            ui_main_login.__init__(self)
            self.setupUi(self)
            self.setFixedSize(self.size())
            self.title = self.setWindowTitle("登录")
            self.connect_object()

        def connect_object(self):
            self.no_pushButton.clicked.connect(self.no_bottom)
            self.yes_pushButton.clicked.connect(self.yes_bottom)

        def no_bottom(self):
            self.user_name_input.clear()
            self.user_password_input.clear()

        def yes_bottom(self):
            user_name = self.user_name_input.text()
            user_psw = self.user_password_input.text()
            if len(user_name) > 15 or len(user_psw) > 18:
                QMessageBox.information(self, "输入错误", "用户名/密码太长了！", QMessageBox.No)
            elif len(user_name) == 0 or len(user_psw) == 0:
                QMessageBox.information(self, "输入错误", "输入为空！", QMessageBox.No)
            elif user_name == "guest" or user_name == "user" or user_name == "admin":
                if user_name == "guest" and user_psw == g_u_a_TOKEN[0]:
                    self.user_password_input.clear()
                    self.guest_window()
                elif user_name == "user" and user_psw == g_u_a_TOKEN[1]:
                    self.user_password_input.clear()
                    self.user_window()
                else:
                    QMessageBox.warning(self, "密码错误", "密码错误", QMessageBox.No)

        def guest_window(self):
            pop_window = GuestWindow()
            pop_window.exec()

        def user_window(self):
            pop_window = UserWindow()
            pop_window.exec()

    class GuestWindow(QtWidgets.QDialog, ui_login_guest_main):
        def __init__(self):
            QtWidgets.QMainWindow.__init__(self)
            ui_login_guest_main.__init__(self)
            self.setupUi(self)
            self.setFixedSize(self.size())
            self.title = self.setWindowTitle("贵宾")

    class UserWindow(QtWidgets.QDialog, ui_login_user_main):
        def __init__(self):
            QtWidgets.QMainWindow.__init__(self)
            ui_login_user_main.__init__(self)
            self.setupUi(self)
            self.setFixedSize(self.size())
            self.title = self.setWindowTitle("用户")

    app = QtWidgets.QApplication(sys.argv)
    main_window = UiMainNotLogin()
    main_window.show()
    sys.exit(app.exec_())


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print("\n[" + str(time.time()) + "][INFO/sqlite3] 连接数据库成功")
    except Error as e:
        print("\n[" + str(time.time()) + "][ERROR/sqlite3] 连接数据库错误，原因：\n" + str(e))
        return None
    return conn


def crud_create_table(create_table_sql):
    conn = create_connection("library.db")
    c = conn.cursor()
    try:
        c.execute(create_table_sql)
        print("[" + str(time.time()) + "][INFO/sqlite3] 建表成功")
    except Error as e:
        print("[" + str(time.time()) + "][ERROR/sqlite3] 数据库建表失败，原因：\n" + str(e))
        c.close()
        conn.close()
        return None
    c.close()
    conn.close()
    print("[" + str(time.time()) + "][INFO/sqlite3] 数据库连接已断开")


def crud_create_data(table_name, create_data_sql, create_date_num):
    conn = create_connection("library.db")
    sql_insert = """INSERT OR IGNORE INTO """ + table_name + """ VALUES(""" + """?,""" * (
            create_date_num - 1) + """?)"""
    c = conn.cursor()
    c.execute(sql_insert, create_data_sql)
    conn.commit()
    print("[" + str(time.time()) + "][INFO/sqlite3] 插入成功")
    c.close()
    conn.close()
    print("[" + str(time.time()) + "][INFO/sqlite3] 数据库连接已断开")


def crud_read_data_where(table_name, condition, column):
    conn = create_connection("library.db")
    c = conn.cursor()
    try:
        c.execute("SELECT " + column + " FROM " + table_name + " WHERE " + condition)
    except Error as e:
        print("[" + str(time.time()) + "][ERROR/sqlite3] 条件查找错误，原因如下\n" + str(e))
        c.close()
        conn.close()
        return None
    else:
        rows = c.fetchall()
        print("[" + str(time.time()) + "][INFO/sqlite3] 条件查找成功")
        c.close()
        conn.close()
        print("[" + str(time.time()) + "][INFO/sqlite3] 数据库连接已断开")
        return rows


def crud_read_all_data(table_name, column):
    conn = create_connection("library.db")
    c = conn.cursor()
    try:
        c.execute("SELECT " + column + " FROM " + table_name)
    except Error as e:
        print("[" + str(time.time()) + "][ERROR/sqlite3] 查找错误，原因如下\n" + str(e))
        c.close()
        conn.close()
        return None
    else:
        rows = c.fetchall()
        print("[" + str(time.time()) + "][INFO/sqlite3] 查找成功")
        c.close()
        conn.close()
        print("[" + str(time.time()) + "][INFO/sqlite3] 数据库连接已断开")
        return rows


def crud_read_data_order(table_name, condition, mode, column):  # 0:升 1:降
    conn = create_connection("library.db")
    temp = "ASC" if mode == 0 else "DESC"
    c = conn.cursor()
    try:
        c.execute("SELECT " + column + " FROM " + table_name + " ORDER BY " + condition + " " + temp)
    except Error as e:
        print("[" + str(time.time()) + "][ERROR/sqlite3] 排序查找错误，原因如下\n" + str(e))
        c.close()
        conn.close()
        return None
    else:
        rows = c.fetchall()
        print("[" + str(time.time()) + "][INFO/sqlite3] 排序查找成功")
        c.close()
        conn.close()
        print("[" + str(time.time()) + "][INFO/sqlite3] 数据库连接已断开")
        return rows


def crud_replace_data(table_name, update_data_sql, update_date_num):
    conn = create_connection("library.db")
    sql_insert = """INSERT OR REPLACE INTO """ + table_name + """ VALUES(""" + """?,""" * (
            update_date_num - 1) + """?)"""
    c = conn.cursor()
    c.execute(sql_insert, update_data_sql)
    conn.commit()
    print("[" + str(time.time()) + "][INFO/sqlite3] 替换更新成功")
    c.close()
    conn.close()
    print("[" + str(time.time()) + "][INFO/sqlite3] 数据库连接已断开")


def crud_update_data(table_name, set, where):
    """
    :param set: 等式： 列名 = 内容
    :param where: 条件： 留""则为全部
    """
    conn = create_connection("library.db")
    c = conn.cursor()
    if where == "":
        sql_update = """UPDATE """ + table_name + """ SET """ + set
        print("not where", end="\n")
        print(sql_update)
    else:
        sql_update = """UPDATE """ + table_name + """ SET """ + set + """ WHERE """ + where
        print("where", end="")

    try:
        c.execute(sql_update)
    except Error as e:
        print("[" + str(time.time()) + "][ERROR/sqlite3] 更新数据错误，原因如下\n" + str(e))
        c.close()
        conn.close()
        return None
    else:
        conn.commit()
        print("[" + str(time.time()) + "][INFO/sqlite3] 更新数据成功")
        c.close()
        conn.close()
        print("[" + str(time.time()) + "][INFO/sqlite3] 数据库连接已断开")


def crud_delete_data(table_name, uuid, uuid_name):
    conn = create_connection("library.db")
    sql_delete = """DELETE FROM """ + table_name + """ WHERE """ + uuid_name + """=""" + uuid
    c = conn.cursor()
    c.execute(sql_delete)
    conn.commit()
    print("[" + str(time.time()) + "][INFO/sqlite3] 删除成功")
    c.close()
    conn.close()
    print("[" + str(time.time()) + "][INFO/sqlite3] 数据库连接已断开")


if __name__ == '__main__':
    import os
    import sys
    import time
    import sqlite3
    from sqlite3 import Error

    # import wx

    user_input_temp = input("[" + str(time.time()) + "][INFO/main] pip pyinstaller qtRuntime 是否已安装？(Yes:y No:n)")
    if user_input_temp == "n" or user_input_temp == "N":
        print("[" + str(time.time()) + "][INFO/sys] pip安装准备")
        os.system(
            "python -m pip install --upgrade pip&pip install pyinstaller&pip install pyqt5&pause&cls&exit")
        print("\n\n[" + str(time.time()) + "][INFO/main]\n请重启程序，十秒后自动退出")
        time.sleep(10)
        sys.exit()
    else:
        # import wx

        # from pygame.locals import *
        main_UI()
