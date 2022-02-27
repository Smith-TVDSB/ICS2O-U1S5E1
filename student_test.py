import pytest
import student 


def test_five(capsys):
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
    student.main()

    out, err = capsys.readouterr()
    assert '31.4'in out and '78.5' in out, "Should have both area and circumference"


def test_three(capsys):
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
    student.main()

    out, err = capsys.readouterr()
    assert '18.84'in out and '28.2' in out, "Should have both area and circumference"
    
def test_two_point_five(capsys):
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
    student.main()
    
    out, err = capsys.readouterr()
    assert '15.7'in out and '19.6' in out, "Should have both area and circumference"
