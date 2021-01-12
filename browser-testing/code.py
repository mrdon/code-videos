from manim import *

from code_video import CodeScene, comment_parser, AutoScaled, PartialCode


class MyIdentitiesScene(CodeScene):
    def construct(self):
        path = "../../sleuth/sleuth/apps/account/tests/selenium/test_my_identities.py"
        code, _ = comment_parser.parse(
            path, keep_comments=False, start_line=34, end_line=46
        )

        code = AutoScaled(PartialCode(code=code, line_no_from=34, style="fruity"))
        self.play(ShowCreation(code))
        self.highlight_lines(
            code,
            36,
            36,
            caption="Log in"
        )
        self.wait()
        self.highlight_lines(
            code,
            37,
            38,
            caption="Load page"
        )
        self.wait()

        self.highlight_lines(
            code,
            40,
            42,
            caption="Make assertions"
        )
        self.wait()

        self.highlight_lines(
            code,
            44,
            46,
            caption="Test database state"
        )
        self.wait()

        self.highlight_none(code)

        self.wait(5)
