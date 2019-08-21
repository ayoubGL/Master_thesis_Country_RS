 # ________________gender__________________
Male ='Male'
Female ='Female'
refuse_to_disc = 'Refuse to disclose'
# ________________Age__________________
under_18 = 'under_18'
b18_24 = '18_24'
b25_35 = '25_35'
b35_45 = '35_45'
b45_55 = '45_55'
bover_55 = 'Over_55'
# ______________ choices  Level ___________
Strongly_Disagree  ='Strongly Disagree'
Disagree = 'Disagree'
Neutral = 'Neutral'
Agree = 'Agree'
Strongly_Agree='Strongly Agree'


Gender_choices = [
        ('Male','Male'),
        ('Female','Female'),
        ('refuse_to_disc','Refuse to disclose')
    ]
    
Age_choices = [
        ('under_18','Under 18'),
        ('b18_24','18 24'),
        ('b25_35','25 35'),
        ('b35_45','35 45'),
        ('b45_55','45 55'),
        ('bover_55','Over 55')
    ]
(Str_vb_D,Str_vb_N)= ('Strongly_Disagree','Strongly Disagree')
(Dis_vb_D,Dis_vb_N)= ('Disagree','Disagree')
(Nt_vb_D,Nt_vb_N)= ('Natural','Natural')
(Ag_vb_D,Ag_vb_N)= ('Agree','Agree')
(StrAG_vb_D,StrAG_vb_N)= ('Strongly_Agree','Strongly Agree')

Imaginative_choices =[
        (Str_vb_D,Str_vb_N),
        (Dis_vb_D,Dis_vb_N),
        (Nt_vb_D,Nt_vb_N),
        (Ag_vb_D,Ag_vb_N),
        (StrAG_vb_D,StrAG_vb_N)
    ]
Organized_choices =[
        (Str_vb_D,Str_vb_N),
        (Dis_vb_D,Dis_vb_N),
        (Nt_vb_D,Nt_vb_N),
        (Ag_vb_D,Ag_vb_N),
        (StrAG_vb_D,StrAG_vb_N)
    ]
Enthusiastic_choices =[
        (Str_vb_D,Str_vb_N),
        (Dis_vb_D,Dis_vb_N),
        (Nt_vb_D,Nt_vb_N),
        (Ag_vb_D,Ag_vb_N),
        (StrAG_vb_D,StrAG_vb_N)
    ]
kind_choices =[
        (Str_vb_D,Str_vb_N),
        (Dis_vb_D,Dis_vb_N),
        (Nt_vb_D,Nt_vb_N),
        (Ag_vb_D,Ag_vb_N),
        (StrAG_vb_D,StrAG_vb_N)
    ]
Calm_choices =[
        (Str_vb_D,Str_vb_N),
        (Dis_vb_D,Dis_vb_N),
        (Nt_vb_D,Nt_vb_N),
        (Ag_vb_D,Ag_vb_N),
        (StrAG_vb_D,StrAG_vb_N)
    ] 

#------------------ Features -----------------------
Education_quality ='Education Quality'
Political_insecurity ='Political Insecurity'
Social_conflict= 'Social Conflict'
work_opportunities= 'Work Opportunities'
Health_care= 'Health care'
Income_difference= 'Income Difference'
Wars_Dictatorship= 'Wars & Dictatorship'
Family_member_abroad= 'Family Member Abroad'
cultural_and_linguistic_similarities= 'Cultural & Linguistic Similarities'
Working_atmosphere= 'Working Atmosphere'
Shorter_Distance = 'Shorter Distance'
Crime_rate= 'Crime Rate'

features_choices = [
(Education_quality ,'Education Quality'),
(Political_insecurity,'Political Insecurity'),
(Social_conflict ,'Social Conflict'),
(work_opportunities, 'Work Opportunities'),
(Health_care, 'Health Care'),
(Income_difference, 'Income Difference'),
(Wars_Dictatorship, 'Wars & Dictatorship'),
(Family_member_abroad, 'Family Member Abroad'),
(cultural_and_linguistic_similarities, 'Cultural & Linguistic Similarities'),
(Working_atmosphere, 'Working Atmosphere'),
(Shorter_Distance , 'Shorter Distance'),
(Crime_rate, 'Crime Rate')
]

# ------------------------ Usability Survey ------------------------

usage_frequency =[
        (Str_vb_D,Str_vb_N),
        (Dis_vb_D,Dis_vb_N),
        (Nt_vb_D,Nt_vb_N),
        (Ag_vb_D,Ag_vb_N),
        (StrAG_vb_D,StrAG_vb_N)
    ]
