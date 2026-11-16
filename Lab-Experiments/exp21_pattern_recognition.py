"""
Experiment 21: Pattern Recognition
Scenario: An image-processing system identifies recurring visual patterns automatically.
Expected Outcome: Detect patterns using AI techniques.
"""

def detect_2d_pattern(image_matrix, template_pattern):
    img_rows, img_cols = len(image_matrix), len(image_matrix[0])
    pat_rows, pat_cols = len(template_pattern), len(template_pattern[0])
    matches = []

    for r in range(img_rows - pat_rows + 1):
        for c in range(img_cols - pat_cols + 1):
            found = True
            for pr in range(pat_rows):
                for pc in range(pat_cols):
                    if image_matrix[r + pr][c + pc] != template_pattern[pr][pc]:
                        found = False
                        break
                if not found:
                    break
            if found:
                matches.append((r, c))
    return matches

if __name__ == "__main__":
    # Binary pixel image matrix
    image_grid = [
        [0, 1, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0]
    ]

    # Plus (+) visual marker pattern
    plus_pattern = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]

    locations = detect_2d_pattern(image_grid, plus_pattern)
    print("Recurring Visual Pattern (+) Detected at Top-Left Coordinates:")
    for loc in locations:
        print(f" -> Row {loc[0]}, Column {loc[1]}")
