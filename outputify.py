
def outputify_comparative_scoring_analysis(control, sm, md, lg):
    dash = '-' * 70

    print(dash)
    print(f'{"Metric":<10s}{"Control":<10s}{"Small Skew":>15s}{"Medium Skew":>18s}{"Large Skew":>16s}')
    print(dash)

    for key, _ in control.items():
        if "COMP" not in key:
            print(
                f'{key:<10s}{f"{control[key]}":>10}{f"{sm[key]}":>15}{f"{md[key]}":>18}{f"{lg[key]}":>16}')

    print("\n***Contig Metrics***")
    print("Control")
    print(control["COMP"])
    print("Small Skewed")
    print(sm["COMP"])
    print("Medium Skewed")
    print(md["COMP"])
    print("Large Skewed")
    print(lg["COMP"])


def outputify_count_contig_pct(count_contig_pct):
    formatted_str = str()
    formatted_str += "Contig Composition Data:\n"
    formatted_str += f"      Total Number of Contis: {count_contig_pct[-1]}\n"
    formatted_str += f"      Percentage of Small Contigs: {round(count_contig_pct[0] * 100, 3)}%\n"
    formatted_str += f"      Percentage of Medium Contigs: {round(count_contig_pct[1] * 100, 3)}%\n"
    formatted_str += f"      Percentage of Large Contigs: {round(count_contig_pct[2] * 100, 3)}%\n"

    return formatted_str
