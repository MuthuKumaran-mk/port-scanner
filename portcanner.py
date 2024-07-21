import pyfiglet
import socket
kumaran = pyfiglet.figlet_format("Muthukumaran")
print('*' * 50)
print(kumaran)
print('-'*30,'by:Muthukumaran')

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
target=input('Enter your ip:')
target_ip = socket.gethostbyname(target)
print('start:', target_ip)

#scanning function
def port_scan(port):
    try:
        s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((target_ip,port))
        return True
    except:
        return False
    finally:
        s.close()
    
    #scarn port
for port in range(1,65532):
        
    if port_scan(port):
        print(f'port {port} is open')


