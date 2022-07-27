class Table:
    # Assigned in get_total_width()
    column_widths = []

    def __init__(self, array):
        self.array = array
        self.number_of_columns = 0
        for row in self.array:
            if len(row) > self.number_of_columns:
                self.number_of_columns = len(row)
        self.column_widths = [0] * self.number_of_columns
        self.calc_column_widths()

    def calc_column_widths(self):
        for row in self.array:
            for col_i in range(0, len(row)):
                if len(row[col_i]) > self.column_widths[col_i]:
                    self.column_widths[col_i] = len(row[col_i])
        return

    def _draw_top_border(self):
        """
        Draws the top border of the table.
        """
        top_border = "╔"
        col = 0
        for i in self.column_widths:
            top_border += "═" * i
            if col < len(self.column_widths) - 1:
                top_border += "╦"
            else:
                top_border += "╗"
            col += 1
        print(top_border)

    def _draw_rows(self):
        """
        Draws the rows of the table.

        """
        for r in range(0, len(self.array)):
            row_string = "║"
            col = 0
            while col < self.number_of_columns:
                if col < len(self.array[r]):
                    row_string += self.array[r][col].ljust(
                        self.column_widths[col])
                else:
                    row_string += "".ljust(self.column_widths[col])
                row_string += "║"
                col += 1
            print(row_string)
            # draw a horizontal line
            row_string = "╠" if r < len(self.array) - 1 else "╚"
            col = 0
            for i in self.column_widths:
                row_string += "═" * i
                if col < len(self.column_widths) - 1:
                    row_string += "╬" if r < len(self.array) - 1 else "╩"
                else:
                    row_string += "╣" if r < len(self.array) - 1 else "╝"
                col += 1
            print(row_string)

    def draw(self):
        self._draw_top_border()
        self._draw_rows()
        return
