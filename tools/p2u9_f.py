"""Paper 2 · Unit 9 · P2-U9-12 Mobile Technology – Part 1, P2-U9-13 Mobile Technology – Part 2 and P2-U9-14 Cloud Computing and IoT
(3 topics × 2 sub-topics × 30), with revision NOTES.
References: Jochen Schiller, Mobile Communications (2nd ed.); Raj Kamal, Mobile Computing; Forouzan, Data Communications and Networking
(chs. 15–16: wireless LANs, cellular and satellite networks); Theodore Rappaport, Wireless Communications (cellular concepts); NIST SP
800-145 (definition of cloud computing); Silberschatz, Operating System Concepts (virtual machines); Arshdeep Bahga & Vijay Madisetti,
Internet of Things – A Hands-on Approach. Each set mixes REAL previous-year questions (exact wording, printed option order, `source`)
with new ones. Official answers: KEA final keys for GTTC 2024 (Lecturer CS – A1, Technician Gr-III CS – C1, options read from the page
images) and Legislative Council 2024 Sr/Jr Programmer P1 (A1). KSET and GFGC answers were worked out by ExamSim. Cellular cluster-size,
reuse-distance and channel numbers were checked by calculation."""
from packlib import AR, I_II
from p2u7_a import kset, PYQ, KLC, GTTC, NOTE

GSM_CDMA = [
    kset("KSET 2024 CS&A · Q90"),
    ("GSM is a second-generation (2G) cellular system that uses which multiple-access method?",
     ["TDMA combined with FDMA", "CDMA only", "OFDMA only", "Pure ALOHA"], 0, PYQ + "Each 200 kHz carrier is divided into 8 time slots."),
    ("In GSM-900, the uplink and downlink bands are:",
     ["890–915 MHz (uplink) and 935–960 MHz (downlink)", "935–960 MHz (uplink) and 890–915 MHz (downlink)", "1800–1900 MHz both", "2.4 GHz both"], 0,
     "Duplex separation 45 MHz; 124 carriers of 200 kHz each."),
    ("How many time slots does one GSM carrier (TDMA frame) have?",
     ["8", "4", "16", "124"], 0, PYQ + "A TDMA frame lasts about 4.615 ms."),
    ("The three main subsystems of the GSM architecture are:",
     ["Mobile Station, Base Station Subsystem and Network & Switching Subsystem (plus OSS)", "Router, switch and hub", "Client, server and database", "Sender, channel and receiver"], 0,
     "BSS = BTS + BSC; NSS = MSC + HLR + VLR + AuC + EIR; OSS = operation and support."),
    ("In GSM, the database that stores permanent subscriber information (service profile, current location area) is the:",
     ["HLR (Home Location Register)", "VLR (Visitor Location Register)", "EIR", "BSC"], 0, PYQ + "VLR keeps temporary data for subscribers currently in the MSC's area."),
    ("The GSM register that holds the list of valid, stolen or blocked handsets (by IMEI) is the:",
     ["EIR (Equipment Identity Register)", "HLR", "AuC", "VLR"], 0, "IMEI identifies the handset; IMSI (on the SIM) identifies the subscriber."),
    ("The Authentication Centre (AuC) in GSM stores:",
     ["The secret key Ki of each subscriber and generates authentication triplets", "Call records", "Handset IMEIs", "Cell tower locations"], 0,
     PYQ + "Algorithms: A3 (authentication), A8 (cipher-key generation), A5 (air-interface encryption)."),
    ("The GSM component that controls several BTSs, allocates radio channels and manages handovers between them is the:",
     ["BSC (Base Station Controller)", "MSC", "HLR", "SIM"], 0, "The MSC switches calls and connects to the public telephone network."),
    ("The GSM air interface between the mobile station and the BTS is called:",
     ["Um interface", "Abis interface", "A interface", "Gb interface"], 0, PYQ + "Abis – BTS to BSC; A – BSC to MSC."),
    ("The SIM card in a GSM phone stores:",
     ["The IMSI, the secret key Ki and personal data such as contacts", "The handset's IMEI only", "The operating system", "The HLR database"], 0, "SIM = Subscriber Identity Module."),
    ("GSM services are classified as:",
     ["Bearer services, teleservices and supplementary services", "Unicast, multicast and broadcast", "IaaS, PaaS and SaaS", "Simplex, half duplex and full duplex"], 0,
     PYQ + "Teleservices – voice, SMS, fax; supplementary – call forwarding, call waiting, caller ID."),
    ("A single SMS message in GSM can carry up to:",
     ["160 characters (7-bit)", "1600 characters", "16 characters", "255 bytes of video"], 0, "Longer texts are split and joined (concatenated SMS)."),
    ("GPRS, often called 2.5G, added to GSM:",
     ["Packet-switched data service", "Analog voice", "Optical fibre", "Satellite links"], 0, PYQ + "EDGE (2.75G) improved data rates further."),
    ("CDMA allows many users to share the same frequency band at the same time by:",
     ["Giving each user a unique spreading code", "Giving each user a separate time slot", "Giving each user a separate carrier frequency", "Using only one user at a time"], 0,
     "Spread-spectrum; codes are orthogonal (e.g. Walsh codes). IS-95 was the first CDMA cellular standard."),
    ("Which handoff is possible in CDMA but not in GSM?",
     ["Soft handoff – connected to two base stations at the same time", "Hard handoff", "No handoff at all", "Manual handoff"], 0, PYQ + "GSM uses hard handoff ('break before make')."),
    ("The 'near–far problem' in CDMA is handled by:",
     ["Tight power control of mobile transmitters", "Using larger antennas", "Adding time slots", "Reducing the number of codes"], 0, "A nearby strong signal can drown distant weak ones."),
    ("In CDMA, the frequency reuse factor is typically:",
     ["1 – every cell uses the same frequency", "7", "12", "4"], 0, PYQ + "FDMA/TDMA systems need a cluster of several cells."),
    ("Match the generation with its key technology:\na. 1G  b. 2G  c. 3G  d. 4G\n1. Analog FDMA (AMPS)  2. Digital GSM/TDMA  3. WCDMA/UMTS  4. LTE with OFDMA, all-IP",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, "5G NR adds mmWave, massive MIMO, network slicing and very low latency."),
    ("Which statement about 4G LTE is correct?",
     ["It is an all-IP packet network; voice is carried as VoLTE", "It is analog", "It uses circuit switching for data", "It cannot carry video"], 0, PYQ + "Downlink OFDMA, uplink SC-FDMA."),
    ("A major feature of 5G is:",
     ["Network slicing, very low latency and support for massive IoT", "Analog voice", "Only 2G compatibility", "Circuit-switched data only"], 0, "Uses sub-6 GHz and mmWave bands."),
    ("In a GSM network, when a subscriber roams into another MSC area, the subscriber's temporary data is stored in the:",
     ["VLR of the visited MSC", "HLR of the visited network", "EIR", "SIM only"], 0, PYQ + "The HLR is updated with the new location."),
    ("The 15-digit number that uniquely identifies a mobile handset is the:",
     ["IMEI", "IMSI", "MSISDN", "TMSI"], 0, "*#06# shows it. MSISDN is the phone number; TMSI a temporary identity for privacy."),
    ("Frequency hopping in GSM is used to:",
     ["Reduce the effect of fading and interference", "Increase the number of SIMs", "Encrypt calls", "Locate users"], 0, PYQ + "The carrier frequency changes from frame to frame."),
    ("Which multiple-access technique is the basis of 4G LTE downlink?",
     ["OFDMA", "FDMA only", "TDMA only", "Pure CDMA"], 0, "Orthogonal Frequency-Division Multiple Access."),
    ("Which statement about GSM security is correct?",
     ["The SIM and the AuC share a secret key used for challenge–response authentication", "GSM sends passwords in plain text", "GSM has no authentication", "Encryption is done by the HLR"], 0,
     PYQ + "A random challenge (RAND) produces a signed response (SRES)."),
    ("Paging in a cellular network means:",
     ["Broadcasting a message in a location area to find a mobile for an incoming call", "Sending SMS", "Turning off the phone", "Charging the battery"], 0, "Location updates tell the network which area to page."),
    ("Consider the statements:\nI. GSM uses hard handoff.\nII. CDMA users are separated by time slots.\nWhich is/are correct?",
     I_II, 0, "Only I. CDMA users are separated by codes."),
    ("Consider the statements:\nI. The HLR stores permanent subscriber data.\nII. The EIR stores handset identities.\nWhich is/are correct?",
     I_II, 2, "Both."),
    ("Assertion (A): CDMA needs strict power control.\nReason (R): All users share the same band, so a strong nearby signal can mask weak distant ones.",
     AR, 0, "Near–far problem; R explains A."),
]

