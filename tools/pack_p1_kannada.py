"""Pack: Paper 1 · General Kannada (ಸಾಮಾನ್ಯ ಕನ್ನಡ), complete (all 17 syllabus topics × 20 questions)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from packlib import build_pack
import p1_kan_a, p1_kan_b, p1_kan_c, p1_kan_d

ORDER = [
    "ಕನ್ನಡ ವರ್ಣಮಾಲೆ",
    "ನಾಮಪದ ಮತ್ತು ಸರ್ವನಾಮ",
    "ಕ್ರಿಯಾಪದ",
    "ಲಿಂಗ, ವಚನ ಮತ್ತು ವಿಭಕ್ತಿ",
    "ಸಂಧಿಗಳು",
    "ಸಮಾಸಗಳು",
    "ಕೃದಂತ ಮತ್ತು ತದ್ಧಿತಾಂತ",
    "ದ್ವಿರುಕ್ತಿ, ಜೋಡುನುಡಿ, ನುಡಿಗಟ್ಟು, ಗಾದೆ",
    "ಅವ್ಯಯ",
    "ವಾಕ್ಯ ರಚನೆ",
    "ಲೇಖನ ಚಿಹ್ನೆಗಳು",
    "ಪದಗಳ ಅರ್ಥ ಮತ್ತು ಶುದ್ಧರೂಪ",
    "ತತ್ಸಮ-ತದ್ಭವ, ಅನ್ಯದೇಶ್ಯ",
    "ಗ್ರಾಮ್ಯ ಮತ್ತು ಗ್ರಾಂಥಿಕ ರೂಪಗಳು",
    "ಛಂದಸ್ಸು ಮತ್ತು ಅಲಂಕಾರ",
    "ಹಳಗನ್ನಡ ಸಾಹಿತ್ಯ",
    "ಹೊಸಗನ್ನಡ ಸಾಹಿತ್ಯ ಚರಿತ್ರೆ"
]

ALL = {
    **p1_kan_a.TOPICS_A,
    **p1_kan_b.TOPICS_B,
    **p1_kan_c.TOPICS_C,
    **p1_kan_d.TOPICS_D
}

assert list(ALL) == ORDER or set(ALL) == set(ORDER), set(ALL) ^ set(ORDER)

topics = []
for t in ORDER:
    sets = []
    for name, qs in ALL[t]:
        assert len(qs) == 20, f"{t} / {name}: {len(qs)} questions (expected 20)"
        tag = name.split(" · ", 1)[1] if " · " in name else name
        sets.append({"name": name, "tag": tag, "questions": qs})
    topics.append({"name": t, "sets": sets})

out_file = sys.argv[1] if len(sys.argv) > 1 else str(Path(__file__).resolve().parent.parent / "packs" / "p1-kannada-complete.json")

build_pack(
    out_file,
    "P1 · General Kannada (ಸಾಮಾನ್ಯ ಕನ್ನಡ — complete)",
    "All 17 syllabus topics for Karnataka GPSTR / CST / TET Paper 1: ವರ್ಣಮಾಲೆ, ಗುಣಿತಾಕ್ಷರ-ಸಂಯುಕ್ತಾಕ್ಷರ, ನಾಮಪದ-ಸರ್ವನಾಮ, ಕ್ರಿಯಾಪದ-ಕಾಲಗಳು, ಲಿಂಗ-ವಚನ-ವಿಭಕ್ತಿ, ಸಂಧಿಗಳು, ಸಮಾಸಗಳು, ಕೃದಂತ-ತದ್ಧಿತಾಂತ, ದ್ವಿರುಕ್ತಿ-ಜೋಡುನುಡಿ-ಗಾದೆಗಳು, ಅವ್ಯಯ, ವಾಕ್ಯರಚನೆ, ಲೇಖನ ಚಿಹ್ನೆಗಳು, ಅರ್ಥ-ಶುದ್ಧರೂಪ, ತತ್ಸಮ-ತದ್ಭವ, ಗ್ರಾಮ್ಯ-ಗ್ರಾಂಥಿಕ, ಛಂದಸ್ಸು-ಅಲಂಕಾರ, ಹಳಗನ್ನಡ ಸಾಹಿತ್ಯ, ಹೊಸಗನ್ನಡ ಸಾಹಿತ್ಯ ಚರಿತ್ರೆ (20 MCQs per set).",
    [{"name": "P1 · General Kannada (ಸಾಮಾನ್ಯ ಕನ್ನಡ)", "icon": "ಕ", "topics": topics}]
)
