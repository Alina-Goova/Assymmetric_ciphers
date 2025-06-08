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
        sock.connect((HOST, PORT))
        
        # Генерируем параметры
        p = 23  # Простое число (в реальных системах должно быть большим)
        g = 5   # Первообразный корень по модулю p
        
        # Генерируем секретный ключ и вычисляем A
        a = generate_secret_key(p)
        A = calculate_public_key(g, a, p)
        
        # Отправляем параметры серверу
        sock.sendall(pickle.dumps((p, g, A)))
        
        # Получаем B от сервера
        data = sock.recv(1024)
        B = pickle.loads(data)
        print(f"Received from server: B={B}")
        
        # Вычисляем общий секрет
        K = calculate_shared_secret(B, a, p)
        print(f"Shared secret: {K}")

if __name__ == "__main__":
    main()
