"""Paper 2 · Unit 9 · P2-U9-08 IPv6, ARP, Delivery & Routing (2 sub-topics × 30).
References: Behrouz A. Forouzan, Data Communications and Networking (5th ed., chs. 9, 18–22: ARP, forwarding, unicast routing, IPv6);
Tanenbaum, Computer Networks (ch. 5); Silberschatz, Operating System Concepts (distributed-system routing strategies).
Each set mixes REAL previous-year questions (exact wording, printed option order, `source`) with new ones. Official answers: KEA final
keys for Legislative Council Secretariat 2024 (Computer Operator P2, Junior Console Operator P2 – booklet A1, read from the page images
where the OCR lost options) and GTTC 2024 (Lecturer CS – A1). KSET/PGCET questions: answers worked out by ExamSim. The
distance-vector and Dijkstra numbers below were checked by hand calculation."""
from packlib import AR, I_II
from p2u7_a import kset, PYQ, KLC, GTTC, NOTE

IPV6_ARP = [
    ("Which of the following statements about IPV6 are true?\na. It uses 128 bit addresses\nb. IPV6 eliminates the need for DHCP\n"
     "c. IPV6 can coexist with IPV4 in dual stack environment\nd. IPV6 addresses are always written in decimal notation",
     ["a and c only", "a and b only", "a, c and d only", "c and b only"], 0,
     "IPv6 still uses DHCPv6 (besides SLAAC) and is written in hexadecimal." + KLC, "Legislative Council 2024 Junior Console Operator P2 · Q58"),
    ("Considering the following statements, choose the correct option.\nAssertion (A): ARP (Address Resolution Protocol) is used to map IP addresses to MAC addresses\n"
     "Reason (R): ARP is used only in IPV4 networks and is not necessary in IPV6",
     ["Both (A) and (R) are correct and (R) is the correct explanation of (A)", "Both (A) and (R) are correct but (R) is not the correct explanation of (A)",
      "(A) is correct but (R) is incorrect", "Both (A) and (R) are incorrect"], 2,
     "KEA treats R as wrong: IPv6 still needs address resolution – it is done by ICMPv6 Neighbor Discovery instead of ARP." + KLC,
     "Legislative Council 2024 Junior Console Operator P2 · Q11"),
    ("Which sequence accurately describes the process of sending data in IPV6?",
     ["Host → Switch → Destination", "Host → Router → Destination", "Host → Network → Router → Destination", "Host → Router → Switch → Destination"], 1,
     "KEA's key: the host hands the packet to a router, which forwards it to the destination network." + KLC, "Legislative Council 2024 Junior Console Operator P2 · Q64"),
    ("What is the correct sequence of ARP (Address resolution protocol)?",
     ["ARP Request → Data Transmission → ARP Reply → Caching", "ARP Reply → ARP Request → Data Transmission → Caching",
      "ARP Request → ARP Reply → Caching → Data Transmission", "ARP Request → Caching → ARP Reply → Data Transmission"], 2,
     "Broadcast request → unicast reply with the MAC address → store it in the ARP cache → send the frame." + KLC, "Legislative Council 2024 Computer Operator P2 · Q48"),
    ("Match the following types of internet connection with their description\n(a) Unicast  (b) Multicast  (c) Broadcast  (d) Any cast\n"
     "i) Broadcasts communication to all devices  ii) Communication from one device to many devices\niii) Communication from one device to another only  iv) Communication to the nearest device in a group",
     ["a – i, b – ii, c – iv, d – iii", "a – i, b – iv, c – ii, d – iii", "a – iii, b – i, c – ii, d – iv", "a – iii, b – ii, c – i, d – iv"], 3,
     "IPv6 has unicast, multicast and anycast addresses – no broadcast." + KLC, "Legislative Council 2024 Computer Operator P2 · Q51"),
    kset("KSET 2024 CS&A · Q87"),
    ("Which among the following features is present in IPv6 but not in IPv4?",
     ["Fragmentation", "Header checksum", "Options", "Auto configuration"], 3,
     "Stateless address autoconfiguration (SLAAC); IPv6 dropped the header checksum and router fragmentation." + NOTE, "PGCET 2023 M.Tech CS · Q44"),
    ("In IPv6 header, the base header can be followed by up to ______ extension headers.",
     ["4", "8", "6", "7"], 2,
     "Forouzan: up to six extension headers – hop-by-hop, destination, routing, fragmentation, authentication, ESP." + NOTE, "PGCET 2023 M.Tech CS · Q45"),
    ("An IPv6 address is written as:",
     ["Eight groups of four hexadecimal digits separated by colons", "Four decimal numbers separated by dots", "Six groups of two hex digits separated by hyphens", "Sixteen octal numbers"], 0,
     PYQ + "IPv6 – colon-hex (128 bits); IPv4 – dotted decimal (32 bits); MAC – 48 bits, hex."),
    ("The abbreviated form of 2001:0DB8:0000:0000:0000:FF00:0042:8329 is:",
     ["2001:DB8::FF00:42:8329", "2001:DB8:FF00:42:8329", "2001::DB8::FF00:42:8329", "21:DB8::FF:42:8329"], 0,
     "Drop leading zeros in each group; replace ONE run of all-zero groups by '::'."),
    ("Why can '::' appear only once in an IPv6 address?",
     ["Otherwise the number of zero groups each '::' stands for would be ambiguous", "It is a reserved prefix", "It marks the end of the address", "It is used only for IPv4"], 0,
     PYQ + "The address must expand back to exactly eight groups."),
    ("The size of the IPv6 base header is:",
     ["40 bytes (fixed)", "20 to 60 bytes", "32 bytes", "128 bytes"], 0, PYQ + "IPv4 header is 20–60 bytes (variable)."),
    ("Which IPv4 header field is removed in IPv6 because upper layers and link layers already check errors?",
     ["Header checksum", "Source address", "Version", "Payload length"], 0, "Removing it speeds up router processing."),
    ("The IPv6 field that plays the role of IPv4's TTL is:",
     ["Hop limit", "Flow label", "Traffic class", "Next header"], 0, PYQ + "Decremented at each router; packet dropped at 0."),
    ("In IPv6, the 'Next Header' field identifies:",
     ["The type of the next extension header or the upper-layer protocol (e.g. TCP)", "The next router's address", "The number of hops left", "The packet's priority"], 0,
     "It works like IPv4's Protocol field."),
    ("The 20-bit 'Flow label' in the IPv6 header is used to:",
     ["Identify packets that need special handling, such as real-time audio/video flows", "Count hops", "Detect errors", "Fragment packets"], 0, PYQ + "Traffic class – priority."),
    ("In IPv6, fragmentation is done:",
     ["Only by the source host (using path-MTU discovery)", "By every router", "Only by the destination", "Never – packets cannot exceed 64 KB"], 0,
     "Routers send ICMPv6 'Packet too big' instead of fragmenting."),
    ("The IPv6 loopback address is:",
     ["::1", "127.0.0.1", "FE80::1", "FF02::1"], 0, PYQ + "127.0.0.1 is the IPv4 loopback."),
    ("IPv6 link-local addresses begin with the prefix:",
     ["FE80::/10", "FF00::/8", "2000::/3", "FC00::/7"], 0, "FF00::/8 – multicast; 2000::/3 – global unicast; FC00::/7 – unique local."),
    ("Which three strategies were defined for the transition from IPv4 to IPv6?",
     ["Dual stack, tunnelling and header translation", "Subnetting, supernetting and NAT", "Static, dynamic and default routing", "Flooding, forwarding and filtering"], 0, PYQ + "Forouzan ch. 22."),
    ("When two IPv6 hosts must communicate across an IPv4-only region, the IPv6 packet is placed inside an IPv4 packet. This is:",
     ["Tunnelling", "Dual stack", "Header translation", "Fragmentation"], 0, "The IPv4 protocol field is set to 41 for IPv6-in-IPv4."),
    ("In IPv6, the job of ARP is done by:",
     ["ICMPv6 Neighbor Discovery", "RARP", "DHCPv6 only", "IGMP"], 0, PYQ + "ND also finds routers and checks duplicate addresses; IGMP's role is done by MLD."),
    ("An ARP request and an ARP reply are sent respectively as:",
     ["Broadcast and unicast", "Unicast and broadcast", "Multicast and multicast", "Unicast and unicast"], 0, PYQ + "Every host on the LAN sees the request; only the owner replies."),
    ("RARP was used to:",
     ["Find a host's IP address from its MAC address (for diskless machines)", "Find a MAC address from an IP address", "Resolve domain names", "Assign ports"], 0,
     "Replaced by BOOTP and then DHCP."),
    ("A router that answers ARP requests on behalf of hosts on another network is performing:",
     ["Proxy ARP", "Gratuitous ARP", "Reverse ARP", "Inverse NAT"], 0, "Gratuitous ARP – a host announces its own IP–MAC pair (also detects duplicate IPs)."),
    ("ARP messages are carried:",
     ["Directly inside data-link frames (Ethernet type 0x0806)", "Inside UDP datagrams", "Inside TCP segments", "Inside ICMP messages"], 0, PYQ + "IPv4 uses Ethernet type 0x0800."),
    ("Why are entries in an ARP cache removed after some time?",
     ["Because IP-to-MAC mappings can change (e.g. a NIC is replaced)", "To save power", "Because ARP is a routing protocol", "Because MAC addresses expire yearly"], 0, "Stale entries would send frames to the wrong host."),
    ("About how many addresses does IPv6 provide?",
     ["2^128 ≈ 3.4 × 10^38", "2^32 ≈ 4.3 × 10^9", "2^64", "2^48"], 0, PYQ + "IPv4: 2^32."),
    ("In modified EUI-64, a 48-bit MAC address is turned into a 64-bit IPv6 interface ID by:",
     ["Inserting FFFE in the middle and inverting the universal/local (7th) bit", "Adding 16 zeros at the end", "Repeating the last 16 bits", "Hashing it with MD5"], 0,
     "Used in stateless autoconfiguration."),
    ("Consider the statements:\nI. IPv6 has no broadcast addresses.\nII. The IPv6 base header contains a header checksum.\nWhich is/are correct?",
     I_II, 0, "Only I. IPv6 uses multicast (e.g. FF02::1 all nodes) instead of broadcast and has no header checksum."),
]

