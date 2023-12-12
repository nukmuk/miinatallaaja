import json

FILENAME = "miinatallaaja_stats.txt"


def save_score(generated_stats):
    scores = load_scores()
    scores.append(generated_stats)
    # print("saving game: ", game)
    with open(FILENAME, "w", encoding="utf-8") as f:
        js = json.dumps(scores)
        f.write(js)


def load_scores():
    scores = []
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            data = f.read()
            scores = json.loads(data)
            # print("loaded: ", scores)
    except FileNotFoundError:
        print("no scores found")
    return scores


def get_scores_nice():
    scores = load_scores()
    text = ""
    for score in scores:
        duration = round((score["time_taken"] / 60), 2)
        text += (
            f"Finished at {score['finished_at']}, "
            f"Duration: {duration} minutes and {score['turns_taken']} turns, "
            f"Outcome: {score['outcome']}, "
            f"Mines left: {score['mines_remaining']}, "
            f"Game size: {score['w']}x{score['h']}\n"
        )
    text += f"Games played: {len(scores)}\n"
    return text
