import os
from PIL import Image
from fpdf import FPDF
from tqdm import tqdm
pdf = FPDF()
w, h = 0, 0
firstfilenumber = 0  # Change this
lastfilenumber = 0  # Change this

for i in tqdm(range(firstfilenumber, lastfilenumber+1)):
    # file name here, %d = number, for eg. file%d.png will be file0.png, %.3d = file000.png
    fname = "file%d.png" % i
    if os.path.exists(fname):
        if i == firstfilenumber:
            cover = Image.open(fname)
            w, h = cover.size
            pdf = FPDF(unit="pt", format=[w, h])
        image = fname
        pdf.add_page()
        pdf.image(image, 0, 0, w, h)
    else:
       ## print("File not found:", fname)
        ##print("processed %d" % i)
pdf.output("output.pdf", "F")
print("done")