ROUTING = [
    ("Which of the following statements are true about the BGP (Border Gateway Protocol)?\na) BGP is a distance vector routing protocol\n"
     "b) BGP is used for routing between different autonomous systems\nc) BGP is a path vector protocol\nd) BGP uses hop count as its routing metric",
     ["b and c", "a and b", "b and d", "a, b and d"], 0, "BGP is a path-vector inter-AS protocol using policies and path attributes." + KLC,
     "Legislative Council 2024 Junior Console Operator P2 · Q6"),
    ("Match the routing protocols with their characteristics.\na) RIP  b) OSPF  c) BGP  d) EIGRP\ni) Uses link state algorithm  ii) Uses distance vector algorithm\n"
     "iii) Path-vector protocol used for inter-domain routing  iv) Hybrid of distance vector and link-state protocols",
     ["a - ii, b - i, c - iii, d - iv", "a - i, b - ii, c - iv, d - iii", "a - ii, b - i, c - iv, d - iii", "a - i, b - iv, c - iii, d - ii"], 0,
     "RIP – distance vector; OSPF – link state; BGP – path vector; EIGRP – advanced distance vector ('hybrid')." + KLC,
     "Legislative Council 2024 Junior Console Operator P2 · Q8"),
    ("Which of the following code value is NOT an Error-reporting message of ICMP message?",
     ["03", "05", "08", "11"], 2,
     "Type 8 is echo request (a query, used by ping). 3 – destination unreachable, 5 – redirect, 11 – time exceeded." + GTTC, "GTTC 2024 Lecturer CS · Q75"),
    ("A router sends an ICMP 'redirect' (type 5) message to a host when:",
     ["The host sent a packet to this router although a better next-hop router exists on the same network", "The TTL reaches zero",
      "The destination port is closed", "The packet is too big"], 0, PYQ + "The host then updates its routing table."),
    ("Which of the following statement/s is/are not correct?\na. OSPF is based on distance vector routing protocol.\nb. Both link-state and distance vector routing are based on the least cost goal.\n"
     "c. BGP is based on the path vector algorithm.\nd. The three-node instability can be avoided using split horizon combined with Poison reverse.\ne. RIP is based on link state algorithm.",
     ["a, d and e only", "a and b only", "b and c only", "b, c and e only"], 0,
     "OSPF is link state and RIP distance vector; split horizon + poison reverse fixes two-node loops, not three-node instability." + NOTE, "PGCET 2024 M.Tech CS · Q70"),
    ("Why does topological addressing enable large networks to be built?",
     ["It reduces the size of routing tables and the amount of information that must be exchanged", "It reduces the size and information in forwarding table",
      "It only reduces the size of routing table", "It reduces the size of routing table and increases the amount of information to be exchanged"], 0,
     "Hierarchical addresses let one entry (prefix) stand for a whole region – route aggregation." + NOTE, "PGCET 2026 CS · Q62"),
    ("Each router in a link state protocol performs these 5 steps, arrange them in chronological order.\n(a) Send the packet to all other routers\n(b) Measure the delay or cost to each of its neighbours\n"
     "(c) Compute the shortest path to every other router\n(d) Construct a packet telling all it has just learned\n(e) Discover its neighbours and learn their network address",
     ["e, b, a, d, c", "b, c, e, a, d", "c, d, a, e, b", "e, b, d, a, c"], 3, "Tanenbaum's five steps: discover, measure, build LSP, flood, run Dijkstra." + NOTE, "PGCET 2026 CS · Q64"),
    ("In the distance vector routing algorithm each router",
     ["Sends the entire network topology to all routers periodically", "Maintains only the distance to each destination and the next hop and exchanges this with neighbours",
      "Chooses routers based on source-routing headers", "Requires a centralized controller to compute all paths"], 1,
     "Topology flooding is link state; distance vector shares its vector only with neighbours (Bellman–Ford)." + NOTE, "PGCET 2026 CS · Q66"),
    ("The IPv6 version of BGP is",
     ["MP-BGPv4", "BGPv5", "BGP IPv6", "MP-BGPv2"], 0, "Multiprotocol extensions to BGP-4 (RFC 4760) carry IPv6 routes." + NOTE, "PGCET 2023 M.Tech CS · Q42"),
    kset("KSET 2023 CS&A · Q30"),
    ("Delivery of a packet is called 'direct' when:",
     ["The destination is on the same network as the deliverer", "It passes through at least one router", "It uses a default route", "It is a broadcast"], 0,
     PYQ + "Indirect delivery – from router to router until the last (direct) delivery."),
    ("A forwarding table that lists one entry per destination NETWORK (not per host) uses:",
     ["Network-specific forwarding", "Host-specific forwarding", "Next-hop only", "Source routing"], 0, "Techniques: next-hop, network-specific, host-specific, default."),
    ("The default route in an IPv4 forwarding table is written as:",
     ["0.0.0.0/0", "255.255.255.255/32", "127.0.0.0/8", "224.0.0.0/4"], 0, PYQ + "Used when no other entry matches."),
    ("In the Internet, each router forwards a packet by looking mainly at:",
     ["The packet's destination address and its own forwarding table (hop-by-hop)", "The full path written by the source", "The source MAC address", "The TCP port number"], 0,
     "IP is connectionless; each router decides only the next hop. Source routing is optional and rarely used."),
    ("When several forwarding-table entries match a destination address, a router chooses the entry with:",
     ["The longest prefix (most specific mask)", "The shortest prefix", "The first entry", "The lowest interface number"], 0, "Longest-prefix match in classless addressing."),
    ("In RIP, the maximum hop count for a reachable network is:",
     ["15 (16 means infinity)", "255", "30", "100"], 0, PYQ + "So RIP suits small networks."),
    ("RIP sends periodic updates every 30 seconds using:",
     ["UDP port 520", "TCP port 179", "IP protocol 89", "UDP port 53"], 0, "BGP – TCP 179; OSPF – directly over IP, protocol 89."),
    ("OSPF computes shortest paths using:",
     ["Dijkstra's algorithm", "Bellman–Ford algorithm", "Kruskal's algorithm", "Flooding only"], 0, PYQ + "OSPF divides an AS into areas joined by backbone area 0."),
    ("BGP sessions between routers run over:",
     ["TCP port 179", "UDP port 520", "IP protocol 89", "ICMP"], 0, "Reliable transport is needed for large route updates."),
    ("The 'count-to-infinity' problem occurs in:",
     ["Distance-vector routing", "Link-state routing", "Static routing", "Flooding"], 0,
     PYQ + "Remedies: split horizon, poison reverse, hold-down timers, a small 'infinity' (16 in RIP)."),
    ("RIP and OSPF are ______ routing protocols, while BGP is ______.",
     ["Intra-domain (interior); inter-domain (exterior)", "Inter-domain; intra-domain", "Both inter-domain", "Both static"], 0, "Interior gateway vs exterior gateway protocols."),
    ("An autonomous system (AS) is:",
     ["A group of networks and routers under one administrative authority", "A single router", "A self-configuring host", "A type of IPv6 address"], 0, PYQ + "Each AS has an AS number; BGP routes between ASes."),
    ("Router A has neighbours B (link cost 2) and C (link cost 5). B reports a distance of 3 to network D; C reports 1. A's distance to D and next hop are:",
     ["5 via B", "6 via C", "3 via B", "1 via C"], 0, "Bellman–Ford: min(2 + 3, 5 + 1) = 5 through B."),
    ("Links: A–B 4, A–C 1, C–B 2, B–D 1, C–D 5. The shortest-path cost from A to D (Dijkstra) is:",
     ["4 (A–C–B–D)", "5 (A–B–D)", "6 (A–C–D)", "3"], 0, PYQ + "A–C 1, C–B 2 (B = 3), B–D 1 → 4; A–B–D = 5; A–C–D = 6."),
    ("'Static routing' means:",
     ["Routes are entered manually by the administrator and do not adapt automatically", "Routes change every second", "Routes are learnt by RIP", "Routes are chosen randomly"], 0,
     "Dynamic routing uses protocols such as RIP, OSPF, BGP."),
    ("The 'ping' command uses which ICMP messages?",
     ["Echo request and echo reply", "Time exceeded only", "Destination unreachable", "Redirect"], 0, PYQ + "traceroute/tracert uses increasing TTL values and 'time exceeded' replies."),
    ("Which protocol do hosts use to tell a local multicast router which multicast groups they want to join (IPv4)?",
     ["IGMP", "ICMP", "ARP", "OSPF"], 0, "IPv6 uses MLD (part of ICMPv6)."),
    ("Link-state routing generally converges faster than distance-vector routing because:",
     ["Every router has the complete topology and computes routes itself", "It uses hop count only", "It never floods packets", "It needs no memory"], 0, "Changes are flooded at once instead of spreading hop by hop."),
    ("Consider the statements:\nI. OSPF is a link-state protocol.\nII. RIP is a path-vector protocol.\nWhich is/are correct?",
     I_II, 0, "Only I. RIP is distance vector; BGP is path vector."),
    ("Assertion (A): BGP can avoid routing loops between autonomous systems.\nReason (R): A BGP route carries the full list of ASes (AS-path) it has passed through.",
     AR, 0, "A router rejects a route whose AS-path already contains its own AS number; R explains A."),
]

