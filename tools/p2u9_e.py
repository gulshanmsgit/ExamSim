"""Paper 2 · Unit 9 · P2-U9-11 Network Security (2 sub-topics × 30), with revision NOTES.
Coverage (planner): malware, cryptography, steganography, secret-key & public-key algorithms, digital signature, VPN, firewalls.
References: Forouzan, Data Communications and Networking (5th ed., chs. 31–32); William Stallings, Cryptography and Network Security;
Kurose & Ross, Computer Networking (ch. 8); IT Act 2000 (Controller of Certifying Authorities). Each set mixes REAL previous-year
questions (exact wording, printed option order, `source`) with new ones. Official answers: KEA final keys for Legislative Council 2024
(Computer Operator P2, Sr/Jr Programmer P2 – booklet A1) and GTTC 2024 Technician Gr-III CS (booklet C1), read from the page images
where the OCR lost options. GFGC/Raichur/PGCET answers were worked out by ExamSim. The transposition, Caesar, RSA and Diffie–Hellman
numbers were checked by hand calculation."""
from packlib import AR, I_II
from p2u7_a import PYQ, KLC, GTTC, NOTE

THREATS_DEFENCES = [
    ("Match the following in relation to security\n(a) Firewall  (b) Firmware  (c) Malware  (d) Phishing\n"
     "i) Exploits device and data  ii) Steals user's sensitive data  iii) Is a security tool  iv) Controls basic function",
     ["a – iii, b – ii, c – iv, d – i", "a – iii, b – iv, c – i, d – ii", "a – iv, b – iii, c – ii, d – i", "a – ii, b – i, c – iii, d – iv"], 1,
     "Firmware is low-level software in hardware (e.g. BIOS); phishing tricks users into revealing data." + KLC, "Legislative Council 2024 Computer Operator P2 · Q6"),
    ("Which of the followings are true about firewalls?",
     ["Firewalls can protect against the attacks that bypass the firewall", "Firewalls may not protect fully against internal threats",
      "Wireless LAN may not be accessed from outside the organisation", "Any portable storage device can be infected outside and cannot be used internally"], 1,
     "A firewall only controls traffic that passes through it; insiders and bypassing links (Wi-Fi, USB drives) need other defences." + GTTC,
     "GTTC 2024 Technician Gr-III CS (C1) · Q48"),
    ("______ is a useful program or command procedure containing hidden code which performs harmful function when it is invoked.",
     ["Malicious Software", "Mobile Code", "Logic Bomb", "Trojan Horse"], 3,
     "Stallings' definition of a Trojan horse; a logic bomb fires when a condition (date, event) is met." + GTTC, "GTTC 2024 Technician Gr-III CS (C1) · Q50"),
    ("What is cross-site scripting in JavaScript?",
     ["A method of encrypting user data", "A vulnerability where attackers inject malicious scripts into web pages", "A way to store cookies securely",
      "A protocol to prevent SQL injection"], 1, "XSS runs the attacker's script in other users' browsers; defend by escaping output and validating input." + KLC,
     "Legislative Council 2024 Sr/Jr Programmer P2 · Q41"),
    ("Which one of the following is not a hacking method?",
     ["Sniffing", "Social engineering", "Spoofing", "Malware"], 3,
     "Sniffing, social engineering and spoofing are attack techniques; malware is the malicious software itself." + NOTE, "GFGC 2021 CS · Q107"),
    ("Which software prevents the external access to a system?",
     ["Firewall", "Gateway", "Router", "Virus checker"], 0, "A firewall filters incoming/outgoing traffic by rules." + NOTE, "PGCET 2024 M.Tech CS · Q12"),
    ("The three goals of information security (the CIA triad) are:",
     ["Confidentiality, Integrity, Availability", "Control, Inspection, Audit", "Cryptography, Identification, Authorisation", "Coding, Indexing, Archiving"], 0,
     PYQ + "Attacks: on confidentiality – snooping, traffic analysis; integrity – modification, masquerading, replay; availability – denial of service."),
    ("Eavesdropping and traffic analysis are examples of:",
     ["Passive attacks", "Active attacks", "Denial of service", "Replay attacks"], 0, "Passive attacks only read data and are hard to detect; active attacks change data or disrupt service."),
    ("Malware that copies itself across a network WITHOUT needing a host program or user action is a:",
     ["Worm", "Virus", "Trojan horse", "Logic bomb"], 0, PYQ + "A virus attaches to a host file and spreads when it runs."),
    ("Malware that encrypts the victim's files and demands payment for the key is:",
     ["Ransomware", "Adware", "Spyware", "Rootkit"], 0, "WannaCry (2017) is a well-known example."),
    ("A network of infected computers controlled remotely by an attacker, often used for DDoS attacks, is a:",
     ["Botnet", "VPN", "Honeypot", "DMZ"], 0, PYQ + "Each infected machine is a 'bot' or 'zombie'."),
    ("Flooding a server with traffic from many machines so that legitimate users cannot reach it is a:",
     ["Distributed denial-of-service (DDoS) attack", "Phishing attack", "Man-in-the-middle attack", "SQL injection"], 0, "It attacks availability."),
    ("Sending a fake e-mail that looks like it is from a bank to steal passwords is:",
     ["Phishing", "Spoofing of MAC address", "Sniffing", "Brute force"], 0, PYQ + "Spear phishing targets a specific person; vishing uses phone calls."),
    ("An attacker secretly relays and possibly alters messages between two parties who believe they are talking directly. This is:",
     ["Man-in-the-middle attack", "Replay attack", "Denial of service", "Dictionary attack"], 0, "Authentication and certificates prevent it."),
    ("A packet-filter firewall makes decisions mainly using:",
     ["Network- and transport-layer header fields (IP addresses, ports, protocol)", "The contents of e-mails", "User passwords", "The MAC address only"], 0,
     PYQ + "A proxy (application-level gateway) firewall examines application data."),
    ("A firewall that remembers the state of connections and allows only packets belonging to established sessions is a:",
     ["Stateful inspection firewall", "Stateless packet filter", "Bridge", "Repeater"], 0, "Stateless filters judge each packet alone."),
    ("A DMZ (demilitarised zone) in a network is:",
     ["A separate segment for public servers, between the Internet and the internal network", "The internal LAN", "A wireless hotspot", "A backup power area"], 0,
     PYQ + "Web and mail servers sit in the DMZ."),
    ("A VPN (Virtual Private Network) provides:",
     ["A secure encrypted tunnel for private communication over a public network", "Faster Internet always", "Free Internet access", "A physical private cable"], 0,
     "VPNs commonly use IPsec or TLS."),
    ("IPsec provides security at the:",
     ["Network layer", "Application layer", "Physical layer", "Data link layer only"], 0, PYQ + "SSL/TLS – between transport and application; PGP/S-MIME – e-mail."),
    ("In IPsec, the protocol that provides encryption (confidentiality) in addition to authentication is:",
     ["ESP (Encapsulating Security Payload)", "AH (Authentication Header)", "IKE only", "ARP"], 0, "AH gives authentication and integrity but no encryption."),
    ("IPsec 'tunnel mode' differs from 'transport mode' because it:",
     ["Protects the entire original IP packet inside a new IP packet", "Protects only the payload", "Works only on LANs", "Uses no encryption"], 0, PYQ + "Tunnel mode is used between gateways (site-to-site VPNs)."),
    ("HTTPS secures web traffic by running HTTP over:",
     ["TLS/SSL on port 443", "IPsec on port 80", "SSH on port 22", "UDP on port 53"], 0, "The browser shows a padlock."),
    ("Which protocol is used for secure remote login, replacing Telnet?",
     ["SSH (port 22)", "FTP (port 21)", "SMTP (port 25)", "HTTP (port 80)"], 0, PYQ + "Telnet sends passwords in plain text."),
    ("Kerberos is an authentication service that uses:",
     ["Tickets issued by a Key Distribution Centre (Authentication Server + Ticket-Granting Server)", "Public-key certificates only", "Passwords sent in clear text", "Biometrics only"], 0,
     "Developed at MIT; based on symmetric keys."),
    ("A system that monitors network traffic and raises alerts on suspicious activity is an:",
     ["Intrusion Detection System (IDS)", "Router", "Proxy cache", "DNS server"], 0, PYQ + "An IPS (intrusion prevention system) can also block it."),
    ("A deliberately vulnerable system set up to lure and study attackers is a:",
     ["Honeypot", "Firewall", "Bastion host", "Proxy"], 0, "Used to learn attackers' methods."),
    ("Two-factor authentication combines, for example:",
     ["A password (something you know) and an OTP on your phone (something you have)", "Two passwords", "A username and a password", "Two security questions"], 0,
     PYQ + "Factors: know, have, are (biometrics)."),
    ("Consider the statements:\nI. A virus needs a host file to spread.\nII. A worm cannot spread without user action.\nWhich is/are correct?",
     I_II, 0, "Only I. Worms spread on their own over networks."),
    ("Consider the statements:\nI. A firewall protects fully against insider attacks.\nII. A firewall can block traffic to specific ports.\nWhich is/are correct?",
     I_II, 1, "Only II (see GTTC 2024 Q48)."),
    ("Assertion (A): Public servers are often placed in a DMZ.\nReason (R): If a public server is compromised, the internal network remains separated by the inner firewall.",
     AR, 0, "R explains A."),
]

