# git """Files tests simple file read related operations"""

class SimpleFile(object):
    """SimpleFile tests using file read api to do some simple math"""
    def __init__(self, file_path):
        self.numbers = []
        with open(file_path) as f1:
            for line in f1:
                line = line.strip().split(" ")
                self.numbers.append(list(map(int,line)))
        """
        TODO: reads the file by path and parse content into two
        dimension array (numbers)
        https://stackoverflow.com/questions/1369526/what-is-the-python-keyword-with-used-for
        """
        

    def get_mean(self, line_number):
        line = self.numbers[line_number]
        return sum(line)/(len(line))
        

    def get_max(self, line_number):
        line = self.numbers[line_number]
        line.sort()
        line.reverse()
        return line[0]
        

    def get_min(self, line_number):
        line = self.numbers[line_number]
        line.sort()
        return line[0]
             

    def get_sum(self, line_number):
        return sum(self.numbers[line_number])