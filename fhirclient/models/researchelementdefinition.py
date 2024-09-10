# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ResearchElementDefinition).
# 2024, SMART Health IT.


from . import domainresource

class ResearchElementDefinition(domainresource.DomainResource):
    """ A population, intervention, or exposure definition.
    
    The ResearchElementDefinition resource describes a "PICO" element that
    knowledge (evidence, assertion, recommendation) is about.
    """
    
    resource_type = "ResearchElementDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.approvalDate = None
        """ When the research element definition was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._approvalDate = None
        """ Primitive extension for approvalDate. Type `FHIRPrimitiveExtension` """
        
        self.author = None
        """ Who authored the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._author = None
        """ Primitive extension for author. Type `FHIRPrimitiveExtension` """
        
        self.characteristic = None
        """ What defines the members of the research element.
        List of `ResearchElementDefinitionCharacteristic` items (represented as `dict` in JSON). """
        self._characteristic = None
        """ Primitive extension for characteristic. Type `FHIRPrimitiveExtension` """
        
        self.comment = None
        """ Used for footnotes or explanatory notes.
        List of `str` items. """
        self._comment = None
        """ Primitive extension for comment. Type `FHIRPrimitiveExtension` """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._contact = None
        """ Primitive extension for contact. Type `FHIRPrimitiveExtension` """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        self._copyright = None
        """ Primitive extension for copyright. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Natural language description of the research element definition.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.editor = None
        """ Who edited the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._editor = None
        """ Primitive extension for editor. Type `FHIRPrimitiveExtension` """
        
        self.effectivePeriod = None
        """ When the research element definition is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        self._effectivePeriod = None
        """ Primitive extension for effectivePeriod. Type `FHIRPrimitiveExtension` """
        
        self.endorser = None
        """ Who endorsed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._endorser = None
        """ Primitive extension for endorser. Type `FHIRPrimitiveExtension` """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        self._experimental = None
        """ Primitive extension for experimental. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Additional identifier for the research element definition.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Intended jurisdiction for research element definition (if
        applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.lastReviewDate = None
        """ When the research element definition was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._lastReviewDate = None
        """ Primitive extension for lastReviewDate. Type `FHIRPrimitiveExtension` """
        
        self.library = None
        """ Logic used by the ResearchElementDefinition.
        List of `str` items. """
        self._library = None
        """ Primitive extension for library. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name for this research element definition (computer friendly).
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ Why this research element definition is defined.
        Type `str`. """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
        self.relatedArtifact = None
        """ Additional documentation, citations, etc..
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        self._relatedArtifact = None
        """ Primitive extension for relatedArtifact. Type `FHIRPrimitiveExtension` """
        
        self.reviewer = None
        """ Who reviewed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._reviewer = None
        """ Primitive extension for reviewer. Type `FHIRPrimitiveExtension` """
        
        self.shortTitle = None
        """ Title for use in informal contexts.
        Type `str`. """
        self._shortTitle = None
        """ Primitive extension for shortTitle. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subjectCodeableConcept = None
        """ E.g. Patient, Practitioner, RelatedPerson, Organization, Location,
        Device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._subjectCodeableConcept = None
        """ Primitive extension for subjectCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.subjectReference = None
        """ E.g. Patient, Practitioner, RelatedPerson, Organization, Location,
        Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subjectReference = None
        """ Primitive extension for subjectReference. Type `FHIRPrimitiveExtension` """
        
        self.subtitle = None
        """ Subordinate title of the ResearchElementDefinition.
        Type `str`. """
        self._subtitle = None
        """ Primitive extension for subtitle. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Name for this research element definition (human friendly).
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.topic = None
        """ The category of the ResearchElementDefinition, such as Education,
        Treatment, Assessment, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._topic = None
        """ Primitive extension for topic. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ population | exposure | outcome.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Canonical identifier for this research element definition,
        represented as a URI (globally unique).
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        self.usage = None
        """ Describes the clinical usage of the ResearchElementDefinition.
        Type `str`. """
        self._usage = None
        """ Primitive extension for usage. Type `FHIRPrimitiveExtension` """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        self._useContext = None
        """ Primitive extension for useContext. Type `FHIRPrimitiveExtension` """
        
        self.variableType = None
        """ dichotomous | continuous | descriptive.
        Type `str`. """
        self._variableType = None
        """ Primitive extension for variableType. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Business version of the research element definition.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(ResearchElementDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ResearchElementDefinition, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("_approvalDate", "_approvalDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("_author", "_author", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("characteristic", "characteristic", ResearchElementDefinitionCharacteristic, True, None, True),
            ("_characteristic", "_characteristic", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("comment", "comment", str, True, None, False),
            ("_comment", "_comment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("_editor", "_editor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("_effectivePeriod", "_effectivePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("_endorser", "_endorser", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("_lastReviewDate", "_lastReviewDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("library", "library", str, True, None, False),
            ("_library", "_library", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("_relatedArtifact", "_relatedArtifact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("_reviewer", "_reviewer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("shortTitle", "shortTitle", str, False, None, False),
            ("_shortTitle", "_shortTitle", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("_subjectCodeableConcept", "_subjectCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("_subjectReference", "_subjectReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subtitle", "subtitle", str, False, None, False),
            ("_subtitle", "_subtitle", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("_topic", "_topic", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("_usage", "_usage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("_useContext", "_useContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("variableType", "variableType", str, False, None, False),
            ("_variableType", "_variableType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class ResearchElementDefinitionCharacteristic(backboneelement.BackboneElement):
    """ What defines the members of the research element.
    
    A characteristic that defines the members of the research element. Multiple
    characteristics are applied with "and" semantics.
    """
    
    resource_type = "ResearchElementDefinitionCharacteristic"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definitionCanonical = None
        """ What code or expression defines members?.
        Type `str`. """
        self._definitionCanonical = None
        """ Primitive extension for definitionCanonical. Type `FHIRPrimitiveExtension` """
        
        self.definitionCodeableConcept = None
        """ What code or expression defines members?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._definitionCodeableConcept = None
        """ Primitive extension for definitionCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.definitionDataRequirement = None
        """ What code or expression defines members?.
        Type `DataRequirement` (represented as `dict` in JSON). """
        self._definitionDataRequirement = None
        """ Primitive extension for definitionDataRequirement. Type `FHIRPrimitiveExtension` """
        
        self.definitionExpression = None
        """ What code or expression defines members?.
        Type `Expression` (represented as `dict` in JSON). """
        self._definitionExpression = None
        """ Primitive extension for definitionExpression. Type `FHIRPrimitiveExtension` """
        
        self.exclude = None
        """ Whether the characteristic includes or excludes members.
        Type `bool`. """
        self._exclude = None
        """ Primitive extension for exclude. Type `FHIRPrimitiveExtension` """
        
        self.participantEffectiveDateTime = None
        """ What time period do participants cover.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._participantEffectiveDateTime = None
        """ Primitive extension for participantEffectiveDateTime. Type `FHIRPrimitiveExtension` """
        
        self.participantEffectiveDescription = None
        """ What time period do participants cover.
        Type `str`. """
        self._participantEffectiveDescription = None
        """ Primitive extension for participantEffectiveDescription. Type `FHIRPrimitiveExtension` """
        
        self.participantEffectiveDuration = None
        """ What time period do participants cover.
        Type `Duration` (represented as `dict` in JSON). """
        self._participantEffectiveDuration = None
        """ Primitive extension for participantEffectiveDuration. Type `FHIRPrimitiveExtension` """
        
        self.participantEffectiveGroupMeasure = None
        """ mean | median | mean-of-mean | mean-of-median | median-of-mean |
        median-of-median.
        Type `str`. """
        self._participantEffectiveGroupMeasure = None
        """ Primitive extension for participantEffectiveGroupMeasure. Type `FHIRPrimitiveExtension` """
        
        self.participantEffectivePeriod = None
        """ What time period do participants cover.
        Type `Period` (represented as `dict` in JSON). """
        self._participantEffectivePeriod = None
        """ Primitive extension for participantEffectivePeriod. Type `FHIRPrimitiveExtension` """
        
        self.participantEffectiveTimeFromStart = None
        """ Observation time from study start.
        Type `Duration` (represented as `dict` in JSON). """
        self._participantEffectiveTimeFromStart = None
        """ Primitive extension for participantEffectiveTimeFromStart. Type `FHIRPrimitiveExtension` """
        
        self.participantEffectiveTiming = None
        """ What time period do participants cover.
        Type `Timing` (represented as `dict` in JSON). """
        self._participantEffectiveTiming = None
        """ Primitive extension for participantEffectiveTiming. Type `FHIRPrimitiveExtension` """
        
        self.studyEffectiveDateTime = None
        """ What time period does the study cover.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._studyEffectiveDateTime = None
        """ Primitive extension for studyEffectiveDateTime. Type `FHIRPrimitiveExtension` """
        
        self.studyEffectiveDescription = None
        """ What time period does the study cover.
        Type `str`. """
        self._studyEffectiveDescription = None
        """ Primitive extension for studyEffectiveDescription. Type `FHIRPrimitiveExtension` """
        
        self.studyEffectiveDuration = None
        """ What time period does the study cover.
        Type `Duration` (represented as `dict` in JSON). """
        self._studyEffectiveDuration = None
        """ Primitive extension for studyEffectiveDuration. Type `FHIRPrimitiveExtension` """
        
        self.studyEffectiveGroupMeasure = None
        """ mean | median | mean-of-mean | mean-of-median | median-of-mean |
        median-of-median.
        Type `str`. """
        self._studyEffectiveGroupMeasure = None
        """ Primitive extension for studyEffectiveGroupMeasure. Type `FHIRPrimitiveExtension` """
        
        self.studyEffectivePeriod = None
        """ What time period does the study cover.
        Type `Period` (represented as `dict` in JSON). """
        self._studyEffectivePeriod = None
        """ Primitive extension for studyEffectivePeriod. Type `FHIRPrimitiveExtension` """
        
        self.studyEffectiveTimeFromStart = None
        """ Observation time from study start.
        Type `Duration` (represented as `dict` in JSON). """
        self._studyEffectiveTimeFromStart = None
        """ Primitive extension for studyEffectiveTimeFromStart. Type `FHIRPrimitiveExtension` """
        
        self.studyEffectiveTiming = None
        """ What time period does the study cover.
        Type `Timing` (represented as `dict` in JSON). """
        self._studyEffectiveTiming = None
        """ Primitive extension for studyEffectiveTiming. Type `FHIRPrimitiveExtension` """
        
        self.unitOfMeasure = None
        """ What unit is the outcome described in?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._unitOfMeasure = None
        """ Primitive extension for unitOfMeasure. Type `FHIRPrimitiveExtension` """
        
        self.usageContext = None
        """ What code/value pairs define members?.
        List of `UsageContext` items (represented as `dict` in JSON). """
        self._usageContext = None
        """ Primitive extension for usageContext. Type `FHIRPrimitiveExtension` """
        
        super(ResearchElementDefinitionCharacteristic, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ResearchElementDefinitionCharacteristic, self).elementProperties()
        js.extend([
            ("definitionCanonical", "definitionCanonical", str, False, "definition", True),
            ("_definitionCanonical", "_definitionCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("definitionCodeableConcept", "definitionCodeableConcept", codeableconcept.CodeableConcept, False, "definition", True),
            ("_definitionCodeableConcept", "_definitionCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("definitionDataRequirement", "definitionDataRequirement", datarequirement.DataRequirement, False, "definition", True),
            ("_definitionDataRequirement", "_definitionDataRequirement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("definitionExpression", "definitionExpression", expression.Expression, False, "definition", True),
            ("_definitionExpression", "_definitionExpression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("exclude", "exclude", bool, False, None, False),
            ("_exclude", "_exclude", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("participantEffectiveDateTime", "participantEffectiveDateTime", fhirdatetime.FHIRDateTime, False, "participantEffective", False),
            ("_participantEffectiveDateTime", "_participantEffectiveDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("participantEffectiveDescription", "participantEffectiveDescription", str, False, None, False),
            ("_participantEffectiveDescription", "_participantEffectiveDescription", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("participantEffectiveDuration", "participantEffectiveDuration", duration.Duration, False, "participantEffective", False),
            ("_participantEffectiveDuration", "_participantEffectiveDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("participantEffectiveGroupMeasure", "participantEffectiveGroupMeasure", str, False, None, False),
            ("_participantEffectiveGroupMeasure", "_participantEffectiveGroupMeasure", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("participantEffectivePeriod", "participantEffectivePeriod", period.Period, False, "participantEffective", False),
            ("_participantEffectivePeriod", "_participantEffectivePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("participantEffectiveTimeFromStart", "participantEffectiveTimeFromStart", duration.Duration, False, None, False),
            ("_participantEffectiveTimeFromStart", "_participantEffectiveTimeFromStart", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("participantEffectiveTiming", "participantEffectiveTiming", timing.Timing, False, "participantEffective", False),
            ("_participantEffectiveTiming", "_participantEffectiveTiming", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("studyEffectiveDateTime", "studyEffectiveDateTime", fhirdatetime.FHIRDateTime, False, "studyEffective", False),
            ("_studyEffectiveDateTime", "_studyEffectiveDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("studyEffectiveDescription", "studyEffectiveDescription", str, False, None, False),
            ("_studyEffectiveDescription", "_studyEffectiveDescription", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("studyEffectiveDuration", "studyEffectiveDuration", duration.Duration, False, "studyEffective", False),
            ("_studyEffectiveDuration", "_studyEffectiveDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("studyEffectiveGroupMeasure", "studyEffectiveGroupMeasure", str, False, None, False),
            ("_studyEffectiveGroupMeasure", "_studyEffectiveGroupMeasure", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("studyEffectivePeriod", "studyEffectivePeriod", period.Period, False, "studyEffective", False),
            ("_studyEffectivePeriod", "_studyEffectivePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("studyEffectiveTimeFromStart", "studyEffectiveTimeFromStart", duration.Duration, False, None, False),
            ("_studyEffectiveTimeFromStart", "_studyEffectiveTimeFromStart", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("studyEffectiveTiming", "studyEffectiveTiming", timing.Timing, False, "studyEffective", False),
            ("_studyEffectiveTiming", "_studyEffectiveTiming", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("unitOfMeasure", "unitOfMeasure", codeableconcept.CodeableConcept, False, None, False),
            ("_unitOfMeasure", "_unitOfMeasure", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("usageContext", "usageContext", usagecontext.UsageContext, True, None, False),
            ("_usageContext", "_usageContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import contactdetail
from . import datarequirement
from . import duration
from . import expression
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import relatedartifact
from . import timing
from . import usagecontext
