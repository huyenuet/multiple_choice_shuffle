class Paragraph_List(object):
    def __init__(self, _doc):
        self.doc = _doc
        self.place = {}
        self.style_level_1 = 0
        self.style_level_2 = 64

    def set_count_of_level(self, level):
        if level == 1:
            self.style_level_1 += 1

            # every time start a new list (1.), nested-list will start over from A.
            self.style_level_2 = 64
        elif level == 2:
            self.style_level_2 += 1

    def add_item(self, item, level):
        if level == 1:
            sp = ""
        else:
            sp = "    "
            sp = sp * (level - 1)

        if level == 1:
            self.set_count_of_level(1)
            self.doc.add_paragraph(sp + str(self.style_level_1) + '. ' + item)
        elif level == 2:
            self.set_count_of_level(2)
            self.doc.add_paragraph(sp + chr(self.style_level_2) + '. ' + item)
