import pytest
from TestResources import constants
from TestResources.readingexcel import getcelldata, isRunnable

class TestA:
    @pytest.mark.parametrize("argvals",getcelldata("TestA", constants.XLS_FILEPATH))
    def test_a(self,argvals):

        testrunmode = isRunnable("TestA", constants.XLS_FILEPATH)
        datarunmode = argvals[constants.RUNMODE]
        if(testrunmode):
            print(argvals)
            if(datarunmode==constants.RUNMODE_Y):
                pass
            else:
                pytest.skip("Testcase skipped due to runmode N on datasheet")
        else:
            pytest.skip("Testcase Skipped due to runmode N on testsheet")
