#For one set of data x[]
#Or for two sets of data x[], y[]
#Add functionality for chi-squared test later
#Add function to directly calculate z values and area values
    #See if Python's math.erf(num) function can do this
import math

SD_MODES = ("sample","pop") #Improvement: make this a dictionary linking to the SD method to use, and put it after the SD methods

#Create normal table: one array for z, one array for area, then create two dictionaries, one going in each direction
#Area is decimal (out of 1, not 100)
def z(area):
def area(z):

def mean(x):
    b=0
    for a in x:
        b += a
    return b/len(x)

def rms(x):
    b=0
    for a in x:
        b += a**2
    return math.sqrt(b/len(x))

def deviationSquared(x):
    avg = mean(x)
    dev = []
    for i in range(0, len(x)):
        dev.append((x[i]-avg)**2)
    return dev
        
def popSD(x):
    avg = mean(x)
    deviationSum = 0
    for i in range(0, len(x)):
        deviationSum +=(x[i]-avg)**2
    return math.sqrt(deviationSum/len(x))

def sampleSD(x):
    avg = mean(x)
    deviationSum = 0
    for i in range(0, len(x)):
        deviationSum +=(x[i]-avg)**2
    return math.sqrt(deviationSum/(len(x)-1))

def SD(x, sdMode):
    if (sdMode == "pop"):
        return popSD(x)
    elif (sdMode == "sample"):
        return sampleSD(x)
    else:
        raise ValueError("Not a valid SD mode")

def rLinear(x, y, sdMode):
    if (len(x) != len(y)): raise ValueError("Arrays x and y are not of the same length, or are not actually arrays.")
    SDx, SDy = (0,0)
    xy = []
    for i in range(0, len(x)):
        xy.append(0)
    SDx = SD(x, sdMode)
    SDy = SD(y, sdMode)
    return (mean(xy) - (mean(x)*mean(y)))/(SDx * SDy)

def zValueSum(x, expectedSum):
    return (sum(x)-expectedSum)/(math.sqrt(len(x))*sampleSD(x))

def zValueMean(x, expectedMean):
    return (mean(experimentalData)-expectedMean)/(math.sqrt(len(x))*sampleSD(x)/len(x))

def pValueSum(x, expectedSum):
    return p(zValueSum(x, expectedSum))

def pValueMean(x, expectedMean):
    return p(zValueMean(x, expectedMean))

#Should be immutable
class BoxModel:
    def __init__(self, name, x, sdMode):
        self.NAME = name
        self.x = x
        if (sdMode in SD_MODES):
            self.SD_MODE = sdMode
        else:
            raise ValueError("Not a valid SD mode")
        self.SD = SD(sdMode)

    def SE_sum(n):
        return math.sqrt(n)*SD

    def SE_mean(n):
        return math.sqrt(n)*SD/n

    def expectedErrorSum(n, includeChance):
        return SE_sum(n)*z(includeChance)

    def expectedErrorMean(n, includeChance):
        return SE_sum(n)*z(includeChance)/n

#Should be immutable
#Box contains only 1s and 0s to represent probability of event happening
class BinaryBoxModel(BoxModel):
    def __init__(self, name, pA):
        self.NAME = name
        self.x = pA    #Note: x is a Number, the probability of event A (worth 1 point) occuring
        self.SD_MODE = "pop"
        self.SD = math.sqrt(pA*(1-pA))
        
#Should be immutable
class RegressionLine:
    def __init__(self, name_x, x, name_y, y, sdMode):
        self.x, self.y = (x,y)
        self.NAME_x, self.NAME_y = (name_x,name_y)
        if (sdMode in SD_MODES):
            self.SD_MODE = sdMode
        else:
            raise ValueError("Not a valid SD mode")
        self.MEAN_x = mean(x)
        self.MEAN_y = mean(y)
        self.SD_x = SD(x, sdMode)
        self.SD_y = SD(y, sdMode)
        self.R_XonY = rLinear(x, y, sdMode)
        self.R_YonX = rLinear(y, x, sdMode)

    def interpolateY(xVal):
        return MEAN_y + SD_y*R_XonY*((xVal - MEAN_x)/SD_x)

    def interpolateX(yVal):
        return MEAN_x + SD_x*R_YonX*((yVal - MEAN_y)/SD_y)

#Create graph with pygame?
print ("Successful execution")
