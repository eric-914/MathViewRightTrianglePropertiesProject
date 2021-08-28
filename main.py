from manim import *

from pathlib import Path
import os
# ---------- FLAGS
RESOLUTION = ""
FLAGS = f"-pql {RESOLUTION}"
SCENE = "Go"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


class Go(Scene):
    fast = False
    white = "#ffffff"
    black = "#000000"
    yellow = "#ffff00"
    dark_blue = "#000080"
    dark_green = "#008000"
    pi_rad = 3.1415926 / 180.0

    v_title = VGroup()
    v_text = VGroup()
    v_canvas = VGroup()
    v_triangle = VGroup()

    def construct(self):
        self.camera.background_color = self.dark_blue
        self.setup_right_triangle()
        self.add(self.v_title)
        self.add(self.v_text)
        self.add(self.v_canvas)

        self.show_title("Right Triangle Properties")

        self.scene1()
        self.scene2()
        self.scene3()

        self.show_title("AA (Angle-Angle) Similarity")

        self.scene4()
        self.scene5()

        self.show_title("Similar Triangles and Ratios")

        self.scene6()

        self.wait()

    def scene1(self):
        self.show_instructions(["Start with a right triangle"])

        v_canvas = VGroup(self.v_triangle)
        v_canvas.shift([-3.5, -1.5, 0.0])

        if self.fast:
            self.add(v_canvas)
        else:
            self.play(Create(v_canvas))
        self.v_canvas.add(v_canvas)

        self.wait(1.0)

    def scene2(self):
        self.show_instructions([
            "Rotate it such that its",
            "hypotenuse becomes the base"
        ])

        self.play(self.v_triangle.animate.rotate(236.15 * self.pi_rad))
        self.play(self.v_triangle.animate.shift([0.0, -1.0, 0.0]))

        self.wait(1.0)

    def scene3(self):
        self.show_instructions([
            "Add a perpendicular segment",
            "to the base that intersects",
            "the far right angle"
        ])

        segment = Polygon([0, 0, 0], [0, 1, 0]).set_color(self.dark_green)
        right_angle = RightAngle(Line(LEFT, RIGHT), Line(DOWN, UP), 0.125)

        v_canvas = VGroup()
        v_canvas.add(segment)
        v_canvas.add(right_angle)
        v_canvas.scale(3.3)
        v_canvas.shift([-4.22, -0.59, 0.0])

        if self.fast:
            self.add(v_canvas)
        else:
            self.play(Create(v_canvas))

        self.v_canvas.add(v_canvas)

        self.wait(1.0)

    def scene4(self):
        self.show_instructions([
            "There are now two smaller right",
            "triangles which are similar to each",
            "other as well as the original triangle"
        ])

        right_triangle = self.basic_right_triangle()\
            .scale(4.0).rotate(236.15 * self.pi_rad).shift([-3.5, -2.5, 0])\
            .set_color(self.black).set_fill(self.dark_green, opacity=0.5)

        self.play(FadeIn(right_triangle))
        self.play(right_triangle.animate.scale(0.4))
        self.play(right_triangle.animate.rotate(-236.15 * self.pi_rad))
        self.play(right_triangle.animate.shift([-3.04, -0.365, 0]))
        self.play(right_triangle.animate.scale([-1, 1, 1]))
        self.play(right_triangle.animate.scale(1.38))
        self.play(right_triangle.animate.rotate(-90.2 * self.pi_rad))
        self.play(right_triangle.animate.shift([3.61, -.01, 0]))
        self.play(right_triangle.animate.scale(1.5))
        self.play(FadeOut(right_triangle))

        self.wait(1.0)

    def scene5(self):
        self.show_instructions(["Label 3 of the segments as shown"])

        label_a = self.segment_label("a")
        label_b = self.segment_label("b")
        label_c = self.segment_label("c")

        v_canvas = VGroup()
        v_canvas.add(label_a)
        v_canvas.shift([-0.64, -0.85, 0.0])
        v_canvas.add(label_b)
        v_canvas.shift([-0.985, 0.85, 0.0])
        v_canvas.add(label_c)
        v_canvas.scale(2.22)
        v_canvas.shift([-2.91, -1.45, 0.0])

        if self.fast:
            self.add(v_canvas)
        else:
            self.play(Create(v_canvas))
        self.v_canvas.add(v_canvas)

        self.show_instructions([
            "Line segments on similar triangles",
            "have equal ratios"
        ])

        self.wait(1.0)

    def scene6(self):
        label_1a = VGroup(self.segment_label("a"))
        label_1b = VGroup(self.segment_label("b"))
        label_2b = VGroup(self.segment_label("b"))
        label_2c = VGroup(self.segment_label("c"))

        triangle_1 = self.basic_right_triangle().set_color(GREEN).scale([-1.0, 1.0, 1.0])
        triangle_2 = self.basic_right_triangle().set_color(ORANGE).rotate(90 * self.pi_rad).scale([-1.5, 1.5, 1.0])

        v_triangle_1 = VGroup()
        v_triangle_1.add(triangle_1)
        v_triangle_1.add(label_1a.shift([0.5, -0.1, 0.0]))
        v_triangle_1.add(label_1b.shift([0.875, 0.75, 0.0]))

        v_triangle_2 = VGroup()
        v_triangle_2.add(triangle_2)
        v_triangle_2.add(label_2c.shift([0.5, -0.1, 0.0]))
        v_triangle_2.add(label_2b.shift([-0.5, 0.75, 0.0]))

        v_canvas = VGroup()
        v_canvas.add(v_triangle_1.shift([-1.63, 0.0, 0.0]))
        v_canvas.add(v_triangle_2)
        v_canvas.scale(2.22)
        v_canvas.shift([-3.0, -0.93, 0.0])

        if self.fast:
            self.add(v_canvas)
        else:
            self.play(FadeIn(v_canvas), FadeOut(self.v_canvas))

        self.v_canvas.shift([-10.0, 0.0, 0.0])  # push off screen

        self.play(v_triangle_1.animate.shift([3.0, 0.0, 0.0]))
        self.play(v_triangle_1.animate.rotate(-90.0 * self.pi_rad))

        self.play(
            label_1a.animate.rotate(90.0 * self.pi_rad),
            label_1b.animate.rotate(90.0 * self.pi_rad)
        )

        self.play(
            label_1a.animate.shift([0.5, 0.0, 0.0]),
            label_2b.animate.shift([-0.5, 0.0, 0.0])
        )

        self.show_instructions([
            'The ratio of <span foreground="yellow">a</span> to <span foreground="yellow">b</span>',
            'is the same as',
            'the ratio of <span foreground="yellow">b</span> to <span foreground="yellow">c</span>']
        )

        self.pause()

        self.play(self.v_text.animate.shift([-1.0, 0.0, 0.0]))

        rt_arrow_0 = MathTex(r"\xrightarrow{}")
        rt_arrow_1 = MathTex(r"\xrightarrow{}")
        rt_arrow_2 = MathTex(r"\xrightarrow{}")

        v_arrows = VGroup(rt_arrow_0, rt_arrow_1, rt_arrow_2).arrange(DOWN)\
            .shift([4.2, 0.0, 0.0])

        self.v_text.add(v_arrows)

        v_ratio_1 = MarkupText('<span foreground="yellow">a</span> : <span foreground="yellow">b</span>')\
            .shift([0.0, 1.0, 0.0])
        v_ratio_2 = MarkupText('<span foreground="yellow">b</span> : <span foreground="yellow">c</span>')\
            .shift([0.0, -1.0, 0.0])
        v_ratio_equal = Text('equals')

        v_text = VGroup(v_ratio_1, v_ratio_2, v_ratio_equal).scale(0.5).shift([5.0, 0.0, 0.0])

        self.show_text(v_text)

        self.pause()

        self.play(FadeOut(self.v_text), v_text.animate.shift([-1.75, 0.0, 0.0]))
        v_text.add(v_arrows)

        self.pause()

        v_ratio_1 = MathTex(r"\frac{a}{b}").shift([0.0, 1.0, 0.0])
        v_ratio_2 = MathTex(r"\frac{b}{c}").shift([0.0, -1.0, 0.0])
        v_ratio_equal = Text('=')

        v_next = VGroup(v_ratio_1, v_ratio_2, v_ratio_equal).scale(0.5).shift([5.0, 0.0, 0.0])

        self.show_text(v_next)

        self.pause()

        self.play(
            FadeOut(v_text),
            v_ratio_1.animate.shift([-1.5, -0.5, 0.0]),
            v_ratio_2.animate.shift([-0.9, 0.5, 0.0]),
            v_ratio_equal.animate.shift([-1.2, 0.0, 0.0])
        )

        self.play(v_next.animate.scale(2.0))

        self.pause()

        self.v_canvas.shift([10.0, 0.0, 0.0])  # push back onto screen
        self.play(FadeIn(self.v_canvas), FadeOut(v_canvas))

        self.pause()

    def setup_right_triangle(self):
        right_triangle = Polygon([0, 0, 0], [0, 1.5, 0], [1, 0, 0])
        right_angle = RightAngle(Line(LEFT, RIGHT), Line(DOWN, UP), 0.125)

        self.v_triangle = VGroup()
        self.v_triangle.add(right_triangle)
        self.v_triangle.add(right_angle)
        self.v_triangle.scale(4.0)

    @staticmethod
    def basic_right_triangle():
        return Polygon([0, 0, 0], [0, 1.5, 0], [1, 0, 0])

    @staticmethod
    def segment_label(text):
        return Text(text).scale(0.25).set_color(YELLOW)

    def show_text(self, text):
        if self.fast:
            self.add(text)
        else:
            self.play(Write(text))

    def show_instructions(self, instructions):
        self.remove(self.v_text)
        self.v_text = VGroup()
        self.v_text.set_color(WHITE)

        for instruction in instructions:
            instruction_text = MarkupText(instruction).scale(0.5)
            self.v_text.add(instruction_text)

        self.v_text.arrange(direction=DOWN, aligned_edge=LEFT)
        self.v_text.shift([3.5, 0.0, 0.0])

        self.show_text(self.v_text)

    def show_title(self, title):
        title_text = Text(title).scale(1).set_color(YELLOW)

        if self.fast:
            self.remove(self.v_title)
        else:
            self.play(FadeOut(self.v_title))

        self.v_title = VGroup()
        self.v_title.add(title_text)
        self.v_title.shift([-2.0, 3.0, 0.0])

        if self.fast:
            self.show_text(self.v_title)
        else:
            self.play(FadeIn(self.v_title))

    def pause(self):
        if not self.fast:
            self.wait(1.0)


if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")