import requests
import json

qa= '{"resourceType":"Questionnaire","id":"hiv-case-report-questionnaire","language":"en","url":"http://openhie.org/fhir/Questionnaire/hiv-case-report-questionnaire","version":"0.2.0","name":"HIVCaseReportForm","status":"draft","subjectType":["Patient"],"date":"2021-01-13T22:08:28+01:00","publisher":"openHIE","contact":[{"telecom":[{"system":"url","value":"http://hl7.org/Special/committees/[something]"}]}],"jurisdiction":[{"coding":[{"system":"http://unstats.un.org/unsd/methods/m49/m49.htm","code":"001"}]}],"item":[{"linkId":"title","text":"HIV Case Report","type":"display"},{"linkId":"regulations","text":"Reporting instructions: Monthly – applicable to each patient during the reporting period","type":"display"},{"linkId":"unit_name","text":"Governing body unit name","type":"string"},{"linkId":"reportDate","text":"Date of report","type":"date"},{"linkId":"intro","text":"Dear:","type":"display"},{"linkId":"patient_identification","prefix":"1","text":"patient_identification","type":"group","item":[{"linkId":"arv_patient_nr","prefix":"1.1","text":"ARV Patient Number","type":"string","required":true},{"linkId":"health_insurance_code","prefix":"1.2","text":"Health insurance code","type":"string"},{"linkId":"passport_nr","prefix":"1.3","text":"Passport Number","type":"string"}]},{"linkId":"personal_information","prefix":"2","text":"Personal Information","type":"group","item":[{"linkId":"name","prefix":"2.1","text":"Full name","type":"string"},{"linkId":"ethnic","prefix":"2.2","text":"Ethnicity","type":"choice","answerValueSet":"http://openhie.org/fhir/ValueSet/vs-ethnicity"},{"linkId":"gender","prefix":"2.3","text":"Gender","type":"choice","answerValueSet":"#Gender"},{"linkId":"birth_year","prefix":"2.4","text":"Year of Birth","type":"integer"},{"linkId":"residence","prefix":"2.3","text":"Residence","type":"group","item":[{"linkId":"current","prefix":"2.3.1","text":"Current residence","type":"string"},{"linkId":"permanent","prefix":"1.3.2","text":"Permanent residence","type":"string"}]},{"linkId":"occupation","prefix":"1.4","text":"Occupation","type":"string"}]},{"linkId":"risk_factors","prefix":"2","text":"Risk Factors","type":"group","item":[{"linkId":"risk_population","prefix":"2.1","text":"Risk population","type":"choice"},{"linkId":"risk_behavior","prefix":"2.2","text":"Risk Behavior","type":"choice","answerValueSet":"#HIVRiskBehavior"},{"linkId":"transmission_route","prefix":"2.3","text":"Transmission Route","type":"choice","answerValueSet":"#HIVTransmissionRoute"}]},{"linkId":"hiv-diagnosis","prefix":"3","text":"HIV Diagnosis","type":"group","item":[{"linkId":"hiv-diagnosis.dateOfConfirmation","prefix":"3.1","text":"Date of Confirmation","type":"date"},{"linkId":"hiv-diagnosis.confirmingLab","prefix":"3.2","text":"Confirming Lab","type":"string"},{"linkId":"hiv-diagnosis.dateOfSpecimenCollection","prefix":"3.3","text":"Date of Specimen Collection","type":"date"},{"linkId":"hiv-diagnosis.placeOfSpecimenCollection","prefix":"3.4","text":"Place of Specimen Collection","type":"string"}]},{"linkId":"hiv-recency-test","prefix":"4","text":"HIV Recency Test","type":"group","item":[{"linkId":"hiv-recency-test.rapidTest","prefix":"4.1","text":"Rapid test","type":"group","item":[{"linkId":"hiv-recency-test.dateOfSpecimenCollection","prefix":"4.1.1","text":"Date of Specimen Collection for rapid test","type":"date"},{"linkId":"hiv-recency-test.dateOfTestPerformance","prefix":"4.1.2","text":"Date of rapid test performance","type":"date"},{"linkId":"hiv-recency-test.placeOfSpecimenCollection","prefix":"4.1.3","text":"Place of Specimen Collection","type":"string"},{"linkId":"hiv-recency-test.testResult","prefix":"4.1.4","text":"Recency from rapid test - result","type":"choice","answerValueSet":"HIVRecencyResults"}]},{"linkId":"recency.vlTest","prefix":"4.2","text":"Rapid VL test","type":"group","item":[{"linkId":"recency.dateOfTestPerformance","prefix":"4.2.1","text":"Date of rapid test performance","type":"date"},{"linkId":"recency.testResult","prefix":"4.2.2","text":"Recency from rapid test - result","type":"choice","answerValueSet":"HIVRecencyResults"}]}]},{"linkId":"cd4BeforeART","prefix":"5","text":"CD4 test before ART","type":"group","item":[{"linkId":"cd4BeforeART.dateOfSpecimenCollection","prefix":"5.1","text":"Date of Specimen Collection for CD4 test before ART","type":"date"},{"linkId":"cd4BeforeART.dateOfTestPerformance","prefix":"5.2","text":"Date of CD4 test before ART performance","type":"date"},{"linkId":"cd4BeforeART.placeOfSpecimenCollection","prefix":"5.3","text":"Place of Specimen Collection for CD4 test before ART","type":"string"},{"linkId":"cd4BeforeART.testResult","prefix":"5.4","text":"CD4 test before ART - result","type":"choice"}]},{"linkId":"cd4DuringART","prefix":"6","text":"CD4 test during ART","type":"group","item":[{"linkId":"cd4DuringART.dateOfSpecimenCollection","prefix":"6.1","text":"Date of Specimen Collection for CD4 test during ART","type":"date"},{"linkId":"cd4DuringART.dateOfTestPerformance","prefix":"6.2","text":"Date of CD4 test during ART performance","type":"date"},{"linkId":"cd4DuringART.placeOfSpecimenCollection","prefix":"6.3","text":"Place of Specimen Collection for CD4 test during ART","type":"string"},{"linkId":"cd4DuringART.testResult","prefix":"6.4","text":"CD4 test during ART - result","type":"choice"}]},{"linkId":"vl4DuringART","prefix":"7","text":"Viral Load test during ART","type":"group","item":[{"linkId":"vl4DuringART.dateOfSpecimenCollection","prefix":"7.1","text":"Date of Specimen Collection for VL test during ART","type":"date"},{"linkId":"vl4DuringART.dateOfTestPerformance","prefix":"7.2","text":"Date of VL test during ART performance","type":"date"},{"linkId":"vl4DuringART.placeOfSpecimenCollection","prefix":"7.3","text":"Place of Specimen Collection for VL test during ART","type":"string"},{"linkId":"vl4DuringART.testResult","prefix":"7.4","text":"VL test during ART - result","type":"choice"}]},{"linkId":"drugResistanceTest","prefix":"8","text":"Drug Resistance test","type":"group","item":[{"linkId":"drugResistanceTest.dateOfSpecimenCollection","prefix":"8.1","text":"Date of Specimen Collection for Drug Resistance test","type":"date"},{"linkId":"drugResistanceTest.dateOfTestPerformance","prefix":"8.2","text":"Date of Drug Resistance test","type":"date"},{"linkId":"drugResistanceTest.placeOfSpecimenCollection","prefix":"8.3","text":"Place of Specimen Collection for Drug Resistance test","type":"string"},{"linkId":"drugResistanceTest.testResult","prefix":"8.4","text":"Drug Resistance test result","type":"choice"}]},{"linkId":"arvTreatment","prefix":"9","text":"ARV Treatment","type":"group","item":[{"linkId":"arvTreatment.treatmentHistory","prefix":"9.1","text":"ARV Treatment history","type":"string"},{"linkId":"arvTreatment.dateOfTreatmentStart","prefix":"9.2","text":"Date of treatment start","type":"date"},{"linkId":"arvTreatment.dateOfTreatmentStop","prefix":"9.3","text":"Date of treatment stop","type":"date"},{"linkId":"arvTreatment.placeOfInitiation","prefix":"9.4","text":"Place of ARV treatment initiation","type":"string"},{"linkId":"arvTreatment.dateOfLossToFollowUp","prefix":"9.5","text":"Date of loss to follow up","type":"date"},{"linkId":"arvTreatment.dateOfTransferredOut","prefix":"9.6","text":"Date ARV treatment transferred out","type":"date"},{"linkId":"arvTreatment.placeTransferredOut","prefix":"9.7","text":"Place ARV treatment transferred out","type":"string"},{"linkId":"arvTreatment.regimens","prefix":"9.8","text":"ARV treatment regimens","type":"group","item":[{"linkId":"regimen.date1stLineStarted","prefix":"9.8.1","text":"Date 1st ARV regimen started","type":"date"},{"linkId":"arvTreatment.date2ndLineStarted","prefix":"9.8.2","text":"Date 3rd ARV regimen started","type":"date"},{"linkId":"arvTreatment.date3rdLineStarted","prefix":"9.8.3","text":"Date 3rd ARV regimen started","type":"date"}]}]},{"linkId":"pregnancies","prefix":"11","text":"ARV Treatment","type":"group","item":[{"linkId":"datePregnancyReported","prefix":"11.1","text":"Date pregnancy reported","type":"date","item":[{"linkId":"TPT","prefix":"10.1.1","text":"TPT","type":"group","item":[{"linkId":"tpt.dateStarted","prefix":"10.1.1.1","text":"Date TPT started","type":"date"},{"linkId":"tpt.dateCompleted","prefix":"10.1.1.2","text":"Date TPT completed","type":"date"},{"linkId":"tpt.placeProvided","prefix":"10.1.1.3","text":"Place TPT provided","type":"string"}]},{"linkId":"tbDiagnosisDate","prefix":"10.1.2","text":"TB Diagnosis Date","type":"date"},{"linkId":"tbTreatment","prefix":"10.1.3","text":"TB Treatment","type":"group","item":[{"linkId":"tbTreatment.dateStarted","prefix":"10.1.3.1","text":"Date TB Treatment started","type":"date"},{"linkId":"tbTreatment.dateCompleted","prefix":"10.1.3.2","text":"Date TB Treatment completed","type":"date"},{"linkId":"tbTreatment.placeProvided","prefix":"10.1.3.3","text":"Place TB Treatment provided","type":"string"}]}]},{"linkId":"placePregnancyReported","prefix":"11.2","text":"Place pregnancy reported","type":"string","item":[{"linkId":"hbv","prefix":"10.2.1","text":"HBV","type":"group","item":[{"linkId":"hbv.diagnosisDate","prefix":"10.2.1.1","text":"Date of HBV diagnosis","type":"date"},{"linkId":"hbv.treatmentStartDate","prefix":"10.2.1.2","text":"Date of HBV treatment start","type":"date"},{"linkId":"hbv.treatmentEndDate","prefix":"10.2.1.3","text":"Date HBV treatment completed","type":"date"},{"linkId":"hbv.placeProvided","prefix":"10.2.1.4","text":"Place HBV treatment provided","type":"string"}]},{"linkId":"hcv","prefix":"10.2.2","text":"HCV","type":"group","item":[{"linkId":"hcv.diagnosisDate","prefix":"10.2.2.1","text":"Date of HBV diagnosis","type":"date"},{"linkId":"hcv.placeProvided","prefix":"10.2.2.2","text":"Place HBV treatment provided","type":"string"}]}]},{"linkId":"childDeliveryDate","prefix":"11.3","text":"Reported child delivery date","type":"date"},{"linkId":"childDeliveryPlace","prefix":"11.4","text":"Reported child delivery place","type":"string"},{"linkId":"pregnancyOutcomes","prefix":"11.5","text":"Pregnancy Outcomes","type":"group","item":[{"linkId":"pregnancyOutcomeCode","prefix":"11.5.1","text":"Pregnancy Outcome code","type":"choice","answerValueSet":"#PregnancyOutcomeCodes"},{"linkId":"childDateOfBirth","prefix":"11.5.2","text":"Date of child birth","type":"date"},{"linkId":"gestationAtDelivery","prefix":"11.5.3","text":"Gestational age at delivery (weeks)","type":"decimal"},{"linkId":"birthWeight","prefix":"11.5.4","text":"Weight at birth (kg)","type":"decimal"},{"linkId":"birtDefects","prefix":"11.5.5","text":"Birth defects","type":"choice","answerValueSet":"#BirthDefects"},{"linkId":"hivStatus","prefix":"11.5.6","text":"HIV status","type":"choice","answerValueSet":"#ChildHIVStatus"},{"linkId":"childHIVDiagnosisDate","prefix":"11.5.7","text":"HIV diagnosis date","type":"date"},{"linkId":"childARTStartDate","prefix":"11.5.8","text":"ART start date","type":"date"}]}]},{"linkId":"death","prefix":"12","text":"Patient death","type":"group","item":[{"linkId":"dateOfDeath","prefix":"12.1","text":"Date of death","type":"date"},{"linkId":"causeOfDeath","prefix":"12.2","text":"Cause of death","type":"string"}]}]}'