system_complexity =[
        (Str_vb_D,Str_vb_N),
        (Dis_vb_D,Dis_vb_N),
        (Nt_vb_D,Nt_vb_N),
        (Ag_vb_D,Ag_vb_N),
        (StrAG_vb_D,StrAG_vb_N)
    ]
usage_ease =[
        (Str_vb_D,Str_vb_N),
        (Dis_vb_D,Dis_vb_N),
        (Nt_vb_D,Nt_vb_N),
        (Ag_vb_D,Ag_vb_N),
        (StrAG_vb_D,StrAG_vb_N)
    ]
need_help =[
        (Str_vb_D,Str_vb_N),
        (Dis_vb_D,Dis_vb_N),
        (Nt_vb_D,Nt_vb_N),
        (Ag_vb_D,Ag_vb_N),
        (StrAG_vb_D,StrAG_vb_N)
    ]
functions_integrated =[
        (Str_vb_D,Str_vb_N),
        (Dis_vb_D,Dis_vb_N),
        (Nt_vb_D,Nt_vb_N),
        (Ag_vb_D,Ag_vb_N),
        (StrAG_vb_D,StrAG_vb_N)
    ] 
system_inconsistency =[
        (Str_vb_D,Str_vb_N),
        (Dis_vb_D,Dis_vb_N),
        (Nt_vb_D,Nt_vb_N),
        (Ag_vb_D,Ag_vb_N),
        (StrAG_vb_D,StrAG_vb_N)
    ]
learn_to_use =[
        (Str_vb_D,Str_vb_N),
        (Dis_vb_D,Dis_vb_N),
        (Nt_vb_D,Nt_vb_N),
        (Ag_vb_D,Ag_vb_N),
        (StrAG_vb_D,StrAG_vb_N)
    ] 
system_inconvenient =[
        (Str_vb_D,Str_vb_N),
        (Dis_vb_D,Dis_vb_N),
        (Nt_vb_D,Nt_vb_N),
        (Ag_vb_D,Ag_vb_N),
        (StrAG_vb_D,StrAG_vb_N)
    ] 
confident_level =[
        (Str_vb_D,Str_vb_N),
        (Dis_vb_D,Dis_vb_N),
        (Nt_vb_D,Nt_vb_N),
        (Ag_vb_D,Ag_vb_N),
        (StrAG_vb_D,StrAG_vb_N)
    ]
learning_before =[
        (Str_vb_D,Str_vb_N),
        (Dis_vb_D,Dis_vb_N),
        (Nt_vb_D,Nt_vb_N),
        (Ag_vb_D,Ag_vb_N),
        (StrAG_vb_D,StrAG_vb_N)
    ] 


# ------------------------ Countries ------------------------

