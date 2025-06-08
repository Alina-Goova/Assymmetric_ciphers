import socket
import pickle
from key_manager import load_keys

HOST = '127.0.0.1'
PORT = 8080

def main():
    # Загружаем или генерируем ключи
    keys = load_keys("server_keys.pkl")
    p, g, a = keys['p'], keys['g'], int(keys['private'], 16)
    A = keys['public']
    
    with socket.socket() as sock:
        sock.bind((HOST, PORT))
        sock.listen(1)
        print(f"Server listening on {HOST}:{PORT}")
        
        conn, addr = sock.accept()
        with conn:
            print(f"Connected by {addr}")
            
            # Получаем публичный ключ клиента
            data = conn.recv(1024)
            client_A = pickle.loads(data)
            
            # Отправляем свой публичный ключ
            conn.sendall(pickle.dumps(A))
            
            # Вычисляем общий секрет
            K = pow(client_A, a, p)
            print(f"Shared secret established: {K}")
            
            # Теперь можно использовать K для симметричного шифрования

if __name__ == "__main__":
    main()
