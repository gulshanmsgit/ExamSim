"""Previous-year paper · GTTC 2024 Competitive Exam · Officer Gr-II / Assistant Gr-II · Paper-2 · Kannada, English & Computer
Knowledge · version A1 · 100 Q (Kannada Q1–35, English Q36–70, Computer Q71–100).
Source: KEA question-paper archive (p1_2024_knd_eng_com.pdf, URL in tools/pyq_manifest.tsv; transcribed from the page images).
All three sections are typed up: KANNADA Q1–35 (added 19 Oct 2026 from page images p04–p07, owner's request; explanations
in Kannada by ExamSim), ENGLISH Q36–70 and COMPUTER Q71–100.
Options (1)–(4) are A–D in the printed order. Q86's decoder figure is described in words.
Answers: KEA's key for GTTC 2024 Officer Gr-II & Assistant Gr-II Paper-II (KEC) (sources/pyq/keys/final_gttc_kec.pdf, version A1,
read from the key image – the earlier text parse was wrong; the image key matches this A1 booklet).
Note: Q73 prints the prefix as 182.144.100.0/26 but the options as 182.144.10.x; the key's answer is the .62 address."""

SRC = "GTTC 2024 Officer/Asst Gr-III KEC · Q{}"
KEY = " (Official answer: KEA final key, GTTC 2024.)"

