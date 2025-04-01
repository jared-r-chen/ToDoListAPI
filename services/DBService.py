import mysql.connector
from dotenv import load_dotenv
import os

# Access values
host = os.getenv("HOST")
user = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
dbname = os.getenv("DATABASE")
port = os.getenv("PORT")

conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=dbname
)


def insertNewTask(userId: int, name: str, status: int):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todoItem (userId, title, status) VALUES (%s, %s, %s)", (userId, name, status))
    conn.commit()
    cursor.close()
    return {"message": "Task created successfully"}

def getAllTasks(userId: int):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todoItem WHERE userId = %s", (userId,))
    tasks = cursor.fetchall()
    cursor.close()
    return tasks

def updateTask(taskId: int, name: str, status: int):
    cursor = conn.cursor()
    cursor.execute("UPDATE todoItem SET title = %s, status = %s WHERE id = %s", (name, status, taskId))
    conn.commit()
    cursor.close()
    return {"message": "Task updated successfully"}

def deleteTask(taskId: int):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todoItem WHERE id = %s", (taskId,))
    conn.commit()
    cursor.close()
    return {"message": "Task deleted successfully"}