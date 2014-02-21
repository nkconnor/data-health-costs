"""
Contains data holder class
author:chris
"""

import pickle as p
import numpy as np
import os

#Debug Timer Wrappers
from wrappers import debug

H143 = {"DUID DWELLING UNIT ID ":(1,5),   "PID PERSON NUMBER ":(6,8), " DUPERSID PERSON ID (DUID + PID) ":(9,16), " PANEL PANEL NUMBER ":(17,18), " FAMID13 FAMILY IDENTIFIER (STUDENT MERGED IN) ":(19,20), " RULETR13 RU LETTER ":(21,22), " RUSIZE13 RU SIZE ":(23,24), " RUCLAS13 RU FIELDED AS: STANDARD, NEW, STUDENT ":(25,25), " FAMSIZ13 RU SIZE INCLUDING STUDENTS ":(26,27), " REGION13 CENSUS REGION ":(28,28), " MSA13 MSA ":(29,29), " RNDREF13 REFERENCE PERSON ":(30,32), " RDRESP13 1ST RESPONDENT INDICATOR ":(33,33), " PROXY13 WAS RESPONDENT A PROXY ":(34,34), " BEGRFD13 REFERENCE PERIOD BEGIN DATE: DAY ":(35,36), " BEGRFM13 REFERENCE PERIOD BEGIN DATE: MONTH ":(37,38), " BEGRFY13 REFERENCE PERIOD BEGIN DATE: YEAR ":(39,42), " ENDRFD13 REFERENCE PERIOD END DATE: DAY ":(43,44), " ENDRFM13 REFERENCE PERIOD END DATE: MONTH ":(45,45), " ENDRFY13 REFERENCE PERIOD END DATE: YEAR ":(46,49), " KEYNESS PERSON KEY STATUS ":(50,50), " INSCOP13 INSCOPE ":(51,51), " PSTAT13 PERSON DISPOSITION STATUS ":(52,53), " RURSLT13 RU RESULT ":(54,55), " RUENDD13 DATE OF INTV (DATE STARTED: DAY) ":(56,57), " RUENDM13 DATE OF INTV (DATE STARTED: MONTH) ":(58,58), " RUENDY13 DATE OF INTV (DATE STARTED: YEAR) ":(59,62), " AGE13X AGE - (EDITED/IMPUTED) ":(63,64), " DOBMM DATE OF BIRTH: MONTH ":(65,66), " DOBYY DATE OF BIRTH: YEAR ":(67,70), " SEX SEX ":(71,71), " RACEBX BLACK AMONG RACES RPTD (EDITED/IMPUTED) ":(72,72), " RACEAX ASIAN AMONG RACES RPTD (EDITED/IMPUTED) ":(73,73), " RACEWX WHITE AMONG RACES RPTD (EDITED/IMPUTED) ":(74,74), " RACEX RACE - (EDITED/IMPUTED) ":(75,75), " RACETHNX RACE/ETHNICITY - (EDITED/IMPUTED) ":(76,76), " HISPANX HISPANIC ETHNICITY - (EDITED/IMPUTED) ":(77,77), " HISPCAT SPECIFIC HISPANIC ETHNICITY GROUP ":(78,79), " MARRY13X MARITAL STATUS - (EDITED/IMPUTED) ":(80,81), " SPOUID13 SPOUSE ID ":(82,84), " SPOUIN13 MARITAL STATUS WITH SPOUSE PRESENT ":(85,86), " EDUCYR YEARS OF EDUC WHEN FIRST ENTERED MEPS ":(87,88), " HIDEG HIGHEST DEGREE WHEN FIRST ENTERED MEPS ":(89,90), " EDUYRDEG YEAR OF EDUCATION OR HIGHEST DEGREE":(91,92), " EDRECODE EDUCATION RECODE ":(93,94), " FTSTD13X STUDENT STATUS AGES 17-23 (EDIT/IMPUTED) ":(95,96), " ACTDTY13 MILITARY FULL-TIME ACTIVE DUTY ":(97,98), " HONRDC13 HONORABLY DISCHARGED FROM ACTIVE DUTY ":(99,100), " RFREL13X RELATION TO REF PERS (EDITED/IMPUTED) ":(101,102), " RTHLTH13 PERCEIVED HEALTH STATUS ":(103,104), " MNHLTH13 PERCEIVED MENTAL HEALTH STATUS ":(105,106), " IADLHP13 IADL SCREENER ":(107,108), " ADLHLP13 ADL SCREENER ":(109,110), " AIDHLP13 USES ASSISTIVE DEVICES ":(111,112), " WLKLIM13 LIMITATION IN PHYSICAL FUNCTIONING ":(113,114), " LFTDIF13 DIFFICULTY LIFTING 10 POUNDS ":(115,116), " STPDIF13 DIFFICULTY WALKING UP 10 STEPS ":(117,118), " WLKDIF13 DIFFICULTY WALKING 3 BLOCKS ":(119,120), " MILDIF13 DIFFICULTY WALKING A MILE ":(121,122), " STNDIF13 DIFFICULTY STANDING 20 MINUTES ":(123,124), " BENDIF13 DIFFICULTY BENDING/STOOPING ":(125,126), " RCHDIF13 DIFFICULTY REACHING OVER HEAD ":(127,128), " FNGRDF13 DIFFICULTY USING FINGERS TO GRASP ":(129,130), " ACTLIM13 LIMITATION WORK/HOUSEWORK/SCHOOL ":(131,132), " WRKLIM13 WORK LIMITATION ":(133,134), " HSELIM13 HOUSEWORK LIMITATION ":(135,136), " SCHLIM13 SCHOOL LIMITATION ":(137,138), " UNABLE13 COMPLETELY UNABLE TO DO ACTIVITY ":(139,140), " SOCLIM13 SOCIAL LIMITATION ":(141,142), " COGLIM13 COGNITIVE LIMITATIONS ":(143,144), " EMPST13 EMPLOYMENT STATUS ":(145,146), " HRWAG13X HOURLY WAGE AT CURRENT MAIN JOB (EDITED) ":(147,152), " HRWGRD13 HOURLY WAGE ROUND FLAG ":(153,154), " HRWAY13 CALCULATION METHODS FOR HOURLY WAGE ":(155,156), " HOUR13 HOURS WORKED PER WEEK AT CMJ ":(157,159), " HELD13X HEALTH INSURANCE HELD FROM CMJ (ED) ":(160,161), " OFFER13X HEALTH INSURANCE OFFERED AT CMJ (ED) ":(162,163), " NUMEMP13 NUMBER OF EMPLOYEES AT LOCATION OF CMJ ":(164,166), " SELFCM13 SELF-EMPLOYED AT CURRENT MAIN JOB ":(167,168), " TRINW13X PID COV BY TRICARE/CHAMPVA AT INT-EDITED ":(169,169), " MCARE13 PID COV BY MEDICARE ":(170,170), " MCARE13X PID COV BY MEDICARE - EDITED ":(171,171), " MCAID13 PID COV BY MEDICAID OR SCHIP ":(172,172), " MCAID13X PID COV BY MEDICAID OR SCHIP - EDITED ":(173,173), " OTPUBA13 PID COV BY/PAYS OTH GOV MCAID/SCHIP HMO ":(174,174), " OTPUBB13 PID COV BY OTH PUB NOT MCAID/SCHIP HMO ":(175,175), " STPRG13 PID COV BY STATE SPECIFIC PROGRAM ":(176,176), " PUB13X PID COV BY PUBLIC INS - EDITED ":(177,177)}
H144A = {"DUID DWELLING UNIT ID":(1, 5) , "PID PERSON NUMBER":(6, 8) , "DUPERSID PERSON ID (DUID + PID)":(9, 16) , "DRUGIDX DRUG ID (DUPERSID + COUNTER)":(17, 27) , "RXRECIDX UNIQUE RX/PRESCRIBED MEDICINE IDENTIFIER":(28, 42) , "LINKIDX ID FOR LINKAGE TO COND/OTH EVENT FILES":(43, 54) , "PANEL PANEL NUMBER":(55, 56) , "PURCHRD ROUND RX/PRESCR MED OBTAINED/PURCHASED":(57, 57) , "RXBEGDD DAY PERSON STARTED TAKING MEDICINE":(58, 59) , "RXBEGMM MONTH PERSON STARTED TAKING MEDICINE":(60, 61) , "RXBEGYRX YEAR PERSON STARTED TAKING MEDICINE":(62, 65) , "RXNAME MEDICATION NAME (IMPUTED)":(66, 115) , "RXNDC NATIONAL DRUG CODE (IMPUTED)":(116, 126) , "RXQUANTY QUANTITY OF RX/PRESCR MED (IMPUTED)":(127, 135) , "RXFORM FORM OF RX/PRESCRIBED MEDICINE (IMPUTED)":(136, 185) , "RXFRMUNT UNIT OF MEAS FORM RX/PRESC MED (IMPUTED)":(186, 235) , "RXSTRENG STRENGTH OF RX/PRESCR MED DOSE (IMPUTED)":(236, 285) , "RXSTRUNT UNIT OF MEAS STRENGTH OF RX (IMPUTED)":(286, 335) , "RXDAYSUP DAYS SUPPLIED OF PRESCRIBED MED":(336, 338) , "PHARTP1 TYPE OF PHARMACY PROV - 1ST":(339, 340) , "PHARTP2 TYPE OF PHARMACY PROV - 2ND":(341, 342) , "PHARTP3 TYPE OF PHARMACY PROV - 3RD":(343, 344) , "PHARTP4 TYPE OF PHARMACY PROV - 4TH":(345, 346) , "PHARTP5 TYPE OF PHARMACY PROV - 5TH":(347, 348) , "PHARTP6 TYPE OF PHARMACY PROV - 6TH":(349, 350) , "PHARTP7 TYPE OF PHARMACY PROV - 7TH":(351, 352) , "PHARTP8 TYPE OF PHARMACY PROV - 8TH":(353, 354) , "RXFLG NDC IMPUTATION SOURCE ON PC DONOR REC":(355, 355) , "IMPFLAG METHOD OF EXPENDITURE DATA CREATION":(356, 356) , "PCIMPFLG TYPE OF HC TO PC PRESCRIPTION MATCH":(357, 357) , "CLMOMFLG CHGE/PYMNT, RX CLAIM FILING, OMTYPE STAT":(358, 358) , "INPCFLG PID HAS AT LEAST 1 RECORD IN PC":(359, 359) , "SAMPLE HOUSEHLD RCVD FREE SAMPLE OF RX IN ROUND":(360, 360) , "RXICD1X 3 DIGIT ICD-9 CONDITION CODE":(361, 363) , "RXICD2X 3 DIGIT ICD-9 CONDITION CODE":(364, 366) , "RXICD3X 3 DIGIT ICD-9 CONDITION CODE":(367, 369) , "RXCCC1X MODIFIED CLINICAL CLASS CODE":(370, 372) , "RXCCC2X MODIFIED CLINICAL CLASS CODE":(373, 375) , "RXCCC3X MODIFIED CLINICAL CLASS CODE":(376, 378) , "PREGCAT MULTUM PREGNANCY CATEGORY":(379, 380) , "TC1 MULTUM THERAPEUTIC CLASS #1":(381, 383) , "TC1S1 MULTUM THERAPEUTIC SUB-CLASS #1 FOR TC1":(384, 386) , "TC1S1_1 MULTUM THERAPEUT SUB-SUB-CLASS FOR TC1S1":(387, 389) , "TC1S1_2 MULTUM THERAPEUT SUB-SUB-CLASS FOR TC1S1":(390, 392) , "TC1S2 MULTUM THERAPEUTIC SUB-CLASS #2 FOR TC1":(393, 395) , "TC1S2_1 MULTUM THERAPEUT SUB-SUB-CLASS FOR TC1S2":(396, 398) , "TC1S3 MULTUM THERAPEUTIC SUB-CLASS #3 FOR TC1":(399, 400) , "TC1S3_1 MULTUM THERAPEUT SUB-SUB-CLASS FOR TC1S3":(401, 402) , "TC2 MULTUM THERAPEUTIC CLASS #2":(403, 405) , "TC2S1 MULTUM THERAPEUTIC SUB-CLASS #1 FOR TC2":(406, 408) , "TC2S1_1 MULTUM THERAPEUT SUB-SUB-CLASS FOR TC2S1":(409, 411) , "TC2S1_2 MULTUM THERAPEUT SUB-SUB-CLASS FOR TC2S1":(412, 414) , "TC2S2 MULTUM THERAPEUTIC SUB-CLASS #2 FOR TC2":(415, 417) , "TC3 MULTUM THERAPEUTIC CLASS #3":(418, 420) , "TC3S1 MULTUM THERAPEUTIC SUB-CLASS #1 FOR TC3":(421, 423) , "TC3S1_1 MULTUM THERAPEUT SUB-SUB-CLASS FOR TC3S1":(424, 426) , "RXSF11X AMOUNT PAID, SELF OR FAMILY (IMPUTED)":(427, 433) , "RXMR11X AMOUNT PAID, MEDICARE (IMPUTED)":(434, 441) , "RXMD11X AMOUNT PAID, MEDICAID (IMPUTED)":(442, 449) , "RXPV11X AMOUNT PAID, PRIVATE INSURANCE (IMPUTED)":(450, 457) , "RXVA11X AMOUNT PAID, VETERANS/CHAMPVA (IMPUTED)":(458, 464) , "RXTR11X AMOUNT PAID, TRICARE (IMPUTED)":(465, 471) , "RXOF11X AMOUNT PAID, OTHER FEDERAL (IMPUTED)":(472, 478) , "RXSL11X AMOUNT PAID, STATE & LOCAL GOV (IMPUTED)":(479, 485) , "RXWC11X AMOUNT PAID, WORKERS COMP (IMPUTED)":(486, 492) , "RXOT11X AMOUNT PAID, OTHER INSURANCE (IMPUTED)":(493, 499) , "RXOR11X AMOUNT PAID, OTHER PRIVATE (IMPUTED)":(500, 506) , "RXOU11X AMOUNT PAID, OTHER PUBLIC (IMPUTED)":(507, 513) , "RXXP11X SUM OF PAYMENTS RXSF11X-RXOU11X(IMPUTED)":(514, 521) , "PERWT11F EXPENDITURE FILE PERSON WEIGHT, 2011":(522, 534) , "VARSTR VARIANCE ESTIMATION STRATUM, 2011":(535, 538) , "VARPSU VARIANCE ESTIMATION PSU, 2011":(539, 539)}
H144D = {"DUID: DWELLING UNIT ID":(1, 5), "PID: PERSON NUMBER":(6, 8),"DUPERSID: PERSON ID (DUID + PID)":(9, 16),"EVNTIDX: EVENT ID":(17, 28),"EVENTRN: EVENT ROUND NUMBER":(29, 29),"ERHEVIDX: EVENT ID FOR CORRESPONDING EMER RM VISIT":(30, 41),"FFEEIDX: FLAT FEE ID":(42, 53),"PANEL: PANEL NUMBER":(54, 55),"MPCDATA: MPC DATA FLAG":(56, 56),"IPBEGYR: EVENT START DATE - YEAR":(57, 60),"IPBEGMM: EVENT START DATE - MONTH":(61, 62),"IPBEGDD: EVENT START DATE - DAY":(63, 64),"IPENDYR: EVENT END DATE - YEAR":(65, 68),"IPENDMM: EVENT END DATE - MONTH":(69, 70),"IPENDDD: EVENT END DATE - DAY":(71, 72),"NUMNIGHX: NUM OF NIGHTS IN HOSPITAL - EDITED/IMPUTED":(73, 75),"NUMNIGHT: NUMBER OF NIGHTS STAYED AT PROVIDER":(76, 77),"EMERROOM: DID STAY BEGIN WITH EMERGENCY ROOM VISIT":(78, 79),"SPECCOND: HOSPITAL STAY RELATED TO CONDITION":(80, 81),"RSNINHOS: REASON ENTERED HOSPITAL":(82, 83),"DLVRTYPE: VAGINAL OR CAESAREAN DELIVERY":(84, 85),"EPIDURAL: RECEIVE AN EPIDURAL OR SPINAL FOR PAIN":(86, 87),"ANYOPER: ANY OPERATIONS OR SURGERIES PERFORMED":(88, 89),"IPICD1X: 3-DIGIT ICD-9-CM CONDITION CODE":(90, 92),"IPICD2X: 3-DIGIT ICD-9-CM CONDITION CODE":(93, 95),"IPICD3X: 3-DIGIT ICD-9-CM CONDITION CODE":(96, 98),"IPICD4X: 3-DIGIT ICD-9-CM CONDITION CODE":(99, 101),"IPPRO1X: 2-DIGIT ICD-9-CM PROCEDURE CODE":(102, 103),"IPPRO2X: 2-DIGIT ICD-9-CM PROCEDURE CODE":(104, 105),"IPCCC1X: MODIFIED CLINICAL CLASSIFICATION CODE":(106, 108),"IPCCC2X: MODIFIED CLINICAL CLASSIFICATION CODE":(109, 111),"IPCCC3X: MODIFIED CLINICAL CLASSIFICATION CODE":(112, 114),"IPCCC4X: MODIFIED CLINICAL CLASSIFICATION CODE":(115, 117),"DSCHPMED: MEDICINES PRESCRIBED AT DISCHARGE":(118, 119),"FFIPTYPE: FLAT FEE BUNDLE":(120, 121),"IPXP11X: TOT EXP FOR EVENT (IPFXP11X+IPDXP11X)":(122, 130),"IPTC11X: TOTAL CHG FOR EVENT (IPFTC11X+IPDTC11X)":(131, 140),"IPFSF11X: FACILITY AMT PD, FAMILY (IMPUTED)":(141, 148),"IPFMR11X: FACILITY AMT PD, MEDICARE (IMPUTED)":(149, 157),"IPFMD11X: FACILITY AMT PD, MEDICAID (IMPUTED)":(158, 166),"IPFPV11X: FACILITY AMT PD, PRIV INSUR (IMPUTED)":(167, 175),"IPFVA11X: FAC AMT PD,VETERANS/CHAMPVA(IMPUTED)":(176, 183),"IPFTR11X: FACILITY AMT PD,TRICARE(IMPUTED)":(184, 191),"IPFOF11X: FACILITY AMT PD, OTH FEDERAL (IMPUTED)":(192, 199),"IPFSL11X FACILITY AMT PD, STATE/LOC GOV (IMPUTED)":(200, 207), "IPFWC11X FACILITY AMT PD, WORKERS COMP (IMPUTED)":(208, 216), "IPFOR11X FACILITY AMT PD, OTH PRIV (IMPUTED)":(217, 225), "IPFOU11X FACILITY AMT PD, OTH PUB (IMPUTED)":(226, 233), "IPFOT11X FACILITY AMT PD, OTH INSUR (IMPUTED)":(234, 241), "IPFXP11X FACILITY SUM PAYMENTS IPFSF11X-IPFOT11X":(242, 250), "IPFTC11X TOTAL FACILITY CHARGE (IMPUTED)":(251, 260), "IPDSF11X DOCTOR AMOUNT PD, FAMILY (IMPUTED)":(261, 268), "IPDMR11X DOCTOR AMOUNT PD, MEDICARE (IMPUTED)":(269, 276), "IPDMD11X DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)":(277, 284), "IPDPV11X DOCTOR AMT PD, PRIV INSUR (IMPUTED)":(285, 292), "IPDVA11X DR AMT PD,VETERANS/CHAMPVA(IMPUTED)":(293, 299), "IPDTR11X DOCTOR AMT PD,TRICARE(IMPUTED)":(300, 307), "IPDOF11X DOCTOR AMT PD, OTH FEDERAL (IMPUTED)":(308, 311), "IPDSL11X DOCTOR AMT PD, STATE/LOC GOV (IMPUTED)":(312, 318), "IPDWC11X DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)":(319, 326), "IPDOR11X DOCTOR AMT PD, OTH PRIVATE (IMPUTED)":(327, 334), "IPDOU11X DOCTOR AMT PD, OTH PUB (IMPUTED)":(335, 341), "IPDOT11X DOCTOR AMT PD, OTH INSUR (IMPUTED)":(342, 348), "IPDXP11X DOCTOR SUM PAYMENTS IPDSF11X-IPDOT11X":(349, 356), "IPDTC11X TOTAL DOCTOR CHARGE (IMPUTED)":(357, 365), "IMPFLAG IMPUTATION STATUS":(366, 366), "PERWT11F EXPENDITURE FILE PERSON WEIGHT, 2011":(367, 378), "VARSTR VARIANCE ESTIMATION STRATUM, 2011":(379, 382), "VARPSU VARIANCE ESTIMATION PSU, 2011":(383, 383)}
H144E = {"DUID DWELLING UNIT ID ":(1, 5),  "PID PERSON NUMBER ":(6, 8),  "DUPERSID PERSON ID (DUID + PID) ":(9, 16),  "EVNTIDX EVENT ID ":(17, 28),  "EVENTRN EVENT ROUND NUMBER ":(29, 29),  "ERHEVIDX EVENT ID FOR CORRESPONDING HOSPITAL STAY ":(30, 41),  "FFEEIDX FLAT FEE ID ":(42, 53),  "PANEL PANEL NUMBER ":(54, 55),  "MPCDATA MPC DATA FLAG ":(56, 56),  "ERDATEYR EVENT DATE - YEAR ":(57, 60),  "ERDATEMM EVENT DATE - MONTH ":(61, 62),  "ERDATEDD EVENT DATE - DAY ":(63, 64),  "SEEDOC DID P TALK TO MD THIS VISIT ":(65, 66),  "VSTCTGRY BEST CATEGORY FOR CARE P RECV ON VST DT ":(67, 68),  "VSTRELCN THIS VST RELATED TO SPEC CONDITION ":(69, 70),  "LABTEST THIS VISIT DID P HAVE LAB TESTS ":(71, 72),  "SONOGRAM THIS VISIT DID P HAVE SONOGRAM OR ULTRSD ":(73, 74),  "XRAYS THIS VISIT DID P HAVE X-RAYS ":(75, 76),  "MAMMOG THIS VISIT DID P HAVE A MAMMOGRAM ":(77, 78),  "MRI THIS VISIT DID P HAVE AN MRI/CATSCAN ":(79, 80),  "EKG THIS VISIT DID P HAVE AN EKG OR ECG ":(81, 82),  "EEG THIS VISIT DID P HAVE AN EEG ":(83, 84),  "RCVVAC THIS VISIT DID P RECEIVE A VACCINATION ":(85, 86),  "ANESTH THIS VISIT DID P RECEIVE ANESTHESIA ":(87, 88),  "THRTSWAB THIS VISIT DID P HAVE A THROAT SWAB ":(89, 90),  "OTHSVCE THIS VISIT DID P HAVE OTH DIAG TEST/EXAM ":(91, 92),  "SURGPROC WAS SURG PROC PERFORMED ON P THIS VISIT ":(93, 94),  "MEDPRESC ANY MEDICINE PRESCRIBED FOR P THIS VISIT ":(95, 96),  "ERICD1X 3-DIGIT ICD-9-CM CONDITION CODE ":(97, 99),  "ERICD2X 3-DIGIT ICD-9-CM CONDITION CODE ":(100, 102),  "ERICD3X 3-DIGIT ICD-9-CM CONDITION CODE ":(103, 105),  "ERPRO1X 2-DIGIT ICD-9-CM PROCEDURE CODE ":(106, 107),  "ERPRO2X 2-DIGIT ICD-9-CM PROCEDURE CODE ":(108, 109),  "ERCCC1X MODIFIED CLINICAL CLASSIFICATION CODE ":(110, 112),  "ERCCC2X MODIFIED CLINICAL CLASSIFICATION CODE ":(113, 115),  "ERCCC3X MODIFIED CLINICAL CLASSIFICATION CODE ":(116, 118),  "FFERTYPE FLAT FEE BUNDLE ":(119, 120),  "ERXP11X TOT EXP FOR EVENT (ERFXP11X + ERDXP11X) ":(121, 128),  "ERTC11X TOTAL CHG FOR EVENT (ERFTC11X+ERDTC11X) ":(129, 137),  "ERFSF11X FACILITY AMT PD, FAMILY (IMPUTED) ":(138, 145),  "ERFMR11X FACILITY AMT PD, MEDICARE (IMPUTED) ":(146, 153),  "ERFMD11X FACILITY AMT PD, MEDICAID (IMPUTED) ":(154, 161),  "ERFPV11X FACILITY AMT PD, PRIV INSUR (IMPUTED) ":(162, 169),  "ERFVA11X FAC AMT PD,VETERANS/CHAMPVA(IMPUTED)":(170, 176),  "ERFTR11X FACILITY AMT PD,TRICARE(IMPUTED) ":(177, 183),  "ERFOF11X FACILITY AMT PD, OTH FEDERAL (IMPUTED) ":(184, 190),  "ERFSL11X FACILITY AMT PD, STATE/LOC GOV (IMPUTED) ":(191, 197),  "ERFWC11X FACILITY AMT PD, WORKERS COMP (IMPUTED) ":(198, 205),  "ERFOR11X FACILITY AMT PD, OTH PRIV (IMPUTED) ":(206, 213),  "ERFOU11X FACILITY AMT PD, OTH PUB (IMPUTED) ":(214, 221),  "ERFOT11X FACILITY AMT PD, OTH INSUR (IMPUTED) ":(222, 229),  "ERFXP11X FACILITY SUM PAYMENTS ERFSF11X-ERFOT11X ":(230, 237),  "ERFTC11X TOTAL FACILITY CHARGE (IMPUTED) ":(238, 246),  "ERDSF11X DOCTOR AMOUNT PAID, FAMILY (IMPUTED) ":(247, 253),  "ERDMR11X DOCTOR AMOUNT PD, MEDICARE (IMPUTED) ":(254, 260),  "ERDMD11X DOCTOR AMOUNT PAID, MEDICAID (IMPUTED) ":(261, 267),  "ERDPV11X DOCTOR AMT PD, PRIV INSUR (IMPUTED) ":(268, 274),  "ERDVA11X DR AMT PD,VETERANS/CHAMPVA(IMPUTED) ":(275, 280),  "ERDTR11X DOCTOR AMT PD,TRICARE(IMPUTED) ":(281, 286),  "ERDOF11X DOCTOR AMT PAID, OTH FEDERAL (IMPUTED) ":(287, 290),  "ERDSL11X DOCTOR AMT PD, STATE/LOC GOV (IMPUTED) ":(291, 297),  "ERDWC11X DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED) ":(298, 303),  "ERDOR11X DOCTOR AMT PD, OTH PRIVATE (IMPUTED) ":(304, 310),  "ERDOU11X DOCTOR AMT PD, OTH PUB (IMPUTED) ":(311, 316),  "ERDOT11X DOCTOR AMT PD, OTH INSUR (IMPUTED) ":(317, 323),  "ERDXP11X DOCTOR SUM PAYMENTS ERDSF11X - ERDOT11X ":(324, 330),  "ERDTC11X TOTAL DOCTOR CHARGE (IMPUTED) ":(331, 338),  "IMPFLAG IMPUTATION STATUS ":(339, 339),  "PERWT11F EXPENDITURE FILE PERSON WEIGHT, 2011 ":(340, 351),  "VARSTR VARIANCE ESTIMATION STRATUM, 2011 ":(352, 355),  "VARPSU VARIANCE ESTIMATION PSU, 2011":(356, 356)}

