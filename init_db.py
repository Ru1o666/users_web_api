import os
import mysql.connector
from dotenv import load_dotenv

# 加载 .env 文件的配置
load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

def init_database():
    try:
        # 第一步：连接到 MySQL 服务器（还不指定数据库）
        print(f"正在尝试连接 MySQL (host={DB_HOST}, user={DB_USER})...")
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()
        print("✅ 成功连接到 MySQL 服务器！")

        # 第二步：创建数据库
        db_name = "python_mysql_demo"
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci")
        print(f"✅ 成功创建/确认数据库: '{db_name}'")

        # 第三步：选中这个数据库
        cursor.execute(f"USE {db_name}")

        # 第四步：创建 users 表
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(create_table_query)
        print("✅ 成功创建/确认数据表: 'users'")

        conn.commit()
        cursor.close()
        conn.close()
        print("🎉 数据库和表初始化全部完成！")

    except mysql.connector.Error as err:
        print(f"❌ 数据库操作失败: {err}")
        print("\n👉 提示：这通常是因为你的 MySQL 密码不对。请打开 .env 文件，修改 DB_PASSWORD 为你真实的 MySQL 密码，然后再运行一次此脚本。")

if __name__ == "__main__":
    init_database()

