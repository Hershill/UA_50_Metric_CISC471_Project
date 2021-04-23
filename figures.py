"""
figures.py file containing the implementation of the functions that generate,
gather, store and output CSV formatted data that can be imported for direct
use in latex files

Group Project for CISC 471, Computational Biology.

By:
    - Andrew Ma (20030440)
    - Rayan Shaikli (20059806)
    - Hershil Devnani (20001045)

"""

# TODO: conduct 5 trials to average data

# TODO: output data for one trial data table

# TODO: output data for averaged data table

# TODO: output data for each of error data trials

from asqm_extension import generate_skewed_data_analysis, \
    generate_n_vs_ua_data_analysis, PCT_ERRS
import csv


def gen_figure_data(genome_size, num_contigs, score_pct, trials=5):
    """Gather the data required to generate the graph figures in latex

    :param genome_size: size of genome
    :param num_contigs: number of contigs per genome set
    :param score_pct: percentage cutoff for metric scoring
    :param trials: number of trial to conduct, default is 5
    :return: data ready to be stored in a csv file
    """

    collection_set = dict()

    for err in PCT_ERRS:
        collection_set[f"{err * 100}"] = dict()

    for trial in range(trials):
        error_trial_data = \
            generate_n_vs_ua_data_analysis(genome_size, num_contigs, score_pct)

        collection_set = collate_results(error_trial_data, collection_set)

    collection_set = collate_average(collection_set, trials)

    return collection_set


def gen_table_data(genome_size, num_contigs, score_pct, trials=5):
    """Gather the data required to generate the table figures in latex

    :param genome_size: size of genome
    :param num_contigs: number of contigs per genome set
    :param score_pct: percentage cutoff for metric scoring
    :param trials: number of trial to conduct, default is 5
    :return: data ready to be stored in a csv file
    """

    data_control, data_sm, data_md, data_lg = dict(), dict(), dict(), dict()

    collection_set = {
        "control": data_control,
        "sm": data_sm,
        "md": data_md,
        "lg": data_lg
    }

    for trial in range(trials):
        control, sm, md, lg = generate_skewed_data_analysis(genome_size,
                                                            num_contigs,
                                                            score_pct)

        data_list = {"control": control, "sm": sm, "md": md, "lg": lg}

        collection_set = collate_results(data_list, collection_set)

    collection_set = collate_average(collection_set, trials)

    return collection_set


def collate_results(identifiers, data):
    """Common loop used to collate data during trials into an easily accessible
    dictionary data structure

    :param identifiers: key values to gather results from
    :param data: data object being modified and updated with new data
    :return: update data structure with results from a given trial call
    """

    for data_key, data_set in identifiers.items():
        for key, value in data_set.items():
            if key in data[data_key]:
                data[data_key][key] += value
            else:
                data[data_key][key] = value

    return data


def collate_average(data, trials):
    """Normalize data with averages based on trials conducted

    :param data: data to normalize
    :param trials: number of trials conducted
    :return: normalized data based on number of trials conducted
    """

    # average collected data based on number of trial conducted
    for i in range(trials):
        for key, value in data.items():
            for metric, score in data[key].items():
                data[key][metric] = \
                    data[key][metric] / trials
    return data


def output_table_data_to_csv(data):
    """Output data from comparative analysis trials to a csv file to be easily
    read in by latex

    :param data: the dictionary containing the data from the trials
    """

    # take in data as a collection of dictionaries
    with open("table.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter='\t')
        writer.writerow(
            ['Metric', 'Control', 'SmallSkew', 'MediumSkew', 'LargeSkew']
        )
        for key in data["control"]:
            if "CONTIG" not in key:
                writer.writerow([key] + [d[key] for d in data.values()])

    # take in data as a collection of dictionaries
    with open("contig_spread.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter='\t')
        writer.writerow(
            ['ContigParam', 'Control', 'SmallSkew', 'MediumSkew', 'LargeSkew']
        )
        for key in data["control"]:
            if "CONTIG" in key:
                temp_key = key.replace("CONTIG_", "")
                temp_key = temp_key.replace("_", "")
                writer.writerow([temp_key] + [d[key] for d in data.values()])


def output_figure_data_to_csv(data):
    """Output data from error analysis trials to a csv file to be easily
    read in by latex

    :param data: the dictionary containing the data from the trials
    """

    # take in data as a collection of dictionaries
    with open("figure.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter='\t')
        writer.writerow(['Metric', '5.0', '10.0', '25.0', '50.0'])

        for key in data[list(data.keys())[0]]:
            if "CONTIG" not in key:
                writer.writerow([key] + [d[key] for d in data.values()])

    # take in data as a collection of dictionaries
    with open("n_vs_ua_contig_spread.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter='\t')
        writer.writerow(['Metric', '5.0', '10.0', '25.0', '50.0'])

        for key in data[list(data.keys())[0]]:
            if "CONTIG" in key:
                temp_key = key.replace("CONTIG_", "")
                temp_key = temp_key.replace("_", "")
                writer.writerow([temp_key] + [d[key] for d in data.values()])


if __name__ == '__main__':
    # reference genome of len 500
    ref_genome_size = 500

    # number of contigs in data set
    contig_genome_scale = 2.25  # percent ratio of contigs to ref_genome_size
    contig_set_size = contig_genome_scale * ref_genome_size

    # normalized data for 50% scoring
    scoring_pct = 50

    # generate data sets

    data_set = \
        gen_table_data(ref_genome_size, contig_set_size, scoring_pct, trials=1)

    output_table_data_to_csv(data_set)

    data_set = gen_figure_data(
        ref_genome_size, contig_set_size, scoring_pct, trials=1
    )

    output_figure_data_to_csv(data_set)