TOPICS = {
    "IPv6, ARP, Delivery & Routing": [
        ("1 · IPv6 Addressing, Header and Transition; ARP and Neighbour Discovery", IPV6_ARP),
        ("2 · Delivery, Forwarding and Routing Protocols (RIP, OSPF, BGP) and ICMP", ROUTING),
    ],
}

NOTES = {
    "IPv6, ARP, Delivery & Routing": [
        {"title": "IPv6, ARP and routing – revision sheet", "md": """## IPv6
- **128-bit**, colon-hex, 8 groups; drop leading zeros; **'::' once** for zero groups
- Base header **40 bytes fixed**; up to **6 extension headers**; no checksum; fragmentation only at source
- Fields: version, traffic class, **flow label (20 bits)**, payload length, **next header**, **hop limit** (= TTL), source, destination
- Addresses: unicast, multicast, **anycast** – **no broadcast**; ::1 loopback; FE80::/10 link-local; FF00::/8 multicast; 2000::/3 global
- SLAAC autoconfiguration (modified EUI-64: insert FFFE, flip 7th bit); DHCPv6 still exists
- Transition: **dual stack, tunnelling (IPv6 in IPv4, protocol 41), header translation**
- ICMPv6 Neighbor Discovery replaces ARP; MLD replaces IGMP

## ARP family
| Protocol | Maps |
|---|---|
| ARP | IP → MAC (request broadcast, reply unicast) |
| RARP | MAC → IP (old; now DHCP) |
| Proxy ARP | router replies for hosts behind it |
| Gratuitous ARP | host announces itself / finds duplicate IP |
- Sequence: request → reply → cache → send data; Ethernet type 0x0806

## Delivery and forwarding
- Direct (same network) vs indirect (via routers)
- Next-hop, network-specific, host-specific, **default (0.0.0.0/0)**; **longest-prefix match**

## Routing protocols
| | RIP | OSPF | BGP |
|---|---|---|---|
| Type | distance vector | link state | path vector |
| Algorithm | Bellman–Ford | Dijkstra | path attributes |
| Scope | intra-AS | intra-AS (areas, area 0) | inter-AS |
| Transport | UDP 520 | IP proto 89 | TCP 179 |
| Metric | hop count, max 15 | cost | policy / AS-path |
- Count-to-infinity in DV → split horizon, poison reverse, hold-down (not enough for 3-node loops)
- Link-state steps: discover → measure → build LSP → flood → Dijkstra
- Distributed-system routing (Silberschatz): fixed, **virtual (fixed per session)**, dynamic

## ICMP
- Errors: 3 destination unreachable, 4 source quench, 5 redirect, 11 time exceeded, 12 parameter problem
- Queries: 8/0 echo request/reply (ping); traceroute uses TTL + time exceeded
- TTL −1 at each router; 0 → discard + ICMP 11
"""}],
}
