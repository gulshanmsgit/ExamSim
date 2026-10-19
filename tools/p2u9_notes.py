"""P2 · Unit 9 – Data Communication & Networks · revision NOTES for the ten topics that had none (no new questions).
Owner's request (19 Oct 2026): more notes for KRIES (Computer Networks is named in the KRIES Paper 2 syllabus). Worked
numericals (Nyquist, Shannon, CRC, Hamming, ALOHA, subnetting, fragmentation, window sizes, IP checksum) were computed with
a script on 19 Oct 2026. Facts follow Forouzan (Data Communications and Networking) and Tanenbaum (Computer Networks)."""

TOPICS = {}  # notes only – question sets come from p2u9_a … p2u9_f

NOTES = {
    "Data Communication – Part 1": [{"title": "Data communication basics – revision sheet", "md": """## Five components
Message, sender, receiver, **transmission medium**, **protocol** (syntax, semantics, timing). Effectiveness: delivery, accuracy, timeliness, jitter.

## Transmission (data flow) modes
| Mode | Direction | Example |
|---|---|---|
| Simplex | one way only | keyboard → computer, TV broadcast |
| Half duplex | both ways, one at a time | walkie-talkie |
| Full duplex | both ways at once | telephone |
Serial (one bit at a time; asynchronous with start/stop bits, synchronous, isochronous) vs parallel (n bits at once, short distance).

## Signals
- **Analog** – continuous (voice); **digital** – discrete levels (0/1)
- Periodic signal: **f = 1/T**; phase in degrees; wavelength λ = c/f (1 MHz in air → 300 m)
- **Bandwidth** (Hz) = highest − lowest frequency; bandwidth in bps = bit rate
- **Bit rate** (bps) vs **baud rate** (signal elements per second): bit rate = baud × log₂ L (L = signal levels)
- Fourier: any composite signal = sum of sine waves; a digital signal has infinite bandwidth in theory
- Decibel: dB = 10 log₁₀(P₂/P₁); 30 dB = 1000× power; −3 dB = half power

## Channel capacity – worked
- **Nyquist** (noiseless): **C = 2B log₂ L** → B = 3000 Hz, L = 2 → **6000 bps**; L = 4 → 12,000 bps
- **Shannon** (noisy): **C = B log₂(1 + SNR)** (SNR as a ratio, not dB)
  - B = 3000 Hz, SNR = 3162 (35 dB) → ≈ **34.9 kbps**
  - B = 1 MHz, SNR = 63 → 1 MHz × log₂ 64 = **6 Mbps**; then Nyquist gives L: 6 Mbps = 2 × 1 MHz × log₂ L → L = 8
- Shannon gives the upper limit; Nyquist gives the levels needed

## Performance
| Measure | Meaning |
|---|---|
| Bandwidth | capacity of the link |
| Throughput | actual data rate achieved (≤ bandwidth) |
| **Latency (delay)** | propagation + transmission + queuing + processing |
| Propagation time | distance / propagation speed (2 × 10⁸ m/s in cable) |
| Transmission time | message size / bandwidth – 1000 bytes at 1 Mbps = **8 ms** |
| Bandwidth–delay product | bits that fill the link |
| Jitter | variation in delay (bad for audio/video) |

## Impairments
**Attenuation** (loss of energy → amplifiers/repeaters), **distortion** (different frequency components arrive at different times), **noise** (thermal, induced, crosstalk, impulse)

## Traps
- Baud rate ≤ bit rate when each signal element carries more than one bit
- Shannon uses SNR as a plain ratio – convert dB first (SNR = 10^(dB/10))
- Throughput can be far below bandwidth"""}],

    "Data Communication – Part 2": [{"title": "Encoding, modulation, multiplexing and media – revision sheet", "md": """## Line coding (digital data → digital signal)
| Scheme | Rule | Note |
|---|---|---|
| Unipolar NRZ | 1 = +V, 0 = 0 | DC component |
| Polar NRZ-L | level shows the bit | sync problem on long runs |
| NRZ-I | 1 = invert, 0 = no change | |
| RZ | returns to zero mid-bit | 2 changes per bit |
| **Manchester** | transition in the middle (IEEE: 0 = high→low, 1 = low→high) | self-clocking; **Ethernet** |
| **Differential Manchester** | always mid-bit transition; 0 = extra transition at start | **Token Ring** |
| AMI (bipolar) | 0 = 0 V, 1 = alternating +/− | no DC |
- Block coding 4B/5B (Fast Ethernet), 8B/10B; scrambling B8ZS, HDB3

## Analog ↔ digital
- **PCM**: sample → quantise → encode. **Nyquist sampling**: rate ≥ 2 × highest frequency (voice 4 kHz → 8000 samples/s × 8 bits = **64 kbps**)
- Delta modulation sends 1 bit per sample (up/down)
- Digital → analog (**modulation**): ASK, FSK, PSK, **QAM** (amplitude + phase; 16-QAM = 4 bits per baud)
- Analog → analog: AM, FM, PM. Modem = modulator–demodulator

## Multiplexing (many signals, one link)
| Type | Divides | Used in |
|---|---|---|
| **FDM** | frequency bands (guard bands) | radio, cable TV |
| **WDM** | light wavelengths | optical fibre |
| **TDM** (synchronous / statistical) | time slots | T1 (24 channels, 1.544 Mbps), E1 (32, 2.048 Mbps) |
| CDM / CDMA | codes | 3G mobile |
- Spread spectrum: FHSS (Bluetooth), DSSS (Wi-Fi)

## Transmission media
| Guided | Note |
|---|---|
| Twisted pair (UTP/STP), RJ-45 | Cat 5e 1 Gbps, Cat 6 – twisting reduces crosstalk |
| Coaxial, BNC | cable TV, old Ethernet (10Base2, 10Base5) |
| **Optical fibre** | light, total internal reflection; single-mode (long distance, laser) vs multimode (LED); immune to EMI, highest bandwidth |

| Unguided | Range |
|---|---|
| Radio waves | 3 kHz – 1 GHz, omnidirectional (AM/FM, Wi-Fi) |
| Microwaves | 1 – 300 GHz, line of sight (satellite, cellular) |
| Infrared | 300 GHz – 400 THz, short range, no walls (TV remote) |

## Baseband vs broadband
Baseband: one digital signal uses the whole bandwidth (Ethernet "Base"). Broadband: many analog channels on carrier frequencies (cable TV).

## Transmission errors
Single-bit error (one bit), **burst error** (2+ bits, more common); detection in the Data Link Layer notes

## Traps
- Manchester needs twice the bandwidth of NRZ (2 transitions per bit possible)
- Sampling rate is twice the **highest frequency**, not the bandwidth (for low-pass signals they coincide)
- Fibre carries **light**, not electricity"""}],

    "Computer Networks & Topologies": [{"title": "Networks and topologies – revision sheet", "md": """## Line configuration
Point-to-point (dedicated link) vs multipoint / multidrop (shared link)

## Topologies (n devices)
| Topology | Links / cables | Strength | Weakness |
|---|---|---|---|
| **Mesh** | **n(n − 1)/2** links, n − 1 ports each | robust, private, fault isolation | costly cabling (10 devices → 45 links) |
| **Star** | n links to a hub/switch | easy install, one cable failure isolated | hub is a single point of failure |
| **Bus** | one backbone + drop lines, terminators | cheap | backbone break stops all; hard to add |
| **Ring** | each node to two neighbours, token | equal access, repeaters | one break stops all (dual ring fixes) |
| Tree | hierarchy of stars | scalable | root failure |
| Hybrid | mix | flexible | complex |

## Network types by size
| Type | Span | Example |
|---|---|---|
| PAN | ~10 m | Bluetooth |
| **LAN** | building/campus | Ethernet, Wi-Fi |
| MAN | city | cable TV network, WiMAX |
| **WAN** | country/world | Internet, leased lines |
- Internet = network of networks; ISPs in tiers; backbone; Internet exchange points
- Intranet (private, organisation), extranet (shared with partners)

## Wireless networks
Wi-Fi (IEEE 802.11), Bluetooth (802.15.1), WiMAX (802.16), cellular (2G–5G), satellite

## Network architectures
- **Client–server** (central server) vs **peer-to-peer** (every node equal – BitTorrent)
- Protocol standards bodies: **IEEE** (802 LAN standards), ISO (OSI), ITU-T, **IETF** (RFCs), ANSI, EIA

## IEEE 802 family
802.3 Ethernet · 802.4 token bus · 802.5 token ring · **802.11 Wi-Fi** · 802.15 Bluetooth/PAN · 802.16 WiMAX · 802.1Q VLAN

## Traps
- Mesh link count n(n − 1)/2 (full duplex); each device needs n − 1 I/O ports
- Star is the most common LAN topology; physical star can be a logical bus (hub)
- A hub failure in star kills the whole network"""}],

    "Network Models": [{"title": "OSI and TCP/IP models – revision sheet", "md": """## OSI reference model (ISO, 7 layers) – "Please Do Not Throw Sausage Pizza Away"
| # | Layer | Job | Data unit | Devices / protocols |
|---|---|---|---|---|
| 7 | Application | services to the user | data | HTTP, FTP, SMTP, DNS |
| 6 | Presentation | translation, **encryption, compression** | data | JPEG, SSL/TLS, ASCII |
| 5 | Session | dialog control, **synchronisation (checkpoints)** | data | RPC, NetBIOS |
| 4 | Transport | **process-to-process**, segmentation, flow & error control | **segment** | TCP, UDP |
| 3 | Network | **host-to-host**, logical addressing, **routing** | **packet / datagram** | IP, ICMP, router |
| 2 | Data link | **hop-to-hop**, framing, MAC address, error detection | **frame** | Ethernet, PPP, switch, bridge |
| 1 | Physical | bits on the medium, signals, cables | **bit** | hub, repeater, cables |

## TCP/IP suite (Internet)
| TCP/IP | OSI equivalent | Protocols |
|---|---|---|
| Application | 5 + 6 + 7 | HTTP, DNS, SMTP, FTP, SNMP, Telnet, DHCP |
| Transport | 4 | TCP, UDP, SCTP |
| Internet (network) | 3 | IP, ICMP, IGMP, ARP* |
| Network access (link + physical) | 1 + 2 | Ethernet, Wi-Fi |
(4-layer version; the 5-layer version separates data link and physical.) *ARP sits between layers 2 and 3.

## Encapsulation
Data → segment (TCP header) → packet (IP header) → frame (header + trailer/FCS) → bits; the receiver de-encapsulates. Trailer is added only at the data link layer.

## Four kinds of address
| Address | Layer | Size | Example |
|---|---|---|---|
| Physical (MAC) | data link | 48 bits | 07:01:02:01:2C:4B |
| Logical (IP) | network | 32 (IPv4) / 128 (IPv6) | 192.168.1.10 |
| Port | transport | 16 bits | 80 (HTTP) |
| Specific | application | | e-mail address, URL |

## Switching
| Type | How | Example |
|---|---|---|
| **Circuit switching** | dedicated path set up first; three phases (setup, transfer, teardown) | telephone |
| **Packet switching – datagram** | each packet routed independently, may arrive out of order | Internet (IP) |
| Packet switching – virtual circuit | path set up, packets follow it, labels | ATM, Frame Relay |
| Message switching | store-and-forward whole messages | old telegraph |

## Traps
- OSI was designed by **ISO**; TCP/IP came first in practice (ARPANET)
- Encryption/compression → **presentation** layer; routing → **network**; MAC → **data link**
- Transport layer = end-to-end (process to process); network = host to host; data link = node to node"""}],

    "Data Link Layer": [{"title": "Data link layer – revision sheet with CRC and Hamming", "md": """## Jobs
Framing, physical addressing, flow control, error control, access control. Sublayers: **LLC** (logical link control) and **MAC** (media access control).

## Framing
Fixed-size (ATM cells, 53 bytes) or variable: character count, **byte stuffing** (escape byte before a flag/ESC in data), **bit stuffing** (after five consecutive 1s insert a 0; flag 01111110 in HDLC)
- Bit stuffing worked: 0111111 → **01111101**

## Error detection
| Method | Detects |
|---|---|
| Simple (even/odd) parity | all **odd** numbers of bit errors, not even |
| 2-D parity | all 1-, 2-, 3-bit errors, most 4-bit |
| Checksum (16-bit one's complement sum) | used by IP, TCP, UDP |
| **CRC** | all single, double, odd and bursts ≤ degree of generator |
- Hamming distance d: detects d − 1 errors, corrects ⌊(d − 1)/2⌋

**CRC worked**: data 1101011011, generator 10011 (x⁴ + x + 1) → append 4 zeros, divide by XOR → remainder **1110** → send 11010110111110. Another: 100100 with generator 1101 → remainder **001** → send 100100001.

**Hamming code**: parity bits at positions 1, 2, 4, 8 …; r parity bits for m data bits need 2ʳ ≥ m + r + 1 (m = 4 → r = 3, m = 7 → 4, m = 16 → 5)
- Data 1011 in (7, 4) even parity: positions 3, 5, 6, 7 = 1, 0, 1, 1 → p1 = 0, p2 = 1, p4 = 0 → codeword **0110011**
- Receiver recomputes the parities; the binary number they form = position of the wrong bit

## Flow and error control (ARQ)
| Protocol | Window (k-bit sequence numbers) | On error |
|---|---|---|
| **Stop-and-wait** | send 1, wait for ACK | resend after timeout; 1-bit sequence numbers |
| **Go-Back-N** | sender ≤ **2ᵏ − 1**, receiver 1 | resend the lost frame and **all after it** |
| **Selective Repeat** | sender = receiver ≤ **2ᵏ⁻¹** | resend only the lost frame (NAK) |
- k = 3 → GBN window 7, SR window 4; k = 4 → 15 and 8
- Stop-and-wait efficiency = 1/(1 + 2a), a = propagation time / transmission time → Tt = 1 ms, Tp = 2 ms → **20%**
- **Piggybacking**: ACK carried inside a data frame

## HDLC and PPP
- **HDLC**: bit-oriented; frames I (information), S (supervisory), U (unnumbered); flag 01111110; modes NRM, ABM
- **PPP**: byte-oriented, point-to-point (dial-up, DSL); LCP sets up the link, NCP (IPCP) the network layer; authentication PAP (plain password) and CHAP (challenge-response, safer)

## Traps
- Parity cannot detect an even number of flipped bits
- GBN receiver window is 1; SR sender and receiver windows are equal
- CRC is computed with modulo-2 (XOR) division, no carries"""}],

    "Multiple Access, Devices & VLANs": [{"title": "Multiple access, devices and VLANs – revision sheet", "md": """## Random access
| Protocol | Idea | Max throughput |
|---|---|---|
| **Pure ALOHA** | send any time; collision → wait random time | **18.4%** (1/2e), vulnerable time 2 × Tfr |
| **Slotted ALOHA** | send only at slot start | **36.8%** (1/e), vulnerable time Tfr |
| CSMA | listen before talking: 1-persistent, non-persistent, p-persistent | |
| **CSMA/CD** | detect collision while sending, jam, binary exponential back-off | wired **Ethernet (802.3)**; min frame = 2 × propagation delay × rate (64 bytes for 10 Mbps) |
| **CSMA/CA** | avoid collisions: IFS, contention window, RTS/CTS, ACK | **Wi-Fi (802.11)** – can't detect collisions over the air |

## Controlled access
Reservation, **polling** (primary asks secondaries – select/poll), **token passing** (token ring, FDDI, token bus)

## Channelization
**FDMA** (frequency bands), **TDMA** (time slots – GSM), **CDMA** (orthogonal codes, Walsh tables – 3G)

## Connecting devices
| Device | Layer | Does |
|---|---|---|
| **Repeater** | 1 | regenerates the signal |
| **Hub** | 1 | multiport repeater; one collision domain |
| **Bridge** | 2 | filters by MAC address; separates collision domains |
| **Switch** | 2 | multiport bridge; each port its own collision domain; one broadcast domain |
| **Router** | 3 | routes by IP; separates broadcast domains |
| Layer-3 switch | 3 | switch with routing |
| **Gateway** | up to 7 | connects different protocols |
| Modem | 1 | modulates/demodulates |
| Access point | 2 | wireless to wired |
- Transparent bridges learn MAC tables; **spanning tree protocol (STP)** removes loops

## Ethernet facts
- MAC address 48 bits (first 24 = OUI, maker); frame: preamble 7 + SFD 1, destination 6, source 6, type/length 2, data **46–1500**, CRC 4 → frame 64–1518 bytes
- 10Base-T (twisted pair), 100Base-TX (Fast), 1000Base-T (Gigabit), 10GBase; "Base" = baseband

## Backbones and VLANs
- Backbone: bus or star connecting LANs
- **VLAN**: groups ports logically (by port, MAC, IP), not physically → smaller broadcast domains, security, easier moves; **IEEE 802.1Q** tagging (4-byte tag, 12-bit VLAN ID → 4094 VLANs); trunk ports carry many VLANs; routers (or L3 switches) connect VLANs

## Traps
- Hub = layer 1; switch = layer 2; router = layer 3
- Wi-Fi uses CSMA/**CA**, Ethernet uses CSMA/**CD**
- Slotted ALOHA doubles pure ALOHA's efficiency"""}],

    "IPv4 Addressing": [{"title": "IPv4 addressing and datagram – revision sheet with subnetting", "md": """## Address basics
32 bits, dotted decimal (4 octets); 2³² ≈ 4.3 billion addresses

## Classful addressing
| Class | First bits | First octet | Default mask | Networks / hosts |
|---|---|---|---|---|
| A | 0 | 0–127 | 255.0.0.0 (/8) | 126 usable, 16,777,214 hosts |
| B | 10 | 128–191 | 255.255.0.0 (/16) | 16,384 / 65,534 |
| C | 110 | 192–223 | 255.255.255.0 (/24) | 2,097,152 / 254 |
| D | 1110 | 224–239 | – | multicast |
| E | 1111 | 240–255 | – | reserved |
- 127.x.x.x = loopback; **private**: 10.0.0.0/8, 172.16.0.0/12 (172.16–172.31), 192.168.0.0/16; 169.254.x.x = APIPA
- Usable hosts = 2ʰ − 2 (network and broadcast addresses excluded)

## Classless (CIDR) and subnetting – worked
- /n means n network bits; block size = 2^(32 − n)
- **192.168.10.0/24 into 4 subnets** → borrow 2 bits → /26 (mask 255.255.255.192), 64 addresses each, 62 hosts:
  .0/26, .64/26, .128/26, .192/26
- **172.16.45.130/20** → mask 255.255.240.0; third octet block 16 → 45 lies in 32–47 → network **172.16.32.0**, broadcast **172.16.47.255**, **4094** hosts
- **10.1.2.200/27** → block 32 → network **10.1.2.192**, broadcast **10.1.2.223**, hosts .193–.222
- Hosts needed h → host bits b with 2ᵇ − 2 ≥ h (50 hosts → 6 bits → /26)
- Supernetting / route aggregation combines blocks (four /24s → one /22)

## NAT
Many private addresses share one public address; the router keeps a translation table (PAT uses port numbers). Saves IPv4 addresses, hides the inside network.

## IPv4 datagram
- Header **20–60 bytes** (HLEN field counts 4-byte words: 5 → 20 bytes); total length field 16 bits → max datagram 65,535 bytes
- Fields: version, HLEN, service type (DSCP), total length, identification, flags (DF, MF), fragment offset (in **8-byte units**), **TTL** (decremented by each router; 0 → discard + ICMP), protocol (1 ICMP, 6 TCP, 17 UDP), header checksum, source, destination, options
- **Checksum** covers only the header and is recomputed at every hop (TTL changes)

## Fragmentation – worked
4000-byte datagram (20-byte header, 3980 data) over an MTU of 1500:
| Fragment | Total length | Offset (×8) | MF |
|---|---|---|---|
| 1 | 1500 | 0 | 1 |
| 2 | 1500 | 185 (= 1480/8) | 1 |
| 3 | 1040 | 370 | 0 |
- Data per fragment must be a multiple of 8 (except the last); only the destination reassembles

## Traps
- 127.0.0.1 is loopback, not a usable host on the network
- Fragment offset is in units of 8 bytes
- /30 gives 2 usable hosts (point-to-point links); /31 and /32 are special"""}],

    "Transport Layer": [{"title": "Transport layer – revision sheet", "md": """## Job
**Process-to-process** delivery using **port numbers** (16 bits, 0–65,535); socket = IP address + port
- Well-known 0–1023, registered 1024–49,151, dynamic/ephemeral 49,152–65,535
| Port | Service | Port | Service |
|---|---|---|---|
| 20/21 | FTP data/control | 53 | DNS (UDP/TCP) |
| 22 | SSH | 67/68 | DHCP server/client (UDP) |
| 23 | Telnet | 80 | HTTP |
| 25 | SMTP | 110 | POP3 |
| 143 | IMAP | 161/162 | SNMP (UDP) |
| 443 | HTTPS | 69 | TFTP (UDP) |
Multiplexing (many processes → one IP) and demultiplexing at the receiver.

## UDP vs TCP vs SCTP
| | UDP | TCP | SCTP |
|---|---|---|---|
| Connection | connectionless | connection-oriented | connection (association) |
| Reliability | none | reliable, ordered | reliable |
| Header | **8 bytes** | **20–60 bytes** | 12-byte common header |
| Unit | user datagram | segment (byte stream) | chunks, **multi-stream, multihoming** |
| Flow/congestion control | no | yes | yes |
| Used by | DNS, DHCP, SNMP, TFTP, VoIP, video, RIP | HTTP, FTP, SMTP, SSH | telephony signalling |

## TCP header
Source/destination port, **sequence number** (32 bits, byte numbering), **acknowledgement number** (next byte expected), HLEN, flags **URG ACK PSH RST SYN FIN**, window size (16 bits), checksum, urgent pointer, options (MSS, window scale, SACK, timestamps)

## Connection management
- **Three-way handshake**: SYN (seq = x) → SYN + ACK (seq = y, ack = x + 1) → ACK (ack = y + 1). A SYN consumes one sequence number.
- Termination: FIN → ACK → FIN → ACK (four-way, or three with FIN+ACK); TIME-WAIT = 2 × MSL
- SYN flooding attack exploits half-open connections

## Flow, error and congestion control
- **Flow control**: sliding window set by the receiver (rwnd); window 0 → sender waits (persist timer)
- **Error control**: checksum, cumulative ACK, retransmission on timeout (RTO from RTT estimates) or **3 duplicate ACKs** (fast retransmit)
- **Congestion control**: cwnd; **slow start** (exponential – doubles each RTT until ssthresh), **congestion avoidance** (additive increase +1 MSS per RTT), on timeout ssthresh = cwnd/2 and cwnd = 1; on 3 dup ACKs **fast recovery** (Reno: cwnd = ssthresh)
- Effective window = min(rwnd, cwnd)
- Worked: cwnd 1, 2, 4, 8, 16 (ssthresh 16) then 17, 18 … per RTT

## Traps
- UDP header is 8 bytes; TCP minimum 20
- TCP numbers **bytes**, not segments
- DNS uses UDP for queries (TCP for zone transfers and large replies)
- Flow control protects the **receiver**, congestion control protects the **network**"""}],

    "World Wide Web & Applications": [{"title": "Web and application protocols – revision sheet", "md": """## World Wide Web
- Invented by **Tim Berners-Lee** (CERN, 1989); browser (client) ↔ web server; hypertext / hypermedia
- **URL**: protocol://host:port/path?query#fragment → `https://www.kea.kar.nic.in:443/index.html`
- Static, dynamic (generated on request – CGI, PHP, JSP) and active (runs in the browser – JavaScript) documents
- Cookies keep state over stateless HTTP; web caching / proxy servers

## HTTP
- Application protocol over TCP port **80** (HTTPS = HTTP + TLS on **443**); **stateless**
- Methods: **GET** (fetch), **POST** (send data), PUT, DELETE, HEAD (headers only), OPTIONS, PATCH
- Status codes: **1xx** info, **2xx** success (200 OK, 201 Created), **3xx** redirect (301 moved permanently, 304 not modified), **4xx** client error (400, 401 unauthorised, 403 forbidden, **404 not found**), **5xx** server error (500, 503)
- Non-persistent (one object per TCP connection, HTTP/1.0) vs **persistent** (HTTP/1.1 default); HTTP/2 multiplexing, HTTP/3 over QUIC (UDP)

## DNS
- Maps names ↔ IP addresses; distributed hierarchy: root → TLD (.com, .in, .org) → second-level (google.com) → hosts
- Recursive vs iterative resolution; caching with TTL
- Records: **A** (IPv4), **AAAA** (IPv6), **CNAME** (alias), **MX** (mail server), **NS** (name server), PTR (reverse), SOA
- Port 53; UDP for queries

## E-mail
| Protocol | Job | Port |
|---|---|---|
| **SMTP** | send / relay mail (push) | 25 (587 submission) |
| **POP3** | download mail, usually deletes from server | 110 (995 SSL) |
| **IMAP4** | manage mail on the server, folders, sync devices | 143 (993 SSL) |
| **MIME** | non-ASCII attachments (images, Kannada text) | – |
- User agent (Outlook), mail transfer agent (server), mail access agent; webmail uses HTTP

## File transfer and remote login
- **FTP**: two TCP connections – **control port 21** (stays open) and **data port 20**; active vs passive mode; ASCII/binary modes; anonymous FTP
- TFTP: UDP 69, no authentication; SFTP/FTPS secure versions
- **TELNET**: remote login, port 23, plain text (insecure) → **SSH** port 22 (encrypted)

## Other application protocols
DHCP (automatic IP configuration, UDP 67/68, DORA: Discover–Offer–Request–Ack), SNMP (network management, UDP 161/162; manager, agent, MIB), NTP (time), RTP (real-time media), SIP (VoIP calls), LDAP, NFS

## Traps
- FTP sends control information **out-of-band** (separate connection)
- POP3 downloads; IMAP keeps mail on the server
- SMTP only sends; retrieval is POP3/IMAP
- HTTP is stateless – cookies add state"""}],
}
