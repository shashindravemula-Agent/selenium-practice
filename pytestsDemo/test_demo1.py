#any pytest file should start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only
#method name should have sense
#-k stands for method names execution, -s logs in output, -v stands for more info (like metadata)
#you can run specific file with py.test <filename>
#you can mark (tag) tests @pytest.mark.smoke and then run with -m in terminal (it runs for the smoke)
#you can skip test with @pytest.mark.skip
#pytest.mark.xfail
#fixtures are used as setup and tear down methods for test cases - confest file to generalize fixture.
#fixture and make it available to all test cases
#datadriven and parameterization can be done with return statements in list format, rahul said it is in tuple why i dont know while those are declared in the square brackets.
#when you define fixture scope to class only, it will run once before class is initiated and at the end.
#to generate html report we need to use this log in terminal "py.test --html=report.html -s" after installing "pip install pytest-html"
def test_firstProgram(setup):
    print("Hello")

def test_thirdProgram(setup):
    msg = "Hello"
    assert msg == "Hi", "The message did not match"

def test_CrossBrowser(CrossBrowser):
    print(CrossBrowser)
    print(CrossBrowser[2])