MOBILE_COMPUTING_IP = [
    ("What is the key characteristic of hybrid mobile applications?",
     ["They are written in platform-specific languages", "They are built using web technologies and run inside a native container",
      "They require separate code bases for each platform", "They offer performance equivalent to native apps"], 1,
     "HTML/CSS/JavaScript wrapped in a native shell (e.g. Cordova/Ionic); native apps use Kotlin/Java or Swift." + GTTC, "GTTC 2024 Technician Gr-III CS (C1) · Q64"),
    ("Mobile computing differs from fixed computing mainly because of:",
     ["Mobility, limited battery and resources, and changing or intermittent wireless connectivity", "Unlimited power", "Wired connections only", "Larger screens"], 0,
     PYQ + "Applications must handle disconnections and low bandwidth."),
    ("In mobile computing, 'middleware' is:",
     ["Software that sits between the mobile application and the network/OS, hiding heterogeneity (e.g. messaging, synchronisation)", "A type of SIM", "The phone's battery", "A radio tower"], 0,
     "Examples: message-oriented middleware, mobile agents, data-sync middleware."),
    ("A WAP gateway's role was to:",
     ["Translate between WAP (WML, compressed protocols) on phones and HTTP/HTML on the Internet", "Store SIM data", "Route GSM calls", "Encrypt Wi-Fi"], 0,
     PYQ + "WAP – Wireless Application Protocol; WML – Wireless Markup Language."),
    ("The main problem that Mobile IP solves is:",
     ["Keeping the same IP address while a host moves between networks", "Assigning MAC addresses", "Encrypting data", "Speeding up DNS"], 0, "Normally an IP address ties a host to one network."),
    ("In Mobile IP, the router on the mobile host's home network that forwards its packets is the:",
     ["Home agent", "Foreign agent", "Correspondent node", "DHCP server"], 0, PYQ + "The foreign agent is on the visited network."),
    ("The temporary address of a mobile host in the visited network in Mobile IP is the:",
     ["Care-of address (COA)", "Home address", "MAC address", "Loopback address"], 0, "It may be the foreign agent's address or a co-located address from DHCP."),
    ("In Mobile IP, the home agent delivers packets to the care-of address by:",
     ["Tunnelling (IP-in-IP encapsulation)", "Broadcasting", "Changing the destination MAC", "Dropping them"], 0, PYQ + "The foreign agent decapsulates and delivers them."),
    ("The three phases of Mobile IP operation are:",
     ["Agent discovery, registration and data transfer (tunnelling)", "Dial, talk and hang up", "Encode, send and decode", "Ping, trace and route"], 0, "Agents send advertisements; mobiles may send solicitations."),
    ("'Triangle routing' in Mobile IP refers to:",
     ["Packets from a correspondent going via the home agent while replies go directly – an inefficient path", "Routing in three cells", "Three home agents", "A routing loop"], 0,
     PYQ + "Route optimisation lets the correspondent learn the care-of address."),
    ("A 'co-located care-of address' is:",
     ["An address obtained by the mobile host itself (e.g. via DHCP) in the foreign network", "The home agent's address", "The foreign agent's MAC", "A multicast address"], 0, "Then the mobile host decapsulates packets itself."),
    ("Which of the following is a mobile operating system?",
     ["Android", "MS-DOS", "Unix System V", "OS/2"], 0, PYQ + "Android (Linux kernel, Google) and iOS (Apple)."),
    ("Android applications are packaged as:",
     [".apk (or .aab) files", ".exe files", ".dmg files", ".deb files"], 0, "iOS apps: .ipa."),
    ("In Android, an 'Activity' represents:",
     ["A single screen with a user interface", "A background database", "A network protocol", "A SIM card"], 0, PYQ + "Others: services, broadcast receivers, content providers; an Intent starts another activity."),
    ("Location-based services on mobiles mainly use:",
     ["GPS and cell/Wi-Fi positioning", "Only the IMEI", "Only SMS", "Bluetooth printers"], 0, "Used in maps, cab booking."),
    ("Which of the following is a challenge for mobile databases?",
     ["Disconnected operation and synchronisation of replicas", "Unlimited bandwidth", "Fixed location", "No battery limits"], 0, PYQ + "Caching and later sync solve some problems."),
    ("SMS, USSD and mobile banking apps are examples of:",
     ["Mobile services used for m-commerce / m-governance", "Satellite links", "Optical networks", "Operating systems"], 0, "USSD codes like *99# work without Internet."),
    ("Bluetooth-based pairing between a phone and a smartwatch forms a:",
     ["Personal area network (piconet)", "WAN", "MAN", "SAN"], 0, PYQ + "Up to 7 active slaves with one master."),
    ("A 'mobile agent' is:",
     ["A program that moves from one host to another, carrying its state, to do work near the data", "A sales person", "A base station", "A SIM card"], 0, "Reduces network traffic for disconnected users."),
    ("Which protocol layer change does Mobile IP require in correspondent hosts?",
     ["None – correspondent hosts need no change", "A new TCP version", "A new Ethernet", "A new DNS"], 0, PYQ + "Only home agent, foreign agent and mobile host take part."),
    ("Which statement about mobile computing is correct?",
     ["Context-aware applications adapt to location, time and device state", "Mobile devices never lose connectivity", "Mobile apps cannot use the cloud", "Batteries are not a concern"], 0, "Context awareness is a key mobile-computing feature."),
    ("Which device in a mobile network acts as a gateway between the cellular core and the Internet for packet data (GPRS)?",
     ["GGSN (Gateway GPRS Support Node)", "BTS", "HLR", "SIM"], 0, PYQ + "SGSN serves mobiles in its area; GGSN connects to external packet networks."),
    ("In 4G LTE, the gateway that connects the mobile network to the Internet is the:",
     ["P-GW (Packet Data Network Gateway)", "BSC", "MSC", "VLR"], 0, "LTE core = EPC (MME, S-GW, P-GW, HSS)."),
    ("Push notifications on smartphones are delivered by:",
     ["Platform notification services such as Firebase Cloud Messaging or Apple Push Notification service", "SMS only", "The SIM card", "The battery"], 0, PYQ + "The app server sends to the push service, which delivers to the device."),
    ("An app that works offline and syncs data later is following the design principle of:",
     ["Disconnected operation / offline-first", "Thin client only", "Always-on connectivity", "Batch processing"], 0, "Important for mobile users in weak-network areas."),
    ("Which is an example of a cross-platform mobile development framework?",
     ["Flutter", "Microsoft Excel", "Oracle Database", "Apache Tomcat"], 0, PYQ + "Others: React Native, Xamarin."),
    ("A 'thin client' mobile application:",
     ["Does most processing on the server and mainly displays results", "Does all processing on the device", "Has no network connection", "Is always native"], 0, "Fat (thick) clients do more processing locally."),
    ("Consider the statements:\nI. In Mobile IP the foreign agent is on the visited network.\nII. The care-of address changes when the mobile moves to another network.\nWhich is/are correct?",
     I_II, 2, "Both."),
    ("Consider the statements:\nI. Hybrid apps always perform exactly like native apps.\nII. Native Android apps are commonly written in Kotlin or Java.\nWhich is/are correct?",
     I_II, 1, "Only II (see GTTC 2024 Q64)."),
    ("Assertion (A): Mobile IP uses tunnelling.\nReason (R): The packet addressed to the home address must reach the mobile at its care-of address without changing the original header.",
     AR, 0, "R explains A."),
]

