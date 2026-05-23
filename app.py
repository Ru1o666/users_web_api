import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    """获取数据库连接"""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "python_mysql_demo")
    )

def add_user(name, age):
    """新增用户"""
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
    cursor.execute(sql, (name, age))
    conn.commit()
    print(f"✅ 成功添加用户: {name}, 年龄: {age}")
    cursor.close()
    conn.close()

def get_all_users():
    """查询所有用户"""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True) # 返回字典格式，方便读取
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print("\n--- 用户列表 ---")
    if not users:
        print("目前没有用户数据")
    for user in users:
        print(f"ID: {user['id']} | 姓名: {user['name']} | 年龄: {user['age']} | 注册时间: {user['created_at']}")
    print("----------------\n")
    cursor.close()
    conn.close()

def update_user(user_id, new_name, new_age):
    """更新用户"""
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE users SET name = %s, age = %s WHERE id = %s"
    cursor.execute(sql, (new_name, new_age, user_id))
    conn.commit()
    # rowcount 表示受影响的行数，如果为 0 说明没找到这个 ID
    if cursor.rowcount > 0:
        print(f"✅ 成功更新 ID={user_id} 的用户为: {new_name}, 年龄: {new_age}")
    else:
        print(f"⚠️ 未找到 ID={user_id} 的用户，更新失败。")
    cursor.close()
    conn.close()

def delete_user(user_id):
    """删除用户"""
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM users WHERE id = %s"
    cursor.execute(sql, (user_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"✅ 成功删除 ID={user_id} 的用户")
    else:
        print(f"⚠️ 未找到 ID={user_id} 的用户，删除失败。")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    print("====== Python MySQL CRUD (增删改查) 演示 ======")
    try:
        print("\n1. 当前的用户列表：")
        get_all_users()
        
        print("2. 尝试增加新数据：")
        add_user("张三", 25)
        add_user("李四", 30)
        get_all_users()
        
        print("3. 尝试更新数据 (假设更新 ID 为 1 的用户)：")
        update_user(1, "张三(已修改)", 26)
        get_all_users()
        
        print("4. 尝试删除数据 (假设删除 ID 为 2 的用户)：")
        delete_user(2)
        get_all_users()

    except mysql.connector.Error as err:
        print(f"数据库错误：{err}")
        print("请确保你已经在 .env 中配置了正确的密码，并且运行过 python init_db.py 创建了数据库和表。")