Q = {
1: ('ವ್ಯಾಪಾರಿ, ವಿದ್ವಾಂಸ, ರೋಗಿ, ಯೋಗಿ ________ ಕ್ಕೆ ಉದಾಹರಣೆ', ['ರೂಢನಾಮ', 'ಅನ್ವರ್ಥ ನಾಮ', 'ಅಂಕಿತ ನಾಮ', 'ಯಾವುದೂ ಅಲ್ಲ'], 1, 'ಗುಣ/ಕೆಲಸಕ್ಕೆ ತಕ್ಕಂತೆ ಬಂದ ಹೆಸರುಗಳು – ಅನ್ವರ್ಥ ನಾಮ.'),
2: ('ಒಕ್ಕಲಿಗ, ಹಾವಾಡಿಗ, ಮೋಸಗಾರ, ಮಾಲೆಗಾರ ಇವು ________', ['ತದ್ಧಿತಾಂತಗಳು', 'ಸಮಾಸಗಳು', 'ಕೃದಂತಗಳು', 'ಯಾವುದೂ ಅಲ್ಲ'], 0, 'ನಾಮಪದಗಳಿಗೆ ಇಗ, ಗಾರ ಮುಂತಾದ ತದ್ಧಿತ ಪ್ರತ್ಯಯ ಸೇರಿದ ತದ್ಧಿತಾಂತ ನಾಮಗಳು.'),
3: ('೧೯೬೩ ನ್ನು ಅಕ್ಷರ ರೂಪದಲ್ಲಿ ಬರೆಯಿರಿ:', ['ಒಂದು ಸಾವಿರದ ಆರುನೂರ ತೊಂಬತ್ತ್ಮೂರು', 'ಒಂದು ಸಾವಿರದ ಒಂಬೈನೂರ ಅರವತ್ತ್ಮೂರು', 'ಮೂರು ಸಾವಿರದ ಆರುನೂರ ತೊಂಬತ್ತ್ಮೂರು', 'ಮೂರು ಸಾವಿರದ ಒಂಬೈನೂರ ಅರವತ್ತ್ಮೂರು'], 1, '೧೯೬೩ = 1963 = ಒಂದು ಸಾವಿರದ ಒಂಬೈನೂರ ಅರವತ್ತಮೂರು.'),
4: ('ಛಂದೋಂಬುಧಿ ಕೃತಿಯ ಕರ್ತೃ ________', ['1 ನೇ ನಾಗವರ್ಮ', '2 ನೇ ನಾಗವರ್ಮ', '1 ನೇ ನಾಗಚಂದ್ರ', '2 ನೇ ನಾಗಚಂದ್ರ'], 0, 'ಕನ್ನಡದ ಮೊದಲ ಛಂದೋಗ್ರಂಥ ಛಂದೋಂಬುಧಿ – ಒಂದನೇ ನಾಗವರ್ಮ.'),
5: ('ಸರಿಯಾದ ಆಯ್ಕೆಯನ್ನು ಗುರುತಿಸಿ:', ['ಊರಲ್ಲಿ – ಆಗಮಸಂಧಿ', 'ಬಾಯ್ದೆರೆ – ಆದೇಶ ಸಂಧಿ', 'ಕೈಯನ್ನು – ಲೋಪಸಂಧಿ', 'ದೇವರಿಂದ – ವಕಾರಾಗಮ ಸಂಧಿ'], 1, 'ಬಾಯ್ + ತೆರೆ = ಬಾಯ್ದೆರೆ (ತ → ದ ಆದೇಶ). ಊರಲ್ಲಿ ಲೋಪ, ಕೈಯನ್ನು ಯಕಾರಾಗಮ, ದೇವರಿಂದ ಲೋಪ.'),
6: ('ಗಮಕ ಸಮಾಸವು ________ದ ಒಂದು ಪ್ರಭೇದವಾಗಿದೆ.', ['ತತ್ಪುರುಷ ಸಮಾಸ', 'ಕರ್ಮಧಾರಯ ಸಮಾಸ', 'ದ್ವಿಗು ಸಮಾಸ', 'ಕ್ರಿಯಾ ಸಮಾಸ'], 1, 'ಗಮಕ ಸಮಾಸ (ಉದಾ: ಆ ಮನೆ) ಕರ್ಮಧಾರಯದ ಒಂದು ಬಗೆ.'),
7: ('ಭಿಕ್ಷುಕರು ಮನೆಮನೆಗಳನ್ನು ತಿರುಗಿ ಭಿಕ್ಷೆ ಬೇಡಿದರು. ಈ ವಾಕ್ಯದಲ್ಲಿ ಅಡಿಗೆರೆ ಎಳೆದ ಪದದ ವಿಶೇಷತೆಯನ್ನು ಗುರುತಿಸಿ: (ಅಡಿಗೆರೆ: ಮನೆಮನೆಗಳನ್ನು)', ['ಜೋಡು ನುಡಿ', 'ನಾಣ್ನುಡಿ', 'ದ್ವಿರುಕ್ತಿ', 'ಅನುಕರಣಾವ್ಯಯ'], 2, 'ಒಂದೇ ಪದ ಎರಡು ಬಾರಿ (ಮನೆ ಮನೆ) – ದ್ವಿರುಕ್ತಿ.'),
8: ('ಉದ್ದಂಡ ಷಟ್ಪದಿಯಲ್ಲಿ ರಚನೆಯಾಗಿರುವ ರಾಘವಾಂಕನ ಕಾವ್ಯ:', ['ವೀರೇಶ ಚರಿತೆ', 'ಸೋಮನಾಥ ಚಾರಿತ್ರ', 'ಸಿದ್ಧರಾಮ ಚಾರಿತ್ರ', 'ಶರಭ ಚಾರಿತ್ರ'], 0, 'ರಾಘವಾಂಕನ ವೀರೇಶ ಚರಿತೆ ಉದ್ದಂಡ ಷಟ್ಪದಿಯಲ್ಲಿದೆ.'),
9: ('ಹೊಂದಿಸಿ ಬರೆಯಿರಿ:\na) ತ್ರಿಪದಿ\nb) ಶರ್ಕರಾ\nc) ಅಕ್ಷರ\nd) ಕಾವ್ಯ\ni) ಕಬ್ಬ\nii) ಅಕ್ಕರ\niii) ಸಕ್ಕರೆ\niv) ತಿವದಿ', ['a - iv, b - iii, c - ii, d - i', 'a - ii, b - i, c - iv, d - iii', 'a - iii, b - iv, c - i, d - ii', 'a - i, b - ii, c - iii, d - iv'], 0, 'ತತ್ಸಮ–ತದ್ಭವ: ತ್ರಿಪದಿ–ತಿವದಿ, ಶರ್ಕರಾ–ಸಕ್ಕರೆ, ಅಕ್ಷರ–ಅಕ್ಕರ, ಕಾವ್ಯ–ಕಬ್ಬ.'),
10: ('ಭೂಮಿ, ಬಾನು, ಬೋನ, ಬಾಯಿ – ಈ ಶಬ್ದಗಳಲ್ಲಿ ಗುಂಪಿಗೆ ಸೇರದ ಪದ ಆರಿಸಿ:', ['ಭೂಮಿ', 'ಬಾನು', 'ಬೋನ', 'ಬಾಯಿ'], 0, 'ಭೂಮಿ ತತ್ಸಮ (ಸಂಸ್ಕೃತ) ಪದ; ಉಳಿದವು ಕನ್ನಡ ಪದಗಳು (KEA ಅಂತಿಮ ಕೀ).'),
11: ('ಒಂದು ಸಾವಿರದ ಒಂಬೈನೂರ ಎಂಬತ್ತ್ಮೂರು ಇದನ್ನು ಕನ್ನಡ ಅಂಕಿಗಳಲ್ಲಿ ಬರೆಯಿರಿ:', ['೧೬೮೨', '೧೯೩೩', '೧೯೮೩', '೧೬೮೩'], 2, '1983 = ೧೯೮೩.'),
12: ('“ಪುರದ ಪುಣ್ಯಂ ಪುರುಷ ರೂಪಿಂದೆ ಪೋಗುತಿದೆ, ಪರಿಜನದ ಭಾಗ್ಯವಡವಿಗೆ ನಡೆಯುತಿದೆ” ಇಲ್ಲಿನ ಅಲಂಕಾರ ಗುರುತಿಸಿ:', ['ಉಪಮಾಲಂಕಾರ', 'ರೂಪಕಾಲಂಕಾರ', 'ಉತ್ಪ್ರೇಕ್ಷಾಲಂಕಾರ', 'ದೀಪಕಾಲಂಕಾರ'], 1, 'ರಾಮನನ್ನೇ ಪುರದ ಪುಣ್ಯ ಎಂದು ಅಭೇದವಾಗಿ ಹೇಳಿರುವುದರಿಂದ ರೂಪಕಾಲಂಕಾರ (KEA ಕೀ).'),
13: ('ಅವನು ಆನೆಯಷ್ಟು ದಪ್ಪಗಿದ್ದಾನೆ. ಅಡಿಗೆರೆ ಎಳೆದ ಶಬ್ದದ ವಿಶೇಷತೆ ತಿಳಿಸಿ. (ಅಡಿಗೆರೆ: ಆನೆಯಷ್ಟು)', ['ಗುಣವಾಚಕ', 'ಸಂಖ್ಯಾವಾಚಕ', 'ಸಂಖ್ಯೆಯ ವಾಚಕ', 'ಪರಿಮಾಣವಾಚಕ'], 3, 'ಅಷ್ಟು/ಇಷ್ಟು – ಗಾತ್ರ, ಅಳತೆ ತಿಳಿಸುವ ಪರಿಮಾಣವಾಚಕ.'),
14: ("'ಹಂಸ' ಪದದ ತದ್ಭವ ರೂಪ ________", ['ಕೊಕ್ಕರೆ', 'ಅಂಚೆ', 'ಬಾತುಕೋಳಿ', 'ಬೆಳ್ಳಕ್ಕಿ'], 1, 'ಹಂಸ → ಅಂಚೆ.'),
15: ("ಗಾಣ + ಇಗ = ಗಾಣಿಗ ಇಲ್ಲಿ 'ಇಗ' ಎಂಬುದು:", ['ಅವ್ಯಯ', 'ತದ್ಧಿತ', 'ಕೃದಂತ', 'ನಾಮಪದ'], 0, "KEA ಅಂತಿಮ ಕೀ ಉತ್ತರ (1) ಅವ್ಯಯ. ಗಮನಿಸಿ: ವ್ಯಾಕರಣ ಪುಸ್ತಕಗಳಲ್ಲಿ 'ಇಗ' ತದ್ಧಿತ ಪ್ರತ್ಯಯ ಎಂದು ಹೇಳಲಾಗುತ್ತದೆ."),
16: ('ಸಾಬೂನು ________ ಭಾಷೆಯಿಂದ ಬಂದ ಶಬ್ದ', ['ಹಿಂದೂಸ್ತಾನಿ', 'ಸಂಸ್ಕೃತ', 'ಪೋರ್ಚುಗೀಸ್', 'ಹಿಂದಿ'], 2, 'ಸಾಬೂನು ಪೋರ್ಚುಗೀಸ್ ಮೂಲದ ಅನ್ಯದೇಶ್ಯ ಪದ.'),
17: ('ವ್ಯಂಜನಗಳಿಗೆ ಸ್ವರಗಳು ಸೇರಿ ________ ಎನಿಸುವುದು', ['ಸಂಧ್ಯಕ್ಷರ', 'ಯೋಗವಾಹಗಳು', 'ಗುಣಿತಾಕ್ಷರ', 'ಅವರ್ಗೀಯ ವ್ಯಂಜನ'], 2, 'ಕ್ + ಅ = ಕ, ಕ್ + ಆ = ಕಾ … – ಗುಣಿತಾಕ್ಷರಗಳು.'),
18: ('ಗುಂಪಿಗೆ ಸೇರದ ಪದ ಆರಿಸಿ:', ['ಅಕ್ಷರ', 'ಜ್ಞಾನ', 'ವಿಜ್ಞಾನ', 'ಅಕ್ಕ'], 3, 'ಅಕ್ಷರ, ಜ್ಞಾನ, ವಿಜ್ಞಾನ ಸಂಸ್ಕೃತ (ಕ್ಷ/ಜ್ಞ ಇರುವ) ಪದಗಳು; ಅಕ್ಕ ಕನ್ನಡ ಪದ.'),
19: ('“ಕನ್ನಡ ಮಧ್ಯಮ ವ್ಯಾಕರಣ” ಕೃತಿಯ ಕರ್ತೃ', ['ಕೇಶಿರಾಜ', 'ತೀ.ನಂ.ಶ್ರೀಕಂಠಯ್ಯ', 'ಬಿ.ಎಂ. ಶ್ರೀಕಂಠಯ್ಯ', 'ಎಚ್. ತಿಪ್ಪೇರುದ್ರಸ್ವಾಮಿ'], 1, 'ಕನ್ನಡ ಮಧ್ಯಮ ವ್ಯಾಕರಣ – ತೀ.ನಂ. ಶ್ರೀಕಂಠಯ್ಯ (KEA ಕೀ).'),
20: ("'ಹಣ್ಣು ರಾಮನಿಂದ ತಿನ್ನಲ್ಪಟ್ಟಿತು' ಈ ವಾಕ್ಯವು ________ ಪ್ರಯೋಗಕ್ಕೆ ಉದಾಹರಣೆ:", ['ಕರ್ತರಿ', 'ಕರ್ಮಣಿ', 'ವಿಭಕ್ತಿ ಪಲ್ಲಟ', 'ಮೇಲಿನ ಯಾವುದೂ ಅಲ್ಲ'], 1, 'ಕರ್ಮ (ಹಣ್ಣು) ಪ್ರಧಾನವಾಗಿ, ಕರ್ತೃವಿಗೆ ತೃತೀಯಾ ವಿಭಕ್ತಿ – ಕರ್ಮಣಿ ಪ್ರಯೋಗ.'),
21: ('ಅತ್ಯಂತ, ಮನ್ವಂತರ, ಪಿತ್ರಾರ್ಜಿತ ಈ ಶಬ್ದಗಳು ________ ಗೆ ಉದಾಹರಣೆ:', ['ಗುಣ ಸಂಧಿ', 'ವೃದ್ಧಿ ಸಂಧಿ', 'ಯಣ್ ಸಂಧಿ', 'ಸವರ್ಣದೀರ್ಘ ಸಂಧಿ'], 2, 'ಅತಿ+ಅಂತ, ಮನು+ಅಂತರ, ಪಿತೃ+ಆರ್ಜಿತ – ಇ/ಉ/ಋ ಗಳಿಗೆ ಯ್/ವ್/ರ್ ಆದೇಶ – ಯಣ್ ಸಂಧಿ.'),
22: ('ತಪ್ಪಾದ ಆಯ್ಕೆಯನ್ನು ಗುರುತಿಸಿ:', ['ಉರಿಯ ನಾಲಗೆ – ಕೀರ್ತಿನಾಥ ಕುರ್ತಕೋಟಿ', 'ಭುವನದ ಭಾಗ್ಯ – ಜಿ.ಎಸ್. ಅಮೂರ', 'ಹೊಸತು ಹೊಸತು – ಚಿದಾನಂದ ಮೂರ್ತಿ', 'ಕಾವ್ಯಾರ್ಥ ಚಿಂತನ – ತೀ.ನಂ.ಶ್ರೀ'], 3, 'ಕಾವ್ಯಾರ್ಥ ಚಿಂತನ ಜಿ.ಎಸ್. ಶಿವರುದ್ರಪ್ಪ ಅವರ ಕೃತಿ; ತೀ.ನಂ.ಶ್ರೀ ಅವರದ್ದು ಭಾರತೀಯ ಕಾವ್ಯಮೀಮಾಂಸೆ.'),
23: ('ಕೇಶಿರಾಜನ ಪ್ರಕಾರ ಕನ್ನಡದಲ್ಲಿ ಶುದ್ಧಗೆಗಳೆಂದರೆ ________ ಅಕ್ಷರಗಳು', ['49', '47', '50', '52'], 1, 'ಶಬ್ದಮಣಿದರ್ಪಣದಲ್ಲಿ ಕೇಶಿರಾಜ 47 ಶುದ್ಧಾಕ್ಷರಗಳನ್ನು ಹೇಳಿದ್ದಾನೆ.'),
24: ("'ಪ್ರಧಾನ' ಶಬ್ದದ ವಿರುದ್ಧ ಪದ ________", ['ಸಮಾಧಾನ', 'ಸಾವಧಾನ', 'ಗೌಣ', 'ಪ್ರಮಾಣ'], 2, 'ಪ್ರಧಾನ × ಗೌಣ (ಮುಖ್ಯವಲ್ಲದ್ದು).'),
25: ("'ಸೂರ್ಯ' ಶಬ್ದದ ಸಮಾನಾರ್ಥಕ ಶಬ್ದಗಳಲ್ಲಿ ತಪ್ಪಾದುದನ್ನು ಆರಿಸಿ:", ['ಬಾನು', 'ಭಾನು', 'ಭಾಸ್ಕರ', 'ರವಿ'], 0, 'ಬಾನು = ಆಕಾಶ; ಭಾನು = ಸೂರ್ಯ.'),
26: ("'ಕವಿ' ಪದದ ಸ್ತ್ರೀಲಿಂಗ ರೂಪ:", ['ಕವಯಿತ್ರಿ', 'ಕವಿಯತ್ರಿ', 'ಕವಯತ್ರಿ', 'ಕವಿಯಿತ್ರಿ'], 0, 'ಸರಿಯಾದ ರೂಪ ಕವಯಿತ್ರಿ.'),
27: ('ವಿಶ್ವಸಾಹಿತ್ಯಕ್ಕೆ ಕನ್ನಡವು ಸಲ್ಲಿಸಿರುವ ಕಾಣಿಕೆ:', ['ಚಂಪೂ ಸಾಹಿತ್ಯ', 'ವಚನ ಸಾಹಿತ್ಯ', 'ಷಟ್ಪದಿ ಸಾಹಿತ್ಯ', 'ಸಾಂಗತ್ಯ'], 1, '12ನೇ ಶತಮಾನದ ವಚನ ಸಾಹಿತ್ಯ ಕನ್ನಡದ ವಿಶಿಷ್ಟ ಕೊಡುಗೆ.'),
28: ('“ದಯಾನಂದರು ವಿದ್ಯಾಭ್ಯಾಸವನ್ನು ಮುಗಿಸಿ ಗುರುವಿನ ಆಶೀರ್ವಾದ ಪಡೆದು, ವೈದಿಕ ಜ್ಞಾನ ಪ್ರಸಾರಕ್ಕಾಗಿ ದೇಶ ಸಂಚಾರ ಹೊರಟರು” ________ ವಾಕ್ಯಕ್ಕೆ ಉದಾಹರಣೆ:', ['ಸ್ವತಂತ್ರ ವಾಕ್ಯ', 'ಸಮ್ಮಿಶ್ರ ವಾಕ್ಯ', 'ಸಂಯೋಜಿತ ವಾಕ್ಯ', 'ಮೇಲಿನ ಯಾವುದೂ ಅಲ್ಲ'], 1, 'KEA ಅಂತಿಮ ಕೀ ಉತ್ತರ: ಸಮ್ಮಿಶ್ರ ವಾಕ್ಯ (ಮುಗಿಸಿ, ಪಡೆದು ಎಂಬ ಅಪೂರ್ಣ ಕ್ರಿಯೆಗಳು ಪ್ರಧಾನ ವಾಕ್ಯಕ್ಕೆ ಸೇರಿವೆ).'),
29: ('“ಜಗನ್ನಾಥ ವಿಜಯ” ಕೃತಿಯನ್ನು ಬರೆದವರು:', ['ಅಗ್ಗಳ', 'ರುದ್ರಭಟ್ಟ', 'ನೇಮಿಚಂದ್ರ', 'ಬಂಧುವರ್ಮ'], 1, 'ಜಗನ್ನಾಥ ವಿಜಯ – ರುದ್ರಭಟ್ಟ.'),
30: ('“ಷಟ್ಪದಿಯ ಬ್ರಹ್ಮ” ಎಂದು ಬಿರುದಾಂಕಿತನಾದ ಕವಿ:', ['ನಾಗಚಂದ್ರ', 'ರತ್ನಾಕರವರ್ಣಿ', 'ಹರಿಹರ', 'ರಾಘವಾಂಕ'], 3, 'ರಾಘವಾಂಕ – ಷಟ್ಪದಿಯ ಬ್ರಹ್ಮ.'),
31: ('“ಎಂಜಲು ಕೈಯಲ್ಲಿ ಕಾಗೆ ಓಡಿಸದವ” ಎಂದರೆ ________', ['ಅಹಿಂಸಾ ಪ್ರವೃತ್ತಿಯುಳ್ಳವ', 'ಶಾಸ್ತ್ರಜ್ಞ', 'ಸೋಮಾರಿ', 'ಜಿಪುಣ'], 3, 'ಎಂಜಲು ಕೈಯಿಂದ ಕಾಗೆಯನ್ನೂ ಓಡಿಸದವನು (ಅನ್ನದ ಅಗುಳು ಬಿದ್ದೀತೆಂದು) – ಜಿಪುಣ.'),
32: ('ಕಂದ ಪದ್ಯದಲ್ಲಿರುವ ಒಟ್ಟು ಮಾತ್ರಾ ಸಂಖ್ಯೆ', ['12', '32', '64', '16'], 2, 'ಕಂದ ಪದ್ಯ: 4 ಸಾಲು, 12+20+12+20 = 64 ಮಾತ್ರೆ.'),
33: ('“ಈ ಹೊಳೆಯಲ್ಲಿ ಮೀನುಗಳು ಹೆಚ್ಚು” ಅಡಿಗೆರೆ ಎಳೆದ ಶಬ್ದದಲ್ಲಿನ ವಿಭಕ್ತಿ ಪ್ರತ್ಯಯ ಗುರುತಿಸಿ: (ಅಡಿಗೆರೆ: ಹೊಳೆಯಲ್ಲಿ)', ['ದ್ವಿತೀಯ', 'ಸಪ್ತಮಿ', 'ಷಷ್ಠಿ', 'ತೃತೀಯ'], 1, 'ಅಲ್ಲಿ – ಸಪ್ತಮೀ ವಿಭಕ್ತಿ (ಅಧಿಕರಣ).'),
34: ('“ಊರು ಉಪಕಾರ ಅರಿಯದು, ಹೆಣ ಶೃಂಗಾರ ಅರಿಯದು” ಈ ವಾಕ್ಯದಲ್ಲಿರುವ ಅಲಂಕಾರ ________.', ['ಅರ್ಥಾಂತರನ್ಯಾಸಾಲಂಕಾರ', 'ರೂಪಕಾಲಂಕಾರ', 'ದೃಷ್ಟಾಂತಾಲಂಕಾರ', 'ಉತ್ಪ್ರೇಕ್ಷಾಲಂಕಾರ'], 2, 'ಒಂದು ಮಾತಿಗೆ ಸಮಾನವಾದ ಇನ್ನೊಂದು ಉದಾಹರಣೆ ಕೊಡುವುದು – ದೃಷ್ಟಾಂತಾಲಂಕಾರ.'),
35: ("'ಆ ಕರಡಿ ತನ್ನ ಪಾಡಿಗೆ ತಾನು ಹೊರಟು ಹೋಯಿತು' ಈ ವಾಕ್ಯದಲ್ಲಿರುವ 'ತಾನು' ಎಂಬುದು:", ['ಪುರುಷವಾಚಕ ಸರ್ವನಾಮ', 'ಪ್ರಶ್ನ ವಾಚಕ ಸರ್ವನಾಮ', 'ನಿರ್ದಿಷ್ಟವಾಚಕ ಸರ್ವನಾಮ', 'ಆತ್ಮಾರ್ಥಕ ಸರ್ವನಾಮ'], 3, 'ತಾನು, ತಾವು, ತನ್ನ – ಆತ್ಮಾರ್ಥಕ ಸರ್ವನಾಮ.'),
36: ("Give one word substitution for the following:\nThe system of single marriage", ["Monogamy", "Monolith", "Monocle", "Monochrome"], 0, "Mono = one, gamy = marriage."),
37: ("A person who believes that people cannot know whether God exists or not is called ____\nFill the blank with suitable word.", ["Theist", "Atheist", "Agnostic", "Nomad"], 2, "An atheist denies God; an agnostic is unsure."),
38: ("Fill in the blank using the correctly-spelt word.\nRanbir ____ his parents' dreams.", ["fullfilled", "fulfilled", "fullfiled", "fulfiled"], 1, "Fulfilled."),
39: ("Choose the option which is opposite in meaning of the underlined word.\nShe is known for her nefarious ways of dealing with people. (underlined: nefarious)", ["positive", "evil", "neutral", "kind"], 3, "Nefarious = wicked."),
40: ("Find out the part of the sentence which contains error.\nLong life is desirable / if one be healthy / and has some money to spare / No error", ["Long life is desirable", "if one be healthy", "and has some money to spare", "No error"], 1, "'if one is healthy' to match 'has'."),
41: ("Out of the four alternatives, choose the one which best expresses the meaning of the given word, which is underlined.\nThe superstar was known for his laconic answers. (underlined: laconic)", ["descriptive", "scandalous", "brief", "copious"], 2, "Laconic = using few words."),
42: ("The following question has words designated as A B C D E and F which are jumbled up and need to be rearranged to form a proper sentence. Find out the correct sequence of the words and select the correct option as the answer.\nA: always   B: coffee\nC: to   D: like\nE: have   F: you", ["FADCEB", "ABDEFC", "DEFABC", "FCEBAD"], 0, "You always like to have coffee."),
43: ("Choose the right option to fill in the blanks.\nAs the students fail to ____ continuously they lose the ____ of the art.", ["practice, practise", "practise, practise", "practice, practice", "practise, practice"], 3, "Verb practise, noun practice."),
44: ("Choose the right option to fill in the blanks.\nThe duty of the ____ of ministers is to offer ____ to the king.", ["counsel, counsel", "council, counsel", "counsel, council", "council, council"], 1, "Council = body; counsel = advice."),
45: ("Find out the error part from the given options:\nAfter many attempts (a) / he gave out (b) / the idea of earning money (c) / through gambling (d).", ["a", "b", "c", "d"], 1, "He gave up the idea."),
46: ("Fill the correct option that agrees to the first part of the sentence.\nWhen I went there ____", ["I found that my sister was studying", "I find that my sister is studying", "I found that my sister is studying", "I find that my sister was studying"], 0, "Sequence of tenses."),
47: ("Fill in the blanks with suitable articles.\nIt was raining heavily. All the students wanted to go home early. Hence, they decided to send ____ student to ____ headmaster to seek permission.", ["a, the", "a, a", "the, a", "the, the"], 0, "Any one student; the particular headmaster."),
48: ("Identify the correct form of tense in the following sentence:\nMy brother ____ tomorrow.", ["arrive", "arrives", "arrived", "has arrived"], 1, "Simple present for a scheduled future event."),
49: ("Identify the correct form of tense in the following sentence:\nI am going to ____ a holiday soon.", ["got", "getting", "get", "gets"], 2, "going to + base verb."),
50: ("Fill in the blanks with correct articles in the following sentences:\nSmitha brought a lot of luggage with her. She got down. She left ____ luggage at ____ railway station.", ["the, a", "a, the", "the, the", "a, a"], 2, "Specific luggage and station."),
51: ("Fill in the blanks with correct articles in the following sentence:\nSuman is going to buy ____ hat and ____ umbrella.", ["an, a", "a, an", "the, a", "a, the"], 1, "an before a vowel sound."),
52: ("Choose the most suitable alternative to make the sentence logical.\nThe football match was ____ live across the nation.", ["broadcasted", "broadcasting", "broadcast", "broadcost"], 2, "Past participle is broadcast."),
53: ("Choose the suitable interjection for the following sentence.\n____!, I didn't expect to see you here.", ["Oh", "Alas", "Bravo", "Ouch"], 0, "Surprise."),
54: ("Choose the most suitable alternative to make the sentence logical.\nHe ____ goes to the market.", ["almost", "enough", "rare", "seldom"], 3, "Adverb of frequency."),
55: ("Read the sentence and choose the most appropriate meaning for the underlined idioms and phrases in the sentence.\nThe two parties decided to bury the hatchet and keep their relations healthy.", ["hide the hatchet", "keep on fighting", "make peace", "keep mum"], 2, "Bury the hatchet = make peace."),
56: ("Choose the mis-spelt word:", ["Auxilliary", "Attainable", "Auspicious", "Available"], 0, "Auxiliary."),
57: ("Choose the most appropriate answer from the alternatives given below to complete the word by adding the prefix.\nThe clerk was dismissed from the job because he was ____ sincere.", ["un-", "in-", "dis-", "less-"], 1, "Insincere."),
58: ("Choose the most appropriate answer from the alternatives given below to complete the word by adding the suffix.\nThe postpone____ of the exams was announced this morning.", ["-ment", "-ed", "-ness", "-ous"], 0, "Postponement."),
59: ("Choose the right conjunction for the following sentence:\nI hurt myself ____ I was playing cricket.", ["how", "Whenever", "while", "Whatever"], 2, "While."),
60: ("Choose the right conjunction for the following sentence.\nWait here ____ I get back.", ["still", "until", "when", "as soon as"], 1, "Until."),
61: ("Choose the most suitable alternative to make the sentence logical.\nRamesh has been working in the same company ____ 2020.", ["since", "from", "before", "afterwards"], 0, "Point of time with perfect continuous."),
62: ("Choose the appropriate word that can be substituted for the given words.\nA woman who is a former student of a school or college.", ["Alumna", "Alumni", "Alumnus", "Almanac"], 0, "Alumnus is masculine; alumni plural."),
63: ("Choose the option which is opposite of the underlined word in the following sentence.\nThomas tried a lot to come out of his knotty situation. (underlined: knotty)", ["Complicated", "Simple", "Difficult", "Onerous"], 1, "Knotty = complicated."),
64: ("Which of the following is a pair of words with opposite meaning?", ["nasty – offensive", "novice – experienced", "mettle – courage", "profuse – lavish"], 1, "The rest are synonyms."),
65: ("Compare the underlined part of each sentence with the expressions (1), (2), (3) and (4). Choose the expression which is an improvement upon the underlined part.\nOne of my friends are working in the largest factory of the city for five years. (underlined: are working)", ["was working", "have been working", "has been working", "were working"], 2, "'One' is singular; duration needs perfect continuous."),
66: ("In the following question, choose the word similar in meaning to the word given below:\nSimpleton", ["Fool", "Minimalist", "Simple", "Decorative"], 0, "A foolish person."),
67: ("My boss is known for his laxity in dealing with various issues.\nChoose the option which is synonymous with the underlined word. (underlined: laxity)", ["Careful", "Slack", "Strict", "Sturdy"], 1, "Laxity = slackness."),
68: ("Select the synonym of the word which is underlined.\nHe came all the way from Pakistan to pay homage to the departed soul. (underlined: homage)", ["humility", "tribute", "obedience", "allegiance"], 1, "Homage = tribute."),
69: ("The following question has words designated as A, B, C, D, E and F which are jumbled up and need to be rearranged to form a proper sentence. Find out the correct sequence of the words and select the correct option as the answer:\nA: know   B: passes\nC: they   D: will\nE: time   F: as", ["ACBDFE", "FEDCBA", "CABFED", "CDAFEB"], 3, "They will know as time passes."),
70: ("The following question contains a paragraph of six sentences. The first and sixth sentences given in the beginning and the end are numbered as (1) and (6) respectively. The four sentences are labelled as P, Q, R and S and jumbled up. Choose the correct combination of sequence.\n(1) Once upon a time a peasant boy fell in love with a princess. He went to the king and said, \"I want to marry the princess\".\nP. But, she did not want her father to know about the visit. She took the help of her friend who was the daughter of the jailor.\nQ. The king became very angry. He jailed the boy.\nR. One night both the princess and her friend, the jailor's daughter, visited the jail. She saw the boy hiding behind a pillar.\nS. The princess came to know about this. She wanted to see the boy out of curiosity.\n(6) She went near the pillar and had close look at him. He was handsome and was well-built. The princess thought, \"Ah! Nice looking young man!\"", ["PQRS", "SQPR", "RSQP", "QSPR"], 3, "Jailed, she learns, plans secretly, visits."),
71: ("In power point, which of the following file types can be used to export your presentation in order to preserve animations and Multimedia?", ["PDF", "HTML", "MP4", "GIF"], 2, "Export as video."),
72: ("The decimal equivalent of (−FACE)₁₆ hexadecimal number is:", ["64204", "−64204", "−64206", "64208"], 2, "FACE₁₆ = 64206."),
73: ("The last usable host address of prefix 182.144.100.0/26 is:\n(a) 182.144.10.255   (b) 182.144.10.62\n(c) 182.144.10.254   (d) 182.144.10.0", ["a only", "b only", "d only", "a and c only"], 1, "A /26 block has 64 addresses: .0 network, .63 broadcast, .62 last host (the paper mixes 100 and 10 in the third octet)."),
74: ("The total number of usable IP address in Class A IP addressing is:", ["16777216", "16777214", "4294967296", "256"], 1, "Per Class A network: 2²⁴ − 2."),
75: ("Find the ODD member out:", ["Asynchronous Transmission", "Synchronous Transmission", "Parallel Transmission", "Isochronous Transmission"], 2, "The others are serial timing modes."),
76: ("____ attacks occur when attacker continuously bombards with various protocol messages designed to consume system resources.", ["Identity theft", "Denial of service", "Man in the middle attack", "Virus attack"], 1, "DoS."),
77: ("Select the WRONG fullform:", ["Enhanced Data rates for Global Evolution (EDGE)", "Short Message Service (SMS)", "General Packet Radio Service (GPRS)", "Cisco Division Multiple Access (CDMA)"], 3, "Code Division Multiple Access."),
78: ("Which among the following is NOT the function of system software?", ["Device Management", "File Management", "Process Management", "Mail Management"], 3, "Mail is an application."),
79: ("A user has a sudden demand of resources such as compute, storage, networking and he does not want to maintain / manage these infrastructure.\nWhich cloud delivery model is suitable for him?", ["Infrastructure as a Service (IaaS)", "Software as a Service (SaaS)", "Platform as a Service (PaaS)", "On Premise"], 0, "On-demand infrastructure."),
80: ("The program which are permanent as hardware and stored in ROM is known as", ["Hardware", "Software", "Firmware", "Operating system"], 2, "Firmware."),
81: ("Which of the following registers holds the address of the next instruction to be executed?", ["Memory Buffer Register (MBR)", "Accumulator Register (AR)", "Memory Address Register (MAR)", "Program Counter Register (PCR)"], 3, "Program counter."),
82: ("Which of the following is an application software?", ["Linux", "Mac OS", "UNIX", "Graphics Software"], 3, "The others are operating systems."),
83: ("Who built India's first super computer PARAM 8000 in 1991?", ["Vijay K. Bhat", "Vijay P. Bhatkar", "A.P.J. Abdul Kalam", "Vijay P. Bhat"], 1, "C-DAC under Vijay Bhatkar."),
84: ("Macros means ____ in MS Excel.", ["Small add-on programs", "Programming language used to customize Ms Word", "Tool to use mail merge", "VBA Program used in MS Excel and can be called repetitively using VBA"], 3, "Recorded VBA routines."),
85: ("____ is a scientist who introduced \"stored program concept\" of modern digital computers.", ["Albert Einstein", "Dennis Ritchie", "Abacus", "Dr. John von Neumann"], 3, "Von Neumann architecture."),
86: ("[Figure: an address decoder for '9' – a 4-input AND gate whose inputs come from the address bits (LSB marked), with inverters on the 0 bits]\nThe output of AND Gate will be '1' if and only if the input is binary", ["0111", "1000", "1001", "1010"], 2, "9 = 1001."),
87: ("CRAY-XP, ETA-10 and Deep Blue computers are examples for:", ["Mainframe Computers", "Mini Computers", "Super Computers", "Micro Computers"], 2, "Supercomputers."),
88: ("____ is a networking device that amplify a weak signal so that the signal can travel over long distance without losing its original strength", ["HUBS", "Repeater", "Switches", "NIC"], 1, "Repeater."),
89: ("Expand RAID related to disk organization technique.", ["Related Array of Independent Disks", "Redundant Array of Independent Disks", "Removable Array of Independent Disks", "Remote Array of Independent Disks"], 1, "RAID."),
90: ("A relation schema R is in 2NF (2 Normal Form) if every ____ attribute 'A' in 'R' is fully functionally dependent on the primary key of R.", ["Prime attribute", "Non-Prime attribute", "Composite attribute", "None of the above"], 1, "Non-prime attributes."),
91: ("Delete operation in a Database can violate which of the following constraints?", ["Entity Integrity Constraint", "Referential Integrity Constraint", "NULL Constraint", "Domain Constraint"], 1, "Deleting a referenced row."),
92: ("Which of the following is NOT the desirable properties of the transactions in the database?", ["Atomicity", "Consistency", "Isolation", "Redundancy"], 3, "ACID."),
93: ("Match the following:\na) Optical fiber cable\nb) STP Cable\nc) UTP Cable\nd) Coaxial Cable\ni. RJ-45 Connector\nii. BNC Connector\niii. ST / SMA Connector\niv. D-Shell Connector", ["a – i, b – ii, c – iii, d – iv", "a – iii, b – iv, c – i, d – ii", "a – iv, b – iii, c – ii, d – i", "a – ii, b – iii, c – iv, d – i"], 1, "Connectors."),
94: ("What is the main purpose of the Windows Pre-installation Environment (WinPE)?\n(a) To boot a system with a graphical user interface.\n(b) To perform disk management tasks\n(c) To connect windows update servers\n(d) To provide a minimal OS environment for installation, recovery and troubleshooting", ["c and d only", "d only", "a only", "b only"], 1, "Minimal OS for setup and recovery."),
95: ("Which gate is used in the design of a NOT Gate when using NAND Gates only?", ["NAND Gate", "OR Gate", "AND Gate", "NOR Gate"], 0, "Tie the NAND inputs together."),
96: ("What is the maximum number of columns available in Excel 2016?", ["1024", "256", "16384", "4096"], 2, "A to XFD."),
97: ("Which command-line tool in Windows allows you to test the integrity of system files and repair missing or corrupted files?\n(a) Diskpart   (b) Ipconfig\n(c) CHKDSK   (d) SFC / scannow", ["a and c only", "d only", "c only", "d and b only"], 1, "System File Checker."),
98: ("In windows, which feature allows multiple virtual desktops to be used for better organisations of open applications and windows?", ["SPAN asset", "Task View", "Aero peek", "Control Panel"], 1, "Win + Tab."),
99: ("Which of the following is the first mechanical computer designed by Charles Babbage?", ["Analytical Engine", "Difference Engine", "Jacquard Loom", "Turing Machine"], 1, "Difference Engine (1822)."),
100: ("Which of these early computer programming languages was designed to run on the UNIVAC and is considered one of the first high-level programming languages?\n(a) LISP\n(b) Fortran\n(c) COBOL\n(d) C", ["c and b only", "b only", "d and a only", "a only"], 1, "KEA's key: Fortran."),
}


def sets():
    out = []
    for lo, hi in ((1, 35), (36, 60), (61, 85), (86, 100)):
        qs = [(q, o, a, e + KEY, SRC.format(n)) for n in sorted(Q) if lo <= n <= hi for q, o, a, e in [Q[n]]]
        out.append({"name": f"Q{lo}–{hi}" + (" (Kannada)" if lo == 1 else ""), "questions": qs, "keep_order": True})
    return out


TOPIC = "GTTC 2024 – Officer/Assistant Paper-2 (English & Computer)"
