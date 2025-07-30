from src.math_operation import Add,sub

def test_add():
    assert Add(2,3)==5
    assert Add(-1,1)==0
    assert Add(5,8)==13
    
    
def test_sub():
    assert sub(5,3)==2
    assert sub(6,3)==3
    assert sub(5,2)==3
    assert sub(5,3)==2