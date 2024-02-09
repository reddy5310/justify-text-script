def justify_text(paragraph, page_width):
    words = paragraph.split()
    lines = []
    current_line = []
    current_length = 0

    # Split words into lines considering page width
    for word in words:
        if current_length + len(word) + len(current_line) <= page_width:
            current_line.append(word)
            current_length += len(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)

    if current_line:  # Add the last line
        lines.append(' '.join(current_line))

    # Justify lines except the last line
    justified_lines = []
    for line in lines[:-1]:  # Exclude the last line for special handling
        if " " not in line:  # Single word in line
            justified_lines.append(line)
        else:
            words = line.split()
            spaces_needed = page_width - sum(len(word) for word in words)
            spaces = len(words) - 1
            extra_spaces = spaces_needed % spaces
            space_between_words = spaces_needed // spaces + 1

            for i in range(extra_spaces):
                words[i] += ' '
            justified_line = (' ' * space_between_words).join(words)
            justified_lines.append(justified_line)

    # Left justify the last line
    justified_lines.append(lines[-1].ljust(page_width))

    return justified_lines

def main():
    try:
        paragraph = input("Enter a paragraph: ")
        page_width = int(input("Enter page width: "))
        
        output = justify_text(paragraph, page_width)
        
        print("\nJustified Text Output:")
        for index, line in enumerate(output, start=1):
            print(f"Array [{index}] = \"{line}\"")
    except ValueError as e:
        print(f"Error: {e}. Page width should be an integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