SATELLITE_CELLULAR = [
    ("A geostationary (GEO) satellite orbits the earth at an altitude of about:",
     ["35,786 km, with a period of 24 hours", "500 km, with a period of 90 minutes", "20,200 km, with a period of 12 hours", "384,000 km"], 0,
     PYQ + "It appears fixed above the equator; three GEO satellites can cover almost the whole earth except the poles."),
    ("GPS satellites are in which type of orbit?",
     ["MEO (about 20,200 km)", "GEO", "LEO below 500 km", "Polar GEO"], 0, "India's NavIC uses GEO and geosynchronous satellites."),
    ("Starlink and Iridium use which type of orbit?",
     ["LEO (low earth orbit)", "GEO", "MEO", "HEO only"], 0, PYQ + "LEO gives low delay but needs many satellites and handovers."),
    ("The main disadvantage of GEO satellites for interactive communication is:",
     ["Long propagation delay (about 0.24 s up and down; about 0.5 s round trip)", "They move fast across the sky", "They cover very small areas", "They need many handovers"], 0,
     "Distance ≈ 2 × 36,000 km at 3 × 10⁸ m/s."),
    ("A device on a communication satellite that receives an uplink signal, amplifies it and retransmits it on a different frequency is a:",
     ["Transponder", "Router", "Modem", "Hub"], 0, PYQ + "Uplink and downlink use different frequencies (e.g. C-band 6/4 GHz) to avoid interference."),
    ("In satellite communication, the uplink frequency is usually:",
     ["Higher than the downlink frequency", "Lower than the downlink frequency", "Equal to the downlink frequency", "Zero"], 0, "E.g. Ku-band 14 GHz up / 12 GHz down."),
    ("Cells in cellular network planning are drawn as hexagons because:",
     ["Hexagons cover an area without gaps or overlaps and approximate a circle", "Towers are hexagonal", "It reduces the number of users", "It is required by law"], 0, PYQ + "Real coverage areas are irregular."),
    ("In a cellular system, the cluster size N is given by N = i² + ij + j². With i = 2 and j = 1, N is:",
     ["7", "3", "4", "12"], 0, "4 + 2 + 1 = 7. Valid values: 1, 3, 4, 7, 9, 12, 13, …"),
    ("The co-channel reuse ratio D/R for cluster size N is √(3N). For N = 7 it is about:",
     ["4.58", "7", "21", "2.65"], 0, PYQ + "√21 ≈ 4.58. Larger N → less interference but fewer channels per cell."),
    ("A system has 700 duplex channels and uses a 7-cell cluster. How many channels does each cell get?",
     ["100", "700", "70", "4,900"], 0, "700 ÷ 7 = 100."),
    ("Reusing the same set of frequencies in cells that are far enough apart is called:",
     ["Frequency reuse", "Frequency hopping", "Handoff", "Multiplexing"], 0, PYQ + "It is what gives cellular systems their capacity."),
    ("Dividing a congested cell into smaller cells with lower-power base stations is called:",
     ["Cell splitting", "Sectoring", "Paging", "Roaming"], 0, "Sectoring uses directional antennas (e.g. three 120° sectors) to cut interference."),
    ("Transferring an ongoing call from one cell's base station to another as the user moves is called:",
     ["Handoff (handover)", "Roaming", "Paging", "Registration"], 0, PYQ + "Roaming = using another operator's network."),
    ("Which frequency band is used by microwaves for line-of-sight point-to-point links?",
     ["About 1 GHz to 300 GHz", "3 kHz to 1 GHz", "300 GHz to 400 THz", "Below 300 Hz"], 0, "Radio waves 3 kHz–1 GHz (omnidirectional); infrared 300 GHz–400 THz."),
    ("Infrared communication (e.g. TV remotes) cannot be used for long-distance links mainly because:",
     ["Infrared cannot pass through walls and is affected by sunlight", "It is too slow", "It needs cables", "It is illegal"], 0, PYQ + "But it gives security inside a room."),
    ("Signals arriving at a receiver by several reflected paths at slightly different times cause:",
     ["Multipath fading", "Attenuation only", "Crosstalk", "Thermal noise"], 0, "OFDM and diversity antennas reduce its effect."),
    ("Radio waves are suitable for broadcasting (AM/FM radio) mainly because they are:",
     ["Omnidirectional and can penetrate walls", "Unidirectional", "Unable to travel far", "Visible light"], 0, PYQ + "Microwaves are unidirectional."),
    ("India's satellite navigation system is:",
     ["NavIC (IRNSS)", "GLONASS", "Galileo", "BeiDou"], 0, "GLONASS – Russia; Galileo – EU; BeiDou – China."),
    ("Which satellite launch vehicle is used by ISRO to place communication satellites in geosynchronous transfer orbit?",
     ["GSLV / LVM3", "SLV-3 only", "Agni", "BrahMos"], 0, PYQ + "PSLV is mainly for polar/sun-synchronous orbits."),
    ("VSAT stands for:",
     ["Very Small Aperture Terminal – small dish earth stations for satellite data links", "Very Secure Access Token", "Virtual Satellite Transmission", "Voice Signal Amplifier"], 0, "Used by banks, lottery, remote offices."),
    ("A 'footprint' of a satellite is:",
     ["The area on earth covered by its signal", "Its weight", "Its orbit time", "Its launch pad"], 0, PYQ + "Spot beams cover smaller areas with higher power."),
    ("Which orbit needs the most satellites to give continuous global coverage?",
     ["LEO", "GEO", "MEO", "All need the same number"], 0, "LEO satellites cover small areas and move fast."),
    ("A cellular system designer wants to increase capacity in a busy city without new spectrum. The best option is:",
     ["Cell splitting and sectoring (smaller cells, more reuse)", "Increasing cluster size", "Removing base stations", "Using only GEO satellites"], 0, PYQ + "Small cells, microcells and femtocells."),
    ("A 'hard handoff' is described as:",
     ["Break-before-make – the old link is dropped before the new one is set up", "Make-before-break", "No handoff", "Handoff between satellites only"], 0, "Soft handoff (CDMA) is make-before-break."),
    ("The time a signal takes to travel is called:",
     ["Propagation delay", "Bandwidth", "Throughput", "Jitter"], 0, PYQ + "Delay = distance / speed."),
    ("Which statement about LEO satellites is correct?",
     ["They have low delay but each is visible from a ground point for only a few minutes", "They stay fixed above one point", "They are at 35,786 km", "They need no handover"], 0, "So handover between satellites is needed."),
    ("A 'transponder' commonly has a bandwidth of about:",
     ["36 MHz", "36 kHz", "36 GHz", "3.6 Hz"], 0, PYQ + "Typical C-band transponder width."),
    ("Consider the statements:\nI. A GEO satellite's period equals the earth's rotation period.\nII. GPS satellites are geostationary.\nWhich is/are correct?",
     I_II, 0, "Only I. GPS is MEO."),
    ("Consider the statements:\nI. Larger cluster size reduces co-channel interference.\nII. Larger cluster size increases channels per cell.\nWhich is/are correct?",
     I_II, 0, "Only I. Channels per cell = total ÷ N, which falls."),
    ("Assertion (A): Uplink and downlink frequencies of a satellite are different.\nReason (R): Using different frequencies prevents the strong transmitted signal from interfering with the weak received signal.",
     AR, 0, "R explains A."),
]

