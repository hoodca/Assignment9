INPUT = r"c:\Users\camjh\Downloads\extracted_files\usscv19d.csv"
OUTPUT = r"c:\Users\camjh\Downloads\extracted_files\state_ratios_no_imports.csv"

def calculate_and_write_ratios(input_path, output_path):
    try:
        infile = open(input_path, "r", encoding="utf-8")
    except Exception as e:
        print("Failed to open input:", e)
        return

    # Read header and determine column indexes
    header_line = infile.readline()
    if not header_line:
        print("Input file is empty")
        infile.close()
        return

    header = [h.strip().lower() for h in header_line.rstrip("\n\r").split(",")]
    try:
        state_idx = header.index("state")
        pos_idx = header.index("positive")
        neg_idx = header.index("negative")
    except ValueError as e:
        print("Required column missing in header:", e)
        infile.close()
        return

    totals = {}  # state -> [pos_sum, neg_sum]
    line_num = 1
    for raw in infile:
        line_num += 1
        line = raw.rstrip("\n\r")
        if not line:
            continue

        parts = line.split(",")
        # Skip malformed rows that don't have enough columns
        if len(parts) <= max(state_idx, pos_idx, neg_idx):
            continue

        state = parts[state_idx].strip()
        pos_s = parts[pos_idx].strip()
        neg_s = parts[neg_idx].strip()

        # Convert to integers robustly (empty or non-numeric -> 0)
        try:
            # handle floats if they appear
            if pos_s == "":
                pos = 0
            else:
                pos = int(float(pos_s))
        except Exception:
            pos = 0

        try:
            if neg_s == "":
                neg = 0
            else:
                neg = int(float(neg_s))
        except Exception:
            neg = 0

        if state == "":
            continue

        if state not in totals:
            totals[state] = [0, 0]
        totals[state][0] += pos
        totals[state][1] += neg

    infile.close()

    # Write output CSV
    try:
        outfile = open(output_path, "w", encoding="utf-8")
    except Exception as e:
        print("Failed to open output for writing:", e)
        return

    outfile.write("state,positive,negative,ratio_pos_over_neg,ratio_pos_over_total\n")
    # Sort states for deterministic output
    for state in sorted(totals.keys()):
        pos, neg = totals[state]
        if neg > 0:
            ratio1 = pos / neg
            ratio1_s = "{:.6f}".format(ratio1)
        else:
            ratio1_s = ""

        total = pos + neg
        if total > 0:
            ratio2_s = "{:.6f}".format(pos / total)
        else:
            ratio2_s = ""

        outfile.write(f"{state},{pos},{neg},{ratio1_s},{ratio2_s}\n")
    outfile.close()

    print("Wrote", len(totals), "state rows to", output_path)


if __name__ == '__main__':
    calculate_and_write_ratios(INPUT, OUTPUT)