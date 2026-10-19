"""P2 · Unit 9 – Data Communication & Networks · second, DETAILED note for the five topics whose first note was short
(no new questions). Owner's request (19 Oct 2026): "continue CS notes until the limit, detailed". IPv6 compression, RSA,
Diffie–Hellman and Caesar examples were computed with a script on 19 Oct 2026."""

TOPICS = {}  # notes only

T = " – detailed notes"

NOTES = {
    "IPv6, ARP, Delivery & Routing": [{"title": "IPv6, ARP and routing" + T, "md": """## IPv6 addressing
- **128-bit** addresses (2¹²⁸ ≈ 3.4 × 10³⁸), written as 8 groups of 4 hex digits separated by `:`
- **Compression**: drop leading zeros in a group; replace **one** run of all-zero groups with `::`
  - 2001:0db8:0000:0000:0000:ff00:0042:8329 → **2001:db8::ff00:42:8329**
- Types: **unicast** (global unicast 2000::/3, **link-local fe80::/10**, unique local fc00::/7), **multicast** (ff00::/8), **anycast** (nearest of a group); **no broadcast** in IPv6
- Special: `::1` loopback, `::` unspecified; prefix notation /64 (64-bit network + 64-bit interface ID)
- Interface ID by **EUI-64** (MAC 00:1A:2B:3C:4D:5E → 021a:2bff:fe3c:4d5e – insert ff:fe and flip the 7th bit) or random (privacy)
- Configuration: **SLAAC** (stateless autoconfiguration from router advertisements) or DHCPv6

## IPv6 header
- Fixed **40-byte** base header: version (6), traffic class, **flow label**, payload length, **next header**, **hop limit** (replaces TTL), source, destination
- No header checksum; options moved to **extension headers** (hop-by-hop, routing, fragment, authentication, ESP)
- Fragmentation only by the **source** (path MTU discovery); minimum MTU 1280 bytes
| IPv4 | IPv6 |
|---|---|
| 32-bit | 128-bit |
| header 20–60 bytes, checksum | fixed 40 bytes, no checksum |
| broadcast | multicast/anycast |
| ARP | Neighbour Discovery (ICMPv6) |
| routers and hosts fragment | only the source fragments |
| IPsec optional | IPsec built into the design |

## Transition from IPv4 to IPv6
**Dual stack** (both protocols), **tunnelling** (IPv6 inside IPv4 – 6to4, Teredo), **header translation** (NAT64) when one side is IPv6-only

## ARP and Neighbour Discovery
- **ARP** (IPv4): finds the **MAC address** for a known IP on the local network – request is **broadcast**, reply is **unicast**; results cached in the ARP table
- RARP (MAC → IP, obsolete; replaced by BOOTP/DHCP); proxy ARP; gratuitous ARP; **ARP spoofing** attack
- IPv6 **Neighbour Discovery Protocol** (ICMPv6 messages: router solicitation/advertisement, neighbour solicitation/advertisement, redirect) replaces ARP

## Delivery and forwarding
- **Direct** delivery (same network) vs **indirect** (via routers); hop-by-hop forwarding using a **routing table** (destination network, mask, next hop, interface)
- **Longest prefix match** chooses the most specific route; default route 0.0.0.0/0
- Host-specific, network-specific and default routing

## Routing protocols
| Protocol | Type | Algorithm | Metric / note |
|---|---|---|---|
| **RIP** | interior (IGP) | **distance vector** (Bellman–Ford) | **hop count**, max 15 (16 = unreachable); updates every 30 s; UDP 520; count-to-infinity → split horizon, poison reverse |
| **OSPF** | interior | **link state** (Dijkstra) | cost (bandwidth); areas, backbone area 0; flooding of LSAs; fast convergence |
| IS-IS | interior | link state | ISP backbones |
| **BGP** (v4) | **exterior** (between autonomous systems) | **path vector** | policies; TCP port 179; runs the Internet |
| EIGRP | interior | advanced distance vector (Cisco) | |
- **Autonomous system (AS)** = networks under one administration
- Static vs dynamic routing; multicast routing (DVMRP, PIM)

## ICMP
- Error reporting and queries for IP (carried inside IP, protocol 1)
- Errors: **destination unreachable** (type 3), source quench, **time exceeded** (type 11 – TTL reached 0), parameter problem, redirect
- Queries: **echo request/reply** (types 8/0 – **ping**), timestamp; **traceroute** uses TTL-exceeded messages
- No ICMP error is sent about an ICMP error message, a fragment other than the first, broadcast/multicast datagrams

## Traps
- `::` can appear only once in an IPv6 address
- ARP request = broadcast, reply = unicast
- RIP = distance vector (hop count ≤ 15); OSPF = link state; BGP = path vector between ASes"""}],

    "Network Security": [{"title": "Network security" + T, "md": """## Goals and attacks
- **CIA**: confidentiality, integrity, availability; plus authentication, non-repudiation, access control
- **Passive attacks** (eavesdropping, traffic analysis – hard to detect) vs **active attacks** (masquerade, replay, modification, **denial of service**)
| Threat | What it does |
|---|---|
| Virus | attaches to a host program, needs user action |
| Worm | self-replicates across networks |
| Trojan horse | disguised as useful software |
| Ransomware | encrypts data and demands payment (WannaCry 2017) |
| Spyware / keylogger / adware | steals information / shows ads |
| Rootkit, backdoor, logic bomb, botnet | hide / bypass / trigger / zombie network |
| **Phishing**, spear phishing, vishing, smishing | fake messages to steal credentials |
| **DoS / DDoS** | flood a server (SYN flood, ping of death) |
| Man-in-the-middle, spoofing (IP, ARP, DNS), session hijacking, SQL injection, XSS | |

## Cryptography basics
- Plaintext → **encryption** (algorithm + key) → ciphertext → decryption; Kerckhoffs: security lies in the key, not the algorithm
- **Substitution** ciphers: **Caesar** (shift 3: HELLO → **KHOOR**), monoalphabetic, **Vigenère** (polyalphabetic), Playfair; **transposition** ciphers rearrange letters (rail fence)
- **One-time pad** – theoretically unbreakable (random key as long as the message, used once)

## Secret-key (symmetric) algorithms
| Algorithm | Block / key | Note |
|---|---|---|
| **DES** | 64-bit block, **56-bit key**, 16 Feistel rounds | broken by brute force (1998) |
| 3DES | 3 × DES, 112/168-bit key | legacy |
| **AES** (Rijndael) | 128-bit block, **128/192/256-bit key**, 10/12/14 rounds | current standard (2001) |
| IDEA, Blowfish, RC4 (stream), RC5 | | |
- Modes: ECB (weak – same block → same ciphertext), CBC, CTR, GCM
- Problem: **key distribution** – n users need n(n − 1)/2 keys (100 users → 4950)

## Public-key (asymmetric) algorithms
- Each user has a **public key** (shared) and a **private key** (secret); n users need 2n keys
- **RSA** (Rivest, Shamir, Adleman, 1977): choose primes p, q; n = pq; φ = (p − 1)(q − 1); e coprime to φ; d = e⁻¹ mod φ; encrypt c = mᵉ mod n; decrypt m = cᵈ mod n
  - p = 3, q = 11 → n = 33, φ = 20; e = 7 → **d = 3**; m = 4 → c = 4⁷ mod 33 = **16**; 16³ mod 33 = 4 ✓
- **Diffie–Hellman** key exchange: public p, g; A = gᵃ mod p, B = gᵇ mod p; shared key = Bᵃ = Aᵇ mod p
  - p = 23, g = 5, a = 6, b = 15 → A = 8, B = 19 → shared key **2**
- ECC (elliptic curve – smaller keys), ElGamal, DSA
- Confidentiality: encrypt with the receiver's **public** key; signature: sign with the sender's **private** key

## Hashes and digital signatures
- Hash: fixed-size digest, one-way, collision-resistant – MD5 (128-bit, broken), SHA-1 (160-bit, deprecated), **SHA-256** (SHA-2), SHA-3
- **MAC / HMAC**: hash with a secret key → integrity + authentication
- **Digital signature** = hash of the message encrypted with the sender's **private key**; verified with the public key → authentication, integrity, **non-repudiation**
- **Digital certificate** (X.509) binds a public key to an identity, signed by a **Certificate Authority**; PKI; in India – Controller of Certifying Authorities (IT Act 2000)

## Firewalls, VPN and security protocols
- **Firewall**: packet-filtering (IP/port rules), stateful inspection, **application-level gateway (proxy)**, circuit-level gateway; DMZ for public servers
- **IDS** (detects – signature-based or anomaly-based) vs **IPS** (blocks); honeypots
- **VPN**: encrypted tunnel over the Internet – **IPsec** (network layer; **AH** = authentication/integrity, **ESP** = encryption + integrity; transport vs tunnel mode; IKE for keys), SSL/TLS VPNs
- **SSL/TLS** (transport layer – HTTPS port 443; handshake uses public-key crypto to agree a symmetric session key), **SSH** (port 22), **PGP / S/MIME** (e-mail), **Kerberos** (authentication with tickets, KDC), WPA2/WPA3 (Wi-Fi)

## Traps
- DES key is 56 bits (64 with parity bits)
- Symmetric = one shared key; asymmetric = key pair
- A digital signature uses the **sender's private** key; encryption for secrecy uses the **receiver's public** key
- IPsec AH does not encrypt"""}],

    "Mobile Technology – Part 1": [{"title": "GSM, CDMA and mobile computing" + T, "md": """## Generations
| Gen | Tech | Key feature |
|---|---|---|
| 1G (1980s) | AMPS – **analog**, FDMA | voice only |
| **2G** (1991) | **GSM** (TDMA), IS-95 CDMA | digital voice, **SMS** |
| 2.5G / 2.75G | **GPRS** (packet data), **EDGE** | mobile Internet, MMS |
| **3G** | UMTS/**WCDMA**, CDMA2000, HSPA | video calls, mobile broadband |
| **4G** | **LTE**, LTE-Advanced, WiMAX | all-IP, OFDMA, VoLTE, 100 Mbps+ |
| **5G** (2019; India Oct 2022) | NR, mmWave, massive MIMO | up to ~10–20 Gbps, ultra-low latency, IoT, network slicing |

## GSM architecture
- **Mobile Station (MS)** = mobile equipment (IMEI) + **SIM** (IMSI, keys)
- **Base Station Subsystem (BSS)**: **BTS** (radio towers) + **BSC** (controls several BTSs, handover)
- **Network and Switching Subsystem (NSS)**: **MSC** (switching, call routing), **HLR** (home location register – permanent subscriber data), **VLR** (visitor location register – temporary data of roaming users), **AuC** (authentication centre), **EIR** (equipment identity register – stolen phones)
- Operation and support subsystem (OSS)
- Radio: **TDMA** – 8 time slots per 200 kHz carrier; frequency bands 900/1800 MHz in India; full-rate speech 13 kbps
- Services: bearer (data), teleservices (voice, SMS, fax), supplementary (call forwarding, waiting); **handover** (hard handover in GSM), roaming, location update

## CDMA
- Users share the same frequency at the same time, separated by **unique codes** (spread spectrum, Walsh codes); **soft handover**; better capacity; IS-95 (2G), CDMA2000 (3G)
| GSM | CDMA |
|---|---|
| TDMA + FDMA | code division |
| SIM card | traditionally no SIM (R-UIM) |
| hard handover | soft handover |
| global standard | mainly US/Korea |

## Mobile computing
- Computing on the move: portability, wireless connectivity, location awareness
- Constraints: limited battery, bandwidth, screen, processing; intermittent connectivity; security risks
- **Mobile middleware**: hides heterogeneity – message-oriented middleware, WAP gateway, synchronisation (SyncML), mobile agents
- **Gateways** translate between networks (WAP gateway between WAP devices and the web; SMS gateway; media gateways)
- **WAP** (Wireless Application Protocol) and WML – early mobile web
- Mobile OS: Android (Linux kernel), iOS; app stores

## Mobile IP
- Lets a device keep its IP address while moving between networks
- **Home agent** (on the home network), **foreign agent** (on the visited network), **care-of address** (temporary address), **home address** (permanent)
- Agent discovery → registration with the home agent → **tunnelling** (home agent encapsulates packets to the care-of address) → **triangle routing** problem (fixed by route optimisation)
- Mobile IPv6 has built-in support (no foreign agent needed)

## Traps
- HLR = permanent subscriber data; VLR = visitors' temporary data
- GSM uses TDMA; CDMA uses codes
- In Mobile IP the home agent tunnels packets to the care-of address"""}],

    "Mobile Technology – Part 2": [{"title": "Satellites, cellular systems and wireless LANs" + T, "md": """## Communication satellites
| Orbit | Height | Period | Use |
|---|---|---|---|
| **GEO** (geostationary) | ~35,786 km above the equator | 24 h (appears fixed) | TV broadcast, VSAT, weather (INSAT, GSAT); 3 satellites cover the globe; ~250 ms one-way delay |
| **MEO** | 5,000–20,000 km | 2–12 h | navigation – **GPS**, **NavIC (IRNSS)** – India's own |
| **LEO** | 500–2,000 km | ~90–120 min | low delay, needs constellations – **Starlink**, OneWeb, Iridium |
- Uplink and downlink use different frequencies (C band 6/4 GHz, Ku band 14/12 GHz, Ka band); transponders; footprint; VSAT networks for remote areas; satellite phones

## Cellular topology
- Area divided into **cells** (drawn as hexagons), each with a base station; **frequency reuse** – the same channels reused in distant cells
- **Cluster size N** (N = i² + ij + j²: 3, 4, 7, 12 …); reuse distance D = R√(3N); smaller N → more capacity but more interference
- Capacity increase: **cell splitting**, **sectoring** (120° antennas), microcells/picocells/femtocells
- **Handoff/handover** when a user moves between cells: hard (break before make – GSM) vs soft (make before break – CDMA)
- Interference: co-channel and adjacent-channel

## Wireless transmission
- Antennas (omnidirectional, directional); propagation – reflection, diffraction, scattering; **multipath fading**; path loss
- Modulation: GMSK (GSM), QPSK, QAM, **OFDM** (Wi-Fi, LTE – many orthogonal sub-carriers); spread spectrum (FHSS, DSSS); **MIMO** (multiple antennas)

## Wireless LANs (IEEE 802.11 – Wi-Fi)
| Standard | Band | Max rate |
|---|---|---|
| 802.11b | 2.4 GHz | 11 Mbps |
| 802.11a | 5 GHz | 54 Mbps |
| 802.11g | 2.4 GHz | 54 Mbps |
| 802.11n (Wi-Fi 4) | 2.4/5 GHz | 600 Mbps (MIMO) |
| 802.11ac (Wi-Fi 5) | 5 GHz | ~3.5–6.9 Gbps |
| 802.11ax (Wi-Fi 6/6E) | 2.4/5/6 GHz | ~9.6 Gbps |
- Architecture: **BSS** (stations + **access point**), **ESS** (several BSSs joined by a distribution system), **IBSS / ad hoc** (no AP); SSID names the network
- MAC: **CSMA/CA** (DCF), RTS/CTS for the hidden-station problem, ACKs; PCF (polling)
- Security: WEP (broken) → WPA → **WPA2 (AES-CCMP)** → WPA3

## Bluetooth (IEEE 802.15.1)
- Short range (~10 m class 2, up to 100 m class 1), **2.4 GHz ISM band**, **FHSS** (1600 hops/s, 79 channels); named after King Harald Bluetooth; Ericsson 1994
- **Piconet**: 1 master + up to **7 active slaves** (255 parked); **scatternet** = connected piconets
- Bluetooth Low Energy (BLE) for wearables; profiles (A2DP audio, HID); Zigbee (802.15.4) for low-power sensors

## Wireless topologies and MANETs
- Infrastructure (via AP/base station) vs **ad hoc** (peer to peer)
- **MANET** (mobile ad hoc network): no infrastructure, nodes act as routers, dynamic topology, limited power; routing protocols – **proactive/table-driven** (DSDV, OLSR), **reactive/on-demand** (**AODV**, **DSR**), hybrid (ZRP)
- VANET (vehicles), wireless sensor networks, mesh networks

## Traps
- GEO satellites are ~36,000 km high with a 24-hour period
- Bluetooth piconet = 1 master + 7 active slaves
- AODV and DSR are reactive (on-demand) MANET protocols"""}],

    "Cloud Computing and IoT": [{"title": "Cloud computing and IoT" + T, "md": """## Cloud computing (NIST definition)
On-demand network access to a shared pool of configurable resources. **Five characteristics**: on-demand self-service, broad network access, **resource pooling** (multi-tenancy), **rapid elasticity**, **measured service** (pay per use).

## Service models
| Model | You manage | Provider manages | Examples |
|---|---|---|---|
| **IaaS** | OS, apps, data | hardware, virtualisation, network | AWS EC2, Azure VMs, Google Compute Engine |
| **PaaS** | apps, data | runtime, OS, infrastructure | Google App Engine, Heroku, Azure App Service |
| **SaaS** | just use it | everything | Gmail, Microsoft 365, Salesforce, Zoom |
- Others: FaaS / serverless (AWS Lambda), DaaS, STaaS (storage), DBaaS

## Deployment models
**Public** (shared, provider-owned – AWS), **private** (one organisation), **community** (shared by organisations with common needs – e.g. government cloud **MeghRaj** in India), **hybrid** (mix)

## Virtualization
- Runs many virtual machines on one physical machine via a **hypervisor** (VMM)
- **Type 1 – bare-metal** (runs on hardware: VMware ESXi, Microsoft Hyper-V, Xen, KVM) vs **Type 2 – hosted** (runs on an OS: VirtualBox, VMware Workstation)
- Full virtualisation, para-virtualisation, hardware-assisted (Intel VT-x, AMD-V)
- **Containers** (Docker) share the host kernel – lighter than VMs; orchestration with Kubernetes
- Benefits: consolidation, isolation, snapshots, live migration

## Cloud storage
- Object storage (Amazon S3, Google Cloud Storage), block storage (EBS), file storage (EFS, Google Drive); replication, CDN
- Data centres; SLAs (availability like 99.9%); concerns – security, privacy, vendor lock-in, data sovereignty, downtime
- Related: grid computing, **edge/fog computing** (process near the data source), MapReduce and Hadoop (HDFS) for big data

## Internet of Things (IoT)
- Physical objects with sensors/actuators connected to the Internet (Kevin Ashton coined the term, 1999)
- **Components**: things (sensors – temperature, motion; actuators), **connectivity** (Wi-Fi, Bluetooth/BLE, **Zigbee**, LoRaWAN, NB-IoT, cellular, RFID/NFC), **gateway**, cloud platform, analytics, user application
- **Architecture**: 3-layer – **perception** (sensing) → **network** (transport) → **application**; 5-layer adds processing (middleware) and business layers
- **Protocols**: **MQTT** (publish–subscribe, lightweight, over TCP, broker), **CoAP** (REST-like over **UDP** for constrained devices), HTTP/REST, AMQP, XMPP, **6LoWPAN** (IPv6 over low-power networks)
- Platforms/boards: Arduino (microcontroller), Raspberry Pi (single-board computer), ESP8266/ESP32
- Applications: smart homes, smart cities, agriculture (soil moisture, irrigation), healthcare wearables, industrial IoT (Industry 4.0), smart meters, vehicle tracking
- Challenges: security (default passwords, Mirai botnet 2016), privacy, interoperability, power

## Traps
- IaaS → you manage the OS; PaaS → you manage only the app; SaaS → you manage nothing
- Type 1 hypervisor = bare metal
- MQTT is publish–subscribe over TCP; CoAP runs over UDP"""}],
}