WLAN_MANET = [
    ("In IEEE 802.11, a group of stations communicating directly without an access point forms an:",
     ["Ad hoc network (IBSS)", "Infrastructure BSS", "ESS", "WAN"], 0, PYQ + "Infrastructure BSS uses an access point (AP); several BSSs joined by a distribution system form an ESS."),
    ("802.11 wireless LANs use which MAC method?",
     ["CSMA/CA", "CSMA/CD", "Token passing", "Pure ALOHA"], 0, "Collision detection is hard on radio, so collisions are avoided (IFS, backoff, ACK)."),
    ("The RTS/CTS exchange in 802.11 mainly helps with the:",
     ["Hidden-terminal problem", "Exposed-terminal problem only", "Near–far problem", "Count-to-infinity problem"], 0, PYQ + "Stations hearing CTS stay silent (set their NAV)."),
    ("The NAV (Network Allocation Vector) in 802.11 is used for:",
     ["Virtual carrier sensing – how long the medium will be busy", "Encryption", "Addressing", "Routing"], 0, "Physical carrier sensing listens to the channel."),
    ("Match the 802.11 standard with its main feature:\na. 802.11b  b. 802.11a  c. 802.11n  d. 802.11ax\n1. 2.4 GHz, 11 Mbps (DSSS)  2. 5 GHz, 54 Mbps (OFDM)  3. MIMO, up to 600 Mbps  4. Wi-Fi 6 (OFDMA)",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, "802.11g – 2.4 GHz, 54 Mbps; 802.11ac – 5 GHz (Wi-Fi 5)."),
    ("The name that identifies a wireless LAN to users is the:",
     ["SSID", "MAC address", "IMEI", "BSSID only"], 0, PYQ + "BSSID is the AP's MAC address."),
    ("Which Wi-Fi security protocol is considered weak and should not be used?",
     ["WEP", "WPA3", "WPA2-AES", "802.1X with EAP"], 0, "WEP's RC4 key handling is easily cracked."),
    ("Bluetooth (IEEE 802.15.1) operates in the 2.4 GHz band using:",
     ["Frequency-hopping spread spectrum (about 1600 hops per second)", "Direct-sequence only", "OFDMA", "Infrared"], 0, PYQ + "Short range (about 10 m for class 2)."),
    ("A Bluetooth piconet can have one master and at most how many ACTIVE slaves?",
     ["7", "1", "15", "255"], 0, "Up to 255 parked slaves; piconets linked together form a scatternet."),
    ("Zigbee, used in low-power sensor and home-automation networks, is based on:",
     ["IEEE 802.15.4", "IEEE 802.3", "IEEE 802.11", "IEEE 802.16"], 0, PYQ + "WiMAX is IEEE 802.16 (broadband wireless MAN)."),
    ("A MANET (Mobile Ad hoc Network) is:",
     ["A self-configuring network of mobile nodes without fixed infrastructure, using multi-hop routing", "A wired campus network", "A satellite constellation", "A cellular core network"], 0,
     "Each node acts as a router; topology changes often."),
    ("Which routing protocol for MANETs is reactive (on-demand)?",
     ["AODV", "DSDV", "OLSR", "OSPF"], 0, PYQ + "DSR is also reactive; DSDV and OLSR are proactive (table-driven); ZRP is hybrid."),
    ("DSDV (Destination-Sequenced Distance Vector) avoids routing loops by using:",
     ["Sequence numbers for routes", "Hop count only", "Source routes in packets", "Flooding every packet"], 0, "A proactive extension of Bellman–Ford for MANETs."),
    ("In DSR (Dynamic Source Routing), the route is carried:",
     ["In the header of each data packet (source routing)", "Only in routing tables", "In the DNS", "In the SIM"], 0, PYQ + "Route discovery floods a route request."),
    ("A key challenge of MANETs is:",
     ["Dynamic topology, limited battery and bandwidth, and security without a central authority", "Fixed topology", "Unlimited power", "Wired links"], 0, "Used in disaster relief, military, VANETs."),
    ("The 'exposed terminal problem' causes a station to:",
     ["Wrongly hold back from sending although its transmission would not cause a collision", "Send without hearing others", "Receive two signals", "Lose power"], 0, PYQ + "Reduces throughput."),
    ("Which device connects wireless stations to a wired LAN in an infrastructure Wi-Fi network?",
     ["Access point (AP)", "Repeater only", "Modem only", "Hub"], 0, "An AP acts as a bridge between 802.11 and Ethernet."),
    ("Wi-Fi in the 2.4 GHz band in India has how many non-overlapping 20 MHz channels commonly used?",
     ["3 (channels 1, 6 and 11)", "13", "1", "24"], 0, PYQ + "5 GHz offers many more non-overlapping channels."),
    ("Which wireless topology has every node connected to several others so that traffic can take multiple paths?",
     ["Mesh", "Star", "Bus", "Ring"], 0, "Wireless mesh networks extend coverage without cables."),
    ("Which is a common wireless network topology in homes, with all devices talking through one access point?",
     ["Star (infrastructure mode)", "Mesh", "Bus", "Ring"], 0, PYQ + "The AP is the centre."),
    ("Vehicular ad hoc networks (VANETs) are a special case of:",
     ["MANETs", "Satellite networks", "Wired LANs", "Optical networks"], 0, "Vehicles exchange safety messages."),
    ("802.11 frames are acknowledged because:",
     ["The sender cannot detect collisions on a wireless channel", "ACKs encrypt data", "ACKs reduce power", "Ethernet needs them"], 0, PYQ + "No ACK → assume collision/loss and retransmit."),
    ("Li-Fi transmits data using:",
     ["Visible light from LEDs", "Radio waves", "Sound waves", "Copper wires"], 0, "Cannot pass through walls."),
    ("WPA2 uses which encryption by default?",
     ["AES-CCMP", "RC4 (WEP)", "DES", "No encryption"], 0, PYQ + "WPA3 adds SAE for stronger password protection."),
    ("Which is the main advantage of wireless LANs?",
     ["Mobility and easy installation without cables", "Higher security than wired LANs by default", "No interference", "Unlimited range"], 0, "Wired LANs are generally faster and more secure."),
    ("In an 802.11 ESS, stations moving between APs is supported by:",
     ["The distribution system linking the APs", "GSM MSC", "Mobile IP only", "DNS"], 0, PYQ + "Handover between APs at layer 2."),
    ("LoRaWAN is designed for:",
     ["Long-range, low-power, low-data-rate IoT communication", "High-speed video streaming", "Satellite TV", "Gigabit Ethernet"], 0, "Can reach several kilometres."),
    ("Consider the statements:\nI. AODV discovers routes only when needed.\nII. OLSR is a reactive protocol.\nWhich is/are correct?",
     I_II, 0, "Only I. OLSR is proactive."),
    ("Consider the statements:\nI. Bluetooth uses frequency hopping.\nII. A piconet can have 7 active slaves.\nWhich is/are correct?",
     I_II, 2, "Both."),
    ("Assertion (A): 802.11 uses CSMA/CA rather than CSMA/CD.\nReason (R): A wireless station cannot reliably detect collisions while transmitting, and hidden stations may exist.",
     AR, 0, "R explains A."),
]

