def justify_text(paragraph, page_width):
    words = paragraph.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) > page_width:
            lines.append(current_line)
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += len(word)

    if current_line:
        lines.append(current_line)

    justified_lines = []
    for idx, line in enumerate(lines):
        if len(line) == 1:
            # If there's only one word, just adjust the spacing accordingly.
            justified_lines.append(line[0].ljust(page_width))
        else:
            total_spaces_needed = page_width - sum(len(word) for word in line)
            minimum_space_between_words = total_spaces_needed // (len(line) - 1)
            extra_spaces_needed = total_spaces_needed % (len(line) - 1)

            for i in range(extra_spaces_needed):
                line[i] += ' '
            
            justified_line = (' ' * minimum_space_between_words).join(line).ljust(page_width)
            justified_lines.append(justified_line)

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
