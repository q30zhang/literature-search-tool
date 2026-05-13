from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
BIB_DIR = ROOT / "data_bibtex"
OUTPUT_DIR = ROOT / "literature_data"
OUTPUT_FILE = OUTPUT_DIR / "bib-files.json"


def main():
    bib_files = sorted(
        path.relative_to(ROOT).as_posix()
        for path in BIB_DIR.glob("*.bib")
        if path.is_file()
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(
        json.dumps({"bibFiles": bib_files}, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
