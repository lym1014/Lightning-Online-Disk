from socket import *
import os,sys,pymysql,signal,time
from multiprocessing import *
from tkinter import *


sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('127.0.0.1',8888))




def choose(database,host = 'localhost',user = 'root',password = 'lym653512',charset = 'utf8',port = 3306):
    a = pymysql.connect(host,user,password,charset,database,port)
    b = a.cursor()
    b.execute('select username from user')
    user_list = b.fetchall()
    data = connfd.recv(1024)
    n = data.decode()
    if n in user_list:
        connfd.send('连接成功'.encode())
        t1 = Process(target=recv)
        t2 = Process(target=send)
        t1.start()
        t2.start()
    else:
        connfd.send('用户名不存在'.encode())

def recv():
    recode = {}
    data = connfd.recv(1024)



def send():
    pass




while True:
    connfd,addr = sockfd.accept()
    choose('wangpan')






















