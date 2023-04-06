from pdf2docx import Converter
"""
this is not the perfect file converter for pdf to doc convert 
the reason is that it cant perfectly convert pdf to docx.
"""

pdf_file_name = "files/CV.pdf"

docx_file_name = "default.docx"
# converted from pdf
pdf_converted_file = Converter(pdf_file_name)

# convert to docx
pdf_converted_file.convert(docx_file_name)
# closing the files
pdf_converted_file.close()