CLOUD = [
    ("Which of the following best describes \"Infrastructure as a service (IaaS)\" in cloud computing?",
     ["A model where users manage software applications while the vendor handles infrastructure", "A delivery model providing visualized computing resources over the Internet",
      "A cloud service that abstracts hardware management from the user completely", "A platform allowing developers to build, test and deploy application without worrying about the underlying hardware"], 1,
     "IaaS gives virtualised servers, storage and networks (e.g. AWS EC2); option 4 describes PaaS." + GTTC, "GTTC 2024 Lecturer CS · Q94"),
    ("Examine the following statements and choose the correct option\nStatement A: Cloud data security is primarily the responsibility of the cloud service provider\n"
     "Statement B: Customer still need to ensure proper data governance, access controls and compliance with regulations.",
     ["Both A and B are true and B is the correct explanation for A", "Both A and B are true and B is not the correct explanation of A", "A is true, but B is false", "A is false but B is true"], 1,
     "KEA's key; it reflects the shared-responsibility model – provider secures the infrastructure, the customer secures its data and access." + GTTC, "GTTC 2024 Lecturer CS · Q95"),
    ("Match the following:\na) Public Cloud  b) Private Cloud  c) Hybrid Cloud\ni. Used exclusively by a single business or organisation  ii. Allows data and applications to be shared  iii. Owned and operated by third party providers",
     ["a – iii, b – i, c – ii", "a – iii, b – ii, c – i", "a – i, b – iii, c – ii", "a – i, b – ii, c – iii"], 0,
     "A hybrid cloud combines public and private clouds and moves data/apps between them." + GTTC, "GTTC 2024 Technician Gr-III CS (C1) · Q61"),
    ("What type of computing technology refers to services and applications that typically run on a distributed network through virtualized resources?",
     ["Distributed computing", "Cloud computing", "Soft computing", "Parallel computing"], 1, "On-demand, virtualised resources over the network." + NOTE, "GFGC 2021 CS · Q106"),
    ("Which of the following protocol is used for discovering and retrieving objects from a cloud?",
     ["OCCI", "SMTP", "HTTP", "FTP"], 0, "Open Cloud Computing Interface – a REST-based standard for managing cloud resources." + NOTE, "GFGC 2021 CS · Q111"),
    kset("KSET 2024 CS&A · Q49"),
    ("Consider the following:\na) Cloud computing  b) The internet of things  c) Machine learning  d) Artificial intelligence\nWhich of the above is/are related to industrial revolution 4.0?",
     ["a only", "b only", "Both a and b", "a, b, c and d"], 3, "Industry 4.0 = cyber-physical systems: IoT, cloud, AI/ML, big data, robotics." + KLC, "Legislative Council 2024 Sr/Jr Programmer P1 · Q85"),
    ("The five essential characteristics of cloud computing (NIST) include:",
     ["On-demand self-service, broad network access, resource pooling, rapid elasticity and measured service", "Fixed capacity and manual provisioning", "Local storage only",
      "One user per server"], 0, PYQ + "NIST SP 800-145."),
    ("Gmail, Google Docs and Salesforce are examples of:",
     ["SaaS", "PaaS", "IaaS", "On-premises software"], 0, "The user just uses the application."),
    ("Google App Engine and Heroku, where developers deploy code without managing servers, are examples of:",
     ["PaaS", "SaaS", "IaaS", "DaaS"], 0, PYQ + "IaaS – AWS EC2, Azure VMs, Google Compute Engine."),
    ("In which service model does the customer manage the operating system, middleware and applications, while the provider manages hardware and virtualisation?",
     ["IaaS", "SaaS", "PaaS", "None"], 0, "The customer's control is highest in IaaS and lowest in SaaS."),
    ("A cloud shared by several organisations with common concerns (e.g. government departments) is a:",
     ["Community cloud", "Public cloud", "Private cloud", "Personal cloud"], 0, PYQ + "Four NIST deployment models: public, private, community, hybrid."),
    ("The ability of a cloud to add or remove resources automatically as demand rises and falls is:",
     ["Rapid elasticity", "Resource pooling", "Measured service", "Multi-tenancy"], 0, "Pay-as-you-go billing uses measured service."),
    ("Serving many customers from the same physical resources while keeping their data separate is called:",
     ["Multi-tenancy", "Single sign-on", "Load shedding", "Sharding only"], 0, PYQ + "Enabled by virtualisation."),
    ("A hypervisor is:",
     ["Software that creates and runs virtual machines on physical hardware", "A fast CPU", "A network cable", "A database"], 0, "Also called a virtual machine monitor (VMM)."),
    ("Type-1 (bare-metal) hypervisors include:",
     ["VMware ESXi, Microsoft Hyper-V, Xen and KVM", "VirtualBox and VMware Workstation", "Microsoft Word", "Docker Desktop only"], 0, PYQ + "Type-2 (hosted) hypervisors run on a host OS: VirtualBox, VMware Workstation."),
    ("Paravirtualisation differs from full virtualisation because:",
     ["The guest OS is modified to cooperate with the hypervisor", "No hypervisor is used", "The guest OS cannot run", "Hardware is emulated in software only"], 0, "Xen popularised paravirtualisation."),
    ("Containers (e.g. Docker) differ from virtual machines because containers:",
     ["Share the host OS kernel and are lighter and faster to start", "Each include a full guest OS", "Need a type-1 hypervisor", "Cannot run applications"], 0,
     PYQ + "Kubernetes orchestrates containers."),
    ("Amazon S3 is an example of:",
     ["Object storage", "Block storage", "A relational database", "A CPU"], 0, "Block storage – EBS volumes; file storage – EFS/NFS."),
    ("A cloud-hosted database managed by the provider (backups, patching, scaling) is called:",
     ["DBaaS (Database as a Service)", "IaaS only", "A local database", "A flat file"], 0, PYQ + "E.g. Amazon RDS, Azure SQL Database, Google Cloud SQL."),
    ("A 'virtual server' in the cloud is:",
     ["A virtual machine that behaves like a dedicated server", "A physical rack server", "A web browser", "A network switch"], 0, "Also called a VPS or cloud instance."),
    ("Moving computation close to where data is produced (e.g. at a factory gateway) instead of a distant data centre is called:",
     ["Edge computing", "Mainframe computing", "Batch computing", "Grid computing"], 0, PYQ + "Fog computing extends the cloud to the network edge."),
    ("A key advantage of cloud computing for a school or small business is:",
     ["No large upfront hardware cost – pay only for what is used", "Guaranteed zero downtime", "No need for Internet", "Unlimited free storage"], 0, "CapEx becomes OpEx."),
    ("A key risk of cloud computing is:",
     ["Dependence on the provider and Internet connectivity, and data-privacy concerns", "Too much local hardware", "No scalability", "No remote access"], 0, PYQ + "Vendor lock-in is another risk."),
    ("Which Indian government cloud initiative provides cloud services to government departments?",
     ["MeghRaj (GI Cloud)", "DigiLocker", "UMANG", "BHIM"], 0, "MeghRaj – Government of India's cloud initiative."),
    ("Live migration in virtualisation means:",
     ["Moving a running VM from one physical host to another with almost no downtime", "Shutting down a VM", "Copying files to USB", "Reinstalling the OS"], 0, PYQ + "Used for maintenance and load balancing."),
    ("Which statement about SaaS is correct?",
     ["The provider manages the application, OS and hardware; users access it through a browser", "Users install it on their own servers", "Users manage the hypervisor", "It needs no Internet"], 0, "Subscription-based."),
    ("Consider the statements:\nI. In IaaS the customer manages the operating system.\nII. In SaaS the customer manages the hardware.\nWhich is/are correct?",
     I_II, 0, "Only I."),
    ("Consider the statements:\nI. Containers share the host kernel.\nII. Type-2 hypervisors run directly on hardware without a host OS.\nWhich is/are correct?",
     I_II, 0, "Only I. Type-1 hypervisors run on bare metal."),
    ("Assertion (A): Virtualisation is a key enabling technology of cloud computing.\nReason (R): It lets one physical server run many isolated virtual machines that can be created and moved on demand.",
     AR, 0, "R explains A."),
]

