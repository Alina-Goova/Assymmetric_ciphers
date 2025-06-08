import socket
import pickle
from pathlib import Path

ALLOWED_KEYS_FILE = "allowed_keys.txt"

def load_allowed_keys():
    if not Path(ALLOWED_KEYS_FILE).exists():
        return set()
    with open(ALLOWED_KEYS_FILE, 'r') as f:
        return set(line.strip() for line in f)

def main():
    allowed_keys = load_allowed_keys()
    keys = load_keys("server_keys.pkl")
    # ... (остальной код до получения client_A)
    
    # Проверяем ключ клиента
    client_key_str = str(client_A)
    if client_key_str not in allowed_keys:
        print(f"Rejected connection from {addr}: key not allowed")
        conn.sendall(pickle.dumps("ERROR: Key not allowed"))
        conn.close()
        return
    
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
