from TestResources import constants
from TestResources.readdata import XLSReader

def getcelldata(testcasename, path):
    datalist =[]
    testcasename = "TestB"
    xls = XLSReader(path)

    teststartrowindex = 0
    while not (xls.getCellData(constants.DATASHEET, teststartrowindex,0) == testcasename):
        teststartrowindex += 1

    colstartrowindex = teststartrowindex + 1
    datastartrowindex = colstartrowindex +1

    maxrow = 0
    try:
        while not (xls.chekemptycell(constants.DATASHEET, datastartrowindex+maxrow, 0)):
            maxrow += 1
    except Exception:
        pass

    maxcol = 0
    try:
        while not (xls.chekemptycell(constants.DATASHEET, colstartrowindex+maxcol, maxcol)):
            maxcol += 1
    except Exception:
        pass


    for rNum in range(datastartrowindex,datastartrowindex+maxrow):
        datadictionary = {}
        for cNum in range(0,maxcol):
            datakey = xls.getCellData(constants.DATASHEET, colstartrowindex, cNum)
            dataValue = xls.getCellData(constants.DATASHEET, rNum, cNum)

            datadictionary[datakey] = dataValue
        datalist.append(datadictionary)
    return datalist

def isRunnable(testcasename,path):
    xls = XLSReader(path)
    rows = xls.getRowcount(constants.TESTSHEET)

    for rNum in range(0, rows):
        tname = xls.getCellDataByColName(constants.TESTSHEET, rNum, constants.TCID)

        if (tname==testcasename):
            runmode = xls.getCellDataByColName(constants.TESTSHEET, rNum, constants.RUNMODE)
            if (runmode ==constants.RUNMODE_Y):
                return True
            else:
                return False



