import pandas as pd
import re

df: pd.DataFrame = pd.read_csv("1.csv")

ERROR_CODE_MAGIC_NUMBER = -113543635432


def find_score_in_quera(student_number, judge_score_string="judge score:", folder_structure_path="scores",
                        file_name="result.txt"):
    """
    This function tries to open file in the address "./folder_structure_path/std_number/file_name"
    and tries to find an string like "judge_score_string score" in the text. If it find the score, it will return it
    otherwise it will return an ErrorCode which is defined as ERROR_CODE_MAGIC_NUMBER.

    :param student_number: int or str
        Student Number. The main identifier in folder structure
    :param judge_score_string: str
        Instructs the code to find an string like "judge_score_string (/d+)" in the file. (/d+) is a regex for numbers.
    :param folder_structure_path: str
        Path to the folder in which we can find folders of each student's results.
    :param file_name: str
        Final file name. For Quera it is usually result.txt
    :return: int or str
        Score of specified student or ERROR_CODE_MAGIC_NUMBER if it cannot find the file.
    """
    try:
        file = open(f"{folder_structure_path}/{student_number}/{file_name}", mode='r', encoding="utf8")
        result = file.read()
        retval = re.search(f"{judge_score_string} (\\d+)", result).group(1)
        file.close()
        return retval
    except FileNotFoundError:
        return ERROR_CODE_MAGIC_NUMBER


def put_scores_in_dataframe(src_csv: str, std_id_header="Students", score_heading="Score", not_found_score="0",
                            judge_score_string="judge score: ", folder_structure="scores",
                            quera_file_name="result.txt"):
    score_df: pd.DataFrame = pd.read_csv(src_csv)
    for std in score_df[std_id_header]:
        score = find_score_in_quera(std, judge_score_string=judge_score_string, folder_structure_path=folder_structure,
                                    file_name=quera_file_name)
        if score==ERROR_CODE_MAGIC_NUMBER:
            score_df.loc[score_df[std_id_header] == std, score_heading] = not_found_score
        else:
            score_df.loc[score_df[std_id_header] == std, score_heading] = score

    return score_df


score_df = put_scores_in_dataframe("1.csv")
score_df.to_csv("result.csv")