Afghanistan=	"Afghanistan"
Albania=	"Albania"
Algeria=	"Algeria"
AmericanSamoa=	"American Samoa"
Andorra=	"Andorra"
Angola=	"Angola"
Anguilla=	"Anguilla"
Antarctica=	"Antarctica"
Antigua =	"Antigua"
Argentina=	"Argentina"
Armenia="Armenia"
Aruba=	"Aruba"
Australia=	"Australia"
Austria=	"Austria"
Azerbaijan=	"Azerbaijan"
Bahamas=	"Bahamas"
Bahrain=	"Bahrain"
Bangladesh=	"Bangladesh"
Barbados=	"Barbados"
Belarus=	"Belarus"
Belgium=	"Belgium"
Belize=	"Belize"
Benin=	"Benin"
Bermuda	= "Bermuda"
Bhutan=	"Bhutan"
Bolivia=	"Bolivia"
Bonaire =	"Bonaire"
Bosnia=	"Bosnia and Herzegovina"
Botswana=	"Botswana"
BouvetIsland=	"Bouvet Island"
Brazil=	"Brazil"
Brunei=	"Brunei"
Bulgaria=	"Bulgaria"
BurkinaFaso=	"Burkina Faso"
Burundi=	"Burundi"
CaboVerde=	"Cabo Verde"
Cambodia=	"Cambodia"
Cameroon=	"Cameroon"
Canada=	"Canada"
CaymanIslands=	"Cayman Islands"
CentralAfrican ="Central African Republic"
Chad=	"Chad"
Chile=	"Chile"
China=	"China"
ChristmasIsland=	"Christmas Island"
Colombia=	"Colombia"
Comoros=	"Comoros"
Congo=	"Congo"
CookIslands=	"Cook Islands"
CostaRica=	"Costa Rica"
CotedIvoire=	"Côte d'Ivoire"
Croatia=	"Croatia"
Cuba=	"Cuba"
Curacao=	"Curaçao"
Cyprus=	"Cyprus"
Czechia=	"Czechia"
Denmark=	"Denmark"
Djibouti=	"Djibouti"
Dominica=	"Dominica"
DominicanRepublic=	"Dominican Republic"
Ecuador=	"Ecuador"
Egypt=	"Egypt"
Salvador=	"El Salvador"
EquatorialGuinea=	"Equatorial Guinea"
Eritrea=	"Eritrea"
Estonia=	"Estonia"
Eswatini=	"Eswatini"
Ethiopia=	"Ethiopia"
Fiji=	"Fiji"
Finland="Finland"
France=	"France"
Gabon=	"Gabon"
Gambia=	"Gambia"
Georgia=	"Georgia"
Germany=	"Germany"
Ghana=	"Ghana"
Gibraltar=	"Gibraltar"
Greece=	"Greece"
Greenland=	"Greenland"
Grenada=	"Grenada"
Guadeloupe=	"Guadeloupe"
Guam=	"Guam"
Guatemala=	"Guatemala"
Guernsey=	"Guernsey"
Guinea=	"Guinea"
GuineaBissau=	"Guinea-Bissau"
Guyana=	"Guyana"
Haiti=	"Haiti"
Honduras=	"Honduras"
HongKong=	"Hong Kong"
Hungary=	"Hungary"
Iceland=	"Iceland"
India=	"India"
Indonesia=	"Indonesia"
Iran=	"Iran"
Iraq=	"Iraq"
Ireland=	"Ireland"
Italy=	"Italy"
Jamaica=	"Jamaica"
Japan=	"Japan"
Jersey=	"Jersey"
Jordan=	"Jordan"
Kazakhstan=	"Kazakhstan"
Kenya=	"Kenya"
Kiribati=	"Kiribati"
Kuwait=	"Kuwait"
Kyrgyzstan=	"Kyrgyzstan"
Laos=	"Laos"
Latvia=	"Latvia"
Lebanon=	"Lebanon"
Lesotho=	"Lesotho"
Liberia=	"Liberia"
Libya=	"Libya"
Liechtenstein=	"Liechtenstein"
Lithuania=	"Lithuania"
Luxembourg=	"Luxembourg"
Macao=	"Macao"
Macedonia=	"Macedonia"
Madagascar=	"Madagascar"
Malawi=	"Malawi"
Malaysia=	"Malaysia"
Maldives=	"Maldives"
Mali=	"Mali"
Malta=	"Malta"
Martinique=	"Martinique"
Mauritania=	"Mauritania"
Mauritius=	"Mauritius"
Mayotte=	"Mayotte"
Mexico=	"Mexico"
Moldova=	"Moldova"
Monaco=	"Monaco"
Mongolia=	"Mongolia"
Montenegro=	"Montenegro"
Montserrat=	"Montserrat"
Morocco=	"Morocco"
Mozambique=	"Mozambique"
Myanmar=	"Myanmar"
Namibia=	"Namibia"
Nauru=	"Nauru"
Nepal=	"Nepal"
Netherlands=	"Netherlands"
NewZealand =	"New Zealand"
Nicaragua=	"Nicaragua"
Niger=	"Niger"
Nigeria=	"Nigeria"
Niue=	"Niue"
NorthKorea=	"North Korea"
Norway=	"Norway"
Oman=	"Oman"
Pakistan=	"Pakistan"
Palau=	"Palau"
Palestine= "Palestine"
Panama=	"Panama"
Paraguay=	"Paraguay"
Peru=	"Peru"
Philippines=	"Philippines"
Pitcairn=	"Pitcairn"
Poland=	"Poland"
Portugal=	"Portugal"
Qatar=	"Qatar"
Reunion=	"Réunion"
Romania=	"Romania"
Russia=	"Russia"
Rwanda=	"Rwanda"
SaudiArabia=	"Saudi Arabia"
Senegal=	"Senegal"
Serbia=	"Serbia"
Seychelles=	"Seychelles"
SierraLeone=	"Sierra Leone"
Singapore=	"Singapore"
Slovakia=	"Slovakia"
Slovenia=	"Slovenia"
SolomonIslands=	"Solomon Islands"
Somalia=	"Somalia"
SouthAfrica="South Africa"
SouthKorea=	"South Korea"
Spain=	"Spain"
SriLanka=	"Sri Lanka"
Sudan=	"Sudan"
Suriname=	"Suriname"
Sweden=	"Sweden"
Switzerland=	"Switzerland"
Syria=	"Syria"
Taiwan=	"Taiwan"
Tajikistan=	"Tajikistan"
Tanzania=	"Tanzania"
Thailand=	"Thailand"
Togo=	"Togo"
Tokelau=	"Tokelau"
Tonga=	"Tonga"
Tunisia=	"Tunisia"
Turkey=	"Turkey"
Tuvalu=	"Tuvalu"
Uganda=	"Uganda"
Ukraine="Ukraine"
UAE="UAE"
UK=	"UK"
USA =	"USA"
Uruguay=	"Uruguay"
Uzbekistan=	"Uzbekistan"
Vanuatu=	"Vanuatu"
Venezuela=	"Venezuela"
Vietnam=	"Vietnam"
Yemen=	"Yemen"
Zambia=	"Zambia"
Zimbabwe=	"Zimbabwe"
# ----------- choices ----------------------

