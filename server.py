import socket
import pickle
import random

HOST = '127.0.0.1'
PORT = 8080

def generate_secret_key(p):
    return random.randint(2, p-2)

def calculate_public_key(g, a, p):
    return pow(g, a, p)

def calculate_shared_secret(B, a, p):
    return pow(B, a, p)

def main():
    with socket.socket() as sock:
        sock.bind((HOST, PORT))
        sock.listen(1)
        print(f"Server listening on {HOST}:{PORT}")
        
        conn, addr = sock.accept()
        with conn:
            print(f"Connected by {addr}")
            
            # Получаем параметры от клиента
            data = conn.recv(1024)
            p, g, A = pickle.loads(data)
            print(f"Received from client: p={p}, g={g}, A={A}")
            
            # Генерируем свой секретный ключ и вычисляем B
            b = generate_secret_key(p)
            B = calculate_public_key(g, b, p)
            
            # Отправляем B клиенту
            conn.sendall(pickle.dumps(B))
            
            # Вычисляем общий секрет
            K = calculate_shared_secret(A, b, p)
            print(f"Shared secret: {K}")

if __name__ == "__main__":
    main()
