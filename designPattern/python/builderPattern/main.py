from concreateBuildar import HTMLBuilder, TextBuilder

"""
物を作るときに違う素材のオブジェクトを作る
"""


# Directorのフォーマットで作成する。
class Director(object):
    def construct(self, builder):
        """
        ここでインスタンスが実行される。
        """
        all_str = ""
        all_str += builder.build_title("Monthly Report")
        all_str += builder.build_header("-------")
        all_str += builder.build_contents(["Monday: 20", "Tuesday: 30"])
        all_str += builder.build_footer("-*-*-*-")
        return all_str


if __name__ == "__main__":
    html = Director().construct(HTMLBuilder())
    text = Director().construct(TextBuilder())
    print(html)
