import os

def count_words_in_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

def main(data_folder, output_file_path):
    word_counts = []
    
    for filename in os.listdir(data_folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(data_folder, filename)
            word_count = count_words_in_file(file_path)
            word_counts.append((filename, word_count))
    
    word_counts.sort(key=lambda x: x[1], reverse=True)
    
    with open(output_file_path, 'w') as output_file:
        for filename, word_count in word_counts:
            output_file.write(f"{filename} - {word_count}\n")

if __name__ == "__main__":
    data_folder = 'data'
    output_file_path = 'word_counts.txt'
    main(data_folder, output_file_path)