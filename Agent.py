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
#import copy
#import operator
import math
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
    
    def rotate90_Image(self, im):
        lrRot = im.transpose(Image.ROTATE_90)
        return lrRot
        
    def rotate180_Image(self, im):
        lrRot = im.transpose(Image.ROTATE_180)
        return lrRot    

    def lRreflectImage(self, im):
        lrReflct = im.transpose(Image.FLIP_LEFT_RIGHT)
        return lrReflct
       
    def tDreflectImage(self, im):
        tdReflect = im.transpose(Image.FLIP_TOP_BOTTOM)
        return tdReflect
   
    def subtractImage(self, im1, im2):
        imagediff = ImageChops.subtract(im1, im2)
       
        """Return the number of pixels in img that are not black.
        img must be a PIL.Image object in mode RGB.

        """
        bbox = imagediff.getbbox()
        if not bbox: return 0
        return sum(imagediff.crop(bbox).point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())        
          
        #root mean square error   
    def rmsdiff(self, im1, im2):
        #"Calculate the root-mean-square difference between two images"
        #image1 = image1.resize((8, 8), Image.ANTIALIAS)  # Reduce it's size.
        #image2 = image2.resize((8, 8), Image.ANTIALIAS)  # Reduce it's size.
        image1 = im1.convert('L')  # Convert it to grayscale.
        image2 = im2.convert('L')  # Convert it to grayscale.
        diff = ImageChops.difference(image1, image2)
        h = diff.histogram()
        sq = (value*(idx**2) for idx, value in enumerate(h))
        sum_of_squares = sum(sq)
        rms = math.sqrt(sum_of_squares/float(image1.size[0] * image1.size[1]))
        return rms

    def handleList (self, dupl, sol3X3, array3X3, index):
        indext = index
        indexpx3 = -1
        if len(dupl) == 0:
            print "stored index" + str(index)
            return str(index)
        elif len(dupl) > 0:
            if len(dupl) == 2:
                minpxl = 100000000000000
                for i in dupl:
                    print sol3X3
                    #dex = dupl[i]
                    if sol3X3[i] == 0:
                        print "stored index" + str(index)
                        return str(index) 
                    else: 
                        pixIm = (array3X3[i]).convert("1")
                        black, white = pixIm.getcolors()
                        pixCount = black[0] 
                        if pixCount < minpxl:
                            pixCount = minpxl
                        indexpx3 = str(i +1)
                        indext = indexpx3                     
        elif len(dupl) > 2:
            minpxl = 0
            for i in dupl:
                if sol3X3[i] == 0:
                    return str(index)
                else: 
                    pixIm = (array3X3[i]).convert("1")
                    black, white = pixIm.getcolors()
                    pixCount = black[0] 
                    if pixCount > minpxl:
                        pixCount = minpxl
                        indexpx3 = str(i +1)
                        indext = indexpx3
        return indext
            
    def Solve(self, problem):
        
        if problem.problemType == "2x2":
            print problem.problemType
            # preinitiallize array with 0s
            array2X2 = []
            for i in xrange(0,6):
               array2X2.append(0)

            #print "problem has verbal part!"
            for figureName in problem.figures:
                #thisFigure = problem.figures[figureName]
                if figureName == "A":
                    figureA = problem.figures['A']
                    figA= Image.open(figureA.visualFilename)
                elif figureName == "B":
                    figureB = problem.figures['B']
                    figB = Image.open(figureB.visualFilename)
                elif figureName == "C":                    
                    figureC = problem.figures['C']
                    figC= Image.open(figureC.visualFilename)
                elif(not figureName.isalpha()):
                    if figureName == "1":
                        solfig1 = problem.figures["1"]
                        solfg1 = Image.open(solfig1.visualFilename)
                        array2X2[0] = solfg1 
                    elif figureName == "2":
                        solfig2 = problem.figures["2"]
                        solfg2 = Image.open(solfig2.visualFilename)
                        array2X2[1] = solfg2
                    elif figureName == "3":     
                        solfig3 = problem.figures["3"]
                        solfg3 = Image.open(solfig3.visualFilename)
                        array2X2[2] = solfg3
                    elif figureName == "4":                    
                        solfig4 = problem.figures["4"]
                        solfg4 = Image.open(solfig4.visualFilename)
                        array2X2[3] = solfg4
                    elif figureName == "5":
                        solfig5 = problem.figures["5"]
                        solfg5 = Image.open(solfig5.visualFilename)
                        array2X2[4] = solfg5
                    elif figureName == "6":    
                        solfig6 = problem.figures["6"]
                        solfg6 = Image.open(solfig6.visualFilename)
                        array2X2[5] = solfg6

                        # pre-calculate transformations 
                        rotA90 = self.rotate90_Image(figA)
                        rotA180 = self.rotate180_Image(figA)
                        lrRltA = self.lRreflectImage(figA)
                        tDRltA = self.tDreflectImage(figA) 
                        #subim = self.subtractImage (self, im1, im2)
                        
                        if self.rmsdiff(rotA90, figB) == 0:
                            # use A to B transformations
                            rotC90 = self.rotate90_Image(figC)
                            index = -1
                            for sol in array2X2:
                                psol = self.rmsdiff(rotC90, sol)
                                if psol == 0:
                                    index = array2X2.index(sol)+1
                            return str(index)
                            
                        elif  self.rmsdiff(rotA90, figC) == 0:
                            #use A to C transformation
                            rotB90 = self.rotate90_Image(figB)
                            index = -1
                            for sol in array2X2:
                                psol = self.rmsdiff(rotB90, sol)
                                if psol == 0:
                                    index = array2X2.index(sol)+1
                            return str(index)
                            
                        elif self.rmsdiff(rotA180, figB) == 0:
                            # use A to B transformations
                            rotC180 = self.rotate90_Image(figC)
                            index = -1
                            for sol in array2X2:
                                psol = self.rmsdiff(rotC180, sol)
                                if psol == 0:
                                    index = array2X2.index(sol)+1
                            return str(index)
                            
                        elif  self.rmsdiff(rotA180, figC) == 0:    
                            #use A to C transformations
                            rotB180 = self.rotate90_Image(figB)
                            index = -1
                            for sol in array2X2:
                                psol = self.rmsdiff(rotB180, sol)
                                if psol == 0:
                                    index = array2X2.index(sol)+1
                            return str(index)
                         
                        elif self.rmsdiff(lrRltA, figB) == 103:
                            # use A to B transformations
                            lRC = self.lRreflectImage(figC)
                            index = -1
                            for sol in array2X2:
                                psol = self.rmsdiff(lRC, sol)
                                if psol == 0:
                                    index = array2X2.index(sol)+1
                            return str(index)
                            
                        elif  self.rmsdiff(tDRltA, figC) == 247:
                            #use A to C to down transformation.
                            tDB = self.rotate90_Image(figB)
                            index = -1
                            for sol in array2X2:
                                psol = self.rmsdiff(tDB, sol)
                                if psol == 0:
                                    index = array2X2.index(sol)+1
                            return str(index)
        
                        else:
                            index = -1
                            min = 1000000000
                            abrms = self.rmsdiff(figA, figB)
                            for sol in array2X2:
                                psol = self.rmsdiff(figC, sol)
                                diff = math.fabs(abrms - psol)
                                if diff < min:
                                    min = diff
                                    index = array2X2.index(sol)+1
                            return str(index)
        
        
        #check if its a 3X3 problem        
        elif problem.problemType == "3x3":
            #comment here    
            print problem.problemType            
            # preinitiallize array with 0s
            array3X3 = []
            for i in xrange(0,8):
                array3X3.append(0)
            
            #sol array    
            sol3X3 = []
            for i in xrange(0,8):
                sol3X3.append(0)    
            
            #get figures    
            for figureName in problem.figures:
                if figureName == "D":
                    figureD = problem.figures['D']
                    figD= Image.open(figureD.visualFilename)
                elif figureName == "G":
                    figureG = problem.figures['G']
                    figG= Image.open(figureG.visualFilename)
                elif figureName == "F":
                    figureF = problem.figures['F']
                    figF= Image.open(figureF.visualFilename)
                elif(not figureName.isalpha()):
                    if figureName == "1":
                        solfig1 = problem.figures["1"]
                        solfg1 = Image.open(solfig1.visualFilename)
                        array3X3[0] = solfg1 
                    elif figureName == "2":
                        solfig2 = problem.figures["2"]
                        solfg2 = Image.open(solfig2.visualFilename)
                        array3X3[1] = solfg2
                    elif figureName == "3":     
                        solfig3 = problem.figures["3"]
                        solfg3 = Image.open(solfig3.visualFilename)
                        array3X3[2] = solfg3
                    elif figureName == "4":                    
                        solfig4 = problem.figures["4"]
                        solfg4 = Image.open(solfig4.visualFilename)
                        array3X3[3] = solfg4
                    elif figureName == "5":
                        solfig5 = problem.figures["5"]
                        solfg5 = Image.open(solfig5.visualFilename)
                        array3X3[4] = solfg5
                    elif figureName == "6":    
                        solfig6 = problem.figures["6"]
                        solfg6 = Image.open(solfig6.visualFilename)
                        array3X3[5] = solfg6    
                    elif figureName == "7":    
                        solfig7 = problem.figures["7"]
                        solfg7 = Image.open(solfig7.visualFilename)
                        array3X3[6] = solfg7   
                    elif figureName == "8":    
                        solfig8 = problem.figures["8"]
                        solfg8 = Image.open(solfig8.visualFilename)
                        array3X3[7] = solfg8
                        index = -1
                        ## begin computations here 
                        min  = 1000000000
                        for sol in array3X3:
                                diff = self.subtractImage(sol, figF)
                                diffdg = self.subtractImage(figD,figG)
                                sol3X3[array3X3.index(sol) ] = diff
                                print "d --> g "+ str(diffdg) + "f--># "+ str(diff)
                                if (diff != 0 and diff < min) :
                                    min = diff
                                    index = array3X3.index(sol)+1
                        
                        dupl = [i for i, x in enumerate(sol3X3) if sol3X3.count(x) > 1]       
                        print dupl
                        ind = self.handleList(dupl, sol3X3, array3X3, index)
                        return  str(ind) 
        return -1
