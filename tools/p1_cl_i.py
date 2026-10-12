"""Paper 1 · Computer Literacy · P1-CL-09 Unit 4 – Internet Basics (2 sub-topics × 20), with revision NOTES.
Coverage (planner): history of the Internet, URLs, ISPs, web page, web links, LAN, WAN, WWW, search engines, browsers, web servers.
References: NCERT / DSERT ICT texts, Forouzan (Data Communications and Networking, ch. 1 and 26), W3C and IETF basics. REAL
previous-year questions come from the KEA 2025–26 Kannada-English-Computer papers and GTTC 2024 KEC; KEA's KEC papers have no published
key and the parsed GTTC KEC key does not match the scanned booklet, so all answers were worked out by ExamSim and say so. Skipped as
unclear: KEA 2025 KEC (HK) Q71 (no option fits), KEA 2026 KEC-1 (NHK) Q74 and KEC (NHK, 11 Jan) Q98 (debatable statements)."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KEA / KPSC / TET computer literacy). "
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

HISTORY_WWW = [
    ("The internet is evolved from the basic ideas of",
     ["ARPANET", ".NET", "USENET News", "Network"], 0,
     "ARPANET (1969) of the US Department of Defense's ARPA was the first packet-switched network to use TCP/IP (from 1 January 1983)." + NOTE,
     "GTTC 2024 Officer/Asst Gr-III KEC · Q75"),
    ("The glue that holds the Internet is",
     ["UDP", "RPC", "TCP/IP", "FTP"], 2, "TCP/IP is the protocol suite every Internet host uses; UDP and FTP are parts of it." + NOTE, "KEA 2026 KEC-2 (HK, 27 Apr 2026) · Q95"),
    ("The internet that provides the basic services to its users are",
     ["Telnet, FTP, Email", "Scanning", "Network analysis", "Probing devices"], 0,
     "Classic Internet services: e-mail, file transfer (FTP), remote login (Telnet), the WWW." + NOTE, "GTTC 2024 Officer/Asst Gr-III KEC · Q86"),
    ("The total number of IP addresses of IPv6 version is",
     ["2^32", "2^48", "2^128", "2^256"], 2, "IPv6 addresses are 128 bits; IPv4 addresses are 32 bits (2^32)." + NOTE, "GTTC 2024 Officer/Asst Gr-III KEC · Q82"),
    ("Who invented the World Wide Web (1989–91) at CERN?",
     ["Tim Berners-Lee", "Vint Cerf", "Bill Gates", "Marc Andreessen"], 0,
     PYQ + "He also wrote the first browser and web server and defined HTML, HTTP and URLs. Vint Cerf and Bob Kahn designed TCP/IP – 'fathers of the Internet'."),
    ("The Internet and the World Wide Web are:",
     ["Different – the Internet is the network; the WWW is a service of linked pages running on it", "Exactly the same thing",
      "The WWW is older than the Internet", "The Internet runs on the WWW"], 0, PYQ + "E-mail and FTP also use the Internet but are not part of the WWW."),
    ("Public Internet access in India began on 15 August 1995 through:",
     ["VSNL", "BSNL", "ERNET", "Reliance Jio"], 0, "Videsh Sanchar Nigam Limited; ERNET (1986) linked educational institutions earlier."),
    ("A company that provides customers with access to the Internet is called a(n):",
     ["ISP – Internet Service Provider", "DNS", "URL", "Web browser"], 0, PYQ + "Examples: BSNL, Airtel, Jio, ACT Fibernet."),
    ("In the URL https://www.karnataka.gov.in/index.html, 'https' is the:",
     ["Protocol", "Domain name", "File name", "Path"], 0,
     PYQ + "URL = protocol :// host (domain) / path / file. 'gov.in' – Indian government domain; '.in' is India's country-code TLD."),
    ("URL stands for:",
     ["Uniform Resource Locator", "Universal Record Link", "Unique Resource Line", "Uniform Request Locator"], 0, "It is the address of a resource on the web."),
    ("What is the well-known port number associated with the HTTP (Hypertext Transfer Protocol)?",
     ["21", "80", "443", "25"], 1, "HTTP 80; HTTPS 443; FTP 21; SMTP 25." + NOTE, "KEA 2025 KEC (HK, 21 Dec 2025) · Q94"),
    ("Which system converts a domain name such as www.google.com into an IP address?",
     ["DNS (Domain Name System)", "DHCP", "HTML", "FTP"], 0, PYQ + "DHCP gives IP addresses to devices automatically."),
    ("Which top-level domain is generally used by educational institutions?",
     [".edu", ".org", ".net", ".mil"], 0, ".com – commercial; .org – organisations; .gov – government; .mil – military; .ac.in – Indian academic."),
    ("The language used to create web pages is:",
     ["HTML", "C", "SQL", "COBOL"], 0, PYQ + "HyperText Markup Language; pages are fetched with HTTP."),
    ("Match the following:\na. Web Client  b. Cloud  c. Website  d. Webpage\ni. Collection of web pages  ii. An HTML document  iii. The device used to access Internet  iv. Internet-based storage and devices",
     ["a-i, b-iv, c-ii, d-iii", "a-iii, b-i, c-iv, d-ii", "a-iii, b-iv, c-i, d-ii", "a-i, b-ii, c-ii, d-iv"], 2,
     "A website is a set of related web pages; each page is an HTML document." + NOTE, "KEA 2026 KEC (NHK, 25 Jan 2026) · Q73"),
    ("A hyperlink on a web page:",
     ["Takes you to another page, file or place when clicked", "Prints the page", "Deletes the page", "Saves the password"], 0,
     "Links usually appear underlined/blue; the mouse pointer turns into a hand."),
    ("The first page of a website is called its:",
     ["Home page", "Main frame", "Index card", "Web server"], 0, PYQ + "Usually index.html."),
    ("Which communication device is used in the conversion of digital data to analog form and vice versa?",
     ["Modulator", "Modem", "Demodulator", "Network interface card"], 1, "Modem = MOdulator + DEModulator." + NOTE, "KEA 2026 KEC (NHK, 25 Jan 2026) · Q93"),
    ("Consider the statements:\nI. HTTPS encrypts data between the browser and the website.\nII. A padlock symbol in the address bar shows an HTTPS connection.\nWhich is/are correct?",
     I_II, 2, "Both are true; HTTPS uses TLS/SSL certificates."),
    ("Assertion (A): Every device on the Internet needs an IP address.\nReason (R): Data packets are delivered to devices using their IP addresses.",
     AR, 0, "R explains A."),
]

WEB_NETWORKS = [
    ("Match the following:\n(a) Cookies  (b) Bookmark  (c) History  (d) Session\n(i) A record stored by web browser of all webpages a user has visited\n"
     "(ii) Temporary storage of user data on the server\n(iii) User created shortcut to a specific webpage\n(iv) A small file stored by website on user's device",
     ["a-iii, b-ii, c-iv, d-i", "a-iv, b-iii, c-i, d-ii", "a-iii, b-i, c-iv, d-ii", "a-iv, b-ii, c-i, d-iii"], 1,
     "Cookie – small file on your device; bookmark/favourite – saved link; history – list of visited pages; session – server-side data for one visit." + NOTE,
     "KEA 2026 KEC-1 (HK, 22 Feb 2026) · Q90"),
    ("Wi-Fi is a standard for wireless LANs called",
     ["IEEE 802.9", "IEEE 802.10", "IEEE 802.11", "IEEE 802.12"], 2, "802.3 – Ethernet; 802.11 – Wi-Fi; 802.15.1 – Bluetooth." + NOTE, "KEA 2026 KEC-1 (HK, 22 Feb 2026) · Q77"),
    ("Match List I with List II:\n(Scenario)\na. Three different buildings in the same city want to connect to a central server\nb. Set up a WiFi network for a small coffee shop\n"
     "c. An MNC that connects Bengaluru, New York and London offices\n(Network Technology) i. WAN  ii. MAN  iii. LAN",
     ["a-ii, b-iii, c-i", "a-iii, b-i, c-ii", "a-iii, b-ii, c-i", "a-ii, b-i, c-iii"], 0,
     "City-wide – MAN; one shop/building – LAN; countries – WAN." + NOTE, "KEA 2026 KEC-1 (NHK, 26 Apr 2026) · Q76"),
    ("Match List I with List II:\n(Network Device) a. Hubs  b. Fibre Optic Cables  c. Modems\n(Network) i. WAN  ii. LAN  iii. MAN",
     ["a-ii, b-i, c-iii", "a-iii, b-ii, c-i", "a-ii, b-iii, c-i", "a-i, b-ii, c-iii"], 2,
     "Hubs join computers in a LAN; fibre backbones serve city networks; modems reach WAN/ISP links." + NOTE, "KEA 2026 KEC-2 (HK, 27 Apr 2026) · Q77"),
    ("Which network covers the smallest area – for example, devices around one person (phone, earbuds, smartwatch)?",
     ["PAN", "LAN", "MAN", "WAN"], 0, PYQ + "PAN < LAN < MAN < WAN. The Internet is the largest WAN."),
    ("A software application used to view web pages is a:",
     ["Web browser", "Web server", "Search engine", "Compiler"], 0, PYQ + "Chrome, Firefox, Edge, Safari, Opera. Mosaic (1993) was the first popular graphical browser."),
    ("Which of the following is a search engine, not a browser?",
     ["Google Search", "Mozilla Firefox", "Microsoft Edge", "Safari"], 0, PYQ + "Search engines: Google, Bing, DuckDuckGo, Yahoo; they index pages using crawlers (spiders)."),
    ("A computer that stores websites and sends pages to browsers on request is a:",
     ["Web server", "Web client", "Router only", "Modem"], 0, "Apache, Nginx and IIS are web-server programs; the browser is the client."),
    ("The program used by search engines to visit and index web pages automatically is called a:",
     ["Crawler (spider/bot)", "Cookie", "Plug-in", "Firewall"], 0, PYQ + "Results are ranked by algorithms (e.g. Google's PageRank)."),
    ("Which browser mode does not save browsing history or cookies after the window is closed?",
     ["Incognito / private mode", "Full-screen mode", "Reader mode", "Safe mode"], 0, "It does not hide your IP address from websites or your ISP."),
    ("To keep a website's address for quick access later, you:",
     ["Bookmark it (add to favourites)", "Delete its cookies", "Clear history", "Refresh it"], 0, "Ctrl + D adds a bookmark in most browsers."),
    ("Which keyboard shortcut reloads (refreshes) the current web page in most browsers?",
     ["F5", "F1", "F12", "Ctrl + P"], 0, PYQ + "Ctrl + T – new tab; Ctrl + W – close tab; Ctrl + H – history; Ctrl + F – find."),
    ("Downloading means:",
     ["Copying a file from the Internet to your computer", "Sending a file from your computer to a server", "Deleting a web page", "Printing a web page"], 0,
     "Uploading is the reverse – your computer to a server."),
    ("Which of the following is NOT a web browser?",
     ["Google Drive", "Opera", "Brave", "Mozilla Firefox"], 0, "Google Drive is cloud storage."),
    ("Internet speed (bandwidth) is commonly measured in:",
     ["Mbps (megabits per second)", "MB (megabytes)", "GHz", "dpi"], 0, PYQ + "1 byte = 8 bits; a 100 Mbps line moves about 12.5 MB per second."),
    ("Which kind of website shows the same fixed content to every visitor, without a database?",
     ["Static website", "Dynamic website", "Web application", "Search engine"], 0, "Dynamic sites build pages on the server (PHP, databases, CMS such as WordPress)."),
    ("An intranet is:",
     ["A private network of an organisation that uses Internet technology", "Another name for the WWW", "A public Wi-Fi hotspot", "A search engine"], 0,
     PYQ + "An extranet gives limited access to outside partners."),
    ("Which device connects different networks and forwards data packets between them using IP addresses?",
     ["Router", "Hub", "Repeater", "Keyboard"], 0, "A hub repeats to all ports; a switch sends to one port using MAC addresses."),
    ("Consider the statements:\nI. A web browser and a search engine are the same thing.\nII. Google Chrome is a web browser.\nWhich is/are correct?",
     I_II, 1, "Only II. A browser opens pages; a search engine is a website that finds pages."),
    ("Assertion (A): Optical-fibre cables are used for high-speed Internet backbones.\nReason (R): Optical fibre carries data as light with very large bandwidth and low loss.",
     AR, 0, "R explains A."),
]

TOPICS = {
    "Unit 4 – Internet Basics": [
        ("1 · History of the Internet, ISPs, URLs and the WWW", HISTORY_WWW),
        ("2 · Browsers, Search Engines, Web Servers, LAN and WAN", WEB_NETWORKS),
    ],
}

NOTES = {
    "Unit 4 – Internet Basics": [
        {"title": "Internet basics – revision sheet", "md": """## History