country_name =[
(Afghanistan,	"Afghanistan"),
(Albania,	"Albania"),
(Algeria,	"Algeria"),
(AmericanSamoa,	"American Samoa"),
(Andorra,	"Andorra"),
(Angola,	"Angola"),
(Anguilla,	"Anguilla"),
(Antarctica,	"Antarctica"),
(Antigua ,	"Antigua"),
(Argentina,	"Argentina"),
(Armenia,"Armenia"),
(Aruba,	"Aruba"),
(Australia,	"Australia"),
(Austria,	"Austria"),
(Azerbaijan,	"Azerbaijan"),
(Bahamas,	"Bahamas"),
(Bahrain,	"Bahrain"),
(Bangladesh,	"Bangladesh"),
(Barbados,	"Barbados"),
(Belarus,	"Belarus"),
(Belgium,	"Belgium"),
(Belize,	"Belize"),
(Benin,	"Benin"),
(Bermuda	, "Bermuda"),
(Bhutan,	"Bhutan"),
(Bolivia,	"Bolivia"),
(Bonaire ,	"Bonaire"),
(Bosnia,	"Bosnia"),
(Botswana,	"Botswana"),
(BouvetIsland,	"Bouvet Island"),
(Brazil,	"Brazil"),
(Brunei,	"Brunei"),
(Bulgaria,	"Bulgaria"),
(BurkinaFaso,	"Burkina Faso"),
(Burundi,	"Burundi"),
(CaboVerde,	"Cabo Verde"),
(Cambodia,	"Cambodia"),
(Cameroon,	"Cameroon"),
(Canada,	"Canada"),
(CaymanIslands,	"Cayman Islands"),
(CentralAfrican ,"Central African Republic"),
(Chad,	"Chad"),
(Chile,	"Chile"),
(China,	"China"),
(ChristmasIsland,	"Christmas Island"),
(Colombia,	"Colombia"),
(Comoros,	"Comoros"),
(Congo,	"Congo"),
(CookIslands,	"Cook Islands"),
(CostaRica,	"Costa Rica"),
(CotedIvoire,	"Côte d'Ivoire"),
(Croatia,	"Croatia"),
(Cuba,	"Cuba"),
(Curacao,	"Curaçao"),
(Cyprus,	"Cyprus"),
(Czechia,	"Czechia"),
(Denmark,	"Denmark"),
(Djibouti,	"Djibouti"),
(Dominica,	"Dominica"),
(DominicanRepublic,	"Dominican Republic"),
(Ecuador,	"Ecuador"),
(Egypt,	"Egypt"),
(Salvador,	"El Salvador"),
(Eritrea,	"Eritrea"),
(Estonia,	"Estonia"),
(Eswatini,	"Eswatini"),
(Ethiopia,	"Ethiopia"),
(Fiji,	"Fiji"),
(Finland,"Finland"),
(France,	"France"),
(Gabon,	"Gabon"),
(Gambia,	"Gambia"),
(Georgia,	"Georgia"),
(Germany,	"Germany"),
(Ghana,	"Ghana"),
(Gibraltar,	"Gibraltar"),
(Greece,	"Greece"),
(Greenland,	"Greenland"),
(Grenada,	"Grenada"),
(Guadeloupe,	"Guadeloupe"),
(Guam,	"Guam"),
(Guatemala,	"Guatemala"),
(Guernsey,	"Guernsey"),
(Guinea,	"Guinea"),
(GuineaBissau,	"Guinea-Bissau"),
(Guyana,	"Guyana"),
(Haiti,	"Haiti"),
(Honduras,	"Honduras"),
(HongKong,	"Hong Kong"),
(Hungary,	"Hungary"),
(Iceland,	"Iceland"),
(India,	"India"),
(Indonesia,	"Indonesia"),
(Iran,	"Iran"),
(Iraq,	"Iraq"),
(Ireland,	"Ireland"),
(Italy,	"Italy"),
(Jamaica,	"Jamaica"),
(Japan,	"Japan"),
(Jersey,	"Jersey"),
(Jordan,	"Jordan"),
(Kazakhstan,	"Kazakhstan"),
(Kenya,	"Kenya"),
(Kiribati,	"Kiribati"),
(Kuwait,	"Kuwait"),
(Kyrgyzstan,	"Kyrgyzstan"),
(Laos,	"Laos"),
(Latvia,	"Latvia"),
(Lebanon,	"Lebanon"),
(Lesotho,	"Lesotho"),
(Liberia,	"Liberia"),
(Libya,	"Libya"),
(Liechtenstein,	"Liechtenstein"),
(Lithuania,	"Lithuania"),
(Luxembourg,	"Luxembourg"),
(Macao,	"Macao"),
(Macedonia,	"Macedonia"),
(Madagascar,	"Madagascar"),
(Malawi,	"Malawi"),
(Malaysia,	"Malaysia"),
(Maldives,	"Maldives"),
(Mali,	"Mali"),
(Malta,	Malta,),
(Martinique,	"Martinique"),
(Mauritania,	"Mauritania"),
(Mauritius,	"Mauritius"),
(Mayotte,	"Mayotte"),
(Mexico,	"Mexico"),
(Moldova,	"Moldova"),
(Monaco,	"Monaco"),
(Mongolia,	"Mongolia"),
(Montenegro,	"Montenegro"),
(Montserrat,	"Montserrat"),
(Morocco,	"Morocco"),
(Mozambique,	"Mozambique"),
(Myanmar,	"Myanmar"),
(Namibia,	"Namibia"),
(Nauru,	"Nauru"),
(Nepal,	"Nepal"),
(Netherlands,	"Netherlands"),
(NewZealand,	"New Zealand"),
(Nicaragua,	"Nicaragua"),
(Niger,	"Niger"),
(Nigeria,	"Nigeria"),
(Niue,	"Niue"),
(NorthKorea,	"North Korea"),
(Norway,	"Norway"),
(Oman,	"Oman"),
(Pakistan,	"Pakistan"),
(Palau,	"Palau"),
(Palestine, "Palestine"),
(Panama,	"Panama"),
(Paraguay,	"Paraguay"),
(Peru,	"Peru"),
(Philippines,	"Philippines"),
(Pitcairn,	"Pitcairn"),
(Poland,	"Poland"),
(Portugal,	"Portugal"),
(Qatar,	"Qatar"),
(Reunion,	"Réunion"),
(Romania,	"Romania"),
(Russia,	"Russia"),
(Rwanda,	"Rwanda"),
(SaudiArabia,	"Saudi Arabia"),
(Senegal,	"Senegal"),
(Serbia,	"Serbia"),
(Seychelles,	"Seychelles"),
(SierraLeone,	"Sierra Leone"),
(Singapore,	"Singapore"),
(Slovakia,	"Slovakia"),
(Slovenia,	"Slovenia"),
(SolomonIslands,	"Solomon Islands"),
(Somalia,	"Somalia"),
(SouthAfrica,"South Africa"),
(SouthKorea,	"South Korea"),
(Spain,	"Spain"),
(SriLanka,	"Sri Lanka"),
(Sudan,	"Sudan"),
(Suriname,	"Suriname"),
(Sweden,	"Sweden"),
(Switzerland,	"Switzerland"),
(Syria,	"Syria"),
(Taiwan,	"Taiwan"),
(Tajikistan,	"Tajikistan"),
(Tanzania,	"Tanzania"),
(Thailand,	"Thailand"),
(Togo,	"Togo"),
(Tokelau,	"Tokelau"),
(Tonga,	"Tonga"),
(Tunisia,	"Tunisia"),
(Turkey,	"Turkey"),
(Tuvalu,	"Tuvalu"),
(Uganda,	"Uganda"),
(Ukraine,"Ukraine"),
(UAE,"UAE"),
(UK,	"UK"),
(USA ,	"USA"),
(Uruguay,	"Uruguay"),
(Uzbekistan,	"Uzbekistan"),
(Vanuatu,	"Vanuatu"),
(Venezuela,	"Venezuela"),
(Vietnam,	"Vietnam"),
(Yemen,	"Yemen"),
(Zambia,	"Zambia"),
(Zimbabwe,	"Zimbabwe")
]