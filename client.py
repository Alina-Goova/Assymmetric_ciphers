import socket
import pickle
from key_manager import load_keys

HOST = '127.0.0.1'
PORT = 8080

def main():
    # Загружаем или генерируем ключи
    keys = load_keys("client_keys.pkl")
    p, g, a = keys['p'], keys['g'], int(keys['private'], 16)
    A = keys['public']
    
    with socket.socket() as sock:
        sock.connect((HOST, PORT))
        
        # Отправляем свой публичный ключ
        sock.sendall(pickle.dumps(A))
        
        # Получаем публичный ключ сервера
        data = sock.recv(1024)
        server_A = pickle.loads(data)
        
        # Вычисляем общий секрет
        K = pow(server_A, a, p)
        print(f"Shared secret established: {K}")
        
        # Теперь можно использовать K для симметричного шифрования

if __name__ == "__main__":
    main()
