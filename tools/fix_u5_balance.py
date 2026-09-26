"""One-off edit: vary assertion-reason answers in the DBMS concepts pack (were all A)."""
import re
from pathlib import Path
HERE = Path(__file__).parent
FN = "pack_p2_u5_01_concepts.py"
CHANGES = [
    (r"Assertion (A): The schema of a relation can remain the same while its state changes many times per second.",
     r"Assertion (A): The schema of a relation can remain the same while its state changes many times per second.\nReason (R): The schema is stored only inside application programs, not in the DBMS catalog.", 2,
     "A is true, but R is false: the schema (meta-data) is stored in the DBMS catalog. The real reason is that the schema is the intension and the state the extension."),
    (r"Assertion (A): SQL is called a declarative language.",
     r"Assertion (A): SQL is called a declarative language.\nReason (R): SQL has been standardised by ANSI and ISO.", 1,
     "Both are true, but standardisation does not explain why SQL is declarative; it is declarative because users state what they want and the DBMS decides how."),
    (r"Assertion (A): In a three-tier architecture, changing a business rule usually requires no change on client machines.",
     r"Assertion (A): In a three-tier architecture, business rules must be installed on every client machine.\nReason (R): In a three-tier architecture, business logic resides in the middle tier.", 3,
     "A is false: that describes fat clients in two-tier systems. R is true."),
]
s = (HERE / FN).read_text(encoding="utf-8")
for prefix, newq, ans, expl in CHANGES:
    pat = re.compile(r'\("' + re.escape(prefix) + r'[^"]*",\s*\n\s*AR, \d, "[^"]*"\),')
    found = list(pat.finditer(s))
    assert len(found) == 1, (prefix, len(found))
    m = found[0]
    s = s[:m.start()] + f'("{newq}",\n     AR, {ans}, "{expl}"),' + s[m.end():]
(HERE / FN).write_text(s, encoding="utf-8")
print("updated", len(CHANGES))
