"""P2 · Unit 9 – Data Communication & Networks · SOLVED EXAM PROBLEMS as an extra note per topic (no new questions).
Owner's request (19 Oct 2026): "continue CS notes until the limit, detailed". Subnet/VLSM/supernet answers come from Python's
ipaddress module; delay, window, ALOHA, CSMA/CD and Hamming-syndrome answers were computed with a script on 19 Oct 2026."""

TOPICS = {}  # notes only

S = "Solved exam problems – "

NOTES = {
    "IPv4 Addressing": [{"title": S + "subnetting, VLSM and supernetting", "md": """**Method**: block size = 256 − (mask octet) in the interesting octet; network = largest multiple of the block ≤ the address; broadcast = next network − 1; hosts = 2ʰ − 2.

| Address | Mask | Network | Broadcast | Usable hosts |
|---|---|---|---|---|
| 192.168.1.77/27 | 255.255.255.224 (block 32) | **192.168.1.64** | 192.168.1.95 | 30 |
| 172.20.130.5/21 | 255.255.248.0 (block 8 in 3rd octet) | **172.20.128.0** | 172.20.135.255 | 2046 |
| 10.0.0.0/8 | 255.0.0.0 | 10.0.0.0 | 10.255.255.255 | 16,777,214 |

### Q1. Are 192.168.10.65 and 192.168.10.126 (/26) on the same subnet?
Block 64 → both in 192.168.10.64–127 → **yes**. 192.168.10.130 is in **192.168.10.128/26** → different subnet.

### Q2. VLSM – split 192.168.5.0/24 for LANs of 100, 50, 25 hosts and one point-to-point link
Allocate the largest first:
| Need | Host bits | Subnet | Range ends at |
|---|---|---|---|
| 100 | 7 (126 hosts) | **192.168.5.0/25** | .127 |
| 50 | 6 (62) | **192.168.5.128/26** | .191 |
| 25 | 5 (30) | **192.168.5.192/27** | .223 |
| 2 | 2 (2) | **192.168.5.224/30** | .227 |
Left over: 192.168.5.228 – .255 for later.

### Q3. Supernetting
Combine 200.10.4.0/24 … 200.10.7.0/24 (4 networks; 4 is a multiple of 4 and the first is divisible by 4) → **200.10.4.0/22**

### Q4. How many subnets and hosts?
Class C network with mask 255.255.255.240 (/28) → borrowed 4 bits → **16 subnets**, **14 hosts** each. Class B with /20 → 16 subnets, 4094 hosts each.

### Q5. Mask for 500 hosts per subnet
2⁹ − 2 = 510 ≥ 500 → 9 host bits → **/23 (255.255.254.0)**

### Q6. First and last usable host of 10.1.2.200/27
Network 10.1.2.192, broadcast .223 → hosts **.193 – .222**

### Q7. Fragmentation
4000-byte datagram (20-byte header) over MTU 1500 → fragments of 1500, 1500, 1040 bytes with offsets 0, 185, 370 (units of 8 bytes) and MF = 1, 1, 0"""}],

    "Data Link Layer": [{"title": S + "CRC, Hamming and sliding windows", "md": """### Q1. CRC
Data 1101011011, generator x⁴ + x + 1 (10011) → append four 0s → modulo-2 division → remainder **1110** → transmit 11010110111110. The receiver divides the whole frame by 10011; remainder 0 = no error detected.

### Q2. Hamming (7, 4)
Data 1011 → codeword (positions 1–7) **0110011** (p1 = 0, p2 = 1, p4 = 0).
Received 0110**1**11 → recompute: c1 = b1 ⊕ b3 ⊕ b5 ⊕ b7 = 1, c2 = b2 ⊕ b3 ⊕ b6 ⊕ b7 = 0, c4 = b4 ⊕ b5 ⊕ b6 ⊕ b7 = 1 → syndrome c4c2c1 = 101 = **5** → bit 5 is wrong → corrected word 0110011.

### Q3. Parity bits needed
2ʳ ≥ m + r + 1: m = 7 → r = 4; m = 16 → r = 5; m = 32 → r = 6.

### Q4. Bit stuffing
Data 01111110 01111111 → after every five consecutive 1s insert a 0 → **011111010 011111011**

### Q5. Stop-and-wait efficiency
1000-byte frames, 10 Mbps, 2000 km, propagation speed 2 × 10⁸ m/s
- Transmission time Tt = 8000/10⁷ = **0.8 ms**; propagation Tp = 2 × 10⁶/2 × 10⁸ = **10 ms**; a = Tp/Tt = 12.5
- Efficiency = 1/(1 + 2a) = 1/26 ≈ **3.8%**
- Window needed for 100% use = 1 + 2a = **26 frames** → sequence-number bits: Go-Back-N needs 2ᵏ − 1 ≥ 26 → k = 5; Selective Repeat needs 2ᵏ⁻¹ ≥ 26 → k = 6

### Q6. Window sizes with k-bit sequence numbers
k = 3: Go-Back-N sender ≤ 7, receiver 1; Selective Repeat sender = receiver ≤ 4.

### Q7. Go-Back-N retransmissions
Window 4, frames 0–6 sent, frame 2 lost, no other errors → frames 2, 3, 4, 5, 6 are resent (Go-Back-N) vs only frame 2 (Selective Repeat)."""}],

    "Data Communication – Part 1": [{"title": S + "capacity, delay and decibels", "md": """### Q1. Nyquist
Noiseless 3 kHz channel, 4 levels → C = 2 × 3000 × log₂ 4 = **12 kbps**. For 64 kbps over 4 kHz: 64000 = 2 × 4000 × log₂ L → log₂ L = 8 → **L = 256** levels.

### Q2. Shannon
B = 1 MHz, SNR = 63 → C = 10⁶ × log₂ 64 = **6 Mbps**. With SNR in dB: 30 dB → SNR = 1000 → C for 3 kHz = 3000 × log₂ 1001 ≈ **29.9 kbps**.

### Q3. Bit rate and baud
A signal with 16 levels at 1000 baud carries log₂ 16 = 4 bits per baud → **4000 bps**.

### Q4. Delays
1000-byte packet, 10 Mbps link of 2000 km (2 × 10⁸ m/s): transmission 0.8 ms + propagation 10 ms = **10.8 ms** (ignoring queuing/processing).
Bandwidth–delay product of a 1 Gbps link with 10 ms delay = 10⁷ bits (1.25 MB "in flight").

### Q5. Decibels
Power drops from 10 W to 5 W → 10 log₁₀(5/10) = **−3 dB**. Three segments with −3, +7, −3 dB → net **+1 dB**.

### Q6. Wavelength and period
Frequency 1 MHz → period 1 µs; wavelength in air = 3 × 10⁸/10⁶ = **300 m**.

### Q7. PCM bit rate
Voice up to 4 kHz → sampling at 8 kHz × 8 bits = **64 kbps**; with 7 bits → 56 kbps."""}],

    "Multiple Access, Devices & VLANs": [{"title": S + "ALOHA, CSMA/CD and devices", "md": """### Q1. ALOHA throughput
Pure ALOHA S = G e⁻²ᴳ → maximum at G = 0.5: S = 1/(2e) ≈ **18.4%**. Slotted ALOHA S = G e⁻ᴳ → maximum at G = 1: **36.8%**.
A 1 Mbps pure ALOHA channel carries at most ≈ 184 kbps of successful data.

### Q2. CSMA/CD minimum frame size
Frame must last at least the round-trip time: L_min = 2 × Tp × rate. For 10 Mbps, 2500 m, 2 × 10⁸ m/s → 2 × 12.5 µs × 10⁷ = **250 bits**. Classic Ethernet uses 51.2 µs → **512 bits = 64 bytes**.

### Q3. Collision and broadcast domains
4 PCs on a hub + that hub on one switch port, and 3 PCs on other switch ports, switch connected to a router:
- Hub = 1 collision domain; each switch port = its own collision domain → 1 (hub side) + 3 (PCs) + 1 (router link) = **5 collision domains**
- Switch (no VLANs) = **1 broadcast domain**; each router interface separates broadcast domains

### Q4. VLANs
A 24-port switch with 3 VLANs → 3 broadcast domains; traffic between VLANs needs a router (or layer-3 switch); 802.1Q tag adds **4 bytes**; 12-bit VLAN ID → up to 4094 VLANs.

### Q5. Exponential back-off
After the 3rd collision a station picks K from 0 … 2³ − 1 = 7 and waits K × 51.2 µs; maximum attempts 16, K range capped at 0 … 1023 after 10 collisions."""}],

    "Transport Layer": [{"title": S + "TCP sequence numbers and congestion window", "md": """### Q1. Three-way handshake
Client ISN 100, server ISN 500: SYN (seq 100) → SYN+ACK (seq 500, ack 101) → ACK (seq 101, ack 501). The first data byte from the client has sequence number **101**.

### Q2. Sequence numbers of segments
Segments of 1000 bytes starting at byte 10,001 → segment 1 seq 10,001 (ack expected 11,001), segment 2 seq 11,001, segment 3 seq 12,001.

### Q3. Congestion window (MSS units)
ssthresh = 16, slow start from cwnd = 1: rounds 1, 2, 4, 8, 16 → then additive increase 17, 18, 19, 20 → **timeout at 20**: ssthresh = 20/2 = 10, cwnd = 1 → 1, 2, 4, 8, 10 (capped at ssthresh), 11, 12 …
With **3 duplicate ACKs** (TCP Reno) at cwnd 20: ssthresh = 10, cwnd = 10 (fast recovery) → 11, 12 …

### Q4. Throughput limited by the window
Receive window 64 KB, RTT 100 ms → maximum throughput = 65,535 × 8/0.1 ≈ **5.2 Mbps** (whatever the link speed) → window scaling option needed on fast links.

### Q5. Port numbers
Socket pair (192.168.1.5:52000 ↔ 142.250.1.1:443) – the client uses an ephemeral port, the server HTTPS port 443; a server can serve many clients on port 443 because each connection is identified by the 4-tuple.

### Q6. UDP length
UDP datagram carrying 100 bytes of data → total length field = 8 + 100 = **108**."""}],
}