- **ARPANET 1969** (US DoD) → TCP/IP adopted 1 Jan 1983; Vint Cerf & Bob Kahn – 'fathers of the Internet'
- **WWW** – Tim Berners-Lee, CERN, 1989–91 (HTML, HTTP, URL, first browser and server)
- First graphical browser – Mosaic (1993)
- India: ERNET 1986; public Internet via **VSNL, 15 Aug 1995**

## Addresses
- **URL** = protocol://domain/path/file – e.g. https://www.karnataka.gov.in/index.html
- **IP address**: IPv4 32-bit (2^32), IPv6 128-bit (2^128); **DNS** turns names into IP addresses
- Domains: .com, .org, .net, .edu, .gov, .mil; country codes .in, .uk; .gov.in, .ac.in, .nic.in
- Ports: HTTP **80**, HTTPS **443**, FTP 21, SMTP 25, DNS 53

## Web terms
| Term | Meaning |
|---|---|
| Web page | one HTML document |
| Website | collection of related pages; first page = home page |
| Hyperlink | clickable link to another page/file |
| Browser | Chrome, Firefox, Edge, Safari, Opera |
| Search engine | Google, Bing, DuckDuckGo – uses crawlers |
| Web server | stores and serves pages (Apache, Nginx, IIS) |
| Cookie | small file a website stores on your device |
| Bookmark | saved link (Ctrl + D) |
| History | list of visited pages (Ctrl + H) |
| Incognito | no local history/cookies kept (IP still visible) |
| Static / dynamic site | fixed pages / pages built from a database |
- Shortcuts: F5 refresh, Ctrl + T new tab, Ctrl + W close tab, Ctrl + F find

## Networks
| Type | Area | Example |
|---|---|---|
| PAN | a few metres | Bluetooth earbuds |
| LAN | room / building | school lab, Wi-Fi in a shop |
| MAN | city | cable TV / city network |
| WAN | country / world | Internet, MNC offices |
- Devices: hub (LAN, all ports), switch (MAC), router (IP, between networks), modem (digital ↔ analog)
- Wi-Fi = **IEEE 802.11**; Ethernet 802.3; Bluetooth 802.15
- **ISP** – BSNL, Jio, Airtel; speed in **Mbps**
- Intranet = private; extranet = partners; Internet = public

## ⚠ Traps
- Internet ≠ WWW; browser ≠ search engine
- 'Glue' of the Internet = **TCP/IP**
"""}],
}
