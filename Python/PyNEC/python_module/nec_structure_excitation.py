#nec_structure_excitation.py

#header generated by SWIG

import _PyNEC

def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name) or (name == "thisown"):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types

#end of the header generated by SWIG



#class "nec_struture_excitation"

class nec_structure_excitation(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, nec_structure_excitation, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, nec_structure_excitation, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C++ nec_structure_excitation instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)

	
    def get_frequency(*args):
    	"""
	Returns the frequency in Hertz.
	"""
    	return _PyNEC.nec_structure_excitation_get_frequency(*args)	
	
	
    def get_tag(*args):
    	"""
	Returns the array of segment tag numbers.
	"""
    	return _PyNEC.nec_structure_excitation_get_tag(*args)
	
	
    def get_segment(*args):
    	"""
	Returns the array of segment numbers.
	"""
    	return _PyNEC.nec_structure_excitation_get_segment(*args)
	
	
    def get_current(*args):
    	"""
	Returns the array of complex currents in Ampere.
	"""
    	return _PyNEC.nec_structure_excitation_get_current(*args)
	
	
    def get_voltage(*args):
    	"""
	Returns the array of complex voltages in Volt.
	"""
    	return _PyNEC.nec_structure_excitation_get_voltage(*args)
	
	
    def get_power(*args):
    	"""
	Returns the array of power in Watt.
	"""
    	return _PyNEC.nec_structure_excitation_get_power(*args)



class nec_structure_excitationPtr(nec_structure_excitation):
    def __init__(self, this):
        _swig_setattr(self, nec_structure_excitation, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, nec_structure_excitation, 'thisown', 0)
        _swig_setattr(self, nec_structure_excitation,self.__class__,nec_structure_excitation)
_PyNEC.nec_structure_excitation_swigregister(nec_structure_excitationPtr)

