"""Pack: Paper 1 · General Kannada (ಸಾಮಾನ್ಯ ಕನ್ನಡ) — 10 High-Difficulty Mock Test Sets.
Each Mock Test contains 20 comprehensive Teacher Exam standard MCQs (Total: 200 MCQs).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from packlib import build_pack
import p1_kan_mock_1_to_5, p1_kan_mock_6_to_10

MOCKS = [
    ("ಮಾದರಿ ಪರೀಕ್ಷೆ 01 (Mock Test 01)", p1_kan_mock_1_to_5.MOCK_01),
    ("ಮಾದರಿ ಪರೀಕ್ಷೆ 02 (Mock Test 02)", p1_kan_mock_1_to_5.MOCK_02),
    ("ಮಾದರಿ ಪರೀಕ್ಷೆ 03 (Mock Test 03)", p1_kan_mock_1_to_5.MOCK_03),
    ("ಮಾದರಿ ಪರೀಕ್ಷೆ 04 (Mock Test 04)", p1_kan_mock_1_to_5.MOCK_04),
    ("ಮಾದರಿ ಪರೀಕ್ಷೆ 05 (Mock Test 05)", p1_kan_mock_1_to_5.MOCK_05),
    ("ಮಾದರಿ ಪರೀಕ್ಷೆ 06 (Mock Test 06)", p1_kan_mock_6_to_10.MOCK_06),
    ("ಮಾದರಿ ಪರೀಕ್ಷೆ 07 (Mock Test 07)", p1_kan_mock_6_to_10.MOCK_07),
    ("ಮಾದರಿ ಪರೀಕ್ಷೆ 08 (Mock Test 08)", p1_kan_mock_6_to_10.MOCK_08),
    ("ಮಾದರಿ ಪರೀಕ್ಷೆ 09 (Mock Test 09)", p1_kan_mock_6_to_10.MOCK_09),
    ("ಮಾದರಿ ಪರೀಕ್ಷೆ 10 (Mock Test 10)", p1_kan_mock_6_to_10.MOCK_10),
]

topics = []
for name, qs in MOCKS:
    assert len(qs) == 20, f"{name}: {len(qs)} questions (expected 20)"
    topics.append({
        "name": name,
        "sets": [{"name": f"Set 1 · {name}", "tag": "ಸಾಮಾನ್ಯ ಕನ್ನಡ ಮಾದರಿ ಪರೀಕ್ಷೆ", "questions": qs}]
    })

out_file = sys.argv[1] if len(sys.argv) > 1 else str(Path(__file__).resolve().parent.parent / "packs" / "p1-kannada-mocks.json")

build_pack(
    out_file,
    "P1 · General Kannada — 10 High-Difficulty Mock Tests (ಸಾಮಾನ್ಯ ಕನ್ನಡ ಸಮಗ್ರ ಮಾದರಿ ಪರೀಕ್ಷೆಗಳು)",
    "10 High-difficulty full mock tests (10 sets × 20 questions = 200 MCQs) for Karnataka GPSTR / KARTET / HSTR / CST Paper 1. Covers advanced grammar, Shabdamanidarpana rules, complex Sandhi & Samasa, Chandassu & Alankara, Halagannada & Hosagannada Sahitya, Jnanpith & Academy awardees, and Assertion-Reason questions.",
    [{"name": "P1 · General Kannada Mocks (ಸಾಮಾನ್ಯ ಕನ್ನಡ ಮಾದರಿ ಪರೀಕ್ಷೆಗಳು)", "icon": "📝", "topics": topics}]
)
