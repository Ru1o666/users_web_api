# Python + MySQL + FastAPI 全栈实战项目

这是一个初学者学习全栈开发的极简项目，主要包含基础的控制台版增删改查（CRUD）应用，以及一个基于 FastAPI + 原生 HTML/JS 实现的 Web 端后台管理系统。

## 🛠 项目使用的技术栈
* **后端引擎:** Python (3.10+) 搭配 FastAPI
* **数据库:** MySQL (配合 mysql-connector-python)
* **前端实现:** HTML CSS JavaScript (原生实现，无需构建工具)
* **环境配置:** python-dotenv (利用 `.env` 文件读取环境变量)

## 📂 项目结构概览

```text
PythonProject-mysql/
│
├─ .env                # 配置文件（存放数据库密码等敏感信息，不应提交到代码库）
├─ .env.example        # 配置说明文件（告诉协作者 .env 文件的格式是什么）
├─ init_db.py          # 数据库初始化脚本（用 Python 代码为你自动新建库和创建表）
├─ app.py              # 控制台版本的项目（最基础的 CRUD 功能实现）
├─ fastapi_app.py      # 服务端项目（对外暴露的 Web API 接口路由与处理函数）
├─ index.html          # Web 前端页面（使用 FetchAPI 与 Web接口联调的前端交互界面）
├─ requirements.txt    # 依赖说明（环境所需安装的所有 Python 库引用列表）
├─ .gitignore          # Git 忽略列表（配置了本地的忽略名单，避免上传不需要的文件）
└─ README.md           # 本说明文档
```

## 🚀 最佳上手实操指南

### 步骤 1：克隆项目并准备基础环境

```bash
# 1. 设置一个独立的 Python 虚拟环境 (在项目目录下)
python -m venv venv

# 2. 激活虚拟环境 (Windows PowerShell 用户)
.\venv\Scripts\Activate.ps1
# Mac / Linux 用户
# source venv/bin/activate

# 3. 安装所需的所有 Python 依赖依赖
pip install -r requirements.txt
```

### 步骤 2：配置本地的 MySQL 并初始化表

复制环境配置样例文件：
把 `.env.example` 复制一份并重命名为 `.env`。接着在里面写入你个人的实际 MySQL 账号密码：
```env
DB_HOST=localhost
DB_USER=root
# 将下面换成自己的数据库密码
DB_PASSWORD=123456
DB_NAME=python_mysql_demo
DB_PORT=3306
```

然后利用随项目自带的脚本，**一键自动创建数据库并建表**：
```bash
python init_db.py
```

### 步骤 3：启动 Web 端服务界面

运行下面这条命令以启动 FastAPI 服务器：
```bash
uvicorn fastapi_app:app --reload --port 8000
```
启动成功后：
* 👉 访问网页效果展示：[http://127.0.0.1:8000](http://127.0.0.1:8000)
* 👉 直接调试并查阅 API 文档功能：[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
