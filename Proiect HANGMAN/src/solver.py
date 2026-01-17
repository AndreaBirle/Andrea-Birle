from src.utils import normalize

class HangmanSolver:
    def __init__(self, dictionary):
        """
        dictionary: listă cu toate cuvintele posibile (string)
        """
        self.dictionary = [normalize(word) for word in dictionary]

    def solve(self, pattern):
        """
        Primește pattern cu * pentru litere necunoscute
        Returnează: total_attempts, found_word, attempts_sequence
        """
        pattern_norm = normalize(pattern)
        candidates = [w for w in self.dictionary if len(w) == len(pattern)]
        guessed_letters = set()
        attempts_sequence = []

        current_pattern = list(pattern_norm)

        while True:
            # Filtrare candidați conform patternului
            filtered = []
            for word in candidates:
                match = True
                for i, c in enumerate(current_pattern):
                    if c != "*" and word[i] != c:
                        match = False
                        break
                if match:
                    filtered.append(word)
            candidates = filtered

            if not candidates:
                # fallback: primul cuvânt de aceeași lungime
                candidates = [w for w in self.dictionary if len(w) == len(pattern)]
                if not candidates:
                    found_word = "".join(["a" if c=="*" else c for c in pattern])
                    return len(found_word), found_word, list(found_word)

            if len(candidates) == 1:
                found_word = candidates[0]
                break

            # alege litera necunoscută cea mai frecventă
            freq = {}
            for word in candidates:
                for i, c in enumerate(word):
                    if current_pattern[i] == "*" and c not in guessed_letters:
                        freq[c] = freq.get(c, 0) + 1

            if not freq:
                found_word = candidates[0]
                break

            guess = max(freq, key=freq.get)
            guessed_letters.add(guess)
            attempts_sequence.append(guess)

            # actualizează current_pattern
            for i, c in enumerate(current_pattern):
                if c == "*" and candidates[0][i] == guess:
                    current_pattern[i] = guess

        # adaugă literele finale neghicite la secvență
        for i, c in enumerate(candidates[0]):
            if current_pattern[i] == "*" and c not in guessed_letters:
                attempts_sequence.append(c)

        total_attempts = len(attempts_sequence)
        return total_attempts, candidates[0], attempts_sequence




















