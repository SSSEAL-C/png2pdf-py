import os
from PIL import Image
from fpdf import FPDF
from tqdm import tqdm 
pdf = FPDF()
w,h = 0,0

for i in range(firstfilenumber, lastfilenumber+1):
    fname = "file%d.png" % i #file name here, %d = number, for eg. file%d.png will be file0.png, %.3d = file000.png
    if os.path.exists(fname):
        if i == 1:
            cover = Image.open(fname)
            w,h = cover.size
            pdf = FPDF(unit = "pt", format = [w,h])
        image = fname
        pdf.add_page()
        pdf.image(image,0,0,w,h)
    else:
        print("File not found:", fname)
    print("processed %d" % i)
pdf.output("output.pdf", "F")
print("done")