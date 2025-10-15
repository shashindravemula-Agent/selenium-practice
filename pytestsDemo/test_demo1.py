#any pytest file should start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only
#method name should have sense
#-k stands for method names execution, -s logs in output, -v stands for more info (like metadata)
#you can run specific file with py.test <filename>
#you can mark (tag) tests @pytest.mark.smoke and then run with -m in terminal (it runs for the smoke)
#you can skip test with @pytest.mark.skip

def test_firstProgram():
    print("Hello")

def test_thirdProgram():
    msg = "Hello"
    assert msg == "Hi", "The message did not match"