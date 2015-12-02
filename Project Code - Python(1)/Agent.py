# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
from PIL import Image
from PIL import ImageChops
from itertools import izip
#import copy
#import operator
import math, operator
class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an integer representing its
    # answer to the question: "1", "2", "3", "4", "5", or "6". These integers
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName() (as Strings).
    #
    # In addition to returning your answer at the end of the method, your Agent
    # may also call problem.checkAnswer(int givenAnswer). The parameter
    # passed to checkAnswer should be your Agent's current guess for the
    # problem; checkAnswer will return the correct answer to the problem. This
    # allows your Agent to check its answer. Note, however, that after your
    # agent has called checkAnswer, it will *not* be able to change its answer.
    # checkAnswer is used to allow your Agent to learn from its incorrect
    # answers; however, your Agent cannot change the answer to a question it
    # has already answered.
    #
    # If your Agent calls checkAnswer during execution of Solve, the answer it
    # returns will be ignored; otherwise, the answer returned at the end of
    # Solve will be taken as your Agent's answer to this problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.

    ##  MSE calculator
    '''def mse(imageA, imageB):
        # the 'Mean Squared Error' between the two images is the
	  # sum of the squared difference between the two images;
	  # NOTE: the two images must have the same dimension
	  err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	  err /= float(imageA.shape[0] * imageA.shape[1])
	
	  # return the MSE, the lower the error, the more "similar"
	  # the two images are
	  return err
 
       #p=(p1) and q=(q1). e(p,q)=sqrt((p1-q1)^2)=abs(p1-q1)
    def euclid(imageA, imageB):
        print "ha"'''
 
    '''def computeRms(file1, file2):
        image1 = Image.open(file1).convert('gray')
        image2 = Image.open(file2).convert('gray')
        h1 = image1.histogram()
        h2 = image2.histogram()
        rms = math.sqrt(reduce(operator.add,
                               map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
        return rms '''
        
    '''def contrived ():
        #numberOfBlackPixels = sum(sum(grayImage == 0));
        #numberOfWhitePixels = sum(sum(grayImage == 255));'''
    
    def computeRms(self, file1, file2):
        image1 = Image.open(file1.visualFilename).convert("L")
        image2 = Image.open(file2.visualFilename).convert("L")
        h1 = image1.histogram()
        h2 = image2.histogram()
        rms = math.sqrt(reduce(operator.add,
                               map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
        return rms
    
    def rmsdiff(self, im1, im2):
        #"Calculate the root-mean-square difference between two images"
        image1 = Image.open(im1.visualFilename).convert("L")
        image2 = Image.open(im2.visualFilename).convert("L") 
        diff = ImageChops.difference(image1, image2)
        h = diff.histogram()
        sq = (value*(idx**2) for idx, value in enumerate(h))
        sum_of_squares = sum(sq)
        rms = math.sqrt(sum_of_squares/float(image1.size[0] * image1.size[1]))
        return rms

    def euclid(self, image1, image2):
        euclid = 0
        diff = 0
        image1 = Image.open(image1.visualFilename).convert("L")
        image2 = Image.open(image2.visualFilename).convert("L")
        image1l = image1.load()
        image2l = image2.load()
        for i in range(0, image1.size[0]):
            for j in range(0, image2.size[1]):
                diff = image1l[i,j]-image2l[i,j]
                euclid += math.pow(diff,2)
        euclid = math.sqrt(euclid)
        return euclid 
        
    def imed(self, im1, im2):
        i1 = Image.open(im1.visualFilename).convert("L")
        i2 = Image.open(im2.visualFilename).convert("L")
        pixels1 = i1.getdata()          # get the pixels as a flattened sequence
        pixels2 =i2.getdata() 
        black_thresh = 50
        nblack = 0
        nblack2 = 0
        for pixel in pixels1:
            if pixel < black_thresh:
                nblack += 1
        n = len(pixels1)
        
        for pixel in pixels2:
            if pixel < black_thresh:
                nblack2 += 1
        n2 = len(pixels2)

        return 1
        
       
       
    def Solve(self, problem):
        solArray = []
        figureA = " "
        figureB = " "
        figureC = " "
        figureD = " "
        figureG = " "
        figureF = " "
        solnum = 1
        rmsCtoAns = 0 
        if problem.problemType == "2x2":
            print problem.problemType
            #print "problem has verbal part!"
            for figureName in problem.figures:
                #thisFigure = problem.figures[figureName]
                if figureName == "A":
                    figureA = problem.figures['A']
                elif figureName == "B":
                    figureB = problem.figures['B'] 
                elif figureName == "C":                    
                    figureC = problem.figures['C']
                elif(not figureName.isalpha()):
                    solfig = problem.figures[str(solnum)]
                    solnum += 1
                    rmsCtoAns = self.rmsdiff(figureC, solfig)
                    solArray.append(rmsCtoAns)
                    if figureName == "6":
                        rmsATB = self.rmsdiff(figureA, figureB)
                        for sol in solArray:
                            print "rmsATB--> " + str(rmsATB) + " rmsCto#--> "+ str(sol)
                        
                        print "######################################################"                        
                        solArray = []
                        figureA = " "
                        figureB = " "
                        figureC = " "
                        solnum = 1
                        rmsCtoAns = 0         
                        
        elif (problem.problemType == "3x3"):
            print problem.problemType
            #print "problem has verbal part!"
            for figureName in problem.figures:
                #thisFigure = problem.figures[figureName]
                print figureName
                if figureName == "A":
                    figureD = problem.figures['A']
                    rat = Image.open(figureD.visualFilename)
                    rat.show()
                elif figureName == "G":
                    figureG = problem.figures['G'] 
                elif figureName == "F":                    
                    figureF = problem.figures['F']
                elif(not figureName.isalpha()):
                    solfig = problem.figures[str(solnum)]
                    solnum += 1
                    rmsCtoAns = self.euclid(figureF, solfig)
                    solArray.append(rmsCtoAns)
                    if figureName == "8":
                        rmsATB = self.euclid(figureD, figureG)
                        for sol in solArray:
                            b = 1
                            #print "lowrt"
                            #print "rmsATB--> " + str(rmsATB) + " rmsCto#--> "+ str(sol)
                        
                        print "######################################################"                        
                        solArray = []
                        figureA = " "
                        figureB = " "
                        figureC = " "
                        solnum = 1
                        rmsCtoAns = 0 
        #end of calli            
        return -1
                    
                    
    
