# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/PlanDefinition).
# 2024, SMART Health IT.


from . import domainresource

class PlanDefinition(domainresource.DomainResource):
    """ The definition of a plan for a series of actions, independent of any
    specific patient or context.
    
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical artifacts
    such as clinical decision support rules, order sets and protocols.
    """
    
    resource_type = "PlanDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ Action defined by the plan.
        List of `PlanDefinitionAction` items (represented as `dict` in JSON). """
        self._action = None
        """ Primitive extension for action. List of `FHIRPrimitiveExtension` """
        
        self.approvalDate = None
        """ When the plan definition was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._approvalDate = None
        """ Primitive extension for approvalDate. Type `FHIRPrimitiveExtension` """
        
        self.author = None
        """ Who authored the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._author = None
        """ Primitive extension for author. List of `FHIRPrimitiveExtension` """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._contact = None
        """ Primitive extension for contact. List of `FHIRPrimitiveExtension` """
        
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
        """ Natural language description of the plan definition.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.editor = None
        """ Who edited the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._editor = None
        """ Primitive extension for editor. List of `FHIRPrimitiveExtension` """
        
        self.effectivePeriod = None
        """ When the plan definition is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        self._effectivePeriod = None
        """ Primitive extension for effectivePeriod. Type `FHIRPrimitiveExtension` """
        
        self.endorser = None
        """ Who endorsed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._endorser = None
        """ Primitive extension for endorser. List of `FHIRPrimitiveExtension` """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        self._experimental = None
        """ Primitive extension for experimental. Type `FHIRPrimitiveExtension` """
        
        self.goal = None
        """ What the plan is trying to accomplish.
        List of `PlanDefinitionGoal` items (represented as `dict` in JSON). """
        self._goal = None
        """ Primitive extension for goal. List of `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Additional identifier for the plan definition.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. List of `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Intended jurisdiction for plan definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. List of `FHIRPrimitiveExtension` """
        
        self.lastReviewDate = None
        """ When the plan definition was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._lastReviewDate = None
        """ Primitive extension for lastReviewDate. Type `FHIRPrimitiveExtension` """
        
        self.library = None
        """ Logic used by the plan definition.
        List of `str` items. """
        self._library = None
        """ Primitive extension for library. List of `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name for this plan definition (computer friendly).
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ Why this plan definition is defined.
        Type `str`. """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
        self.relatedArtifact = None
        """ Additional documentation, citations.
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        self._relatedArtifact = None
        """ Primitive extension for relatedArtifact. List of `FHIRPrimitiveExtension` """
        
        self.reviewer = None
        """ Who reviewed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._reviewer = None
        """ Primitive extension for reviewer. List of `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subjectCodeableConcept = None
        """ Type of individual the plan definition is focused on.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._subjectCodeableConcept = None
        """ Primitive extension for subjectCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.subjectReference = None
        """ Type of individual the plan definition is focused on.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subjectReference = None
        """ Primitive extension for subjectReference. Type `FHIRPrimitiveExtension` """
        
        self.subtitle = None
        """ Subordinate title of the plan definition.
        Type `str`. """
        self._subtitle = None
        """ Primitive extension for subtitle. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Name for this plan definition (human friendly).
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.topic = None
        """ E.g. Education, Treatment, Assessment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._topic = None
        """ Primitive extension for topic. List of `FHIRPrimitiveExtension` """
        
        self.type = None
        """ order-set | clinical-protocol | eca-rule | workflow-definition.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Canonical identifier for this plan definition, represented as a URI
        (globally unique).
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        self.usage = None
        """ Describes the clinical usage of the plan.
        Type `str`. """
        self._usage = None
        """ Primitive extension for usage. Type `FHIRPrimitiveExtension` """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        self._useContext = None
        """ Primitive extension for useContext. List of `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Business version of the plan definition.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(PlanDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinition, self).elementProperties()
        js.extend([
            ("action", "action", PlanDefinitionAction, True, None, False),
            ("_action", "_action", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("_approvalDate", "_approvalDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("_author", "_author", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("_editor", "_editor", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("_effectivePeriod", "_effectivePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("_endorser", "_endorser", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("goal", "goal", PlanDefinitionGoal, True, None, False),
            ("_goal", "_goal", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("_lastReviewDate", "_lastReviewDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("library", "library", str, True, None, False),
            ("_library", "_library", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("_relatedArtifact", "_relatedArtifact", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("_reviewer", "_reviewer", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
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
            ("_topic", "_topic", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("_usage", "_usage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("_useContext", "_useContext", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class PlanDefinitionAction(backboneelement.BackboneElement):
    """ Action defined by the plan.
    
    An action or group of actions to be taken as part of the plan.
    """
    
    resource_type = "PlanDefinitionAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ A sub-action.
        List of `PlanDefinitionAction` items (represented as `dict` in JSON). """
        self._action = None
        """ Primitive extension for action. List of `FHIRPrimitiveExtension` """
        
        self.cardinalityBehavior = None
        """ single | multiple.
        Type `str`. """
        self._cardinalityBehavior = None
        """ Primitive extension for cardinalityBehavior. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Code representing the meaning of the action or sub-actions.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. List of `FHIRPrimitiveExtension` """
        
        self.condition = None
        """ Whether or not the action is applicable.
        List of `PlanDefinitionActionCondition` items (represented as `dict` in JSON). """
        self._condition = None
        """ Primitive extension for condition. List of `FHIRPrimitiveExtension` """
        
        self.definitionCanonical = None
        """ Description of the activity to be performed.
        Type `str`. """
        self._definitionCanonical = None
        """ Primitive extension for definitionCanonical. Type `FHIRPrimitiveExtension` """
        
        self.definitionUri = None
        """ Description of the activity to be performed.
        Type `str`. """
        self._definitionUri = None
        """ Primitive extension for definitionUri. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Brief description of the action.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.documentation = None
        """ Supporting documentation for the intended performer of the action.
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        self._documentation = None
        """ Primitive extension for documentation. List of `FHIRPrimitiveExtension` """
        
        self.dynamicValue = None
        """ Dynamic aspects of the definition.
        List of `PlanDefinitionActionDynamicValue` items (represented as `dict` in JSON). """
        self._dynamicValue = None
        """ Primitive extension for dynamicValue. List of `FHIRPrimitiveExtension` """
        
        self.goalId = None
        """ What goals this action supports.
        List of `str` items. """
        self._goalId = None
        """ Primitive extension for goalId. List of `FHIRPrimitiveExtension` """
        
        self.groupingBehavior = None
        """ visual-group | logical-group | sentence-group.
        Type `str`. """
        self._groupingBehavior = None
        """ Primitive extension for groupingBehavior. Type `FHIRPrimitiveExtension` """
        
        self.input = None
        """ Input data requirements.
        List of `DataRequirement` items (represented as `dict` in JSON). """
        self._input = None
        """ Primitive extension for input. List of `FHIRPrimitiveExtension` """
        
        self.output = None
        """ Output data definition.
        List of `DataRequirement` items (represented as `dict` in JSON). """
        self._output = None
        """ Primitive extension for output. List of `FHIRPrimitiveExtension` """
        
        self.participant = None
        """ Who should participate in the action.
        List of `PlanDefinitionActionParticipant` items (represented as `dict` in JSON). """
        self._participant = None
        """ Primitive extension for participant. List of `FHIRPrimitiveExtension` """
        
        self.precheckBehavior = None
        """ yes | no.
        Type `str`. """
        self._precheckBehavior = None
        """ Primitive extension for precheckBehavior. Type `FHIRPrimitiveExtension` """
        
        self.prefix = None
        """ User-visible prefix for the action (e.g. 1. or A.).
        Type `str`. """
        self._prefix = None
        """ Primitive extension for prefix. Type `FHIRPrimitiveExtension` """
        
        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """
        self._priority = None
        """ Primitive extension for priority. Type `FHIRPrimitiveExtension` """
        
        self.reason = None
        """ Why the action should be performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reason = None
        """ Primitive extension for reason. List of `FHIRPrimitiveExtension` """
        
        self.relatedAction = None
        """ Relationship to another action.
        List of `PlanDefinitionActionRelatedAction` items (represented as `dict` in JSON). """
        self._relatedAction = None
        """ Primitive extension for relatedAction. List of `FHIRPrimitiveExtension` """
        
        self.requiredBehavior = None
        """ must | could | must-unless-documented.
        Type `str`. """
        self._requiredBehavior = None
        """ Primitive extension for requiredBehavior. Type `FHIRPrimitiveExtension` """
        
        self.selectionBehavior = None
        """ any | all | all-or-none | exactly-one | at-most-one | one-or-more.
        Type `str`. """
        self._selectionBehavior = None
        """ Primitive extension for selectionBehavior. Type `FHIRPrimitiveExtension` """
        
        self.subjectCodeableConcept = None
        """ Type of individual the action is focused on.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._subjectCodeableConcept = None
        """ Primitive extension for subjectCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.subjectReference = None
        """ Type of individual the action is focused on.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subjectReference = None
        """ Primitive extension for subjectReference. Type `FHIRPrimitiveExtension` """
        
        self.textEquivalent = None
        """ Static text equivalent of the action, used if the dynamic aspects
        cannot be interpreted by the receiving system.
        Type `str`. """
        self._textEquivalent = None
        """ Primitive extension for textEquivalent. Type `FHIRPrimitiveExtension` """
        
        self.timingAge = None
        """ When the action should take place.
        Type `Age` (represented as `dict` in JSON). """
        self._timingAge = None
        """ Primitive extension for timingAge. Type `FHIRPrimitiveExtension` """
        
        self.timingDateTime = None
        """ When the action should take place.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._timingDateTime = None
        """ Primitive extension for timingDateTime. Type `FHIRPrimitiveExtension` """
        
        self.timingDuration = None
        """ When the action should take place.
        Type `Duration` (represented as `dict` in JSON). """
        self._timingDuration = None
        """ Primitive extension for timingDuration. Type `FHIRPrimitiveExtension` """
        
        self.timingPeriod = None
        """ When the action should take place.
        Type `Period` (represented as `dict` in JSON). """
        self._timingPeriod = None
        """ Primitive extension for timingPeriod. Type `FHIRPrimitiveExtension` """
        
        self.timingRange = None
        """ When the action should take place.
        Type `Range` (represented as `dict` in JSON). """
        self._timingRange = None
        """ Primitive extension for timingRange. Type `FHIRPrimitiveExtension` """
        
        self.timingTiming = None
        """ When the action should take place.
        Type `Timing` (represented as `dict` in JSON). """
        self._timingTiming = None
        """ Primitive extension for timingTiming. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ User-visible title.
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.transform = None
        """ Transform to apply the template.
        Type `str`. """
        self._transform = None
        """ Primitive extension for transform. Type `FHIRPrimitiveExtension` """
        
        self.trigger = None
        """ When the action should be triggered.
        List of `TriggerDefinition` items (represented as `dict` in JSON). """
        self._trigger = None
        """ Primitive extension for trigger. List of `FHIRPrimitiveExtension` """
        
        self.type = None
        """ create | update | remove | fire-event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(PlanDefinitionAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionAction, self).elementProperties()
        js.extend([
            ("action", "action", PlanDefinitionAction, True, None, False),
            ("_action", "_action", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("cardinalityBehavior", "cardinalityBehavior", str, False, None, False),
            ("_cardinalityBehavior", "_cardinalityBehavior", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("condition", "condition", PlanDefinitionActionCondition, True, None, False),
            ("_condition", "_condition", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("definitionCanonical", "definitionCanonical", str, False, "definition", False),
            ("_definitionCanonical", "_definitionCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("definitionUri", "definitionUri", str, False, "definition", False),
            ("_definitionUri", "_definitionUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("documentation", "documentation", relatedartifact.RelatedArtifact, True, None, False),
            ("_documentation", "_documentation", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("dynamicValue", "dynamicValue", PlanDefinitionActionDynamicValue, True, None, False),
            ("_dynamicValue", "_dynamicValue", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("goalId", "goalId", str, True, None, False),
            ("_goalId", "_goalId", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("groupingBehavior", "groupingBehavior", str, False, None, False),
            ("_groupingBehavior", "_groupingBehavior", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("input", "input", datarequirement.DataRequirement, True, None, False),
            ("_input", "_input", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("output", "output", datarequirement.DataRequirement, True, None, False),
            ("_output", "_output", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("participant", "participant", PlanDefinitionActionParticipant, True, None, False),
            ("_participant", "_participant", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("precheckBehavior", "precheckBehavior", str, False, None, False),
            ("_precheckBehavior", "_precheckBehavior", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("prefix", "prefix", str, False, None, False),
            ("_prefix", "_prefix", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("_priority", "_priority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False),
            ("_reason", "_reason", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("relatedAction", "relatedAction", PlanDefinitionActionRelatedAction, True, None, False),
            ("_relatedAction", "_relatedAction", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("requiredBehavior", "requiredBehavior", str, False, None, False),
            ("_requiredBehavior", "_requiredBehavior", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("selectionBehavior", "selectionBehavior", str, False, None, False),
            ("_selectionBehavior", "_selectionBehavior", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("_subjectCodeableConcept", "_subjectCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("_subjectReference", "_subjectReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("textEquivalent", "textEquivalent", str, False, None, False),
            ("_textEquivalent", "_textEquivalent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingAge", "timingAge", age.Age, False, "timing", False),
            ("_timingAge", "_timingAge", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingDateTime", "timingDateTime", fhirdatetime.FHIRDateTime, False, "timing", False),
            ("_timingDateTime", "_timingDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingDuration", "timingDuration", duration.Duration, False, "timing", False),
            ("_timingDuration", "_timingDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("_timingPeriod", "_timingPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingRange", "timingRange", range.Range, False, "timing", False),
            ("_timingRange", "_timingRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("_timingTiming", "_timingTiming", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("transform", "transform", str, False, None, False),
            ("_transform", "_transform", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("trigger", "trigger", triggerdefinition.TriggerDefinition, True, None, False),
            ("_trigger", "_trigger", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class PlanDefinitionActionCondition(backboneelement.BackboneElement):
    """ Whether or not the action is applicable.
    
    An expression that describes applicability criteria or start/stop
    conditions for the action.
    """
    
    resource_type = "PlanDefinitionActionCondition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expression = None
        """ Boolean-valued expression.
        Type `Expression` (represented as `dict` in JSON). """
        self._expression = None
        """ Primitive extension for expression. Type `FHIRPrimitiveExtension` """
        
        self.kind = None
        """ applicability | start | stop.
        Type `str`. """
        self._kind = None
        """ Primitive extension for kind. Type `FHIRPrimitiveExtension` """
        
        super(PlanDefinitionActionCondition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionActionCondition, self).elementProperties()
        js.extend([
            ("expression", "expression", expression.Expression, False, None, False),
            ("_expression", "_expression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("kind", "kind", str, False, None, True),
            ("_kind", "_kind", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class PlanDefinitionActionDynamicValue(backboneelement.BackboneElement):
    """ Dynamic aspects of the definition.
    
    Customizations that should be applied to the statically defined resource.
    For example, if the dosage of a medication must be computed based on the
    patient's weight, a customization would be used to specify an expression
    that calculated the weight, and the path on the resource that would contain
    the result.
    """
    
    resource_type = "PlanDefinitionActionDynamicValue"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expression = None
        """ An expression that provides the dynamic value for the customization.
        Type `Expression` (represented as `dict` in JSON). """
        self._expression = None
        """ Primitive extension for expression. Type `FHIRPrimitiveExtension` """
        
        self.path = None
        """ The path to the element to be set dynamically.
        Type `str`. """
        self._path = None
        """ Primitive extension for path. Type `FHIRPrimitiveExtension` """
        
        super(PlanDefinitionActionDynamicValue, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionActionDynamicValue, self).elementProperties()
        js.extend([
            ("expression", "expression", expression.Expression, False, None, False),
            ("_expression", "_expression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("path", "path", str, False, None, False),
            ("_path", "_path", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class PlanDefinitionActionParticipant(backboneelement.BackboneElement):
    """ Who should participate in the action.
    
    Indicates who should participate in performing the action described.
    """
    
    resource_type = "PlanDefinitionActionParticipant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.role = None
        """ E.g. Nurse, Surgeon, Parent.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._role = None
        """ Primitive extension for role. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ patient | practitioner | related-person | device.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(PlanDefinitionActionParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionActionParticipant, self).elementProperties()
        js.extend([
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("_role", "_role", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class PlanDefinitionActionRelatedAction(backboneelement.BackboneElement):
    """ Relationship to another action.
    
    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """
    
    resource_type = "PlanDefinitionActionRelatedAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actionId = None
        """ What action is this related to.
        Type `str`. """
        self._actionId = None
        """ Primitive extension for actionId. Type `FHIRPrimitiveExtension` """
        
        self.offsetDuration = None
        """ Time offset for the relationship.
        Type `Duration` (represented as `dict` in JSON). """
        self._offsetDuration = None
        """ Primitive extension for offsetDuration. Type `FHIRPrimitiveExtension` """
        
        self.offsetRange = None
        """ Time offset for the relationship.
        Type `Range` (represented as `dict` in JSON). """
        self._offsetRange = None
        """ Primitive extension for offsetRange. Type `FHIRPrimitiveExtension` """
        
        self.relationship = None
        """ before-start | before | before-end | concurrent-with-start |
        concurrent | concurrent-with-end | after-start | after | after-end.
        Type `str`. """
        self._relationship = None
        """ Primitive extension for relationship. Type `FHIRPrimitiveExtension` """
        
        super(PlanDefinitionActionRelatedAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionActionRelatedAction, self).elementProperties()
        js.extend([
            ("actionId", "actionId", str, False, None, True),
            ("_actionId", "_actionId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("offsetDuration", "offsetDuration", duration.Duration, False, "offset", False),
            ("_offsetDuration", "_offsetDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("offsetRange", "offsetRange", range.Range, False, "offset", False),
            ("_offsetRange", "_offsetRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relationship", "relationship", str, False, None, True),
            ("_relationship", "_relationship", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class PlanDefinitionGoal(backboneelement.BackboneElement):
    """ What the plan is trying to accomplish.
    
    Goals that describe what the activities within the plan are intended to
    achieve. For example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """
    
    resource_type = "PlanDefinitionGoal"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.addresses = None
        """ What does the goal address.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._addresses = None
        """ Primitive extension for addresses. List of `FHIRPrimitiveExtension` """
        
        self.category = None
        """ E.g. Treatment, dietary, behavioral.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Code or text describing the goal.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.documentation = None
        """ Supporting documentation for the goal.
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        self._documentation = None
        """ Primitive extension for documentation. List of `FHIRPrimitiveExtension` """
        
        self.priority = None
        """ high-priority | medium-priority | low-priority.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._priority = None
        """ Primitive extension for priority. Type `FHIRPrimitiveExtension` """
        
        self.start = None
        """ When goal pursuit begins.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._start = None
        """ Primitive extension for start. Type `FHIRPrimitiveExtension` """
        
        self.target = None
        """ Target outcome for the goal.
        List of `PlanDefinitionGoalTarget` items (represented as `dict` in JSON). """
        self._target = None
        """ Primitive extension for target. List of `FHIRPrimitiveExtension` """
        
        super(PlanDefinitionGoal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionGoal, self).elementProperties()
        js.extend([
            ("addresses", "addresses", codeableconcept.CodeableConcept, True, None, False),
            ("_addresses", "_addresses", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", codeableconcept.CodeableConcept, False, None, True),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("documentation", "documentation", relatedartifact.RelatedArtifact, True, None, False),
            ("_documentation", "_documentation", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("_priority", "_priority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("start", "start", codeableconcept.CodeableConcept, False, None, False),
            ("_start", "_start", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("target", "target", PlanDefinitionGoalTarget, True, None, False),
            ("_target", "_target", fhirprimitiveextension.FHIRPrimitiveExtension, True, None, False),
        ])
        return js


class PlanDefinitionGoalTarget(backboneelement.BackboneElement):
    """ Target outcome for the goal.
    
    Indicates what should be done and within what timeframe.
    """
    
    resource_type = "PlanDefinitionGoalTarget"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.detailCodeableConcept = None
        """ The target value to be achieved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._detailCodeableConcept = None
        """ Primitive extension for detailCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.detailQuantity = None
        """ The target value to be achieved.
        Type `Quantity` (represented as `dict` in JSON). """
        self._detailQuantity = None
        """ Primitive extension for detailQuantity. Type `FHIRPrimitiveExtension` """
        
        self.detailRange = None
        """ The target value to be achieved.
        Type `Range` (represented as `dict` in JSON). """
        self._detailRange = None
        """ Primitive extension for detailRange. Type `FHIRPrimitiveExtension` """
        
        self.due = None
        """ Reach goal within.
        Type `Duration` (represented as `dict` in JSON). """
        self._due = None
        """ Primitive extension for due. Type `FHIRPrimitiveExtension` """
        
        self.measure = None
        """ The parameter whose value is to be tracked.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._measure = None
        """ Primitive extension for measure. Type `FHIRPrimitiveExtension` """
        
        super(PlanDefinitionGoalTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionGoalTarget, self).elementProperties()
        js.extend([
            ("detailCodeableConcept", "detailCodeableConcept", codeableconcept.CodeableConcept, False, "detail", False),
            ("_detailCodeableConcept", "_detailCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detailQuantity", "detailQuantity", quantity.Quantity, False, "detail", False),
            ("_detailQuantity", "_detailQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detailRange", "detailRange", range.Range, False, "detail", False),
            ("_detailRange", "_detailRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("due", "due", duration.Duration, False, None, False),
            ("_due", "_due", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("measure", "measure", codeableconcept.CodeableConcept, False, None, False),
            ("_measure", "_measure", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import age
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
from . import quantity
from . import range
from . import relatedartifact
from . import timing
from . import triggerdefinition
from . import usagecontext