# Python program to create
# a pdf file

# imports
# pip install fpdf
from fpdf import FPDF


if __name__ == '__main__':
    CONFIGURATION = [{"hfont-style":"Arial","hfont-size":15,"bfont-style":"Arial","bfont-size":11,"cell-width":200,"cell-height":10,"ln":1,'head-align':'C','text-align':'J'},
                     {"hfont-style":"Arial","hfont-size":15,"bfont-style":"Arial","bfont-size":11,"cell-width":200,"cell-height":10,"ln":1,'head-align':'C','text-align':'J'},
                     {"hfont-style":"Arial","hfont-size":15,"bfont-style":"Arial","bfont-size":11,"cell-width":200,"cell-height":10,"ln":1,'head-align':'C','text-align':'J'}]

    heading = input("Enter the main heading: ")
    body = input("Enter the body: ")
    style = int(input("Choose style (1,2,3): "))

    pdf = FPDF()
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font(CONFIGURATION[style]['hfont-style'], size=CONFIGURATION[style]['hfont-size'])
    pdf.cell(w=CONFIGURATION[style]['cell-width'], h=CONFIGURATION[style]['cell-height'], txt=heading, ln=CONFIGURATION[style]['ln'], align=CONFIGURATION[style]['head-align'])
    pdf.set_font(CONFIGURATION[style]['bfont-style'], size=CONFIGURATION[style]['bfont-size'])
    pdf.cell(w=CONFIGURATION[style]['cell-width'], h=CONFIGURATION[style]['cell-height'], txt=body, ln=CONFIGURATION[style]['ln'], align=CONFIGURATION[style]['text-align'])

    output_file_name = input("PDF ready! Save as: ")
    if output_file_name[:-4] != '.pdf':
        output_file_name += ".pdf"

    # save the pdf with name .pdf
    pdf.output(output_file_name)