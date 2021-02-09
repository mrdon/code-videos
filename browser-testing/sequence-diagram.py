from code_video import AutoScaled, PartialCode, HighlightLines, HighlightLine
from code_video import CodeScene
from code_video import SequenceDiagram
from manim import ShowCreation, Text
from manim import UR


class SequenceDiagramsScene(CodeScene):
    def construct(self):
        diagram: SequenceDiagram = AutoScaled(SequenceDiagram())
        test, browser, database = diagram.add_objects("Test", "Browser", "Database")
        self.wait()

        test.to(database, "Set up initial data")
        test.to(browser, "Starts a Chrome instance,\noften headless")
        test.to(browser, "Issues commands")
        browser.to(test, "Returns element data")
        test.to(database, "Run SQL queries")
        test.to(test, "Asserts based on the data")
        test.to(test, "Another go")

        diagram.to_edge(UR)
        self.play(ShowCreation(diagram))
        for interaction in diagram.get_interactions():
            self.play(ShowCreation(interaction))
            self.wait()

        self.play_movie("/home/mrdon/Videos/browser-tests/02-test-notifications.mkv")


        self.clear()

        notif_code: PartialCode = AutoScaled(PartialCode(path="/home/mrdon/dev/sleuth/sleuth/apps/account/tests/selenium/test_notifications.py",
                                            start_line=29, end_line=43))
        self.play(ShowCreation(notif_code))
        self.wait()
        self.play(HighlightLine(notif_code, 30))
        self.wait()
        self.play(HighlightLines(notif_code, 31))
        self.wait()
        self.play_movie("/home/mrdon/Videos/browser-tests/02-login.mkv")

        self.clear()

        login_code: PartialCode = AutoScaled(
            PartialCode(path="/home/mrdon/dev/sleuth/sleuth/apps/account/tests/selenium/login_page.py",
                        start_line=18, end_line=27))
        self.play(ShowCreation(login_code))
        self.wait()
        self.play(HighlightLines(login_code, start=19, end=27))
        self.wait()

        self.play_movie("/home/mrdon/Videos/browser-tests/02-login-to-test-notifications.mkv")

        self.clear()

        notif_code: PartialCode = AutoScaled(
            PartialCode(path="/home/mrdon/dev/sleuth/sleuth/apps/account/tests/selenium/test_notifications.py",
                        start_line=29, end_line=43))

        self.add(notif_code)
        self.highlight_line(notif_code, 32)
        self.wait()
        self.highlight_lines(notif_code, 36, 38)
        self.wait()

        self.highlight_line(notif_code, 40)
        self.wait()

        # add voiceover bits

        self.clear()
        ui_code: PartialCode = AutoScaled(PartialCode(path="/home/mrdon/dev/sleuth/sleuth/apps/account/tests/selenium/login_page.py",
                        start_line=74, end_line=81))
        self.play(ShowCreation(ui_code))
        self.wait()




