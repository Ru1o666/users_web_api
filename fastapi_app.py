import os
import mysql.connector
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv

# 加载环境变量 (包括 MySQL 密码等)
load_dotenv()

# 初始化 FastAPI 实例
app = FastAPI(title="用户管理 Web API")

# 获取数据库连接的公共函数
def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "python_mysql_demo")
    )

# 使用 Pydantic 定义请求体结构，用于数据校验
class UserCreate(BaseModel):
    name: str
    age: int

class UserUpdate(BaseModel):
    name: str
    age: int

# 1. 首页路由：当浏览器访问根目录 "/" 时，返回编写好的 index.html 网页文件
@app.get("/")
def index():
    return FileResponse("index.html")

# 2. 查询接口：获取所有用户 (Read)
@app.get("/api/users")
def get_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True) # 使用 dictionary 会让结果变成 JSON 友好的字典格式
    cursor.execute("SELECT * FROM users ORDER BY id DESC")
    users = cursor.fetchall()

    cursor.close()
    conn.close()
    return users

# 3. 新增接口：添加一个用户 (Create)
@app.post("/api/users")
def create_user(user: UserCreate):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
    cursor.execute(sql, (user.name, user.age))
    conn.commit()
    new_id = cursor.lastrowid

    cursor.close()
    conn.close()
    return {"message": "添加成功", "id": new_id}

# 4. 更新接口：修改指定 id 的用户资料 (Update)
@app.put("/api/users/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE users SET name = %s, age = %s WHERE id = %s"
    cursor.execute(sql, (user.name, user.age, user_id))
    conn.commit()
    affected = cursor.rowcount

    cursor.close()
    conn.close()

    if affected == 0:
        raise HTTPException(status_code=404, detail="未找到该用户")
    return {"message": "更新成功"}

# 5. 删除接口：删除指定 id 的用户 (Delete)
@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM users WHERE id = %s"
    cursor.execute(sql, (user_id,))
    conn.commit()
    affected = cursor.rowcount

    cursor.close()
    conn.close()

    if affected == 0:
        raise HTTPException(status_code=404, detail="未找到该用户")
    return {"message": "删除成功"}