IOT = [
    ("Match the following terms with their definitions in the context of Internet of things.\na) Sensor  b) Analytics  c) Connectivity  d) Actuator\n"
     "i. The process of making collected data useful by turning raw data into actionable insights  ii. A device that detects and responds to some type of input from the physical environment\n"
     "iii. A device that converts energy into motion  iv. Makes sharing data and insights possible. This is 'internet' in Internet of Things",
     ["a – ii, b – i, c – iv, d – iii", "a – ii, b – iii, c – iv, d – i", "a – iii, b – iv, c – i, d – ii", "a – iv, b – iii, c – i, d – ii"], 0,
     "Sensors sense, actuators act (motors, valves), connectivity links, analytics gives insight." + GTTC, "GTTC 2024 Technician Gr-III CS (C1) · Q62"),
    ("Match the IoT components to their descriptions:\na) Sensor  b) Actuator  c) IoT platform  d) Cloud Computing\n"
     "i. Converts digital signals from a sensor into physical system  ii. Aggregates, processes and analyses data from IoT devices providing insights and managing data flows\n"
     "iii. Collects data from physical environment through sensors  iv. Provides scalable storage and computational resources over the internet to handle large volumes of data",
     ["a – ii, b – i, c – iii, d – iv", "a – i, b – iii, c – ii, d – iv", "a – iii, b – i, c – ii, d – iv", "a – iv, b – i, c – iii, d – ii"], 2,
     "Sensor – collects; actuator – acts physically; platform – manages and analyses; cloud – storage and compute." + GTTC, "GTTC 2024 Technician Gr-III CS (C1) · Q63"),
    ("You are deploying a network of sensors that operate on a constrained power supply and require efficient Communication over IPv6.\nWhich among the following protocols should you consider for optimal performance?",
     ["BLE", "6LoWPAN", "HTTP/2", "XMPP"], 1, "6LoWPAN compresses IPv6 headers to run over low-power IEEE 802.15.4 radios." + GTTC, "GTTC 2024 Lecturer CS · Q99"),
    ("How does TSCH technique contribute to energy efficiency in IOT devices?",
     ["By keeping all devices powered at a constant level to maintain connectivity.", "By allowing devices to sleep and wake only during their scheduled time slots",
      "By sending data at random times to prevent disconnection", "By requiring all devices to perform computations synchronously."], 1,
     "Time-Slotted Channel Hopping (IEEE 802.15.4e) schedules slots so radios can sleep otherwise." + GTTC, "GTTC 2024 Lecturer CS · Q100"),
    ("______ is the community that is working together to establish an IoT architecture based on open source technologies and standards.",
     ["Eclipse IoT", "Red Hat", "Intercloud", "Bot&Bot"], 0, "Eclipse IoT hosts projects such as Paho (MQTT) and Mosquitto." + NOTE, "GFGC 2021 CS · Q109"),
    ("______ is the standard port number of secure MQTT?",
     ["1883", "8000", "8883", "8888"], 2, "MQTT uses 1883; MQTT over TLS uses 8883." + NOTE, "GFGC 2021 CS · Q110"),
    ("The term 'Internet of Things' was coined in 1999 by:",
     ["Kevin Ashton", "Tim Berners-Lee", "Vint Cerf", "Mark Weiser"], 0, PYQ + "Mark Weiser coined 'ubiquitous computing'."),
    ("The Internet of Things refers to:",
     ["Everyday physical objects with sensors and network connectivity that collect and exchange data", "Only smartphones", "Only the WWW", "Cable TV"], 0, "Smart homes, wearables, smart agriculture, smart cities."),
    ("MQTT follows which communication model?",
     ["Publish–subscribe through a broker", "Request–response only", "Peer-to-peer file sharing", "Broadcast only"], 0, PYQ + "Clients publish to topics; subscribers receive them."),
    ("CoAP (Constrained Application Protocol) runs over:",
     ["UDP, with a REST-like request/response model for constrained devices", "TCP only", "Bluetooth only", "Ethernet frames directly"], 0, "Port 5683; like a lightweight HTTP."),
    ("A passive RFID tag:",
     ["Has no battery and is powered by the reader's radio signal", "Has a large battery", "Uses GPS", "Uses Wi-Fi"], 0, PYQ + "Used in FASTag tolls, library books, supply chains."),
    ("NFC (Near Field Communication), used in contactless payments, works over a distance of about:",
     ["4–10 cm", "100 m", "10 km", "1 m to 50 m"], 0, "13.56 MHz."),
    ("A common three-layer IoT architecture consists of:",
     ["Perception (sensing) layer, network layer and application layer", "Physical, data link and network layers", "Client, server and database", "Input, process and output only"], 0,
     PYQ + "Five-layer models add processing (middleware) and business layers."),
    ("An IoT gateway's role is to:",
     ["Connect local sensor networks (e.g. Zigbee, BLE) to the Internet/cloud, often translating protocols and filtering data", "Generate electricity", "Act as a sensor", "Replace the cloud entirely"], 0,
     "Often does edge processing."),
    ("Which sensor would be used in an automatic irrigation system?",
     ["Soil-moisture sensor", "Gyroscope", "Microphone", "Barcode scanner"], 0, PYQ + "An actuator (valve/pump) switches the water on."),
    ("Which device in an IoT system turns a digital command into physical action?",
     ["Actuator", "Sensor", "Gateway", "Cloud server"], 0, "Motors, relays, solenoid valves."),
    ("IPv6 is important for IoT mainly because:",
     ["Its huge address space can give every device a unique address", "It is slower", "It needs no routers", "It removes security"], 0, PYQ + "2^128 addresses."),
    ("BLE (Bluetooth Low Energy) is widely used in IoT because it:",
     ["Consumes very little power for short-range, low-data-rate links", "Gives gigabit speed", "Works over many kilometres", "Needs wired power"], 0, "Fitness bands, beacons."),
    ("Which of the following is a popular low-cost microcontroller board used in IoT prototyping?",
     ["Arduino", "Mainframe", "Supercomputer", "Optical drive"], 0, PYQ + "Raspberry Pi is a single-board computer; ESP8266/ESP32 add Wi-Fi."),
    ("A 'digital twin' is:",
     ["A virtual model of a physical object or system kept up to date with real-time data", "A duplicate SIM", "A backup hard disk", "A twin processor"], 0, "Used in manufacturing and smart cities."),
    ("A smart meter that sends electricity readings automatically to the utility is an example of:",
     ["IoT (machine-to-machine communication)", "A mainframe", "A word processor", "Batch processing"], 0, PYQ + "M2M – devices communicate without human input."),
    ("A major security concern in IoT is:",
     ["Default passwords and unpatched devices that can be hijacked into botnets", "Too much battery", "Excessive screen size", "Lack of sensors"], 0, "The Mirai botnet (2016) used insecure IoT cameras and routers."),
    ("Which protocol is designed for long-range, low-power IoT over licensed cellular spectrum?",
     ["NB-IoT", "Bluetooth classic", "Wi-Fi 6E", "Ethernet"], 0, PYQ + "LoRaWAN uses unlicensed spectrum."),
    ("FASTag, used for highway toll payment in India, is based on:",
     ["Passive RFID", "GPS only", "Bluetooth", "Infrared"], 0, "A reader at the toll plaza reads the tag on the windshield."),
    ("Data from millions of IoT devices is huge, fast and varied. Its processing belongs to the field of:",
     ["Big data analytics", "Desktop publishing", "Word processing", "Compiler design"], 0, PYQ + "Volume, velocity, variety."),
    ("Which of the following is NOT a typical IoT application?",
     ["Manual typewriter", "Smart home lighting", "Wearable fitness tracker", "Smart traffic signals"], 0, "No sensing or connectivity."),
    ("In MQTT, the 'QoS 2' level guarantees that a message is delivered:",
     ["Exactly once", "At most once", "At least once", "Never"], 0, PYQ + "QoS 0 – at most once; QoS 1 – at least once."),
    ("Consider the statements:\nI. Sensors convert physical quantities into electrical signals.\nII. Actuators collect data from the environment.\nWhich is/are correct?",
     I_II, 0, "Only I. Actuators act on the environment."),
    ("Consider the statements:\nI. MQTT is a lightweight publish–subscribe protocol.\nII. CoAP is designed for constrained devices.\nWhich is/are correct?",
     I_II, 2, "Both."),
    ("Assertion (A): IoT devices often send data to the cloud.\nReason (R): Small devices have limited storage and processing, while the cloud offers scalable storage and analytics.",
     AR, 0, "R explains A."),
]

