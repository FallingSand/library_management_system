<h1>图书馆管理系统</h1>

## 功能：查、借、还、加（管理员）、用户
## 注：有多本相同的书也要用不同的uuid

---

# 查
<h3>

1. 用sql查找<br>
2. 显示<br>
3. 通过按钮转到借函数<br>

</h3>

---

# 借
<h3>

1. 通过指定的uuid借书<br>
2. sql书本减一，在日志sql中增加一条记录，并使用独一的uuid标识借书用户

</h3>

---

# 还
<h3>

1. 通过uuid在日志sql中查找并记录还书

</h3>

---

# 加（管理员）
<h3>

1. 在User数据库中查找，登录
2. 添加在sql

</h3>

---

# 用户
<h3>

1. 直接在User sql中添加    （数据分析也是如此）

</h3>

---

<br><br>

## 数据库内容

# 表 - 书（books）
<h3>

1. 书名（book_name）<br>
2. uuid（book_uuid） [关键字]<br>
3. 作者（book_writer）<br>
4. 页数（book_page）<br>
5. 放入书本时间（book_insert_time）<br>
6. 目录（book_index）<br>
7. 阅读次数（book_read_count）<br>
8. 阅读时长（book_read_time）<br>
9. 分类（book_sort）<br>
10. 书本数量（book_count_all）<br>
11. 剩余数（book_count_last）<br>

</h3>

---

# 表 - 用户（users）
<h3>

1. 用户名（user_name）<br>
2. uuid（user_uuid）[关键字]<br>
3. 注册时间（user_reg_time）<br>
4. 阅读次数（user_read_count）<br>
5. 阅读时长（user_read_time）<br>
6. 邮箱（user_email）<br>
7. 违规次数（user_illegal）<br>
8. 个人简介（user_remake）<br>
9. 用户等级（user_level）<br>
10. 用户密码（user_psw）<br>

</h3>

---

# 表 - 日志（logs）
<h3>

1. 借书日期（log_data_borrow）<br>
2. 归还日期（log_data_return）<br>
3. 日志uuid（log_uuid）[关键字]<br>
4. 用户uuid（log_user_uuid）<br>
5. 书本uuid（log_book_uuid）<br>
6. 备注（log_remake）<br>
7. 日志类型（log_mode）<br>
8. 建书 2. 读 3.更新用户 4.更新书本<br>
9. 删书 6. 加验证码 7. 改码 8. 删码<br>

</h3>

---

# 表 - 验证码（vcode）
<h3>

1. 验证码（vcode_vcode）<br>
2. 答案（vcode_answer）<br>

</h3>
