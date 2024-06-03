import socket


# 소켓통신 클래스
class BotServer:
    def __init__(self, srv_port, listen_num):
        self.port = srv_port
        self.listen = listen_num
        self.mySock = None

    # socket 생성
    def create_sock(self):
        self.mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mySock.bind(("192.168.0.35", int(self.port)))
        self.mySock.listen(int(self.listen))

        return self.mySock

    # client 대기, 접속 승인
    def ready_for_client(self):
        return self.mySock.accept()

    # socket 반환
    def get_sock(self):
        return self.mySock
