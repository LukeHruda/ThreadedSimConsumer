"""
    Author: Eric Whalls 
    Global message handler as one instance for all parameters
    Hash mapped dictionary of objects

"""
from DesignPatterns import Singleton

# decorated
@Singleton 
class Parameters :
    """
        Inherit Singleton class so only one instance of all system parameters are present 
        Note:
        Parameters.
    """

    ## Add Parameter
    # Adds parameter object as an attribute of this singleton class
    def addParameter(self, parameter) :
        if not hasattr(self, parameter.name) : 
            setattr(self, parameter.name, parameter)
            print('added',parameter.name)
            print(getattr(self, parameter.name))
        else :
            raise ValueError("Parameter "+parameter.name+" already exists!")
    
    ## Remove Parameters
    # Takes in arguments as list or just single
    def removeParameters(self, parameters) :
        if not type(parameters) == list() :
            parameters = [parameters]
        
        # remove the parameter from memory and all hooked signals
        for parameter in parameters : 
            par = getattr(self, parameter.name)
            if not par == None :
                setattr(self, parameter.name, None)
                del par 

    def get(self) : 
        return dir(self)