class Data():
	"""
	Data Handler object that has methods for handling references 
	for our variables, such as looking up variables,
	getting data for features as well as loading data, 
	saving and loading temporary sessions
	"""
	@debug
	def __init__ (self, data = dict(), codebook = H144D, filename = os.path.join("..","data","h144d.dat")):
		self.datafile = filename
		self.codebook = codebook
		self.createRefs()
		self.results = dict()
		self.ignored = []
		self.data = self.loadData(os.path.join("..","data",filename))

	def createBins(self, data, bins = 10):
		#Create ranges for data
		ranges = np.linspace(np.min(data), np.max(data), bins)
		#Ranges between ranges
		for low,high in zip(ranges[:1], ranges[1:]):
			data[np.where((data > low) * (data < high))] = (low + high)/2.0
		return data

	@debug
	def createRefs(self):
		"""
		Create Reference Dicts
		Feature - Var:(Description, Index)
		"""
		count = 0
		self.features = dict()
		for key,item in self.codebook.iteritems():
			self.features["V" + str(count)] = [key, item]
			count += 1

	def lookUp(self, var = None, desc = None):
		"""
		Look up a feature using the variable name or a description
		returns acroynym-description, indices
		"""
		if var:
			return self.features[var]
		elif desc:
			results = []
			for key,item in self.features.iteritems():
				if desc.lower() in item[0].lower():
					results.append((key,item))
			return results
		else:
			return list

	def loadData(self,filename):
		"""
		Loads the Data Set from filename as numpy array
		"""
		data = []
		with open(filename, 'rb') as f:
			for line in f:
				data.append(list(line.strip()))
		self.data = np.array(data)
		self.costId = self.lookUp(desc = "CHG")[0][0] # V49
		self.cost = self.getColumn(self.costId)
		return self.data

	def getColumn(self, var):
		"""
		Gets the column of data given by var
		"""
		ranges = self.lookUp(var = var)[1]
		rawData = self.data[:,ranges[0] - 1:ranges[1]]
		newFormat = np.zeros(shape = (rawData.shape[0]))
		print var
		for i in range(len(rawData)):
			try:
				newFormat[i] = "".join(rawData[i]).strip()
			except:
				print "data is not a number"
		return newFormat
	def save(self, filename):
		with open(filename, 'wb') as f:
			p.dump(self, f)
			print filename + " Saved Successfully"

	def load(self, filename):
		"""
		Saves this object as a pickle file for access later
		"""
		with open(filename, 'rb') as f:
			self = p.load(f)
			print filename + " Loaded Successfully"

	"""
	Class native methods
	"""
	def __repr__(self):
		return "Data Handler Object"

	def __str__(self):
		return "Attributes: \ndata\t\t - contains dataset as a numpy array\nindicies\t - contains variables:indicies dictionary\nfeatures\t - contains variables:feature descriptions as dictionary"

if __name__ == "__main__":
	print "See Documentation"