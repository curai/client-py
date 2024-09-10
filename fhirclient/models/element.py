# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Element).
# 2024, SMART Health IT.


from . import fhirabstractbase

class Element(fhirabstractbase.FHIRAbstractBase):
    """ Base for all elements.
    
    Base definition for all elements in a resource.
    """
    
    resource_type = "Element"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.extension = None
        """ Additional content defined by implementations.
        List of `Extension` items (represented as `dict` in JSON). """
        self._extension = None
        """ Primitive extension for extension. List of `FHIRPrimitiveExtension` """
        
        self.id = None
        """ Unique id for inter-element referencing.
        Type `str`. """
        self._id = None
        """ Primitive extension for id. Type `FHIRPrimitiveExtension` """
        
        super(Element, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Element, self).elementProperties()
        from . import extension
        js.extend([
            ("extension", "extension", extension.Extension, True, None, False),
            ("_extension", "_extension", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("id", "id", str, False, None, False),
            ("_id", "_id", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension
