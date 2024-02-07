def justify_text(paragraph, page_width):
    words = paragraph.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) <= page_width:
            current_line.append(word)
            current_length += len(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)

    if current_line:
        lines.append(' '.join(current_line))  # Add the last line

    # Right justify the lines
    for i in range(len(lines) - 1):  # Last line should remain left-justified
        spaces_needed = page_width - len(lines[i])
        spaces = lines[i].count(' ')
        if spaces > 0:
            extra_space = spaces_needed // spaces
            extra_space_remainder = spaces_needed % spaces
            line_words = lines[i].split(' ')
            for j in range(extra_space_remainder):
                line_words[j] += ' '
            lines[i] = (' ' * extra_space).join(line_words)

    return lines

# Sample input
paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
page_width = 20

# Process the sample input
output = justify_text(paragraph, page_width)

# Display the output
for index, line in enumerate(output, start=1):
    print(f"Array [{index}] = \"{line}\"")
