import unittest

from fhirclient.models.patient import Patient
from fhirclient.models.encounter import Encounter


class PrimitiveExtensionTests(unittest.TestCase):

    def test_patient(self):
        json = {
            "id": "1234",
            "name": [{
                "family": "Smith",
                "given": ["John"]
            }],
            "birthDate": "2000-01-01",
            "_birthDate": {
                "extension": [{
                    "url": "http://example.com/patient-birthdate-descriptor",
                    "valueString": "Y2K baby"
                }]
            },
            "gender": "male",
            "_gender": {
                "extension": [{
                    "url": "http://example.com/patient-gender-descriptor",
                    "valueString": "XY"
                }]
            },
            "resourceType": "Patient"
        }

        fhir_patient = Patient(json)
        assert fhir_patient.as_json() == json

    def test_encounter(self):
        encounter_json = {
            "resourceType":
            "Encounter",
            "id":
            "example-mother-encounter",
            "meta": {
                "profile": [
                    "https://fhir-ig.curaihealth.com/StructureDefinition/CuraiEncounter"
                ]
            },
            "text": {
                "status":
                "extensions",
                "div":
                "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p class=\"res-header-id\"><b>Generated Narrative: Encounter example-mother-encounter</b></p><a name=\"example-mother-encounter\"> </a><a name=\"hcexample-mother-encounter\"> </a><a name=\"example-mother-encounter-en-US\"> </a><p><b>Reason for Encounter Extension</b>: My tooth aches</p><p><b>Dynamic Charting Fields Order</b>: [{&quot;type&quot;: &quot;hpi&quot;, &quot;childEncounterIds&quot;: [&quot;example-child-encounter&quot;]}]</p><p><b>Designated for return Extension</b>: false</p><p><b>status</b>: Finished</p><p><b>class</b>: <a href=\"http://terminology.hl7.org/6.0.2/CodeSystem-v3-ActCode.html#v3-ActCode-VR\">ActCode</a> VR: virtual</p><p><b>type</b>: <span title=\"Codes:{http://snomed.info/sct 1197766005}\">Encounter by electronic text-based asynchronous communication (procedure)</span></p><p><b>subject</b>: <a href=\"Patient-example-curai-patient.html\">John Doe  Female, DoB: 1984-01-01 ( https://fhir-ig.curaihealth.com/user-id#123456789)</a></p><p><b>episodeOfCare</b>: Identifier: example-episodeofcare-medical-history-finished</p><h3>Participants</h3><table class=\"grid\"><tr><td style=\"display: none\">-</td><td><b>Type</b></td><td><b>Individual</b></td></tr><tr><td style=\"display: none\">*</td><td><span title=\"Codes:{http://terminology.hl7.org/CodeSystem/v3-ParticipationType PPRF}\">Primary Performer</span></td><td><a href=\"Encounter/example-curai-practitioner\">Encounter/example-curai-practitioner</a></td></tr></table><p><b>period</b>: 2022-08-03 00:00:00+0000 --&gt; 2022-08-03 01:00:00+0000</p><h3>Locations</h3><table class=\"grid\"><tr><td style=\"display: none\">-</td><td><b>Location</b></td></tr><tr><td style=\"display: none\">*</td><td><a href=\"#hcexample-mother-encounter/example-encounter-location\">Location Curai State</a></td></tr></table><hr/><blockquote><p class=\"res-header-id\"><b>Generated Narrative: Location  #example-encounter-location</b></p><a name=\"example-mother-encounter/example-encounter-location\"> </a><a name=\"hcexample-mother-encounter/example-encounter-location\"> </a><a name=\"example-mother-encounter/example-encounter-location-en-US\"> </a><p><b>identifier</b>: <code>http://exampleoflocation.com</code>/curai\u00a0(use:\u00a0temp,\u00a0)</p><p><b>name</b>: Curai State</p><p><b>address</b>: GA </p></blockquote></div>"
            },
            "contained": [{
                "resourceType":
                "Location",
                "id":
                "example-encounter-location",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/qicore/StructureDefinition/qicore-location"
                    ]
                },
                "identifier": [{
                    "use": "temp",
                    "system": "http://exampleoflocation.com",
                    "value": "curai"
                }],
                "name":
                "Curai State",
                "address": {
                    "state": "GA"
                }
            }],
            "extension": [{
                "url":
                "https://fhir-ig.curaihealth.com/StructureDefinition/reason-for-encounter",
                "valueString": "My tooth aches",
                "_valueString": {
                    "extension": [{
                        "url":
                        "http://hl7.org/fhir/StructureDefinition/translation",
                        "extension": [{
                            "url": "lang",
                            "valueCode": "es"
                        }, {
                            "url": "content",
                            "valueString": "Me duele el diente"
                        }]
                    }]
                }
            }, {
                "url":
                "https://fhir-ig.curaihealth.com/StructureDefinition/dynamic-charting-fields-order",
                "valueString":
                "[{\"type\": \"hpi\", \"childEncounterIds\": [\"example-child-encounter\"]}]"
            }, {
                "url":
                "https://fhir-ig.curaihealth.com/StructureDefinition/designated-for-return",
                "valueBoolean": False
            }],
            "status":
            "finished",
            "class": {
                "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                "code": "VR",
                "display": "virtual"
            },
            "type": [{
                "coding": [{
                    "system":
                    "http://snomed.info/sct",
                    "code":
                    "1197766005",
                    "display":
                    "Encounter by electronic text-based asynchronous communication (procedure)"
                }]
            }],
            "subject": {
                "reference": "Patient/example-curai-patient",
                "identifier": {
                    "value": "example-curai-patient"
                }
            },
            "episodeOfCare": [{
                "identifier": {
                    "value": "example-episodeofcare-medical-history-finished"
                }
            }],
            "participant": [{
                "type": [{
                    "coding": [{
                        "system":
                        "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
                        "code": "PPRF",
                        "display": "primary performer"
                    }],
                    "text":
                    "Primary Performer"
                }],
                "individual": {
                    "reference": "Encounter/example-curai-practitioner"
                }
            }],
            "period": {
                "start": "2022-08-03T00:00:00.000Z",
                "end": "2022-08-03T01:00:00.000Z"
            },
            "location": [{
                "location": {
                    "reference": "#example-encounter-location"
                }
            }]
        }

        fhir_encounter = Encounter(encounter_json)
        assert fhir_encounter.as_json() == encounter_json
