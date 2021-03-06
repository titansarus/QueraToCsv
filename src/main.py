import pandas as pd
import re
import os
import argparse


ERROR_CODE_MAGIC_NUMBER = -113543635432


def english_to_persian_number(number):
    """
    converts a number from English alphabet to Persian alphabet. It is used because some students use Persian alphabet
    in their student number and for each student number, we must check both English and Persian alphabet.

    :param number: int or str
        Number in English alphabet
    :return: str
        Number in Persian alphabet
    """
    number = str(number)
    input_chars = '1234567890'
    output_chars = '۱۲۳۴۵۶۷۸۹۰'
    translation_table = str.maketrans(input_chars, output_chars)
    return number.translate(translation_table)


def find_score_in_quera(student_id, folder_structure_path, judge_score_string="judge score:",
                        result_filename="result.txt"):
    """
    This function tries to open file in the address "./folder_structure_path/student_id/file_name"
    and tries to find an string like "judge_score_string score" in the text. If it find the score, it will return it
    otherwise it will return an ErrorCode which is defined as ERROR_CODE_MAGIC_NUMBER.

    :param student_id: int or str
        Student id. The main identifier in folder structure
    :param judge_score_string: str
        Instructs the code to find an string like "judge_score_string (/d+)" in the file. (/d+) is a regex for numbers.
    :param folder_structure_path: str
        Path to the folder in which we can find folders of each student's results.
    :param result_filename: str
        Final file name. For Quera it is usually result.txt
    :return: int or str
        Score of specified student or ERROR_CODE_MAGIC_NUMBER if it cannot find the file.
    """
    english_path = f"{folder_structure_path}/{student_id}/{result_filename}"
    persian_path = f"{folder_structure_path}/{english_to_persian_number(student_id)}/{result_filename}"
    if os.path.exists(english_path):
        file = open(english_path, encoding='utf8')
    elif os.path.exists(persian_path):
        file = open(persian_path, encoding='utf8')
    else:
        return ERROR_CODE_MAGIC_NUMBER
    result = file.read()
    retval = re.search(f"{judge_score_string}(\\d+)", result).group(1)
    file.close()
    return retval


def put_scores_in_dataframe(src_csv: str, folder_structure_path, student_id_heading="Students", score_heading="Score",
                            not_found_score="0",
                            judge_score_string="judge score: ",
                            result_filename="result.txt"):
    """
    Put scores that are in Quera results files into a Pandas DataFrame.
    At first, it Loads a base csv located in `src_csv` that includes student IDs and headers for Student column and Score column.
    Then it searches the directories in `folder_structure_path` for that student IDs and get their scores.
    After that it puts them in a DataFrame and returns that.


    :param src_csv: str
        Name of the Source CSV file that has student IDs and header name for Students and Scores.
    :param student_id_heading: str
        Name of the heading in CSV file that has Student IDs.
    :param score_heading: str
        Name of the heading in CSV file that is going to have Scores.
    :param not_found_score: int
        The default score for students that didn't submitted their answer of their result file couldn't be found.
    :param judge_score_string: str
        Instructs the code to find an string like "judge_score_string (/d+)" in the file. (/d+) is a regex for numbers.
    :param folder_structure_path: str
        Path to the folder in which we can find folders of each student's results.
    :param result_filename: str
        Final file name. For Quera it is usually result.txt
    :return: Pandas.DataFrame
        A Pandas DataFrame that contains student IDs and scores.
    """
    _score_df: pd.DataFrame = pd.read_csv(src_csv)
    for std in _score_df[student_id_heading]:
        score = find_score_in_quera(std, judge_score_string=judge_score_string,
                                    folder_structure_path=folder_structure_path,
                                    result_filename=result_filename)
        if score == ERROR_CODE_MAGIC_NUMBER:
            _score_df.loc[_score_df[student_id_heading] == std, score_heading] = not_found_score
        else:
            _score_df.loc[_score_df[student_id_heading] == std, score_heading] = score

    return _score_df


def parser_factory():
    """
    Creates Python ArgumentParser.

    :return: argparse.ArgumentParser
    """
    _parser = argparse.ArgumentParser(description='Process some integers.')
    _parser.add_argument('-s', '--src', help='Source csv filename', nargs="?", required=True)
    _parser.add_argument('-d', '--dest', help='Destination csv filename', nargs="?", required=True)
    _parser.add_argument('-f', '--folder', help='Folder structure ath', nargs="?", required=True)
    _parser.add_argument('-r', '--result', help='Result file name', default="result.txt", nargs="?")
    _parser.add_argument('-j', '--judge', help='Judge Score string in result file', default="judge score: ", nargs="?")
    _parser.add_argument('-n', '--not-found', help='Score to replace when student id is not found', default=0,
                         nargs="?")
    _parser.add_argument('--id', help='Student ID heading in CSV', default="Students", nargs="?")
    _parser.add_argument('--score', help='Score heading in CSV', default="Score", nargs="?")
    return _parser


def handle_parse_errors(_args: argparse.Namespace, _parser: argparse.ArgumentParser):
    if not _args.src:
        _parser.error("Missing --src. Source CSV filename is required.")
    if not _args.dest:
        _parser.error("Missing --dest. Destination CSV filename is required.")


if __name__ == '__main__':
    parser = parser_factory()
    args = parser.parse_args()
    handle_parse_errors(args, parser)
    score_df = put_scores_in_dataframe(src_csv=args.src, student_id_heading=args.id,
                                       score_heading=args.score, not_found_score=args.not_found,
                                       judge_score_string=args.judge,
                                       folder_structure_path=args.folder, result_filename=args.result)
    score_df.to_csv(args.dest)
