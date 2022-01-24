# Python program to create
# a pdf file

# imports
# pip install fpdf
from fpdf import FPDF


if __name__ == '__main__':
    CONFIGURATION = [{"hfont-family":"Arial","hfont-style":"B","hfont-size":15,"bfont-family":"Arial","bfont-size":11,"cell-width":200,"cell-height":10,"ln":1,'head-align':'C','text-align':'J'},
                     {"hfont-family":"Times","hfont-style":"B","hfont-size":15,"bfont-family":"Arial","bfont-size":11,"cell-width":200,"cell-height":10,"ln":1,'head-align':'C','text-align':'J'},
                     {"hfont-family":"Times","hfont-style":"B","hfont-size":15,"bfont-family":"Courier","bfont-size":11,"cell-width":200,"cell-height":10,"ln":1,'head-align':'C','text-align':'J'}]

    heading = input("Enter the main title: ")
    body = input("Enter the body: ")
    style = int(input("Choose style (1,2,3): "))-1

    pdf = FPDF()
    pdf.set_margins(15, 5, 15)
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font(family=CONFIGURATION[style]['hfont-family'],style=CONFIGURATION[style]['hfont-style'], size=CONFIGURATION[style]['hfont-size'])
    pdf.cell(w=CONFIGURATION[style]['cell-width'], h=CONFIGURATION[style]['cell-height'], txt=heading, ln=CONFIGURATION[style]['ln'], align=CONFIGURATION[style]['head-align'])
    pdf.set_font(CONFIGURATION[style]['bfont-family'], size=CONFIGURATION[style]['bfont-size'])
    pdf.set_line_width(0)
    pdf.multi_cell(w=CONFIGURATION[style]['cell-width'], h=CONFIGURATION[style]['cell-height'], txt=body, align=CONFIGURATION[style]['text-align'])

    output_file_name = heading+".pdf"

    # save the pdf with name .pdf
    pdf.output(output_file_name)

    print("PDF ready!")