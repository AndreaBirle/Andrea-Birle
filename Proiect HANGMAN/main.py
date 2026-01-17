import argparse
import os
from src.utils import read_csv, write_csv, normalize
from src.solver import HangmanSolver

def load_dictionary(path):
    """Încarcă dicționarul din fișier text, câte un cuvânt pe linie"""
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Fișier CSV cu jocuri")
    parser.add_argument("--output", required=True, help="Fișier CSV cu rezultate")
    parser.add_argument("--dict", required=True, help="Fișier text cu dicționarul")
    args = parser.parse_args()

    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    games = read_csv(args.input)
    dictionary = load_dictionary(args.dict)
    solver = HangmanSolver(dictionary)

    results = []

    for game in games:
        game_id = game.get("game_id")
        pattern = game.get("pattern_initial")
        target = game.get("cuvant_tinta")

        print(f"Joc {game_id}: pattern={pattern}")

        total_attempts, found_word, attempts_sequence = solver.solve(pattern)

        status = "OK" if normalize(found_word) == normalize(target) else "FAIL"

        print(f"Rezultat: {found_word} ({status}) în {total_attempts} încercări")
        print(f"Secvență încercări: {' '.join(attempts_sequence)}\n")

        results.append({
            "game_id": game_id,
            "total_incercari": total_attempts,
            "cuvant_gasit": found_word,
            "status": status,
            "secventa_incercari": " ".join(attempts_sequence)
        })

    write_csv(args.output, results)
    print(f"Rezultatele au fost salvate în {args.output}")

if __name__ == "__main__":
    main()















