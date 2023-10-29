import PyPDF2
import tkinter as tk
import tkinter.filedialog as fd


def merge_pdfs(input_pdfs, output_pdf):
    pdf_merger = PyPDF2.PdfMerger()

    try:
        for pdf_file in input_pdfs:
            pdf_merger.append(pdf_file)

        with open(output_pdf, 'wb') as output_file:
            pdf_merger.write(output_file)
        print("PDFs merged successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def page_split_pdf(input_pdf):
    try:
        with open(input_pdf, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            
            for page_num in range(pdf_reader.getNumPages()):
                pdf_writer = PyPDF2.PdfFileWriter()
                pdf_writer.addPage(pdf_reader.getPage(page_num))
                
                output_pdf = f'page{page_num + 1}.pdf'
                
                with open(output_pdf, 'wb') as output_file:
                    pdf_writer.write(output_file)
                    print(f"{output_pdf} created successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def extract_text(input_pdf):
    try:
        with open(input_pdf, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            
            for page_num in range(pdf_reader.getNumPages()):
                page = pdf_reader.getPage(page_num)
                text = page.extractText()
                print(f"Page {page_num + 1}:\n{text}\n")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Function to open a file dialog and select PDF files
def browse_files():
    file_paths = fd.askopenfilenames(
        title="Select PDF Files",
        filetypes=[("PDF files", "*.pdf")]
    )
    input_files_listbox.delete(0, tk.END)  # Clear the current list
    for file_path in file_paths:
        input_files_listbox.insert(tk.END, file_path)


if __name__ == "__main__":
    # input_pdfs = ["input1.pdf", "input2.pdf", "input3.pdf"]

    # output_pdf = "output.pdf"
    # merge_pdfs(input_pdfs, output_pdf)

    # input_pdf = "input.pdf"  
    # page_split_pdf(input_pdf)

    # input_pdf = "input.pdf"  
    # extract_text(input_pdf)

    # Create the main application window
    app = tk.Tk()
    app.title("GreatNotes")

    # Create a label for the input files list
    input_files_label = tk.Label(app, text="Input PDF Files:")
    input_files_label.pack()

    # Create a listbox to display selected input files
    input_files_listbox = tk.Listbox(app, selectmode=tk.MULTIPLE)
    input_files_listbox.pack()

    # Create a button to browse for input PDF files
    browse_button = tk.Button(app, text="Browse Files", command=browse_files)
    browse_button.pack()

    # Create a button to merge selected PDF files
    merge_button = tk.Button(app, text="Merge PDFs", command=lambda: merge_pdfs(input_files_listbox.get(0, tk.END), "output.pdf"))
    merge_button.pack()

    # Create a label for displaying the result
    result_label = tk.Label(app, text="")
    result_label.pack()

    # Start the Tkinter main loop
    app.mainloop()