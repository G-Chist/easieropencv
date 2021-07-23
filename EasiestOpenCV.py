import tkinter as tk
from math import *
import os

beginning = """package org.firstinspires.ftc.teamcode;

import org.firstinspires.ftc.robotcore.external.Telemetry;
import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.Point;
import org.opencv.core.Rect;
import org.opencv.core.Scalar;
import org.opencv.imgproc.Imgproc;
import org.openftc.easyopencv.OpenCvPipeline;

public class SkystoneDetector extends OpenCvPipeline {
    Telemetry telemetry;
    Mat mat = new Mat();
    public enum Location {"""

ending = """
    return mat;
    }

    public Location getLocation() {
        return location;
    }
}"""

clicknum = 0

def motion(event):
    x, y = event.x, event.y
    btn_text.set('{}, {}'.format(x-23, y-72))

prevx, prevy = 0, 0

def callback11(event):
    global clicknum, panel, prevx, prevy
    clicknum += 1
    if clicknum == 1:
        prevx, prevy = event.x, event.y
        panel.create_oval(prevx - 2, prevy - 2, prevx + 2, prevy + 2, fill = "red")
    x, y = event.x, event.y
    if clicknum > 1:
        if clicknum % 2 == 0:
            panel.create_rectangle(prevx, prevy, x, y)
            coords.insert(float(clicknum) / 2, '({}, {}), ({}, {});'.format(str(prevx - 23), str(prevy - 72), str(x - 23), str(y - 72)) + "\n")

            loc1 = str('RX, ' * (int(clicknum / 2)))
            loc2 = ""
            c1 = 1
            for i in loc1:
                if i == "X":
                    loc2 += str(c1)
                    c1 += 1
                else:
                    loc2 += i
            location = " " + loc2 + "NOT_FOUND }"
            coordsarr = coords.get('1.0', 'end-1c')
            coordsarr = ''.join([i for i in coordsarr if i != "(" and i != ")" and i != ";" and i != ","]).split()
            coordsarrx = []
            coordsarry = []
            for i in range(len(coordsarr)):
                if (i + 1) % 2 != 0:
                    coordsarrx.append(coordsarr[i])
                else:
                    coordsarry.append(coordsarr[i])
            vst1 = """
    private Location location;

    public SkystoneDetector(Telemetry t) { telemetry = t; }

    @Override
    public Mat processFrame(Mat input) {
"""
            rect1 = str("""
    final Rect rА = new Rect(
        new Point(input.cols()*Бf/441f, input.rows()*Вf/788f),
        new Point(input.cols()*Бf/441f, input.rows()*Вf/788f));
""" * (int(clicknum / 2)))
            rect2 = ""
            c1 = 1
            d1 = 0
            e1 = 0
            for i in rect1:
                if i == "А":
                    rect2 += str(c1)
                    c1 += 1
                elif i == "Б":
                    rect2 += coordsarrx[d1]
                    d1 += 1
                elif i == "В":
                    rect2 += coordsarry[e1]
                    e1 += 1
                else:
                    rect2 += i
            vst2 = """
        double PERCENT_COLOR_THRESHOLD = """ + str(threshvar.get()) + """;

        Imgproc.cvtColor(input, mat, Imgproc.COLOR_RGB2GRAY);

        Scalar lowHSV = new Scalar(""" + str(colvar.get()) + """);
        Scalar highHSV = new Scalar(""" + str(colvar2.get()) + """);"""

            mat1 = """

        Mat mr$ = mat.submat(r$);
        double v$ = Core.sumElems(mr$).val[0] / r$.area() / 255;
        mr$.release();
        telemetry.addData("v$", (int) Core.sumElems(mr$).val[0]);
        telemetry.addData("%$", Math.round(v$ * 100) + "%");""" * (int(clicknum / 2))

            mat2 = ""
            c1 = 1

            for i in mat1:
                if i == "$":
                    mat2 += str(floor(c1))
                    c1 += 0.1
                else:
                    mat2 += i

            vst3 = """
        telemetry.update();

        Imgproc.cvtColor(mat, mat, Imgproc.COLOR_GRAY2RGB);

        Scalar colorel1 = new Scalar(255, 0, 0);
        Scalar colorel2 = new Scalar(0, 255, 0);

"""
            img1 = """      Imgproc.rectangle(mat, r$,
        location == Location.R$? colorel2:colorel1);\n""" * (int(clicknum / 2))

            c1 = 1
            img2 = ""
            for i in img1:
                if i == "$":
                    img2 += str(floor(c1))
                    c1 += 0.5
                else:
                    img2 += i

            code.delete(1.0, tk.END)
            code.insert(1.0, beginning + location + vst1 + rect2 + vst2 + mat2 + vst3 + img2 + ending)

        prevx, prevy = event.x, event.y
    panel.create_oval(x - 2, y - 2, x + 2, y + 2, fill = "red")

