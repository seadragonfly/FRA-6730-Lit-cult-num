import os
import fitz

IN_FOLDER='./assets/pdf/'
OUT_FOLDER ='./output/text-from-pdf'

pdf="programme-saison-odeon.pdf"
path= os.path.join(IN_FOLDER, pdf)
doc = fitz.open(path)
for page in range(len(doc)):
        text = doc[page].get_text("text")
    
        # Define output file name (e.g., "2013_1.txt", "2013_2.txt", etc.)
        output_txt = os.path.join(OUT_FOLDER, f"odeon-p{page+1}.txt")
    
        with open(output_txt, "w", encoding="utf-8") as file:
            file.write(f"--- Page {page+1} ---\n")  # Page header
            file.write(text + "\n")  # Write extracted text

print("Extraction complete. All pages saved separately in 'extracted_data'.")
