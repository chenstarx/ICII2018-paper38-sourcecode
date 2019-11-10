import socket

host = "0.0.0.0" # 0.0.0.0表示建立一个localhost并接受所有ip地址过来的连接
port = 7670 # 端口

flag = True

count = 0

while True:
    
    if flag:
        # 初始化socket
        tcps = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcps.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        
        # 将socket绑定到ip和端口上
        tcps.bind((host, port))

        # 开始监听连接
        tcps.listen(1)
        print("Waiting for incoming connections\n")

        # 有连接请求后才到这一行
        conn, addr = tcps.accept()
        print("incoming connection from: ", addr, "\n")

    try:
        # 接受client传过来的数据
        data = conn.recv(1024).decode()
        
        print("receive data: ", data, "\n")
        
        if data == "end":  # 关闭连接
            flag = True
            tcps.close()
            print("Connection Ended\n")

            # 回复给client表示服务器已关闭          
            conn.sendall("server closed".encode())
            
        else:
            # 把flag置为false防止重新跑一遍连接的代码
            flag = False

            # 回复给client表示收到            
            conn.sendall("server received".encode())
            
    except:
        flag = True
        tcps.close()
        print("Client end Connection\n")
