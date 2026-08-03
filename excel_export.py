from openpyxl import Workbook


def export_to_excel(candidate_list, file_name):

    workbook = Workbook()

    sheet = workbook.active

    sheet.title = "Candidate Ranking"

    sheet.append([
        "Rank",
        "Candidate Name",
        "ATS Score",
        "Rating"
    ])

    rank = 1

    for candidate in candidate_list:

        sheet.append([
            rank,
            candidate["name"],
            candidate["score"],
            candidate["rating"]
        ])

        rank += 1

    workbook.save(file_name)