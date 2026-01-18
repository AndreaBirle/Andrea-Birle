import random
import csv
import os

# ----------------- SCORURI -----------------
SCOR_LINIE_3 = 5
SCOR_LINIE_4 = 10
SCOR_LINIE_5 = 50
SCOR_L = 20
SCOR_T = 30

# ----------------- PATRONI -----------------
PATRON_L = [
    [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0)],
    [(-2, 0), (-1, 0), (0, 0), (0, 1), (0, 2)],
    [(-2, 0), (-1, 0), (0, -2), (0, -1), (0, 0)],
    [(0, -2), (0, -1), (0, 0), (1, 0), (2, 0)],
]

PATRON_T = [
    [(-1, 0), (0, -2), (0, -1), (0, 0), (0, 1), (0, 2), (1, 0)],
    [(-2, 0), (-1, 0), (0, -1), (0, 0), (0, 1), (1, 0), (2, 0)],
]

# ----------------- UTIL -----------------
def in_bounds(board, r, c):
    return 0 <= r < len(board) and 0 <= c < len(board[0])

def random_board(r, c):
    return [[random.randint(1, 4) for _ in range(c)] for _ in range(r)]

# ----------------- DETECTIE -----------------
def detect_lines(board):
    R, C = len(board), len(board[0])
    found = []

    for r in range(R):
        c = 0
        while c < C:
            v = board[r][c]
            if v == 0:
                c += 1
                continue
            start = c
            while c + 1 < C and board[r][c + 1] == v:
                c += 1
            length = c - start + 1
            if length >= 3:
                k = min(length, 5)
                score = {3: SCOR_LINIE_3, 4: SCOR_LINIE_4, 5: SCOR_LINIE_5}[k]
                found.append({"score": score, "cells": [(r, start + i) for i in range(k)]})
            c += 1

    for c in range(C):
        r = 0
        while r < R:
            v = board[r][c]
            if v == 0:
                r += 1
                continue
            start = r
            while r + 1 < R and board[r + 1][c] == v:
                r += 1
            length = r - start + 1
            if length >= 3:
                k = min(length, 5)
                score = {3: SCOR_LINIE_3, 4: SCOR_LINIE_4, 5: SCOR_LINIE_5}[k]
                found.append({"score": score, "cells": [(start + i, c) for i in range(k)]})
            r += 1

    return found

def detect_L_T(board):
    R, C = len(board), len(board[0])
    found = []

    for r in range(R):
        for c in range(C):
            v = board[r][c]
            if v == 0:
                continue
            for p in PATRON_L:
                cells = []
                ok = True
                for dr, dc in p:
                    rr, cc = r + dr, c + dc
                    if not in_bounds(board, rr, cc) or board[rr][cc] != v:
                        ok = False
                        break
                    cells.append((rr, cc))
                if ok:
                    found.append({"score": SCOR_L, "cells": cells})
            for p in PATRON_T:
                cells = []
                ok = True
                for dr, dc in p:
                    rr, cc = r + dr, c + dc
                    if not in_bounds(board, rr, cc) or board[rr][cc] != v:
                        ok = False
                        break
                    cells.append((rr, cc))
                if ok:
                    found.append({"score": SCOR_T, "cells": cells})

    return found

# ----------------- CASCADE -----------------
def apply_matches(board, matches):
    matches.sort(key=lambda x: -x["score"])
    used = set()
    to_clear = set()
    score = 0
    for m in matches:
        if any(c in used for c in m["cells"]):
            continue
        score += m["score"]
        for c in m["cells"]:
            used.add(c)
            to_clear.add(c)
    for r, c in to_clear:
        board[r][c] = 0
    return score

def gravity(board):
    R, C = len(board), len(board[0])
    for c in range(C):
        stack = [board[r][c] for r in range(R) if board[r][c] != 0]
        for r in range(R - 1, -1, -1):
            board[r][c] = stack.pop() if stack else 0

def refill(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 0:
                board[r][c] = random.randint(1, 4)

def resolve(board):
    cascades = 0
    score = 0
    while True:
        matches = detect_lines(board) + detect_L_T(board)
        if not matches:
            break
        score += apply_matches(board, matches)
        gravity(board)
        refill(board)
        cascades += 1
    return cascades, score

# ----------------- STRATEGIE RAPIDA -----------------
def best_swap(board):
    R, C = len(board), len(board[0])
    best = None
    best_score = 0
    for r in range(R):
        for c in range(C):
            for dr, dc in [(0, 1), (1, 0)]:  # doar dreapta și jos
                r2, c2 = r + dr, c + dc
                if r2 >= R or c2 >= C:
                    continue
                if board[r][c] == board[r2][c2]:
                    continue

                # swap temporar
                board[r][c], board[r2][c2] = board[r2][c2], board[r][c]

                # detectare doar linii 3 pentru scor estimat
                matches = detect_lines(board)
                if matches:
                    score = sum(m["score"] for m in matches)
                    if score > best_score:
                        best_score = score
                        best = (r, c, r2, c2)

                # undo swap
                board[r][c], board[r2][c2] = board[r2][c2], board[r][c]

    return best


# ----------------- JOC -----------------
def run_game(game_id, rows, cols, target):
    board = random_board(rows, cols)
    points = 0
    swaps = 0
    cascades = 0
    moves_to_target = None

    c, s = resolve(board)
    cascades += c
    points += s

    while True:
        if points >= target:
            return {
                "game_id": game_id,
                "points": points,
                "swaps": swaps,
                "total_cascades": cascades,
                "reached_target": True,
                "stopping_reason": "REACHED_TARGET",
                "moves_to_10000": moves_to_target if moves_to_target is not None else swaps,
            }
        move = best_swap(board)
        if not move:
            return {
                "game_id": game_id,
                "points": points,
                "swaps": swaps,
                "total_cascades": cascades,
                "reached_target": False,
                "stopping_reason": "NO_MOVES",
                "moves_to_10000": "",
            }
        r1, c1, r2, c2 = move
        board[r1][c1], board[r2][c2] = board[r2][c2], board[r1][c1]
        swaps += 1
        c, s = resolve(board)
        cascades += c
        points += s
        if points >= target and moves_to_target is None:
            moves_to_target = swaps

# ----------------- MAIN + CSV -----------------
def main():
    random.seed(42)
    results = []
    for i in range(100):
        print(f"-> Jocul {i + 1}/100")
        results.append(run_game(i, 11, 11, 10000))
    os.makedirs("results", exist_ok=True)
    with open("results/summary.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "game_id","points","swaps","total_cascades",
            "reached_target","stopping_reason","moves_to_10000"
        ])
        for r in results:
            writer.writerow([
                r["game_id"], r["points"], r["swaps"], r["total_cascades"],
                r["reached_target"], r["stopping_reason"], r["moves_to_10000"]
            ])
    print("\nFINAL:")
    print(f"Avg points: {sum(r['points'] for r in results)/len(results):.2f}")
    print(f"Avg swaps: {sum(r['swaps'] for r in results)/len(results):.2f}")

# ----------------- EXECUTIE -----------------
if __name__ == "__main__":
    main()


