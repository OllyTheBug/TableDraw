class Table:
    # Assigned in get_total_width()
    longest_row = None
    def __init__(self, array):
        self.array = array
        self.width = self.get_total_width()

    def get_total_width(self):
        """
        Returns the width of the widest row, and sets the width-defining row.
        """
        highest = 0
        for row in self.array:
            total_width = 0
            for col in row:
                total_width += len(col)
            if total_width > highest:
                highest = total_width
                self.longest_row = row
                
        return highest
    
    def draw_top_border(self):
        """
        Draws the top border of the table.
        """
        top_border = "╔"
        for i in self.longest_row:
            for e in range(0, len(i)):
                top_border += "═"
            # if i is not the last element, add a "╦"
            if i is not self.longest_row[-1]:
                top_border += "╦"
            else:
                top_border += "╗"
        
        print(top_border)
    
    def draw_rows(self):
        """
        Draws the rows of the table, and the bottom border.
        """
        for row in self.array:
            row_string = "║"
            for col_i in range(0, len(row)):
                row_string += row[col_i]
                # padding = len of longest_row[col_i] - len(row[col_i])
                row_string += " " * (len(self.longest_row[col_i])-len(row[col_i]))
                row_string += "║"
            print(row_string)
            #draw horizontal borders
            if row == self.array[-1]:
                row_string = "╚"
                for i in self.longest_row:
                    for e in range(0, len(i)):
                        row_string += "═"
                    # if i is not the last element, add a "╩"
                    if i is not self.longest_row[-1]:
                        row_string += "╩"
                    else:
                        row_string += "╝"
                print(row_string)
                    
            else:
                row_string = "╠"
                for i in self.longest_row:
                    for e in range(0, len(i)):
                        row_string += "═"
                    # if i is not the last element, add a "╬"
                    if i is not self.longest_row[-1]:
                        row_string += "╬"
                    else:
                        row_string += "╣"
                print(row_string)
        

test_array = [["abbcbdc","ab"],
              ["ab","abc"],
              ["a","bc"]]
test_table = Table(test_array)

print(test_table.longest_row)
test_table.draw_top_border()
test_table.draw_rows()