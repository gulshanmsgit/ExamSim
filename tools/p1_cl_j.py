"""Paper 1 · Computer Literacy · P1-CL-10 Unit 4 – E-mail (2 sub-topics × 20), with revision NOTES.
Coverage (planner): creating e-mail IDs, sending, attaching, composing, downloading, viewing, folders.
References: Gmail and Outlook help centres; Tanenbaum, Computer Networks (§ 7.2 Electronic mail); NCERT / DSERT ICT texts. REAL
previous-year questions come from the KEA 2025–26 Kannada-English-Computer papers; KEA has published no key for them, so answers were
worked out by ExamSim and say so."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KEA / KPSC / TET computer literacy). "
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

ID_COMPOSE = [
    ("Match the following:\na. Inbox  b. Starred  c. Labels  d. Archive\ni. A folder where you store mail that is no longer needed\n"
     "ii. A categorized and organized email folder\niii. Screen where incoming messages are received\niv. Option used to mark messages as important",
     ["a-iii, b-iv, c-ii, d-i", "a-ii, b-iii, c-iv, d-i", "a-iv, b-ii, c-i, d-iii", "a-ii, b-i, c-iv, d-iii"], 0,
     "Gmail: archived mail leaves the Inbox but stays in 'All Mail'; labels work like folders." + NOTE, "KEA 2026 KEC (NHK, 25 Jan 2026) · Q79"),
    ("Identify the 5 basic functions supported by email systems.\na. Composition  b. Decomposition  c. Transfer  d. Reporting  e. Filing  f. Displaying  g. Disposition",
     ["a, b, c, d, e and g", "a, c, d, f and g", "a, c, d, e and f", "a, b, c, e and g"], 1,
     "Tanenbaum's five functions: composition, transfer, reporting, displaying, disposition." + NOTE, "KEA 2026 KEC-2 (HK, 27 Apr 2026) · Q98"),
    ("Identify the features that are associated with \"Microsoft Outlook\" from the options given below.\na. Email management  b. Calendar and Scheduling  c. Contact and Task management\n"
     "d. Image or Video editing  e. Deep Data Analytics",
     ["a, b and c", "c, d and e", "d and e", "c and e"], 0, "Outlook is a personal information manager: mail, calendar, contacts, tasks." + NOTE, "KEA 2026 KEC-2 (HK, 27 Apr 2026) · Q93"),
    ("In the e-mail address ravi.kumar@gmail.com, 'gmail.com' is the:",
     ["Domain name of the mail server", "Username", "Password", "Protocol"], 0, PYQ + "Format: username@domain; the '@' separates them."),
    ("Which symbol must appear in every e-mail address?",
     ["@", "#", "&", "%"], 0, "No spaces are allowed in an e-mail address."),
    ("Who is credited with sending the first network e-mail (1971) and choosing the '@' symbol?",
     ["Ray Tomlinson", "Tim Berners-Lee", "Vint Cerf", "Bill Gates"], 0, PYQ + "On ARPANET."),
    ("When creating a new e-mail ID, which of the following is the strongest password?",
     ["K@rn#2026!sun", "123456", "password", "ravi1990"], 0, "Mix of upper/lower case, digits and symbols; at least 8–12 characters."),
    ("To send a copy of a mail to other people so that all recipients can see their addresses, you use:",
     ["Cc (carbon copy)", "Bcc (blind carbon copy)", "Subject", "Signature"], 0, PYQ + "Bcc recipients are hidden from others."),
    ("Bcc is best used when:",
     ["Sending one mail to many people without revealing their addresses to each other", "Attaching a file", "Marking a mail urgent", "Replying to the sender only"], 0,
     "It protects privacy and reduces 'reply all' storms."),
    ("The short line that tells the recipient what a mail is about is the:",
     ["Subject", "Signature", "Footer", "Header bar"], 0, PYQ + "A clear subject helps searching later."),
    ("A file sent along with an e-mail message is called an:",
     ["Attachment", "Signature", "Draft", "Label"], 0, "Usually shown with a paper-clip icon. Gmail limits attachments to 25 MB; bigger files go as Drive links."),
    ("An unfinished mail saved for later sending is stored in:",
     ["Drafts", "Sent", "Spam", "Trash"], 0, PYQ + "Gmail saves drafts automatically."),
    ("Text automatically added at the end of every mail you send, such as name and designation, is the:",
     ["Signature", "Subject", "Cc", "Label"], 0, "Set it in Settings."),
    ("'Reply all' sends the reply to:",
     ["The sender and all other recipients of the original mail (To and Cc)", "Only the sender", "Only Bcc recipients", "Everyone in your contacts"], 0, PYQ + "Bcc recipients are not included."),
    ("'Forward' is used to:",
     ["Send a received mail, with its attachments, to someone else", "Reply only to the sender", "Delete a mail", "Mark a mail as spam"], 0, "Subject line gets 'Fwd:'; a reply gets 'Re:'."),
    ("Which keyboard shortcut in Gmail (with shortcuts on) opens a new message to compose?",
     ["c", "r", "f", "e"], 0, "r – reply; a – reply all; f – forward; e – archive."),
    ("If you receive an email in the name of your bank from an unknown person asking you to click a link and verify your password, then the target of security threat is known as",
     ["Phishing", "Trojan Horse", "Malware", "Social Engineering"], 0,
     "Phishing is a social-engineering attack through fake mails; never share passwords or OTPs." + NOTE, "KEA 2025 KEC (HK, 21 Dec 2025) · Q84"),
    ("Unwanted bulk commercial e-mail is called:",
     ["Spam", "Draft", "Archive", "Thread"], 0, PYQ + "Mail providers move it to the Spam/Junk folder."),
    ("Consider the statements:\nI. Recipients in Cc can see each other's addresses.\nII. Recipients in Bcc can see each other's addresses.\nWhich is/are correct?",
     I_II, 0, "Only I."),
    ("Assertion (A): Large files are often shared as cloud links instead of attachments.\nReason (R): E-mail services limit the size of attachments.",
     AR, 0, "R explains A (Gmail: 25 MB)."),
]

PROTOCOLS_FOLDERS = [
    ("Identify the correct sequence of E-mail communication from sender to receiver:",
     ["User → SMTP → DNS → Receiver SMTP → IMAP/POP → Inbox", "User → DNS → SMTP → IMAP/POP → Receiver SMTP → Inbox",
      "User → IMAP/POP → SMTP → Receiver SMTP → DNS → Inbox", "User → DNS → Receiver SMTP → IMAP/POP → SMTP → Inbox"], 0,
     "The sender's SMTP server looks up the receiver's mail server (MX record) in DNS, delivers by SMTP; the receiver reads with IMAP/POP." + NOTE,
     "KEA 2025 KEC (HK, 21 Dec 2025) · Q72"),
    ("Which protocol is used to SEND e-mail between mail servers?",
     ["SMTP", "POP3", "IMAP", "HTTP"], 0, PYQ + "SMTP port 25 (587 for submission)."),
    ("Which protocol downloads mail to one device and usually deletes it from the server?",
     ["POP3", "IMAP", "SMTP", "FTP"], 0, "POP3 – port 110."),
    ("Which protocol keeps mail on the server and synchronises folders across several devices?",
     ["IMAP", "POP3", "SMTP", "SNMP"], 0, PYQ + "IMAP – port 143 (993 with SSL)."),
    ("MIME is used in e-mail to:",
     ["Send non-text content such as images, audio and attachments", "Encrypt passwords", "Find the mail server", "Block spam"], 0, "Multipurpose Internet Mail Extensions."),
    ("Reading mail in a web browser (e.g. Gmail website) without installing a program is called:",
     ["Webmail", "POP mail", "Telnet", "FTP"], 0, PYQ + "Desktop clients: Outlook, Thunderbird."),
    ("Mails you have sent are stored in the:",
     ["Sent folder", "Inbox", "Drafts", "Spam"], 0, "Deleted mails go to Trash/Bin (Gmail empties it after 30 days)."),
    ("In Gmail, 'Archive' a message means:",
     ["Remove it from the Inbox but keep it in All Mail", "Delete it permanently", "Send it to Spam", "Forward it"], 0, PYQ + "Searchable later."),
    ("In Gmail, labels are similar to:",
     ["Folders – but one mail can have several labels", "Passwords", "Attachments", "Signatures"], 0, "Filters can apply labels automatically."),
    ("A rule that automatically moves incoming mails from a particular sender into a folder is a:",
     ["Filter (rule)", "Signature", "Draft", "Bcc"], 0, PYQ + "Outlook calls them Rules."),
    ("To download an attachment received in mail, you:",
     ["Click the attachment's download icon", "Click Reply", "Click Forward", "Mark it as spam"], 0, "Scan unknown attachments for viruses first."),
    ("Which attachment type is most likely to carry a virus and should not be opened from unknown senders?",
     [".exe file", ".txt file", ".jpg photo from a known contact", "A plain-text message"], 0, PYQ + "Executable files run programs."),
    ("A series of related mails – an original message and its replies – shown together is called a:",
     ["Conversation thread", "Label", "Filter", "Draft"], 0, "Gmail groups them by subject."),
    ("An automatic reply sent while you are on leave is set up using:",
     ["Vacation responder / Out-of-office reply", "Bcc", "Spam filter", "Archive"], 0, PYQ + "Found in Settings."),
    ("The 'Contacts' (address book) feature helps to:",
     ["Store e-mail addresses and details of people you write to", "Store passwords", "Edit photos", "Create filters only"], 0, "Typing a name suggests the saved address."),
    ("Which of these is a good e-mail etiquette (netiquette)?",
     ["Write a clear subject and avoid typing everything in CAPITALS", "Use Reply-all for every mail", "Forward chain mails", "Send large files to everyone"], 0,
     PYQ + "Capitals look like shouting."),
    ("In an e-mail, the 'From' field shows:",
     ["The sender's address", "The receiver's address", "The subject", "The attachment name"], 0, "'To' – main recipients."),
    ("Which of the following is NOT a free web-based e-mail service?",
     ["Microsoft Excel", "Gmail", "Outlook.com", "Yahoo Mail"], 0, PYQ + "Excel is a spreadsheet."),
    ("Consider the statements:\nI. SMTP is used to send mail.\nII. IMAP deletes mail from the server as soon as it is read.\nWhich is/are correct?",
     I_II, 0, "Only I. IMAP keeps mail on the server."),
    ("Assertion (A): IMAP is preferred when the same mailbox is used on a phone and a laptop.\nReason (R): IMAP keeps messages on the server and synchronises them across devices.",
     AR, 0, "R explains A."),
]

TOPICS = {
    "Unit 4 – E-mail": [
        ("1 · E-mail IDs, Composing, Cc/Bcc, Attachments and Replies", ID_COMPOSE),
        ("2 · Mail Protocols, Folders, Labels, Filters and Netiquette", PROTOCOLS_FOLDERS),
    ],
}

NOTES = {
    "Unit 4 – E-mail": [
        {"title": "E-mail – revision sheet", "md": """## Basics
