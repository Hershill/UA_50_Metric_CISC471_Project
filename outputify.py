
def outputify_comparative_scoring_analysis(control, sm, md, lg):
    dash = '-' * 70

    print("\n***Scoring Analysis***")
    print(dash)
    print(f'{"Metric":<10s}{"Control":<10s}{"Small Skew":>15s}{"Medium Skew":>18s}{"Large Skew":>16s}')
    print(dash)

    for key, _ in control.items():
        if "CONTIG" not in key:
            print(
                f'{key:<10s}{f"{control[key]}":>10}{f"{sm[key]}":>15}{f"{md[key]}":>18}{f"{lg[key]}":>16}')

    print("\n***Contig Analysis***")
    print(dash)
    print(f'{"Metric":<10s}{"Control":<10s}{"Small Skew":>15s}{"Medium Skew":>18s}{"Large Skew":>16s}')
    print(dash)

    contig_data = ["CONTIG_SM_PCT", "CONTIG_MD_PCT", "CONTIG_LG_PCT"]

    key = "CONTIG_NUM"
    print(f'{"NUM":<10s}{f"{control[key]}":>10}{f"{sm[key]}":>15}{f"{md[key]}":>18}{f"{lg[key]}":>16}')

    for i in contig_data:
        heading = i.replace("CONTIG_", "")
        print(f'{heading:<10s}{f"{control[i]}%":>10}{f"{sm[i]}%":>15}{f"{md[i]}%":>18}{f"{lg[i]}%":>16}')


def outputify_count_contig_pct(count_contig_pct):
    formatted_str = str()
    formatted_str += "Contig Composition Data:\n"
    formatted_str += f"      Total Number of Contis: {count_contig_pct[-1]}\n"
    formatted_str += f"      Percentage of Small Contigs: {round(count_contig_pct[0] * 100, 3)}%\n"
    formatted_str += f"      Percentage of Medium Contigs: {round(count_contig_pct[1] * 100, 3)}%\n"
    formatted_str += f"      Percentage of Large Contigs: {round(count_contig_pct[2] * 100, 3)}%\n"

    return formatted_str