TOPICS = {
    "Mobile Technology – Part 1": [
        ("1 · GSM and CDMA – Architecture, Services and Generations", GSM_CDMA),
        ("2 · Mobile Computing, Middleware, Gateways and Mobile IP", MOBILE_COMPUTING_IP),
    ],
    "Mobile Technology – Part 2": [
        ("1 · Communication Satellites, Cellular Topology and Wireless Transmission", SATELLITE_CELLULAR),
        ("2 · Wireless LANs, Bluetooth, Wireless Topologies and MANETs", WLAN_MANET),
    ],
    "Cloud Computing and IoT": [
        ("1 · Cloud Service and Deployment Models, Virtualization and Storage", CLOUD),
        ("2 · Internet of Things – Components, Architecture and Protocols", IOT),
    ],
}

NOTES = {
    "Mobile Technology – Part 1": [
        {"title": "GSM, CDMA and mobile computing – revision sheet", "md": """## GSM (2G)
- TDMA + FDMA; GSM-900: up 890–915, down 935–960 MHz; 124 × 200 kHz carriers; **8 slots** per carrier
- **MS** (ME + SIM) · **BSS** (BTS, BSC) · **NSS** (MSC, HLR, VLR, AuC, EIR) · OSS
- HLR permanent data; VLR visitors; AuC key Ki (A3 auth, A8 key, A5 encryption); EIR – IMEI list
- Interfaces: Um (air), Abis (BTS–BSC), A (BSC–MSC); MAP runs on **SS7**
- IDs: IMEI (handset, 15 digits), IMSI (SIM), MSISDN (number), TMSI (temporary)
- Services: bearer, teleservices (voice, SMS 160 chars), supplementary
- GPRS 2.5G (packet; SGSN, GGSN), EDGE 2.75G; hard handoff

## CDMA and generations
- Unique spreading codes; reuse factor 1; **soft handoff**; power control (near–far)
- 1G analog AMPS → 2G GSM/IS-95 → 3G WCDMA/UMTS, CDMA2000 → 4G LTE (OFDMA, all-IP, VoLTE; EPC: MME, S-GW, P-GW, HSS) → 5G NR (slicing, mmWave, low latency)

## Mobile computing
- Constraints: mobility, battery, bandwidth, disconnections; context-aware apps; offline-first sync
- Middleware; mobile agents; WAP gateway (WML ↔ HTML); thin vs fat clients
- Native (Kotlin/Java, Swift) vs **hybrid** (web tech in native container) vs cross-platform (Flutter, React Native)
- Android: .apk, Activity, Intent; push via FCM/APNs

## Mobile IP
- Home agent (home network), foreign agent (visited), **care-of address** (FA or co-located via DHCP)
- Phases: agent discovery → registration → **tunnelling (IP-in-IP)**; triangle routing → route optimisation
- Correspondent hosts need no change
"""}],
    "Mobile Technology – Part 2": [
        {"title": "Satellites, cellular design and wireless LANs – revision sheet", "md": """## Satellites
| Orbit | Altitude | Example |
|---|---|---|
| LEO | 500–2000 km | Starlink, Iridium |
| MEO | ~20,200 km | GPS |
| GEO | **35,786 km**, 24 h | INSAT/GSAT |
- GEO delay ≈ 0.24 s one way (≈0.5 s round trip); 3 GEOs cover the earth (not poles)
- Transponder (~36 MHz); uplink > downlink frequency (C 6/4, Ku 14/12 GHz); footprint; VSAT; NavIC (India)

## Cellular design
- Hexagonal cells; **N = i² + ij + j²** (1, 3, 4, 7, 12…); **D/R = √(3N)** (N=7 → 4.58)
- Channels per cell = total ÷ N; cell splitting, sectoring; hard (break-before-make) vs soft handoff; roaming, paging
- Radio waves 3 kHz–1 GHz omni; microwaves 1–300 GHz line of sight; infrared no walls; multipath fading

## Wireless LANs (802.11)
- Ad hoc (IBSS) vs infrastructure (BSS with AP); ESS via distribution system; SSID/BSSID
- **CSMA/CA** + ACK; RTS/CTS for hidden terminal; NAV = virtual carrier sense; exposed terminal problem
- 802.11b 2.4 GHz 11 Mbps · a 5 GHz 54 · g 2.4 GHz 54 · n MIMO 600 · ac 5 GHz · ax Wi-Fi 6
- Security: WEP (weak) → WPA2 (AES-CCMP) → WPA3
- Bluetooth 802.15.1: FHSS 1600 hops/s, piconet 1 master + **7 active**, scatternet; Zigbee 802.15.4; WiMAX 802.16; Li-Fi; LoRaWAN

## MANET
- No infrastructure, multi-hop, dynamic topology; VANET
- Proactive: DSDV (sequence numbers), OLSR · Reactive: **AODV**, DSR (source routing) · Hybrid: ZRP
"""}],
    "Cloud Computing and IoT": [
        {"title": "Cloud computing and IoT – revision sheet", "md": """## Cloud (NIST SP 800-145)
- 5 characteristics: on-demand self-service, broad network access, resource pooling, **rapid elasticity**, measured service
- Service models: **SaaS** (Gmail, Salesforce) · **PaaS** (App Engine, Heroku) · **IaaS** (EC2, Azure VMs); DBaaS
- Deployment: public, private, community, hybrid; India – MeghRaj
- Shared responsibility; multi-tenancy; pay-as-you-go; risks – lock-in, privacy, connectivity
- Storage: object (S3), block (EBS), file; OCCI; edge/fog computing

## Virtualization
- Hypervisor/VMM; **type-1** bare metal (ESXi, Hyper-V, Xen, KVM) vs **type-2** hosted (VirtualBox)
- Full vs paravirtualisation; programming-environment virtualisation (JVM); live migration
- Containers (Docker, Kubernetes) share host kernel

## IoT
- Term – **Kevin Ashton 1999**; Industry 4.0 = IoT + cloud + AI/ML + big data
- Components: sensor, actuator, connectivity, gateway, platform/analytics, cloud; layers: perception–network–application
- Protocols: **MQTT** (pub/sub, broker, 1883 / **8883 TLS**, QoS 0/1/2), **CoAP** (UDP, REST, 5683), **6LoWPAN** (IPv6 over 802.15.4), TSCH, Zigbee, BLE, LoRaWAN, NB-IoT, RFID (passive – FASTag), NFC (~4–10 cm)
- Boards: Arduino, Raspberry Pi, ESP32; digital twin; M2M; security – default passwords, Mirai botnet
- Eclipse IoT – open-source IoT community
"""}],
}