- Address = **username@domain** (ravi@gmail.com); first network e-mail – **Ray Tomlinson, 1971**, chose '@'
- Strong password: 8–12+ characters, upper/lower case, digits, symbols; turn on 2-step verification
- Five functions (Tanenbaum): composition, transfer, reporting, displaying, disposition

## Composing
| Field | Use |
|---|---|
| To | main recipients |
| Cc | copy – everyone sees addresses |
| Bcc | blind copy – hidden addresses |
| Subject | topic of the mail |
| Attachment | file (paper clip); Gmail limit 25 MB |
| Signature | auto text at the end |
- Reply (Re:) – sender only; Reply all – sender + To + Cc; Forward (Fwd:) – to someone else with attachments
- Gmail shortcuts: c compose, r reply, a reply all, f forward, e archive

## Folders
Inbox · Sent · Drafts · Spam/Junk · Trash/Bin (30 days) · Starred/Important · Archive (All Mail) · Labels (many per mail) · Filters/Rules · Vacation responder

## Protocols
| Protocol | Job | Port |
|---|---|---|
| **SMTP** | send / transfer | 25 (587) |
| **POP3** | download to one device | 110 |
| **IMAP** | keep on server, sync devices | 143 (993) |
| MIME | attachments, non-text | – |
- Path: user → SMTP → DNS (MX lookup) → receiver SMTP → IMAP/POP → inbox
- Webmail (browser) vs mail client (Outlook – mail, calendar, contacts, tasks; Thunderbird)

## Safety & netiquette
- Phishing mails ask for passwords/OTP – never click; don't open unknown .exe attachments; spam = unwanted bulk mail
- Clear subject, no ALL CAPS, avoid needless Reply-all and chain mails
"""}],
}
