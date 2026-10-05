"""Paper 1 · General Knowledge · P1-GK-09 Chronology of World History Events and P1-GK-10 Geography – Basic Concepts, Land and
People (2 topics × 2 sub-topics × 20), with detailed revision NOTES for both (owner's request, 5 Oct 2026).
References: NCERT History (classes 9, 11 – Themes in World History) and Geography (class 11 – Fundamentals of Physical Geography),
KTBS Social Science (classes 8–10), Goh Cheng Leong, Certificate Physical and Human Geography. REAL previous-year questions come from
GFGC 2021 GK, the KEA 2025–26 GK papers, Legislative Council 2024 Paper-1, GTTC 2024 GK (official KEA key), PSI 2024, KRIES 2025 and
a UPSC-coaching entrance test; answers without an official key were worked out by ExamSim and say so. World-history questions are
rare in KEA GK papers, so GK-09 is mostly "PYQ pattern" questions in the KPSC / SSC style."""
from packlib import AR, I_II

PYQ = "PYQ pattern (KPSC / KEA / SSC GK). "
KEY = " (Official answer: KEA final key.)"
NOTE = " (Answer worked out by ExamSim; not KEA's official key.)"

WORLD_EARLY = [
    ("Arrange the following Periods/Ages in chronological order.\n(i) Neolithic Age\n(ii) Bronze Age\n(iii) Iron Age\n(iv) Paleolithic Period\n(v) Chalcolithic Period\n(vi) Mesolithic Period",
     ["(iv), (vi), (i), (v), (iii) and (ii)", "(vi), (ii), (iii), (i), (v) and (iv)", "(ii), (iii), (iv), (i), (vi) and (v)", "(iv), (vi), (i), (v), (ii) and (iii)"], 3,
     "Old Stone Age → Middle Stone Age → New Stone Age → Copper-Stone (Chalcolithic) → Bronze → Iron." + NOTE, "KEA 2026 GK-1 (NHK, 11 Jan 2026) · Q35"),
    ("Out of the seven wonders of the Ancient world, which of the following are still preserved?\na. Pyramids of Egypt\nb. Temple of Diana\nc. Light house of Pharos",
     ["Only b", "Only a", "Both a and c", "All a, b and c"], 1,
     "Only the Great Pyramid of Giza survives; the Temple of Artemis (Diana) at Ephesus and the Pharos of Alexandria were destroyed." + NOTE, "GFGC 2021 GK · Q46"),
    ("The world's earliest known writing system, cuneiform, developed in:",
     ["Mesopotamia (Sumer)", "Egypt", "China", "Greece"], 0, PYQ + "Sumerians wrote on clay tablets around 3200 BCE; Egyptians used hieroglyphs."),
    ("The Code of Hammurabi, one of the earliest written law codes, belongs to:",
     ["Babylon", "Egypt", "Rome", "Persia"], 0, "King Hammurabi ruled Babylon around 1792–1750 BCE ('an eye for an eye')."),
    ("The first recorded ancient Olympic Games were held in Greece in:",
     ["776 BCE", "1896 CE", "490 BCE", "323 BCE"], 0, PYQ + "The modern Olympics began at Athens in 1896."),
    ("Alexander the Great died in:",
     ["323 BCE at Babylon", "326 BCE at Taxila", "336 BCE at Macedonia", "300 BCE at Athens"], 0,
     "He fought Porus at the Battle of the Hydaspes (Jhelum) in 326 BCE."),
    ("The first Roman emperor was:",
     ["Augustus (Octavian), 27 BCE", "Julius Caesar", "Nero", "Constantine"], 0, PYQ + "Julius Caesar was assassinated in 44 BCE but never became emperor."),
    ("The Western Roman Empire is traditionally said to have fallen in:",
     ["476 CE", "1453 CE", "44 BCE", "800 CE"], 0, "The Eastern (Byzantine) Empire lasted until the fall of Constantinople in 1453."),
    ("China was first unified, and work on linking the Great Wall begun, under:",
     ["Qin Shi Huang (221 BCE)", "Kublai Khan", "Confucius", "Sun Yat-sen"], 0, PYQ + "The name 'China' is thought to come from Qin."),
    ("The Hijra of Prophet Muhammad from Mecca to Medina, which marks the beginning of the Islamic calendar, took place in:",
     ["622 CE", "570 CE", "632 CE", "711 CE"], 0, "He was born about 570 CE and died in 632 CE."),
    ("Charlemagne was crowned Emperor of the Romans by the Pope in:",
     ["800 CE", "476 CE", "1066 CE", "1215 CE"], 0, PYQ + "He ruled the Frankish kingdom."),
    ("The Magna Carta, which limited the powers of the English king, was signed by King John in:",
     ["1215", "1066", "1688", "1789"], 0, "1066 was the Norman Conquest (Battle of Hastings)."),
    ("The Fall of Constantinople to the Ottoman Turks took place in:",
     ["1453", "1492", "1517", "1299"], 0, PYQ + "It closed the old land routes to the East and encouraged sea voyages of discovery."),
    ("Arrange in chronological order:\n1. Columbus reaches the Americas\n2. Vasco da Gama reaches Calicut\n3. Fall of Constantinople\n4. Martin Luther's 95 Theses",
     ["3, 1, 2, 4", "1, 3, 2, 4", "3, 2, 1, 4", "2, 1, 3, 4"], 0, "1453, 1492, 1498, 1517."),
    ("The Renaissance ('rebirth' of classical learning) began in the 14th century in:",
     ["Italy", "England", "Spain", "Germany"], 0, PYQ + "Florence was its centre; Leonardo da Vinci and Michelangelo were Renaissance artists."),
    ("The Protestant Reformation began in 1517 when ____ posted his 95 Theses at Wittenberg.",
     ["Martin Luther", "John Calvin", "Henry VIII", "Erasmus"], 0, "It protested against the sale of indulgences."),
    ("The first voyage around the world (1519–1522) was led by:",
     ["Ferdinand Magellan (completed by Elcano)", "Christopher Columbus", "Vasco da Gama", "James Cook"], 0, PYQ + "Magellan was killed in the Philippines in 1521."),
    ("Consider the statements:\nI. The Hundred Years' War was fought between England and France.\nII. It lasted exactly one hundred years.",
     I_II, 0, "It lasted 116 years (1337–1453); Joan of Arc fought in it."),
    ("Assertion (A): The printing press helped spread the ideas of the Renaissance and the Reformation.\nReason (R): Johannes Gutenberg developed movable-type printing in Europe around 1440.",
     AR, 0, "The Gutenberg Bible was printed in the 1450s."),
    ("Match:\na. Cuneiform  b. Hieroglyphics  c. Code of laws  d. Democracy\n1. Sumer  2. Egypt  3. Babylon  4. Athens",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Cleisthenes introduced democracy at Athens in 508 BCE."),
]

WORLD_MODERN = [
    ("Arrange the following global events in the correct chronological order:\n(a) Agenda-21\n(b) Brundtland Report\n(c) Sustainable Development Goals\n(d) Stockholm Conference",
     ["d, b, a, c", "c, b, a, d", "a, b, c, d", "d, c, b, a"], 0,
     "Stockholm Conference 1972 → Brundtland Report 1987 → Agenda 21 at the Rio Earth Summit 1992 → SDGs 2015." + NOTE, "KEA 2025 GK (HK, 21 Dec 2025) · Q24"),
    ("Arrange the following in the chronological order\na. Nationalisation of 14 major private banks\nb. Iraq's invasion on Kuwait\nc. Liberalisation, Privatisation and Globalisation reforms (LPG reforms)\nd. Asian Financial Crisis.\nSelect the correct answer using the codes given below",
     ["c, b, a, d", "d, b, c, a", "a, b, c, d", "b, a, d, c"], 2,
     "1969 → August 1990 → July 1991 → 1997." + NOTE, "Legislative Council 2024 Data Entry P1 · Q16"),
    ("The Glorious Revolution, which established the supremacy of Parliament in England, took place in:",
     ["1688", "1215", "1642", "1832"], 0, PYQ + "The Bill of Rights followed in 1689."),
    ("The American Declaration of Independence was adopted on:",
     ["4 July 1776", "14 July 1789", "4 July 1783", "17 September 1787"], 0, "It was drafted mainly by Thomas Jefferson; Britain recognised independence by the Treaty of Paris (1783)."),
    ("The French Revolution began in 1789 with the storming of the:",
     ["Bastille (14 July)", "Winter Palace", "Reichstag", "Tower of London"], 0, PYQ + "Its slogan was 'Liberty, Equality, Fraternity'."),
    ("Napoleon Bonaparte was finally defeated at the Battle of:",
     ["Waterloo (1815)", "Trafalgar (1805)", "Austerlitz (1805)", "Leipzig (1813)"], 0, "He was exiled to St Helena, where he died in 1821."),
    ("The Industrial Revolution first began in the late 18th century in:",
     ["Britain", "France", "Germany", "USA"], 0, PYQ + "James Watt's improved steam engine (1769) was one of its key inventions."),
    ("The Communist Manifesto (1848) was written by:",
     ["Karl Marx and Friedrich Engels", "Lenin and Trotsky", "Rousseau and Voltaire", "Adam Smith and Ricardo"], 0, "Das Kapital (vol. 1) followed in 1867."),
    ("The unification of Germany was completed in 1871 under the leadership of:",
     ["Otto von Bismarck", "Giuseppe Garibaldi", "Napoleon III", "Metternich"], 0, PYQ + "Italy's unification is linked with Mazzini, Garibaldi and Cavour (kingdom of Italy, 1861)."),
    ("The American Civil War (1861–1865) was fought mainly over:",
     ["Slavery and the unity of the Union", "Independence from Britain", "Oil", "Religious freedom"], 0, "Abraham Lincoln was President; the 13th Amendment abolished slavery (1865)."),
    ("The immediate cause of the First World War was:",
     ["The assassination of Archduke Franz Ferdinand at Sarajevo (28 June 1914)", "The invasion of Poland", "The bombing of Pearl Harbor", "The Russian Revolution"], 0,
     PYQ + "The war ended with the armistice of 11 November 1918."),
    ("The Treaty of Versailles (1919) was signed between the Allies and:",
     ["Germany", "Russia", "Japan", "Italy"], 0, "It also created the League of Nations (1920, Geneva)."),
    ("The Bolshevik (October) Revolution of 1917 in Russia was led by:",
     ["Vladimir Lenin", "Joseph Stalin", "Tsar Nicholas II", "Mikhail Gorbachev"], 0, PYQ + "The USSR was formed in 1922 and dissolved on 26 December 1991."),
    ("The Second World War began on 1 September 1939 when Germany invaded:",
     ["Poland", "France", "Czechoslovakia", "Austria"], 0, "Britain and France declared war on 3 September 1939."),
    ("The USA entered the Second World War after the Japanese attack on:",
     ["Pearl Harbor (7 December 1941)", "Hiroshima", "Midway", "Manila"], 0, PYQ + "Atomic bombs fell on Hiroshima (6 Aug 1945) and Nagasaki (9 Aug 1945)."),
    ("Arrange in chronological order:\n1. Fall of the Berlin Wall\n2. Cuban Missile Crisis\n3. Formation of NATO\n4. Dissolution of the USSR",
     ["3, 2, 1, 4", "2, 3, 1, 4", "3, 1, 2, 4", "1, 2, 3, 4"], 0, "1949, 1962, 1989, 1991."),
    ("The People's Republic of China was proclaimed by Mao Zedong on:",
     ["1 October 1949", "15 August 1947", "1 January 1912", "4 May 1919"], 0, PYQ + "The 1911 Xinhai Revolution led by Sun Yat-sen ended the Qing dynasty."),
    ("The first human to walk on the Moon (20 July 1969) was:",
     ["Neil Armstrong", "Yuri Gagarin", "Buzz Aldrin", "Alan Shepard"], 0, "Gagarin was the first human in space (12 April 1961)."),
    ("Assertion (A): The Cold War was a direct military war between the USA and the USSR.\nReason (R): The Cold War was a rivalry of ideology, arms race and influence after 1945.",
     AR, 3, "The superpowers never fought each other directly; they competed through proxies, alliances and the arms race."),
    ("Match:\na. Nelson Mandela  b. Martin Luther King Jr.  c. Mikhail Gorbachev  d. Winston Churchill\n1. End of apartheid  2. US civil-rights movement  3. Glasnost and perestroika  4. Britain's wartime Prime Minister",
     ["a-1, b-2, c-3, d-4", "a-2, b-1, c-3, d-4", "a-1, b-3, c-2, d-4", "a-4, b-2, c-3, d-1"], 0, PYQ + "Mandela became South Africa's first black President in 1994."),
]

EARTH = [
    ("An imaginary latitude which divides the earth into two equal halves is",
     ["Tropic of Cancer", "Tropic of Capricorn", "Equator", "Arctic Circle"], 2,
     "The Equator (0°) divides the Earth into the Northern and Southern Hemispheres." + NOTE, "KRIES 2025 entrance · Q89"),
    ("India is located in which part of the Asian continent?",
     ["East", "West", "North", "South"], 3,
     "India lies in South Asia, entirely in the Northern and Eastern Hemispheres." + NOTE, "KRIES 2025 entrance · Q93"),
    ("Arrange the following in the ascending order from the Earth's surface:\na. Exosphere\nb. Ionosphere\nc. Stratosphere\nd. Mesosphere",
     ["c, d, b, a", "b, c, a, d", "d, b, c, a", "a, b, c, d"], 0,
     "Troposphere → stratosphere → mesosphere → ionosphere (thermosphere) → exosphere." + NOTE, "GFGC 2021 GK · Q35"),
    ("The gas that makes up the largest share (about 78%) of the Earth's atmosphere by volume is:",
     ["Nitrogen", "Oxygen", "Argon", "Carbon dioxide"], 0, PYQ + "Oxygen is about 21%, argon 0.93% and carbon dioxide about 0.04%."),
    ("Select the correct match.",
     ["Ozone depletion - Earth summit", "Ozone hole - Arctic region", "Bad ozone - Troposphere", "Good ozone - Thermosphere"], 2,
     "Ground-level (tropospheric) ozone is a pollutant; the protective ozone layer is in the stratosphere, and the big ozone hole forms over Antarctica." + NOTE,
     "KEA 2026 GK-3 (NHK, 10 May 2026) · Q8"),
    ("What do you mean by ITCZ?",
     ["Zone of Tropic of Cancer", "Intensive Temperature Core Zone", "Inter Tropical Convergence Zone", "Intensive Zone of Tropical Zone"], 2,
     "The ITCZ is the low-pressure belt near the Equator where the trade winds meet; it shifts north and south with the seasons." + NOTE,
     "UPSC coaching entrance 2025 GS-1 · Q82"),
    ("Match the following:\nList - I\n(a) Isohel\n(b) Isobar\n(c) Isoneph\n(d) Isohyet\nList - II\n(i) Equal Clouds\n(ii) Equal Sunshine\n(iii) Equal Rainfall\n(iv) Equal Pressure",
     ["a – iv, b – iii, c – i, d – ii", "a – iv, b – ii, c – i, d – iii", "a – i, b – ii, c – iv, d – iii", "a – ii, b – iv, c – i, d – iii"], 3,
     "Isohel – sunshine, isobar – pressure, isoneph – cloudiness, isohyet – rainfall (isotherm – temperature)." + NOTE, "KEA 2026 GK-1 (NHK, 11 Jan 2026) · Q86"),
    ("Match List-I with List-II and select the correct answer using the codes given below:\nList-I\n(a) Cyclones\n(b) Typhoons\n(c) Hurricanes\n(d) Willy-willies\nList-II\n(i) Philippine islands\n(ii) North American and Caribbean Sea\n(iii) Australian Region\n(iv) Bay of Bengal and Arabian Sea (India)",
     ["a – iii, b – iv, c – i, d – ii", "a – iv, b – i, c – ii, d – iii", "a – ii, b – i, c – iii, d – iv", "a – iv, b – ii, c – i, d – iii"], 1,
     "Tropical cyclones have local names: cyclones (Indian Ocean), typhoons (western Pacific, China Sea, Philippines), hurricanes (Atlantic, Caribbean), willy-willies (Australia)." + NOTE,
     "KEA 2026 GK-1 (NHK, 11 Jan 2026) · Q83"),
    ("The Earth takes about ____ to complete one rotation on its axis.",
     ["24 hours (23 h 56 min sidereal)", "365¼ days", "12 hours", "30 days"], 0, PYQ + "Rotation causes day and night; revolution around the Sun causes the seasons (with the axial tilt)."),
    ("The Earth's axis is inclined to the plane of its orbit at about:",
     ["66½° (23½° from the vertical)", "90°", "45°", "0°"], 0, "This tilt causes seasons and varying day length."),
    ("On 21 June (summer solstice), the Sun's rays fall vertically on the:",
     ["Tropic of Cancer (23½° N)", "Equator", "Tropic of Capricorn", "Arctic Circle"], 0, PYQ + "On 22 December the Sun is overhead at the Tropic of Capricorn."),
    ("Days and nights are of equal length all over the world on:",
     ["21 March and 23 September (equinoxes)", "21 June and 22 December", "1 January", "4 July"], 0, "The Sun is overhead at the Equator on the equinoxes."),
    ("The Prime Meridian (0° longitude) passes through:",
     ["Greenwich, near London", "Paris", "Ujjain", "New York"], 0, PYQ + "The International Date Line roughly follows 180° longitude."),
    ("Indian Standard Time is based on the longitude of:",
     ["82½° E (passing near Mirzapur / Prayagraj)", "75° E", "90° E", "0°"], 0, "IST is 5 h 30 min ahead of GMT (82.5 × 4 min = 330 min)."),
    ("Each degree of longitude corresponds to a time difference of:",
     ["4 minutes", "1 hour", "15 minutes", "1 minute"], 0, PYQ + "360° = 24 hours, so 15° = 1 hour."),
    ("The point in the Earth's orbit nearest to the Sun (about 3 January) is called:",
     ["Perihelion", "Aphelion", "Apogee", "Solstice"], 0, "Aphelion (farthest) is about 4 July."),
    ("Which is the largest planet of the solar system?",
     ["Jupiter", "Saturn", "Earth", "Neptune"], 0, PYQ + "Mercury is the smallest and nearest to the Sun; Venus is the hottest."),
    ("Consider the statements:\nI. Latitudes are parallel circles that become smaller towards the poles.\nII. All meridians of longitude are of equal length.",
     I_II, 2, "Every meridian is a half circle joining the two poles."),
    ("Assertion (A): When it is noon at Greenwich, it is 5:30 p.m. in India.\nReason (R): India is east of Greenwich and IST is 5 h 30 min ahead of GMT.",
     AR, 0, "Places east of Greenwich are ahead in time."),
    ("Assertion (A): The troposphere is the layer in which almost all weather occurs.\nReason (R): Temperature in the troposphere increases with height.",
     AR, 2, "Temperature falls by about 6.5 °C per km in the troposphere (normal lapse rate)."),
]

LAND = [
    ("The oceanic crust mainly consists of",
     ["Silicon and Aluminium", "Silicon and Manganese", "Silicon and Magnesium", "Silicon and Calcium"], 2,
     "The oceanic crust is SIMA (silica + magnesium, mainly basalt); the continental crust is SIAL (silica + aluminium)." + NOTE,
     "Legislative Council 2024 Asst/Computer Operator P1 · Q58"),
    ("Read the following and match correctly.\na) Inner Core\nb) Outer Core\nc) Mantle\nd) Crust\ni. 5 – 40 kms\nii. 2895 kms\niii. 1255 kms\niv. 2245 kms",
     ["a – iii, b – i, c – iv, d – ii", "a – ii, b – iii, c – iv, d – i", "a – iv, b – iii, c – ii, d – i", "a – iii, b – iv, c – ii, d – i"], 3,
     "Crust 5–40 km; the mantle extends to about 2,895 km depth; the outer core is about 2,245 km thick and the inner core has a radius of about 1,255 km." + NOTE,
     "PSI 2024 General Paper · Q34"),
    ("Which of the following are not an igneous rock?\na) Batholiths\nb) Barchan\nc) Phyllite\nd) Moraines\ne) Zeolites\nChoose the correct answer from the option given below:",
     ["a, b and d are correct", "a, b, c and d are correct", "b, c and d are correct", "b, c, d and e are correct"], 2,
     "A batholith is a large intrusive igneous body; a barchan is a sand dune, phyllite a metamorphic rock and a moraine a glacial deposit. (Zeolites are minerals that form in volcanic rocks.)" + NOTE,
     "Legislative Council 2024 Asst/Computer Operator P1 · Q88"),
    ("Match the items in List-I with the items in List-II and choose the correct answer.\nList – I (Mountains)\n(a) Mt. Mckinley\n(b) Mt. Aconcagua\n(c) Mt. Elbrus\n(d) Mt. Kosciuszko\nList – II (Continents)\n(i) Australia\n(ii) North America\n(iii) South America\n(iv) Europe",
     ["a – ii, b – iii, c – iv, d – i", "a – i, b – ii, c – iii, d – iv", "a – ii, b – iii, c – i, d – iv", "a – iv, b – i, c – ii, d – iii"], 0,
     "Denali (McKinley) – North America; Aconcagua – South America; Elbrus – Europe; Kosciuszko – Australia." + NOTE, "KEA 2026 GK-3 (HK, 4 Jul 2026) · Q1"),
    ("Consider the following statements.\nStatement-I: Earthquakes tend to occur at the boundaries of earth's plates and these boundaries are known as fault zones.\nStatement-II: It is possible to predict when and where the next earthquake might occur.\nWhich one of the following is correct in respect of the above statements?",
     ["Both statement-I and statement-II are correct", "Statement-I is correct, but statement-II is incorrect", "Statement-I is incorrect, but statement-II is correct", "Both statement-I and statement-II are incorrect"], 1,
     "Most earthquakes occur along plate boundaries, but scientists still cannot predict the exact time and place of an earthquake." + NOTE,
     "KEA 2026 GK-3 (NHK, 10 May 2026) · Q3"),
    ("Principal fishing ground in the world are located in",
     ["Continental shelves", "Continental slope", "Abyssal plain", "Deep ocean trenches"], 0,
     "Shallow continental shelves get sunlight and nutrients, so plankton and fish are plentiful (e.g. Grand Banks, Dogger Bank)." + KEY, "GTTC 2024 Asst Gr-II GK · Q75"),
    ("The three layers of the Earth's interior, from the surface inwards, are:",
     ["Crust, mantle, core", "Mantle, crust, core", "Core, crust, mantle", "Crust, core, mantle"], 0, PYQ + "The boundary between crust and mantle is the Mohorovičić (Moho) discontinuity."),
    ("The core of the Earth is made mainly of:",
     ["Nickel and iron (NIFE)", "Silica and aluminium", "Silica and magnesium", "Carbon and oxygen"], 0, "The outer core is liquid; the inner core is solid because of the enormous pressure."),
    ("Rocks formed by the cooling and solidification of magma or lava are:",
     ["Igneous rocks", "Sedimentary rocks", "Metamorphic rocks", "Organic rocks"], 0, PYQ + "Granite (intrusive) and basalt (extrusive) are igneous; they are called primary rocks."),
    ("Limestone, sandstone and shale are examples of:",
     ["Sedimentary rocks", "Igneous rocks", "Metamorphic rocks", "Volcanic rocks"], 0, "Fossils are found in sedimentary rocks."),
    ("Marble is formed by the metamorphism of:",
     ["Limestone", "Granite", "Shale", "Sandstone"], 0, PYQ + "Shale → slate; sandstone → quartzite; granite → gneiss."),
    ("The theory that the continents were once joined in a supercontinent called Pangaea was proposed by:",
     ["Alfred Wegener (continental drift, 1912)", "Harry Hess", "Charles Darwin", "Isaac Newton"], 0, "The surrounding ocean was called Panthalassa."),
    ("The Himalayas were formed by the collision of:",
     ["The Indian plate with the Eurasian plate", "The Pacific and Nazca plates", "The African and South American plates", "Two oceanic plates"], 0,
     PYQ + "They are young fold mountains, still rising."),
    ("The 'Ring of Fire', which has most of the world's active volcanoes, surrounds the:",
     ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], 0, "It marks the subduction zones around the Pacific plate."),
    ("Which is the largest continent by area?",
     ["Asia", "Africa", "North America", "Antarctica"], 0, PYQ + "Australia is the smallest; Antarctica is the coldest and highest on average."),
    ("The largest and deepest ocean is the:",
     ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Southern Ocean"], 0, "The deepest point is the Challenger Deep (Mariana Trench), about 11 km deep."),
    ("Landforms such as V-shaped valleys, gorges and waterfalls are formed mainly by:",
     ["Running water (rivers)", "Wind", "Glaciers", "Sea waves"], 0, PYQ + "Glaciers carve U-shaped valleys; wind forms sand dunes such as barchans."),
    ("The breaking down of rocks in place by heat, frost, water and living things is called:",
     ["Weathering", "Erosion", "Deposition", "Folding"], 0, "Erosion removes and transports the weathered material."),
    ("Consider the statements:\nI. Plateaus are flat-topped highlands.\nII. The Deccan plateau is made largely of basalt from ancient lava flows.",
     I_II, 2, "The Deccan Traps formed about 66 million years ago."),
    ("Assertion (A): Sedimentary rocks often contain fossils.\nReason (R): They are formed by layers of sediment that bury the remains of plants and animals.",
     AR, 0, "Heat and pressure in igneous and metamorphic rocks usually destroy fossils."),
]

TOPICS = {
    "Chronology of World History Events": [("1 · Ancient and Medieval World up to 1500", WORLD_EARLY),
                                           ("2 · Modern World – Revolutions, World Wars and After", WORLD_MODERN)],
    "Geography – Basic Concepts, Land and People": [("1 · Earth, Latitudes and Longitudes, Motions and Atmosphere", EARTH),
                                                    ("2 · Earth's Interior, Rocks, Landforms, Continents and Oceans", LAND)],
}

NOTES = {
    "Chronology of World History Events": [{"title": "World history timeline – revision notes", "md": """# Chronology of world history

## 1. Prehistory (order of ages)
**Palaeolithic (Old Stone) → Mesolithic → Neolithic (farming, polished tools) → Chalcolithic (copper + stone) → Bronze Age → Iron Age.**

## 2. Ancient world
| Date | Event |
|---|---|
| c. 3200 BCE | **Cuneiform** writing in **Sumer (Mesopotamia)**; hieroglyphs in Egypt |
| c. 2560 BCE | **Great Pyramid of Giza** (Khufu) – the only surviving ancient wonder |
| c. 1754 BCE | **Code of Hammurabi**, Babylon |
| 776 BCE | First ancient **Olympic Games** (Olympia, Greece) |
| 753 BCE | Legendary founding of **Rome** |
| 508 BCE | **Democracy** at Athens (Cleisthenes) |
| 490 BCE | Battle of Marathon (Greeks v. Persians) |
| 326 / 323 BCE | Alexander defeats Porus (Hydaspes) / dies at Babylon |
| 221 BCE | **Qin Shi Huang** unifies China; Great Wall linked |
| 44 BCE | Julius Caesar assassinated |
| 27 BCE | **Augustus** – first Roman emperor |
| 476 CE | Fall of the **Western Roman Empire** |
| 622 CE | **Hijra** – start of the Islamic calendar |
| 800 CE | **Charlemagne** crowned emperor |

**Seven ancient wonders:** Great Pyramid of Giza, Hanging Gardens of Babylon, Temple of Artemis (Diana) at Ephesus, Statue of Zeus at Olympia, Mausoleum at Halicarnassus, Colossus of Rhodes, Lighthouse (Pharos) of Alexandria – **only the Pyramid survives**.

## 3. Medieval to early modern
| Date | Event |
|---|---|
| 1066 | Norman Conquest of England (Battle of Hastings) |
| 1215 | **Magna Carta** (King John) |
| 1337–1453 | **Hundred Years' War** (England v. France; Joan of Arc) – 116 years |
| 1347–51 | **Black Death** (bubonic plague) in Europe |
| 14th c. | **Renaissance** begins in **Italy** (Florence) |
| c. 1440 | **Gutenberg** printing press |
| **1453** | **Fall of Constantinople** to the Ottomans |
| **1492** | **Columbus** reaches the Americas |
| **1498** | **Vasco da Gama** reaches **Calicut** |
| **1517** | **Martin Luther's 95 Theses** – Reformation |
| 1519–22 | **Magellan**–Elcano – first circumnavigation |
| 1618–48 | Thirty Years' War → Peace of Westphalia (1648) |

## 4. Age of revolutions
| Date | Event |
|---|---|
| **1688** | **Glorious Revolution** (England); Bill of Rights 1689 |
| 1760s → | **Industrial Revolution** begins in **Britain** (Watt's steam engine 1769) |
| **4 July 1776** | **American Declaration of Independence** (Jefferson); Treaty of Paris 1783 |
| **14 July 1789** | **French Revolution** – storming of the Bastille; 'Liberty, Equality, Fraternity' |
| 1804 / **1815** | Napoleon emperor / defeated at **Waterloo**; Congress of Vienna |
| 1848 | **Communist Manifesto** (Marx & Engels); revolutions across Europe |
| 1861 / 1870 | Kingdom of **Italy** (Mazzini, Garibaldi, Cavour) / Rome joined |
| 1861–65 | **American Civil War** (Lincoln); 13th Amendment ends slavery |
| 1868 | **Meiji Restoration**, Japan |
| 1869 | **Suez Canal** opened |
| **1871** | **Unification of Germany** (Bismarck) |
| 1911 | **Xinhai Revolution**, China (Sun Yat-sen) – end of the Qing |

## 5. World wars and the 20th century
| Date | Event |
|---|---|
| 28 June 1914 | Assassination of **Archduke Franz Ferdinand** at **Sarajevo** → **WW I** (1914–18) |
| 1917 | **Russian Revolution** – February; **October (Bolshevik, Lenin)** |
| **28 June 1919** | **Treaty of Versailles** (with Germany) |
| 1920 | **League of Nations** (Geneva) |
| 1922 | USSR formed; Mussolini in power in Italy |
| 1929 | **Great Depression** (Wall Street crash) |
| 1933 | Hitler becomes Chancellor of Germany |
| **1 Sept 1939** | Germany invades **Poland** → **WW II** |
| 7 Dec 1941 | **Pearl Harbor** – USA enters the war |
| 6 / 9 Aug 1945 | Atomic bombs on **Hiroshima / Nagasaki** |
| 24 Oct 1945 | **United Nations** founded |
| 1947 | India's independence; Marshall Plan; Cold War begins |
| 1949 | **NATO**; **People's Republic of China** (1 Oct, Mao) |
| 1950–53 | Korean War |
| 1955 | Warsaw Pact |
| 1957 | **Sputnik 1** (USSR) – space age |
| 1961 | **Gagarin** first in space; **Berlin Wall** built |
| 1962 | **Cuban Missile Crisis** |
| **20 July 1969** | **Moon landing** (Armstrong, Aldrin) |
| 1972 | **Stockholm Conference** on the Human Environment (UNEP) |
| 1987 | **Brundtland Report** 'Our Common Future' (sustainable development) |
| **9 Nov 1989** | **Fall of the Berlin Wall** |
| 3 Oct 1990 | German reunification; Aug 1990 Iraq invades Kuwait → Gulf War 1991 |
| **26 Dec 1991** | **Dissolution of the USSR** |
| 1992 | **Rio Earth Summit** – **Agenda 21** |
| 1993 / 1995 | **European Union** (Maastricht) / **WTO** |
| 1994 | End of apartheid – **Nelson Mandela** President |
| 1997 | Asian Financial Crisis; Kyoto Protocol |
| 11 Sept 2001 | 9/11 attacks in the USA |
| 2015 | **SDGs** (Agenda 2030) and **Paris Agreement** |

## 6. India-linked dates often mixed into world chronology
Bank nationalisation **1969** → LPG reforms **1991** → Asian Financial Crisis **1997**.

## 7. Traps
- Hundred Years' War lasted **116** years.
- Julius Caesar was **not** an emperor; **Augustus** was the first.
- Columbus (1492) came **before** Vasco da Gama (1498).
- Treaty of **Versailles** ended WW I (1919); Treaty of **Paris** (1783) ended the American war.
- Gagarin – first in space; Armstrong – first on the Moon.
"""}],
    "Geography – Basic Concepts, Land and People": [{"title": "Basic geography – revision notes", "md": """# Geography – basic concepts, land and people

## 1. Earth and the solar system
- 8 planets: Mercury, Venus, **Earth**, Mars, **Jupiter** (largest), Saturn, Uranus, Neptune (farthest). Venus – hottest; Mercury – smallest.
- Earth: 3rd planet, the 'blue planet'; average distance from the Sun ≈ **150 million km**; light takes ~8 min 20 s.
- **Rotation**: west → east, ~24 h → day and night. **Revolution**: 365¼ days → seasons (with the **23½° tilt**; axis makes 66½° with the orbital plane).
- **Perihelion** (nearest, ~3 Jan) / **Aphelion** (farthest, ~4 July).
- **Solstices**: 21 June – Sun overhead at the **Tropic of Cancer** (longest day in the north); 22 Dec – **Tropic of Capricorn**.
- **Equinoxes**: 21 March and 23 September – Sun over the **Equator**, equal day and night everywhere.

## 2. Latitudes and longitudes
| Item | Fact |
|---|---|
| Equator | 0°, divides Earth into two equal halves (N and S hemispheres) |
| Tropic of Cancer / Capricorn | 23½° N / 23½° S (Cancer passes through 8 Indian states) |
| Arctic / Antarctic Circle | 66½° N / S |
| Prime Meridian | 0°, **Greenwich** (London) |
| International Date Line | about **180°** |
| Time | 15° = 1 hour; **1° = 4 minutes** |
| **IST** | **82½° E** (near Mirzapur / Prayagraj) = GMT **+ 5 h 30 min** |
- Latitude circles get smaller towards the poles; all meridians are equal half-circles.
- India lies wholly in the **Northern and Eastern** hemispheres, in **South Asia**.

## 3. Interior of the Earth
| Layer | Facts |
|---|---|
| **Crust** | 5–40 km (thicker under mountains); continental = **SIAL** (silica + aluminium); oceanic = **SIMA** (silica + magnesium, basalt) |
| **Mantle** | down to ~**2,895 km**; asthenosphere (partly molten) is the source of magma |
| **Outer core** | liquid, ~2,245 km thick |
| **Inner core** | solid, radius ~**1,255 km**; **NIFE** (nickel + iron) |
Discontinuities: **Moho** (crust/mantle), **Gutenberg** (mantle/core). Lithosphere = crust + upper mantle.

## 4. Rocks
| Type | How formed | Examples |
|---|---|---|
| **Igneous** (primary) | cooling of magma/lava | granite, basalt, batholiths |
| **Sedimentary** | layers of sediment; **fossils** | limestone, sandstone, shale, coal |
| **Metamorphic** | heat + pressure | limestone → **marble**, shale → **slate**, sandstone → quartzite, granite → gneiss; phyllite, schist |
Not rocks: **barchan** (crescent sand dune), **moraine** (glacial deposit).

## 5. Plates, mountains, earthquakes and volcanoes
- **Continental drift** – Alfred **Wegener** (1912): **Pangaea** + Panthalassa. Plate tectonics (1960s).
- **Himalayas** – Indian plate colliding with the Eurasian plate (young fold mountains).
- Earthquakes and volcanoes occur mainly along **plate boundaries**; the **Pacific 'Ring of Fire'**. Earthquakes **cannot be predicted** precisely. Measured on the **Richter / moment-magnitude** scale with a seismograph.
- Highest peaks of continents: **Everest** (Asia), **Kilimanjaro** (Africa), **Aconcagua** (S. America), **Denali/McKinley** (N. America), **Elbrus** (Europe), **Vinson** (Antarctica), **Kosciuszko** (Australia mainland).

## 6. Landforms
- Rivers: V-shaped valleys, gorges, waterfalls, meanders, ox-bow lakes, deltas. Glaciers: U-shaped valleys, cirques, moraines. Wind: sand dunes (barchans), mushroom rocks. Sea: cliffs, sea arches, beaches.
- Weathering (breaking in place) vs erosion (removal and transport).
- Plateaus: Deccan (basalt, Deccan Traps), Tibetan (highest). Continental **shelf** – shallow, richest **fishing grounds**; then slope, abyssal plain, trenches (**Mariana – Challenger Deep ~11 km**).

## 7. Continents and oceans
- Continents by area: **Asia > Africa > North America > South America > Antarctica > Europe > Australia**.
- Oceans: **Pacific** (largest, deepest) > Atlantic > Indian > Southern > Arctic (smallest).

## 8. Atmosphere and weather
- Composition: **nitrogen 78%**, oxygen 21%, argon 0.93%, CO₂ ~0.04%.
- Layers upward: **troposphere** (weather; temperature falls ~6.5 °C/km; 8 km at poles, 18 km at Equator) → **stratosphere** (**ozone layer**, jets fly) → **mesosphere** (**coldest**, meteors burn) → **thermosphere/ionosphere** (radio waves, auroras) → **exosphere**.
- Good ozone = stratosphere; **bad ozone = troposphere** (smog). Ozone hole – mainly over **Antarctica**.
- **ITCZ** – Inter-Tropical Convergence Zone, the equatorial low-pressure belt where trade winds meet.
- Tropical cyclone names: **cyclones** (Indian Ocean), **typhoons** (W. Pacific/Philippines/China), **hurricanes** (Atlantic/Caribbean/N. America), **willy-willies** (Australia).
- Isolines: isotherm (temperature), **isobar** (pressure), **isohyet** (rainfall), **isohel** (sunshine), **isoneph** (cloud), isobath (depth), contour (height).

## 9. People (basics – details in GK-11)
- World population passed **8 billion** on 15 Nov 2022 (UN); India is the most populous country (UN estimate, 2023).
- Census of India every 10 years; the next (Census 2027) has reference date 1 March 2027 (1 Oct 2026 for snow-bound areas).

## 10. Traps
- Mesosphere (not thermosphere) is the **coldest** layer.
- Oceanic crust = **SIMA**, continental = **SIAL**.
- IST meridian is **82½° E**, not 80° or 90°.
- **Equinox** = equal day and night; **solstice** = longest/shortest day.
"""}],
}
