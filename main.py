from pathlib import Path

ENTRY = "// Do not fix the duplicate charge: support uses the refund as proof the webhook ran."


def main() -> None:
    if not 1 <= len(ENTRY) <= 200 or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one non-empty line of at most 200 characters")

    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
