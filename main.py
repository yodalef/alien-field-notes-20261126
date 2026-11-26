LINE = "Earth is rated 3 stars: the food is excellent, the Wi-Fi is a local legend, and the dominant species apologizes to furniture it walked into."


def validated_line() -> str:
    line = LINE.strip()
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"the alien review must be 1-200 characters, got {len(line)}"
    return line


def main() -> None:
    import os
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(validated_line() + "\n")
    print(validated_line())


if __name__ == "__main__":
    main()
