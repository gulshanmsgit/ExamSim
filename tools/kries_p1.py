"""KRIES Paper 1 as 15 subjects (owner, 26 Oct 2026): every item (A)–(O) of the KRIES Paper 1 syllabus is a SUBJECT with its own topics,
not a single topic. Used by build_subject.py (EXTRA_SUBJECTS, PACKS p1-kries-a … p1-kries-o), make_kries_plan.py (Paper 1 sheet) and the
per-subject modules p1_kx_<letter>.py.

Each topic first PULLS the matching sets that already exist in the bank (GPSTR GK and current-affairs topics, the earlier KRIES Karnataka
topics, monthly current affairs – read from the built packs, so they repeat by design; check_packs lets p1-kries-* packs repeat questions).
New Kannada sets (KEA style) are added by p1_kx_<letter>_new.py modules. Each subject also gets a topic of REAL KEA previous-year questions:
the 477 general-knowledge questions of the KEA papers in packs/pyq-p1.json (Legislative Council 2024 P1 ×2, GTTC 2024 Assistant GK,
KEA 2025 HK GK, KEA 2026 HK GK-3), sorted into items A–O by hand (PYQ_ITEMS)."""
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKS = ROOT / "packs"

# (letter, subject name, icon, [(topic, KRIES coverage, priority, hours, [(pack file, source topic, set indices or None = all)])])
SUBJECTS = [
    ("A", "P1 · KRIES A – Current Affairs (ಪ್ರಚಲಿತ ವಿದ್ಯಮಾನಗಳು)", "📰", [
        ("International Affairs and Organisations", "(A) World events, summits, international organisations and India's foreign relations", "High", 1.0,
         [("p1-ca.json", "Current International Affairs", None), ("p1-ca.json", "United Nations Organizations and Headquarters", None),
          ("p1-ca.json", "Current International Affairs – India's Foreign Relations", None)]),
        ("National Affairs, Schemes and Defence", "(A) Governance, central schemes, defence, abbreviations in the news", "High", 1.0,
         [("p1-ca.json", "Current National Affairs", None), ("p1-ca.json", "Three Wings of the Army", None), ("p1-ca.json", "Abbreviations", None)]),
        ("Karnataka Current Affairs", "(A) Karnataka – government decisions, schemes, appointments, events (January–October 2026)", "High", 1.5,
         [("p1-ca.json", "Current State and National Affairs", [0])] + [("p1-ca.json", f"{m} 2026", [0]) for m in
          ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October")]),
        ("National Current Affairs – Month by Month", "(A) National events of 2026, month by month", "Medium", 1.0,
         [("p1-ca.json", "Current State and National Affairs", [1])] + [("p1-ca.json", f"{m} 2026", [1]) for m in
          ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October")]),
        ("Awards, Books, Films and Sports", "(A) Awards and honours, books and authors, films, sports", "Medium", 0.75,
         [("p1-gk.json", "Awards, Honours and Prizes", None), ("p1-gk.json", "Famous Books and Authors", None), ("p1-ca.json", "Movies", None)]),
        ("Important Days and Events", "(A) National and international days, themes and slogans", "Low", 0.5,
         [("p1-ca.json", "Important Days and Slogans", None)]),
    ]),
    ("B", "P1 · KRIES B – General Science (ಸಾಮಾನ್ಯ ವಿಜ್ಞಾನ)", "🔬", [
        ("Physics", "(B) Motion, force, energy, heat, light, sound, electricity and magnetism (SSLC level)", "High", 1.0,
         [("p1-gk.json", "Basic Science – Concepts and Scientific Phenomena", [0, 3])]),
        ("Chemistry", "(B) Matter, acids, bases and salts, metals, carbon compounds, everyday chemistry", "High", 1.0,
         [("p1-gk.json", "Basic Science – Concepts and Scientific Phenomena", [1])]),
        ("Biology", "(B) Cell, life processes, plants and animals, heredity, ecology", "High", 1.0,
         [("p1-gk.json", "Basic Science – Concepts and Scientific Phenomena", [2])]),
        ("Health, Nutrition and Diseases", "(B) Nutrition, vitamins, diseases, immunisation, public health", "Medium", 0.75,
         [("p1-gk.json", "Health and Hygiene", None)]),
        ("Inventions, Discoveries, Space and Technology", "(B) Inventions, discoveries, scientists, space and defence technology", "Medium", 0.75,
         [("p1-gk.json", "Important Inventions and Discoveries", None)]),
    ]),
    ("C", "P1 · KRIES C – Geography (ಭೂಗೋಳಶಾಸ್ತ್ರ)", "🌍", [
        ("Physical Geography – Earth, Landforms and Climate", "(C) Earth, latitudes and longitudes, interior, rocks, landforms, atmosphere, climate", "High", 1.0,
         [("p1-gk.json", "Geography – Basic Concepts, Land and People", None)]),
        ("Geography of India – Regions, Soils, Resources and Crops", "(C) Physical divisions, rivers, soils, forests, minerals, agriculture of India", "High", 1.0,
         [("p1-gk.json", "Geography – Natural Regions, Natural Resources, Food Crops", None)]),
        ("Geography of Karnataka", "(C) Regions, rivers, climate, soils, forests, minerals, crops, districts of Karnataka", "High", 1.0, []),
        ("Population, Industries and Transport", "(C) Population and census, industries and ores, highways, railways, ports and airports", "Medium", 0.75,
         [("p1-gk.json", "Geography – Festivals, Population and Literacy", [0]), ("p1-ca.json", "Industries and Ores", None),
          ("p1-ca.json", "Highways, Railways and Airport Names", None)]),
        ("World Geography, Countries and Places", "(C) Countries, capitals and currencies, peaks, tourist places, monuments and parks", "Medium", 0.75,
         [("p1-ca.json", "Currency and Capitals of Countries", None), ("p1-ca.json", "Important Tourist Places and Peaks", None),
          ("p1-ca.json", "Monuments and National Forests", None)]),
    ]),
    ("D", "P1 · KRIES D – Social Science (ಸಮಾಜ ವಿಜ್ಞಾನ)", "📘", [
        ("Civics and Political Science", "(D) SSLC civics – government, rights, international relations, political science", "Medium", 0.75,
         [("p1-kries.json", "Social Science – SSLC Basics", [0])]),
        ("Economics – Indian Economy, Banking and Money", "(D) Indian economy, planning, banking, money, budget, industries", "High", 1.0,
         [("p1-kries.json", "Social Science – SSLC Basics", [1]), ("p1-gk.json", "Indian Economics – Major Industries, Projects, Public Undertakings", None)]),
        ("Sociology", "(D) Society, social groups, social stratification, social change (SSLC sociology)", "Medium", 0.75, []),
        ("Business Studies and Commerce", "(D) Business, trade, banking services, consumer protection, entrepreneurship (SSLC business studies)", "Low", 0.5, []),
    ]),
    ("E", "P1 · KRIES E – Indian Society and its Development (ಭಾರತೀಯ ಸಮಾಜ)", "👪", [
        ("Indian Society – Diversity, Caste, Family and Religion", "(E) Features of Indian society, unity in diversity, caste, family, religion", "Medium", 0.75, []),
        ("Social Reform Movements in India", "(E) Brahmo Samaj to Ambedkar – reformers and movements", "High", 0.75,
         [("p1-gk.json", "Indian History and Culture – Modern", [1])]),
        ("Culture – Festivals, Dances, Arts and Tribes", "(E) Festivals, classical and folk dances, arts, tribes of India", "Medium", 0.75,
         [("p1-ca.json", "Festivals, Folk Dances, Tribes of the Country", None), ("p1-gk.json", "Geography – Festivals, Population and Literacy", [1])]),
        ("Education, Women and Social Welfare", "(E) Education policies, women and child welfare, weaker sections, social laws", "Medium", 0.75,
         [("p1-ca.json", "Initiatives in Education in India", None)]),
    ]),
    ("F", "P1 · KRIES F – History of India and Karnataka (ಭಾರತ ಮತ್ತು ಕರ್ನಾಟಕದ ಇತಿಹಾಸ)", "🏺", [
        ("Ancient India", "(F) Prehistory, Indus, Vedic age, Jainism and Buddhism, Mauryas, Guptas", "High", 1.0,
         [("p1-gk.json", "Indian History and Culture – Ancient", None)]),
        ("Medieval India", "(F) Sultanate, Mughals, Marathas, Bhakti and Sufi, medieval South India", "High", 1.0,
         [("p1-gk.json", "Indian History and Culture – Medieval", None)]),
        ("Modern India and the Freedom Struggle", "(F) British rule, 1857, national movement, Gandhian era, independence", "High", 1.0,
         [("p1-gk.json", "Indian History and Culture – Modern", [0, 2])]),
        ("History of Karnataka – Dynasties", "(F) Satavahanas to Vijayanagara and the Bahmanis; Nayakas and Mysore", "High", 1.0,
         [("p1-gk.json", "Karnataka History, Culture and Art", [0, 1, 3])]),
        ("World History", "(F) Ancient, medieval and modern world events", "Low", 0.5, [("p1-gk.json", "Chronology of World History Events", None)]),
    ]),
    ("G", "P1 · KRIES G – Constitution and Public Administration (ಸಂವಿಧಾನ ಮತ್ತು ಆಡಳಿತ)", "⚖", [
        ("Making of the Constitution, Preamble, Rights and Duties", "(G) Constituent Assembly, sources, Preamble, citizenship, rights, DPSP, duties", "High", 1.0,
         [("p1-gk.json", "Indian Constitution – Fundamental Rights, Legislature, Executive, Judiciary", [0])]),
        ("Union and State Governments", "(G) President, Parliament, Prime Minister, Governor, State Legislature", "High", 1.0,
         [("p1-gk.json", "Indian Constitution – Fundamental Rights, Legislature, Executive, Judiciary", [1])]),
        ("Judiciary and Constitutional Bodies", "(G) Supreme Court, High Courts, writs, Election Commission, CAG, UPSC, Finance Commission", "High", 1.0,
         [("p1-gk.json", "Indian Constitution – Fundamental Rights, Legislature, Executive, Judiciary", [2])]),
        ("Amendments, Articles and Schedules", "(G) Important amendments, articles, parts and schedules", "Medium", 0.75,
         [("p1-ca.json", "Indian Constitution", None)]),
        ("Public Administration and Local Government", "(G) Public administration, civil services, budget process, local bodies, RTI, ombudsman", "High", 1.0, []),
    ]),
    ("H", "P1 · KRIES H – Practical Knowledge, SSLC Level (ಪ್ರಾಯೋಗಿಕ ಜ್ಞಾನ)", "🧮", [
        ("Number System, Percentage, Ratio and Average", "(H) Numbers, LCM/HCF, percentage, ratio and proportion, average", "High", 1.0,
         [("p1-kries.json", "Practical Knowledge – SSLC Arithmetic", [0])]),
        ("Profit, Loss and Interest", "(H) Profit and loss, discount, simple and compound interest", "High", 1.0,
         [("p1-kries.json", "Practical Knowledge – SSLC Arithmetic", [1])]),
        ("Time, Work, Speed and Mensuration", "(H) Time and work, pipes, speed and distance, trains, boats, areas and volumes", "High", 1.0,
         [("p1-kries.json", "Practical Knowledge – SSLC Arithmetic", [2])]),
        ("Data Interpretation and Everyday Practical Knowledge", "(H) Tables, bar and pie charts, probability, practical problems", "Medium", 0.75, []),
    ]),
    ("I", "P1 · KRIES I – Social and Cultural History of Karnataka (ಕರ್ನಾಟಕದ ಸಾಮಾಜಿಕ-ಸಾಂಸ್ಕೃತಿಕ ಇತಿಹಾಸ)", "🛕", [
        ("Religious and Social Reform – Vachanas and Dasas", "(I) Basavanna and the Vachana movement, Haridasas, saints and reformers", "High", 1.0,
         [("p1-kries.json", "Social and Cultural History of Karnataka", [0])]),
        ("Literature, Arts and Culture of Karnataka", "(I) Kannada literature, art and architecture, music, folk arts", "High", 1.0,
         [("p1-gk.json", "Karnataka History, Culture and Art", [2])]),
        ("Wodeyars, Dewans and Princely Mysore", "(I) Mysore Wodeyars, Dewans, modernisation of Mysore State", "High", 0.75, []),
        ("Rebellions, Freedom Movement and Unification", "(I) Armed rebellions, freedom struggle in Karnataka, Ekikarana", "High", 1.0,
         [("p1-kries.json", "Social and Cultural History of Karnataka", [1])]),
    ]),
    ("J", "P1 · KRIES J – Land Reforms and Social Change in Karnataka (ಭೂ ಸುಧಾರಣೆ)", "🌾", [
        ("Land Reform Acts and Land Tribunals", "(J) 1961 and 1974 Acts, land tribunals, tenancy, ceiling", "High", 1.0,
         [("p1-kries.json", "Land Reforms and Social Change in Karnataka", [0])]),
        ("Social Change – Urs Era, Backward Classes and Reservation", "(J) Devaraj Urs, backward class commissions, reservation, social justice", "High", 1.0,
         [("p1-kries.json", "Land Reforms and Social Change in Karnataka", [1])]),
    ]),
    ("K", "P1 · KRIES K – Economy of Karnataka (ಕರ್ನಾಟಕದ ಅರ್ಥವ್ಯವಸ್ಥೆ)", "💹", [
        ("Structure, Strengths and Weaknesses of Karnataka's Economy", "(K) GSDP, sectors, strengths, weaknesses, human development", "High", 1.0,
         [("p1-kries.json", "Karnataka Economy – Strengths, Weaknesses and Current Status", [0])]),
        ("Budget, Industries and Guarantee Schemes", "(K) State budget, industrial policy, IT-BT, guarantee schemes", "High", 1.0,
         [("p1-kries.json", "Karnataka Economy – Strengths, Weaknesses and Current Status", [1])]),
        ("Agriculture, Irrigation, Energy and Regional Imbalance", "(K) Agriculture, irrigation projects, power, Nanjundappa report, Kalyana Karnataka", "Medium", 0.75, []),
    ]),
    ("L", "P1 · KRIES L – Rural Development, Panchayat Raj and Co-operatives (ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ)", "🏡", [
        ("Panchayat Raj Institutions", "(L) Committees, 73rd Amendment, Karnataka Panchayat Raj Act, gram sabha", "High", 1.0,
         [("p1-kries.json", "Rural Development, Panchayat Raj and Rural Co-operatives", [0])]),
        ("Rural Development Programmes", "(L) MGNREGA, rural housing, drinking water, rural livelihood schemes", "High", 1.0,
         [("p1-kries.json", "Rural Development, Panchayat Raj and Rural Co-operatives", [1])]),
        ("Co-operative Movement in Karnataka", "(L) Co-operative principles, history (Kanaginahal), co-operative banks and societies", "Medium", 0.75, []),
    ]),
    ("M", "P1 · KRIES M – Science and Technology in Administration (ವಿಜ್ಞಾನ-ತಂತ್ರಜ್ಞಾನ ಮತ್ತು ಆಡಳಿತ)", "💻", [
        ("e-Governance Projects of Karnataka", "(M) Bhoomi, Kaveri, Seva Sindhu, Nemmadi, Sakala and other projects", "High", 1.0,
         [("p1-kries.json", "Science and Technology in Karnataka Administration", [0])]),
        ("Technology Institutions and Digital Services", "(M) Science and technology institutions, digital services, space and IT policy", "Medium", 0.75,
         [("p1-kries.json", "Science and Technology in Karnataka Administration", [1])]),
    ]),
    ("N", "P1 · KRIES N – Environment and Development of Karnataka (ಪರಿಸರ)", "🌳", [
        ("Western Ghats, Forests and Wildlife", "(N) Western Ghats, forests, protected areas, biodiversity", "High", 1.0,
         [("p1-kries.json", "Environment and Development of Karnataka", [0])]),
        ("Water, Pollution, Laws and Sustainable Development", "(N) River disputes, pollution, environmental laws, sustainability", "High", 1.0,
         [("p1-kries.json", "Environment and Development of Karnataka", [1])]),
        ("Climate Change, Disasters and Environmental Movements", "(N) Climate change, droughts and floods, Appiko, Chipko and other movements", "Medium", 0.75, []),
    ]),
    ("O", "P1 · KRIES O – Mental Ability (ಬೌದ್ಧಿಕ ಸಾಮರ್ಥ್ಯ)", "🧠", [
        ("Series, Analogy, Odd One Out and Coding–Decoding", "(O) Number and letter series, analogy, classification, coding", "High", 1.0,
         [("p1-kries.json", "Mental Ability – Reasoning", [0])]),
        ("Blood Relations, Directions and Ranking", "(O) Blood relations, direction sense, ranking and arrangement", "High", 1.0,
         [("p1-kries.json", "Mental Ability – Reasoning", [1])]),
        ("Clocks, Calendars, Syllogism and Venn Diagrams", "(O) Clocks, calendars, syllogisms, Venn diagrams", "High", 1.0,
         [("p1-kries.json", "Mental Ability – Reasoning", [2])]),
        ("Statements, Assumptions, Puzzles and Figures", "(O) Statement–assumption/conclusion, puzzles, seating, cubes and dice, figures", "Medium", 0.75, []),
    ]),
]
LETTERS = {letter: (name, icon, topics) for letter, name, icon, topics in SUBJECTS}
PYQ_TOPIC = {"A": "Current Affairs", "B": "General Science", "C": "Geography", "D": "Social Science", "E": "Indian Society", "F": "History of India and Karnataka",
             "G": "Constitution and Public Administration", "H": "Practical Knowledge", "I": "Social and Cultural History of Karnataka",
             "J": "Land Reforms and Social Change", "K": "Economy of Karnataka", "L": "Rural Development and Panchayat Raj",
             "M": "Science and Technology in Administration", "N": "Environment of Karnataka", "O": "Mental Ability"}


def pyq_topic(letter):
    return f"KEA Previous-Year Questions – {PYQ_TOPIC[letter]}"


def topic_names(letter):
    return [t[0] for t in LETTERS[letter][2]] + [pyq_topic(letter)]


def plan_ids(letter):
    return {t: f"P1-K{letter}-{i:02d}" for i, t in enumerate(topic_names(letter), 1)}


# Item (A–O) of every KEA general-knowledge question in packs/pyq-p1.json, in file order (English & Computer papers skipped)
PYQ_ITEMS = ("GGGGGLGGCA" "FFFFFCCCCK" "CCCCKNCNDD" "HOHOHHOHHO" "HDFGBBBBBB" "BBJAAFLCNF" "DDBDIELFLL" "CCGFIFFDDK" "AOBOAACCEG" "KCCCFCDE"
             "FFFIAIFIFF" "FMGGGGAMNN" "CCCCCCCCCH" "HOGOHHOHHH" "BBBBBBBBBB" "BBBBBDDBCD" "CCAANAGGAE" "FFFIEIIILI" "DDAMBELDDE" "GGGOFFAAI"
             "GGGGGGAEFI" "FIIIFEFFIA" "IBBBBBBBBB" "BBBBBBNCBB" "HGHHHHOHOO" "HOLKKLKEDN" "LLDAALCEAC" "CANCCCNCEC" "FCCCDMALAA" "AAAGAAAAA"
             "LALLLDGGGG" "GGEACCCBCN" "NNAFFIIFFF" "EFFFIOOHHH" "HOOOHHOHAA" "JAMAAAANAN" "KJJKEEIADD" "ADCDGBBBBB" "BBBBBFBBBK" "KMM"
             "CCCCECCCCC" "FFFIEFFFFF" "FFFFFADLED" "DDBBNBBBBB" "BBBBBBBBBH" "HHHHOOOOOH" "HOAAAAAMLG" "GGGGGGGFID" "DOEBCAAA")

_cache = {}


def _pack(f):
    if f not in _cache:
        _cache[f] = json.loads((PACKS / f).read_text(encoding="utf-8"))
    return _cache[f]


def _tuple(q):
    opts = [q["options"][k] for k in "ABCD"]
    t = (q["question"], opts, "ABCD".index(q["answer"]), q.get("explanation", ""))
    return t + ((q["source"],) if q.get("source") else ())


def _key(q, opts):
    norm = lambda s: re.sub(r"\s+", " ", unicodedata.normalize("NFKC", s)).strip().lower()
    return norm(q) + "|" + "|".join(sorted(norm(o) for o in opts))


def pyq_questions():
    d = _pack("pyq-p1.json")
    qs = [q for s in d["subjects"] for t in s["topics"] if "English & Computer" not in t["name"] for st in t["sets"] for q in st["questions"]]
    assert len(qs) == len(PYQ_ITEMS), (len(qs), len(PYQ_ITEMS))
    return list(zip(PYQ_ITEMS, qs))


def pulled(letter, chunk=25):
    """TOPICS and NOTES of one subject: pulled sets (duplicates inside the subject dropped) + the subject's real KEA questions."""
    name, icon, topics = LETTERS[letter]
    seen, out, notes = set(), {}, {}
    for tname, _cov, _pri, _hrs, pulls in topics:
        for f, src, idxs in pulls:
            t = next(t for s in _pack(f)["subjects"] for t in s["topics"] if t["name"] == src)
            for i, st in enumerate(t["sets"]):
                if idxs is not None and i not in idxs:
                    continue
                qs = []
                for q in st["questions"]:
                    k = _key(q["question"], list(q["options"].values()))
                    if k not in seen:
                        seen.add(k)
                        qs.append(_tuple(q))
                tag = st["name"].split(" · ", 1)[-1]
                if src.endswith("2026") and src.split()[0] in ("January", "February", "March", "April", "May", "June", "July", "August",
                                                                  "September", "October"):
                    tag = f"{tag} – {src}"
                if len(qs) >= 4:
                    out.setdefault(tname, []).append((f"0 · {tag}", qs))
            for n in t.get("notes", []):
                if n["title"] not in {x["title"] for x in notes.get(tname, [])}:
                    notes.setdefault(tname, []).append(n)
    real = [_tuple(q) for item, q in pyq_questions() if item == letter and _key(q["question"], list(q["options"].values())) not in seen]
    from p1_kx_pyq26 import PYQ26  # unused KEA 2026 GK questions sorted by item
    for t in PYQ26.get(letter, []):
        k = _key(t[0], t[1])
        if k not in seen:
            seen.add(k)
            real.append(t)
    for i in range(0, len(real), chunk):
        part = real[i:i + chunk]
        if len(part) >= 4:
            out.setdefault(pyq_topic(letter), []).append((f"0 · Previous-Year Questions – KEA GK papers {i // chunk + 1}", part))
        else:  # a short tail joins the previous set
            k, qs = out[pyq_topic(letter)][-1]
            out[pyq_topic(letter)][-1] = (k, qs + part)
    return out, notes


def extra_subjects():
    """EXTRA_SUBJECTS entries for build_subject.py / check_packs.py."""
    return {name: {"icon": icon, "topics": topic_names(letter), "plan": plan_ids(letter), "sizes": {}, "size": 20, "anysize": True, "renumber": True,
                   "group": "② Paper 1 · General (20 questions per set)"} for letter, name, icon, _ in SUBJECTS}


def build_packs():
    return {f"p1-kries-{letter.lower()}": {"subject": name, "modules": [f"p1_kx_{letter.lower()}"] + _new_modules(letter)} for letter, name, _, _ in SUBJECTS}


def _new_modules(letter):
    tools = Path(__file__).parent
    return sorted(p.stem for p in tools.glob(f"p1_kx_{letter.lower()}_*.py"))
