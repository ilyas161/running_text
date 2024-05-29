from manim import *


class RunningTextRightToLeft(MovingCameraScene):
    def __init__(self, text, **kwargs):
        self.text = text
        super().__init__(**kwargs)

    def construct(self):
        text = Text(self.text, font_size=96)
        text.set_width(config.frame_width - 1)
        text.set_height(config.frame_height / 2)
        text.to_edge(RIGHT).shift(RIGHT * text.width)

        self.add(text)

        self.play(text.animate.shift(LEFT * (config.frame_width + text.width)), run_time=3, rate_func=linear)


def generate_manim_video(text):
    output_dir = "./media/videos/"
    config.media_dir = output_dir
    scene = RunningTextRightToLeft(text=text)
    scene.render()
    return scene.renderer.file_writer.movie_file_path