def callback12():
    global clicknum, panel, prevx, prevy, beginning, ending
    clicknum += 1
    if clicknum == 1:
        prevx, prevy = int(coordvar.get().split(',')[0]) + 23, int(coordvar.get().split(',')[1]) + 72
        panel.create_oval(prevx - 2, prevy - 2, prevx + 2, prevy + 2, fill = "red")
    x, y = int(coordvar.get().split(',')[0]) + 23, int(coordvar.get().split(',')[1]) + 72
    if clicknum > 1:
        if clicknum % 2 == 0:
            panel.create_rectangle(prevx, prevy, x, y)
            panel.create_oval(x - 2, y - 2, x + 2, y + 2, fill="red")
            coords.insert(float(clicknum)/2, '({}, {}), ({}, {});'.format(str(prevx - 23), str(prevy - 72), str(x - 23), str(y - 72)) + "\n")

            loc1 = str('RX, ' * (int(clicknum / 2)))
            loc2 = ""
            c1 = 1
            for i in loc1:
                if i == "X":
                    loc2 += str(c1)
                    c1 += 1
                else:
                    loc2 += i
            location = " " + loc2 + "NOT_FOUND }"
            coordsarr = coords.get('1.0', 'end-1c')
            coordsarr = ''.join([i for i in coordsarr if i != "(" and i != ")" and i != ";" and i != ","]).split()
            coordsarrx = []
            coordsarry = []
            for i in range(len(coordsarr)):
                if (i + 1) % 2 != 0:
                    coordsarrx.append(coordsarr[i])
                else:
                    coordsarry.append(coordsarr[i])
            vst1 = """
    private Location location;

    public SkystoneDetector(Telemetry t) { telemetry = t; }

    @Override
    public Mat processFrame(Mat input) {
            """
            rect1 = str("""
    final Rect rА = new Rect(
        new Point(input.cols()*Бf/441f, input.rows()*Вf/788f),
        new Point(input.cols()*Бf/441f, input.rows()*Вf/788f));
            """ * (int(clicknum / 2)))
            rect2 = ""
            c1 = 1
            d1 = 0
            e1 = 0
            for i in rect1:
                if i == "А":
                    rect2 += str(c1)
                    c1 += 1
                elif i == "Б":
                    rect2 += coordsarrx[d1]
                    d1 += 1
                elif i == "В":
                    rect2 += coordsarry[e1]
                    e1 += 1
                else:
                    rect2 += i
            vst2 = """
        double PERCENT_COLOR_THRESHOLD = """ + str(threshvar.get()) + """;

        Imgproc.cvtColor(input, mat, Imgproc.COLOR_RGB2GRAY);

        Scalar lowHSV = new Scalar(""" + str(colvar.get()) + """);
        Scalar highHSV = new Scalar(""" + str(colvar2.get()) + """);"""

            mat1 = """

        Mat mr$ = mat.submat(r$);
        double v$ = Core.sumElems(mr$).val[0] / r$.area() / 255;
        mr$.release();
        telemetry.addData("v$", (int) Core.sumElems(mr$).val[0]);
        telemetry.addData("%$", Math.round(v$ * 100) + "%");""" * (int(clicknum / 2))

            mat2 = ""
            c1 = 1

            for i in mat1:
                if i == "$":
                    mat2 += str(floor(c1))
                    c1 += 0.1
                else:
                    mat2 += i

            vst3 = """
        telemetry.update();

        Imgproc.cvtColor(mat, mat, Imgproc.COLOR_GRAY2RGB);

        Scalar colorel1 = new Scalar(255, 0, 0);
        Scalar colorel2 = new Scalar(0, 255, 0);

            """
            img1 = """      Imgproc.rectangle(mat, r$,
        location == Location.R$? colorel2:colorel1);\n""" * (int(clicknum / 2))

            c1 = 1
            img2 = ""
            for i in img1:
                if i == "$":
                    img2 += str(floor(c1))
                    c1 += 0.5
                else:
                    img2 += i

            code.delete(1.0, tk.END)
            code.insert(1.0, beginning + location + vst1 + rect2 + vst2 + mat2 + vst3 + img2 + ending)

        else:
            panel.create_oval(x - 2, y - 2, x + 2, y + 2, fill = "red")
        prevx, prevy = int(coordvar.get().split(',')[0]) + 23, int(coordvar.get().split(',')[1]) + 72

