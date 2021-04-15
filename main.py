import pandas as pd
import re

df: pd.DataFrame = pd.read_csv("1.csv")

ERROR_CODE_MAGIC_NUMBER = -113543635432


def find_score_in_quera(std_number, judge_score_string="judge score: ", folder_structure="scores",
                        file_name="result.txt"):
    try:
        file = open(f"{folder_structure}/{std_number}/{file_name}", mode='r', encoding="utf8")
        result = file.read()
        retval = re.search(f"{judge_score_string}(\\d+)", result).group(1)
        file.close()
        return retval
    except FileNotFoundError:
        return ERROR_CODE_MAGIC_NUMBER


def put_scores_in_dataframe(src_csv: str, std_id_header="Students", score_heading="Score", not_found_score="0",
                            judge_score_string="judge score: ", folder_structure="scores",
                            quera_file_name="result.txt"):
    score_df: pd.DataFrame = pd.read_csv(src_csv)
    for std in score_df[std_id_header]:
        score = find_score_in_quera(std, judge_score_string=judge_score_string, folder_structure=folder_structure,
                                    file_name=quera_file_name)
        if score==ERROR_CODE_MAGIC_NUMBER:
            score_df.loc[score_df[std_id_header] == std, score_heading] = not_found_score
        else:
            score_df.loc[score_df[std_id_header] == std, score_heading] = score

    return score_df


score_df = put_scores_in_dataframe("1.csv")
score_df.to_csv("result.csv")