CRYPTOGRAPHY = [
    ("A signs the message and sends to B, to prove that he is the sender of the message. Which of the following keys does A need to use?",
     ["A's public key", "B's public key", "A's private key", "B's private key"], 2,
     "Only A has A's private key; anyone can verify with A's public key." + GTTC, "GTTC 2024 Technician Gr-III CS (C1) · Q40"),
    ("Match the following message digest size with the given Hash functions.\na) SHA-1  b) SHA-224  c) SHA-256  d) SHA-512\ni. 512 bits  ii. 160 bits  iii. 224 bits  iv. 256 bits",
     ["a – ii, b – iii, c – iv, d – i", "a – i, b – ii, c – iii, d – iv", "a – ii, b – i, c – iv, d – iii", "a – iv, b – iii, c – i, d – ii"], 0,
     "SHA-2 names give the digest size; SHA-1 gives 160 bits, MD5 128 bits." + GTTC, "GTTC 2024 Technician Gr-III CS (C1) · Q49"),
    ("What is the purpose of XML signature?",
     ["To ensure the authenticity of the XML document by providing integrity and authenticity", "To compress the XML data for faster transmission",
      "To encrypt the XML document for confidentiality", "To format the XML data for human-readable output"], 0,
     "Signatures give integrity and authentication; XML Encryption is a separate standard for confidentiality." + KLC, "Legislative Council 2024 Sr/Jr Programmer P2 · Q49"),
    ("Encrypt the plain text message \"INTRANET\" using Transposition cipher technique with the following key:\n3 5 2 1 4 (Cipher text)\n1 2 3 4 5 (Plain text)\nUse 'X' as bogus character.",
     ["TANIRTXENX", "TNAIRTXENX", "TANRITXENX", "TANIRTEXNX"], 0,
     "Blocks of 5: INTRA, NETXX. Output order = plaintext positions 3, 5, 2, 1, 4: INTRA → T A N I R; NETXX → T X E N X." + NOTE, "GFGC 2021 CS · Q104"),
    ("Which of the following are used to generate a message digest by the network security protocols?\nP. RSA  Q. SHA-1  R. DES  S. MD5",
     ["P and R only", "Q and R only", "Q and S only", "R and S only"], 2, "SHA-1 and MD5 are hash functions; RSA and DES are encryption algorithms." + NOTE, "GFGC 2021 CS · Q112"),
    ("______ is a popular cryptographic algorithm for digital signatures and public key infrastructure.",
     ["RSA", "MD5", "AES", "SHA-1"], 0, "RSA is public-key; AES is symmetric; MD5/SHA-1 are hashes." + NOTE, "Raichur University 2024 CS&A · Q48"),
    ("Why is the ECB (Electronic Codebook) mode of a block cipher considered weak?",
     ["Identical plaintext blocks give identical ciphertext blocks, revealing patterns", "It uses no key", "It cannot decrypt", "It is slower than all other modes"], 0,
     PYQ + "CBC, CFB, OFB and CTR modes mix in an IV or previous block to hide patterns."),
    ("In symmetric-key (secret-key) cryptography:",
     ["The same key is used to encrypt and decrypt", "Two different keys are used", "No key is used", "Only hashing is done"], 0, PYQ + "Examples: DES, 3DES, AES, Blowfish, RC4."),
    ("How many secret keys are needed for every pair of 10 people to communicate privately using symmetric-key cryptography?",
     ["45", "10", "20", "100"], 0, PYQ + "n(n − 1)/2 = 10 × 9 / 2 = 45. With public-key cryptography each person needs one key pair (20 keys)."),
    ("DES uses a block size and an effective key length of:",
     ["64-bit block, 56-bit key, 16 rounds", "128-bit block, 128-bit key, 10 rounds", "64-bit block, 128-bit key", "32-bit block, 64-bit key"], 0,
     "Triple DES applies DES three times (encrypt–decrypt–encrypt)."),
    ("AES uses a block size of:",
     ["128 bits, with 128-, 192- or 256-bit keys (10, 12 or 14 rounds)", "64 bits with a 56-bit key", "256 bits with a 512-bit key", "32 bits"], 0, PYQ + "Based on the Rijndael cipher."),
    ("Using the Caesar cipher (shift of 3), 'HELLO' is encrypted as:",
     ["KHOOR", "IFMMP", "EBIIL", "LIPPS"], 0, PYQ + "H→K, E→H, L→O, L→O, O→R."),
    ("A cipher that rearranges the order of characters without changing them is a:",
     ["Transposition cipher", "Substitution cipher", "Stream cipher", "Hash function"], 0, "Substitution ciphers replace characters (Caesar, Playfair, Vigenère)."),
    ("The Vigenère cipher is an example of a:",
     ["Polyalphabetic substitution cipher", "Monoalphabetic cipher", "Transposition cipher", "Public-key cipher"], 0, "The one-time pad is theoretically unbreakable if the key is random and used once."),
    ("In RSA with p = 3 and q = 11, n and φ(n) are:",
     ["n = 33, φ(n) = 20", "n = 14, φ(n) = 33", "n = 33, φ(n) = 32", "n = 30, φ(n) = 20"], 0, PYQ + "n = p·q = 33; φ(n) = (p − 1)(q − 1) = 2 × 10 = 20."),
    ("In RSA with n = 33, φ(n) = 20 and public exponent e = 3, the private exponent d is:",
     ["7", "3", "13", "11"], 0, "d is the inverse of e mod 20: 3 × 7 = 21 ≡ 1 (mod 20)."),
    ("Using RSA with public key (e = 3, n = 33), the plaintext M = 4 is encrypted to:",
     ["31", "12", "64", "4"], 0, PYQ + "C = M^e mod n = 4³ mod 33 = 64 mod 33 = 31. Check: 31⁷ mod 33 = 4."),
    ("Diffie–Hellman with p = 23, g = 5, Alice's secret a = 4 and Bob's secret b = 3 gives the shared key:",
     ["18", "4", "10", "23"], 0, "A = 5⁴ mod 23 = 4; B = 5³ mod 23 = 10; key = 10⁴ mod 23 = 4³ mod 23 = 18."),
    ("The Diffie–Hellman algorithm is used for:",
     ["Securely agreeing on a shared secret key over an insecure channel", "Digital signatures only", "Hashing passwords", "Compressing data"], 0,
     PYQ + "It is vulnerable to man-in-the-middle attacks without authentication."),
    ("A digital signature provides:",
     ["Authentication, integrity and non-repudiation", "Only confidentiality", "Only compression", "Only availability"], 0, "To add confidentiality, the message must also be encrypted."),
    ("To verify a digital signature, the receiver uses:",
     ["The sender's public key", "The sender's private key", "The receiver's private key", "A shared secret key"], 0, PYQ + "Sign with private key → verify with public key."),
    ("To send a message that only B can read, A encrypts it with:",
     ["B's public key", "A's private key", "A's public key", "B's private key"], 0, "Only B's private key can decrypt it."),
    ("A hash function used in security must be:",
     ["One-way and collision-resistant, producing a fixed-length digest", "Reversible", "Variable-length output", "Keyed with a public key"], 0, PYQ + "MD5 – 128 bits; SHA-1 – 160 bits (both now considered weak)."),
    ("A digital certificate binds:",
     ["A public key to the identity of its owner, signed by a Certifying Authority (CA)", "A password to a username", "A private key to an IP address", "Two private keys"], 0,
     "Format X.509; in India CAs are licensed by the Controller of Certifying Authorities under the IT Act, 2000."),
    ("Steganography is:",
     ["Hiding the existence of a message, e.g. inside an image", "Encrypting with two keys", "Compressing data", "Checking passwords"], 0, PYQ + "LSB (least-significant-bit) image hiding is common."),
    ("Which of the following is an asymmetric (public-key) algorithm?",
     ["Elliptic Curve Cryptography (ECC)", "AES", "DES", "Blowfish"], 0, "Public-key: RSA, ECC, ElGamal, DSA."),
    ("A Message Authentication Code (MAC) such as HMAC provides:",
     ["Integrity and authentication using a shared secret key", "Non-repudiation", "Encryption of the message", "Compression"], 0, PYQ + "MAC cannot give non-repudiation because both sides share the key."),
    ("Consider the statements:\nI. In public-key cryptography the private key must be kept secret.\nII. MD5 produces a 160-bit digest.\nWhich is/are correct?",
     I_II, 0, "Only I. MD5 → 128 bits; SHA-1 → 160 bits."),
    ("Consider the statements:\nI. A digital signature gives non-repudiation.\nII. Symmetric-key encryption is generally faster than public-key encryption.\nWhich is/are correct?",
     I_II, 2, "Both. Hence hybrid systems: public key to exchange a session key, symmetric key for the data (as in TLS)."),
    ("Assertion (A): TLS uses public-key cryptography only to set up a session key.\nReason (R): Symmetric encryption is much faster for bulk data.",
     AR, 0, "R explains A."),
]

