import PyPDF2


def search_pdf(file_path, search_term):
    try:  
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            occurrence_count = 0
            search_results = []
            for page_num, page in enumerate(reader.pages):
                
                text = page.extract_text()
                lines = text.split("\n")
                for line_num, line in enumerate(lines):
                    if search_term.lower() in line.lower():  
                        occurrence_count += 1
                        search_results.append(
                            {"page": page_num + 1, "line_num": line_num + 1, "line_text": line}
                        )

            print(f"Search results for '{search_term}':")
            if occurrence_count > 0:
                print(f"Found {occurrence_count} occurrence(s) in the document.")
                for result in search_results:
                    print(
                        f"Page {result['page']} - Line {result['line_num']}: {result['line_text']}"
                    )
            else:
                print("No matches found.")

    except FileNotFoundError:
        print(f"Error: Could not find the file at {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#change the filepath here
pdf_path = ""   

search_word = input("Enter the word or phrase you want to search for: ")
search_pdf(pdf_path, search_word)
