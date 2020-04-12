class Matrix:

    def __init__(self, matrix_string):
        self.matrix = self._create_matrix(matrix_string)

    def row(self, index):
        return [int(i) for i in self.matrix[index-1]]

    def column(self, index):
        return [int(row[index-1]) for row in self.matrix]

    @staticmethod
    def _create_matrix(matrix_string: str):
        input_values_lines_list = matrix_string.split("\n")

        return [input_values_lines_list[i].split(" ") for i in range(len(input_values_lines_list))]