root = tk.Tk()
root.title('EasiestOpenCV')
root.geometry("2000x1000")

btn_text = tk.StringVar(root)
btn_text.set("0, 0")
coordvar = tk.StringVar(root)
coordvar.set("1, 1")
colvar = tk.StringVar(root)
colvar.set("0, 0, 0")
colvar2 = tk.StringVar(root)
colvar2.set("0, 0, 0")
threshvar = tk.StringVar(root)
threshvar.set("0.4")

btn = tk.Button(root, width = 10, height = 2, textvariable = btn_text, command = motion)
btn.place(x = 320, y =0)

img = tk.PhotoImage(file="telefon.gif")
panel = tk.Canvas(root, width = 489, height = 966, bd = 0, highlightthickness = 0)
panel.bind('<Motion>', motion)
panel.bind('<Button-1>', callback11)
panel.focus_set()
panel.create_image(0, 0, image = img, anchor = "nw")
panel.place(x = 110, y = 60)

textfield = tk.Entry(root, textvariable = coordvar)
textfield.place(x = 750, y = 60)
btncoord = tk.Button(root, text = "Set coords", width = 20, height = 1, command = callback12)
btncoord.place(x = 740, y = 85)

textfieldcol = tk.Entry(root, textvariable = colvar)
textfieldcol.place(x = 750, y = 260)
btncol = tk.Button(root, text = "Set color 1", width = 20, height = 1)
btncol.place(x = 740, y = 285)

textfieldcol2 = tk.Entry(root, textvariable = colvar)
textfieldcol2.place(x = 750, y = 360)
btncol = tk.Button(root, text = "Set color 2", width = 20, height = 1)
btncol.place(x = 740, y = 385)

thresh = tk.Entry(root, textvariable = threshvar)
thresh.place(x = 750, y = 460)
btnthresh = tk.Button(root, text = "Set color threshold", width = 20, height = 1)
btnthresh.place(x = 740, y = 485)

coordslabel = tk.Button(root, text = "Coords", width = 20, height = 1)
coordslabel.place(x = 995, y = 60)
coords = tk.Text(width = 30, height = 30)
coords.place(x = 950, y = 90)

codelabel = tk.Button(root, text = "Code", width = 20, height = 1)
codelabel.place(x = 1455, y = 60)
code = tk.Text(root, width = 70, height = 50)
code.place(x = 1250, y = 90)

root.mainloop()