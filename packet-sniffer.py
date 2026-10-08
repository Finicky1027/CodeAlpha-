from scapy.all import sniff, wrpcap, IP, TCP, UDP, ICMP, Raw
from datetime import datetime
from collections import Counter

PACKET_LIMIT = 100
BPF_FILTER = ""
SAVE_FILE = "captured_packets.pcap"

captured_packets = []
protocol_counter = Counter()
ip_counter = Counter()


def process_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto_num = ip_layer.proto
        proto_name = {6: "TCP", 17: "UDP", 1: "ICMP"}.get(proto_num, str(proto_num))

        protocol_counter[proto_name] += 1
        ip_counter[src_ip] += 1
        captured_packets.append(packet)

        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Packet #{len(captured_packets)} - {proto_name}")
        print(f"  Source IP:      {src_ip}")
        print(f"  Destination IP: {dst_ip}")

        if TCP in packet:
            print(f"  Src Port: {packet[TCP].sport}  ->  Dst Port: {packet[TCP].dport}")
        elif UDP in packet:
            print(f"  Src Port: {packet[UDP].sport}  ->  Dst Port: {packet[UDP].dport}")
        elif ICMP in packet:
            print(f"  ICMP Type: {packet[ICMP].type}")

        if Raw in packet:
            payload = packet[Raw].load
            print(f"  Payload (first 50 bytes): {payload[:50]}")


def print_summary():
    print("\n" + "=" * 50)
    print("CAPTURE SUMMARY")
    print("=" * 50)
    print(f"Total packets captured: {len(captured_packets)}")

    print("\nProtocol breakdown:")
    for proto, count in protocol_counter.most_common():
        print(f"  {proto:<6}: {count}")

    print("\nTop source IPs:")
    for ip, count in ip_counter.most_common(5):
        print(f"  {ip:<15} : {count} packet(s)")

    if captured_packets:
        wrpcap(SAVE_FILE, captured_packets)
        print(f"\nSaved {len(captured_packets)} packets to '{SAVE_FILE}'")
    print("=" * 50)


def main():
    print("Starting packet sniffer...")
    print(f"Filter: '{BPF_FILTER or 'ALL TRAFFIC'}' | Limit: {PACKET_LIMIT or 'Unlimited'}")
    print("Press Ctrl+C to stop early.\n")

    try:
        sniff(
            prn=process_packet,
            filter=BPF_FILTER,
            store=False,
            count=PACKET_LIMIT if PACKET_LIMIT > 0 else 0,
        )
    except KeyboardInterrupt:
        print("\nStopped by user.")
    except PermissionError:
        print("\nPermission denied. Run this script as admin/root.")
        return

    print_summary()


if __name__ == "__main__":
    main()
