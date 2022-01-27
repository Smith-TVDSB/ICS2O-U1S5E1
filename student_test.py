import pytest
import student 


def test_five():
    input_values=['5']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert '31.4'in output[1] and '78.5' in output[1], "Should have both area and circumference"


def test_three():
    input_values=['3']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert '18.84'in output[1] and '28.2' in output[1], "Should have both area and circumference"
    
def test_two_point_five():
    input_values=['2.5']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert '15.7'in output[1] and '19.6' in output[1], "Should have both area and circumference"
