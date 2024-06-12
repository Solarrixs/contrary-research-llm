# Contrary-Research-LLM

This project aims to create a Retrieval-Augmented Generation (RAG) based Language Model fine-tuned on Contrary's Research Memos. The project includes tools for web scraping to gather text from Contrary's Memos, data processing, and model fine-tuning using the cleaned text files.

## Directory Structure

- `main.ipynb`: Jupyter notebook for fine-tuning and running the LLM.
- `scrape.py`: Python script for scraping the body content from a provided Contrary Memo URL.
- `websites.py` and `websites2.py`: Python scripts to scrape for all available Contrary Memo URLs.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Contrary-Research-LLM.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Contrary-Research-LLM
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Note
The cleaned and processed text of Contrary's Research Memos are not provided.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.