TOPICS = {
    "Network Security": [
        ("1 · Threats, Malware, Firewalls, VPN and Security Protocols", THREATS_DEFENCES),
        ("2 · Cryptography – Ciphers, Secret-Key and Public-Key Algorithms, Hashes and Digital Signatures", CRYPTOGRAPHY),
    ],
}

NOTES = {
    "Network Security": [
        {"title": "Network security – revision sheet", "md": """## Goals and attacks
- **CIA**: confidentiality, integrity, availability (+ authentication, non-repudiation)
- Passive (snooping, traffic analysis) vs active (modification, masquerade, replay, DoS)
- Malware: **virus** (needs host), **worm** (self-spreading), **Trojan** (hidden harmful code), **logic bomb** (condition), ransomware, spyware, adware, rootkit, botnet
- Phishing, spoofing, sniffing, MITM, DDoS, XSS, SQL injection, social engineering

## Defences
- **Firewall**: packet filter (IP/port), stateful, proxy/application gateway; cannot stop insiders or bypass links
- DMZ for public servers; IDS/IPS; honeypot; 2FA (know + have + are)
- **VPN** – encrypted tunnel; **IPsec** (network layer): AH (auth) / **ESP** (auth + encryption); transport vs **tunnel** mode
- **TLS/SSL** – HTTPS 443; **SSH 22** replaces Telnet; PGP/S-MIME – e-mail
- **Kerberos** – tickets from KDC (AS + TGS)

## Cryptography
| | Symmetric | Asymmetric |
|---|---|---|
| Keys | one shared | public + private |
| Examples | DES (64-bit block, 56-bit key, 16 rounds), 3DES, AES (128-bit block, 128/192/256 key) | RSA, ECC, ElGamal, DSA |
| Keys for n users | n(n−1)/2 | 2n |
- Classical: substitution (Caesar shift 3, Playfair, Vigenère = polyalphabetic), transposition; one-time pad
- **RSA**: n = pq, φ = (p−1)(q−1), e·d ≡ 1 mod φ; C = M^e mod n (p=3, q=11, e=3 → d=7; M=4 → C=31)
- **Diffie–Hellman**: key agreement (p=23, g=5, a=4, b=3 → key 18); needs authentication against MITM
- **Hash**: MD5 128, SHA-1 160, SHA-224/256/512 as named; one-way, collision-resistant
- **MAC/HMAC** – shared key, integrity + auth
- **Digital signature**: sign with **sender's private key**, verify with sender's public key → auth + integrity + non-repudiation
- Confidentiality: encrypt with **receiver's public key**
- Certificates: X.509 by CA; India – Controller of Certifying Authorities (IT Act 2000)
- **Steganography** – hiding a message's existence (LSB in images)
"""}],
}
