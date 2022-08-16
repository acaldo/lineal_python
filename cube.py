from arreglo import Arreglo

class Cube():
    def __init__(self,rows,cols,depth,fill_value=None):
        self.data=Arreglo(rows)
        for row in range(rows):
            self.data[row]=Arreglo(cols)
            for col in range(cols):
                self.data[row][col]=Arreglo(depth,fill_value)

    def get_height(self):
        """Return the height of the cube."""
        return len(self.data)

    def get_width(self):
        """Return the width of the cube."""
        return len(self.data[0])

    def get_depth(self):
        """Return the depth of the cube."""
        return len(self.data[0][0])

    def __getitem__(self,index):
        """Return the specified row of the cube."""
        return self.data[index]

    def __setitem__(self,index,new_value):
        """Set the specified row of the cube to new_value."""
        self.data[index]=new_value

    def __str__(self):
        """Return a string representation of the cube."""
        result = ''

        for row in range(self.get_height()):
            for column in range(self.get_width()):
                for depth in range(self.get_depth()):
                    result += str(self.data[row][column][depth]) + ' '
                result += '\n'

        return str(result)
    