questionnaire = json.loads(qa)


# This creates anentry from a single questionnaire item
def createSingleItem(item):
  sitem = {}
  sitem["title"] = item["text"] # set title from questionnaire.item.text
  if (item["type"] == "boolean"): # A big switch clause
      sitem["type"] = "boolean"
      sitem["format"]: "checkbox"
  elif (item["type"] == "display"):
    sitem["type"] = "info"
  elif (item["type"] == "string"):
    sitem["type"] = "string"
  elif (item["type"] == "date"):
    sitem["type"] = "string"
    sitem["format"] = "date"
  elif (item["type"] == "choice"):
    sitem["type"] = "string"
    sitem["enum"] = ["To Do", "Still to do", "Not done"] 
  elif (item["type"] == "group"): # if nested items, recurse
    if ('type' in item):
      sitem["type"] = "object"
      sitem["required"] = []
      for it in item['item']:
        if ('required' in it):
          if (it['required'] == True):
            sitem['required'].append(it['linkId'])
      sitem["properties"] ={}
      for child in item["item"]: 
        sitem["properties"].update(createSingleItem(child))
  return {item["linkId"]: sitem}


def createItem(qitem):
  fitem = {}
  if ('repeats' in qitem):
    fitem["type"]= "array"
    fitem["items"]["type"] = "object"
    tempitem = createSingleItem(qitem)
    fitem["items"]["properties"].update(tempitem)
  else: 
    fitem = createSingleItem(qitem)
  return(fitem)    


#setup form schema
mainForm = json.loads ('{"title": "","type": "object","required": [],"properties": {}}') 
if ('title' in questionnaire):
    mainForm['title'] = questionnaire['title']
  

  
  
# process all items in questionnaire
for qitem in questionnaire["item"]:
  print(json.dumps(createItem(qitem))) 
  if ('required' in qitem):
      if (qitem['required'] == True):
        mainForm['required'].add(qitem['linkId'])
  mainForm["properties"].update(createItem(qitem))


# Save
with open('mainform.json', 'w') as outfile:
    json.dump(mainForm, outfile, indent=4)  

exit(0)




