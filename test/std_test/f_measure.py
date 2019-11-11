class f_measure:

    def dff(self, sentence_correct, thai_hmong):

        # ตัดเครื่องหมายออก
        split = [',', '?', "!",'.']
        for i in split:
            sentence_correct = sentence_correct.split(i)
            sentence_correct = " ".join(sentence_correct)
            thai_hmong = thai_hmong.split(i)
            thai_hmong = " ".join(thai_hmong)

        # เปลี่ยนเป็นอักษรตัวเล็กให้หมด
        sentence_correct = sentence_correct.lower()
        thai_hmong = thai_hmong.lower()

        # แยกคำเพื่อตรวจสอบ
        sentence_correct = sentence_correct.split()
        thai_hmong = thai_hmong.split()

        print("se :", sentence_correct)
        print("th :", thai_hmong)

        total = []
        total.append(thai_hmong)
        correct = []
        for sentence in total:
            true = 0
            sentence_true = []
            for word in sentence:
                if (word in sentence_correct):
                    true += 1
                    sentence_true.append(word)
            correct.append([true, sentence_true])

        # print(correct)
        output = []
        for i in range(len(correct)):
            try:
                pre = correct[i][0] / len(total[i])
            except Exception as e:
                pre = 0
            try:
                re = correct[i][0] / len(sentence_correct)
            except Exception as e:
                re = 0
            try:
                f_m = 2 * ((re * pre) / (re + pre))
            except Exception as e:
                f_m = 0

            get = {
                "precision": pre,
                "recall": re,
                "f_measure": f_m
            }
            del re, pre, f_m

            output.append(get)

        # print("\n--------------------\n")

        for i in output:
            print(i)
        return output


if __name__ == '__main__':

    # tt = f_measure()
    # t= 'zoo li cas lawm os'
    # test ='zoo li cas lawm '
    # print(tt.dff(t,test))

    text_true = """
tsis zoo li	tsis zoo	Tsis zoo hlo li
tsis yog kuv hais wb tsis tau sib ntsib dua nawb	tsis yog kuv hais wb tsis tau sib ntsib dua	
kuv tsis xav hais tias  wb tsis tau sib ntsib dua los nawb	kuv tsis xav hais tias  wb tsis tau sib ntsib dua los 	
tsis kuv tseem tsis tau muaj tus hlub		
kuv tsis muaj kwv tij li	kuv tsis muaj kwv tij	
tsis niam nyob tim kuv lub tsev	tsis niam nyob tim kuv tsev	
tu siab kuv tsis paub	tu siab kuv tsis paub dua	
ntshe kuv yuav pab tsis tau	xav tias kuv yuav pab tsis tau	
tsis thas rho		
tsis ua cas	tsis ua li cas	
kuv thov txim ntshe kuv mus tsis tau	kuv thov txim kuv mus tsis tau	
tsis ua cas kuv tsis khoom		
qhov ntawv  tsis yog teeb meem	ntawv tsis yog teeb meem	
tsis ua cas	tsis ua li cas	
tsis nawb ntawm no huab cua no	tsis tim no huab cua no	
ntuj tsis muaj huab	lub ntuj tsis muj huab	
kuv tsis nyiam ntuj no		
tseem tsis tau zaub mov na	tseem tsis tau zaub mov nawb	tsis tau zaub mov li
cov zaub mov uas kuv xaiv tseg tseem tsis tau nawb	cov khoom noj kuv tau hais tseg tseem tsis tau 	
no tsis yog yam kuv tau hais tseg na	qhov no tsis yog  yam uas kuv xaiv 	no tsis yog qhov xaiv tseg nawb
thov txim vim peb tsis tau muaj chaw khoom tam sim no li	thov txim peb tsis muaj chaw khoom tam sim no	
kuv tsis paub tseeb		
tsis hais txog noj tshais	tsis hais koom txog mov sawv ntxov	tsis koom zaub mov sawv ntxov
naws tsis yog koj li		
nws tsis to taub lawv	nws tsis nkag siab lawv	
kuv noj mov tsis tshua kab li	kuv noj mov tsis kab li	
koj yuav tsum tsis ua li ntawv		
tsis ua cas li	tsis ua cas	
kuv tsis muaj dab tsi yuav pom zoo thiab	kuv tsis muaj dab tsi yuav pom zoo 	
thov txim kuv tsis pom zoo nro koj thaib	thov txim kuv tsis pom zoo nro koj 	
tsis paub ua	tsis txawj ua	
kuv tsis paub tsav tsheb		
tseem tsis tau noj kuv tab tom xav tib yam		
ntshe yuav tsis tau		
kuv tsis muaj kwv tij li		
tseem tsis tau txiav txim siab		
kuv tsis muaj me nyuam		
tsis ua cas		
tsis ua cas		
tsis ua cas nrhiav tau nawb	tsis ua cas nrhiav tau	
kuv tu siab ntshe kuv yuav ua yam ntawv tsis tau rau koj		
thov txim tam sis qhov ntawv ua mus tsis tau 		
ntshe kuv xav tias kuv tsis hnov yam ntawv		
tiam sis kuv tsis tau txhob txwm ua li ntawv		
tsis ua cas		
tsis ua cas kuv yuam qhuav nkag los		
kuv tsis tshuam nyiam xim no npaum cas		
tsis aum dab tsi lawm ua tsaug		
tsis thas rov		
thov tsim pab tsis muag nqaij nyuj		
tsis deb ntawm no		
tsis muaj kuv yog me nyuam ib leeg 	tsis muaj kuv yog ib leej me nyuam 	
kuv xav tsis tawm li		
dej tsis muaj xim li		
luav tsis noj nqaij tsiaj		
nab tsis muaj kaw taw		
tsis muaj		
tsis kuv tsis tau  teem sib hawm	tsis yog kuv tsis tau teem sib hawm	
kuv ntshai hais tias yuav tsis txog	kuv ntshai hais tias yuav tsis hauv lub sijhawm	
tsis lawm ua tsaug		
tam sim no lawv tsis nyob		
ua tsaug tsis yog tam sim no		
tsis yog kuv tsav tsheb mus kuv xwb	tsis yog kuv tsav tsheb mus xeb	
kuv tsis paub tseeb		
ua tsaug tsis ua cas	ua tsaug tsis us li cas	
tsis ntev ntshe 10 feeb	tsis txog 10 feeb	
tsis ua cas		
kuv tsis paub lawv tiam sis kuv xav tias kuv tus muam paub		
tsis ua cas thov kom muaj kev xyiv fab nrog kev taug kev		
kuv tseem txiav txim siab tsis tau 	kuv tseem txiav txim siab tsis tau  lib	
tsis muaj li pib mob thaum twg		
tam sis kuv tsis nyiam xim no		
kuv tsis nyiam caij ntuj no		
tsis tau dua	tsis tau ua dua	
tiam sis kuv xav tias kuv yuav mus tsis tau	tiam sis ntshe kuv xav tias kuv yuav mus tsis tau	
kuv tsis tau pom koj los 2-3 hlis lawm		
kuv yuav tsis peem paiv lawm		
kuv tsis nyiam nab		
kuv tsis tshuam muaj sib hawm khoom		
kuv tsis muaj sib hawm nyeem ntawv li		
kuv tsis tau noj nws los dua li		
nws tsis khoom li nws tuaj tsis tau		
koj tsis nyob tsev kawm ntawv nag hmo	koj tsis nyob tim tsev kawm ntawv nag hmo	
tsis thas ntshai miv		
txiv thiab niam tsis pov tseg me nyaum cia ib leeg tim tsev	niam txiv tsis pov tseg me nyaum cia ib leeg tim tsev	
lus noog nyuaj tshaj kuv teb tsis tau		
tus ris no tsis ntxim nro kuv		
koj tsis tau pw tsaug zog tam sim no koj sawv	koj tsis tau pw tsaug zog tam sim no koj pw sawv	
qhov no yog txiv chais tsis zoo	no yog txiv fhais tsis zoo	
peb  npo pa siav tsis tau ntev		
dej tsis ntshiab		
peb ntsia tsis pom dab tsi		
xib hwb hais zaj tseem tsis xaus 		
kuv yuav tsis nco hnub ntawd 		
kuv tsis paub lo lus txhais lo lus no 		
tsis muaj leej twg paub koj txoj hmoov 		
koj tsis tau muaj nplhaib 		
tsiaj nyob tsis tau yog tsis muaj zaub mov 		
koj tsis muaj dab tsi yuav ua 		
Nws mob siab thaum nws cov phooj ywg nyob deb.		
nws tsis zoo nyob		
hnub no nws tsis mus kawm ntawv.		
tus kws kho mob nriav nws li kab mob tsis tau.		
tiab no tsis phim rau kuv 		
nws mus tsev kawm ntawv tsis tau vim nws mob 	koj mus tsev kawm ntawv tsis tau vim koj mob	
nws yog mus tsis tau uas ntse yuav ya	nes yog tsis tau uas ntse yuav ya	
tsis muaj leej twg nyob haum ntawd 	tsis muaj leej twg nyob haum hauv	
zaj no tsis yog qhov ntxim siab 	zaj no tsis yog yam uas ntxim siab	
no tsis yog tsev viv poj niam 		
peb tsis nyiam mloog nkauj 		
nyiaj tsis yog yam uas tseem ceeb 		
koj tsis tau mus qhov twg li	nws tsis tau mus qhov twg li	
nws tsis nyiam kev tsav tsheb hauv sij hawm hmo ntuj 	nws tsis nyiam kev tsav tsheb haum sij hawm hmo ntuj	
kuv tsis ntseeg txiv thiab niam	kuv tsis moog niam txiv lus	kuv tsis moog niam txiv 
kuv tsis muaj kev xav	kuv tsis tawm kev xav	
tsis tau hais tias nws zoo	tsis tau hais tias nws zoo tshaj	
tsis muaj lus nug ntawm tub kawm 	tsis muaj lo lus nug ntawm tub kawm 	
kuv tsis tau yog tub kawm 	kuv tsis yog tub kawm ntawv	
nws tseem tsis txhij rau kev xeem 	nws tseem tsis txhij rau kev xeem ntawv	
no tsis yog khoom tiag	nov tsis yog yam tiag	
kuv tseem tsis tau txais tsab ntawv ntawm koj 		
koj li lus teb tsis ncaj raws lus teb 	koj lo lus teb tsis ncaj nro lo lus teb	
koj cim tsis tau koj li xov tooj 	new cim tsis tau nws tus xov tooj	
tsis muaj leej twg yuav hais li ntawv tau		
ntshe kuv yuav ntsia tsis pom koj tau	ntshe kuv yuav ntsia tsis pom koj 	
nws tsis tau txaj muag dua ntawm yam nws ua		
kuv tsis tau txob txwm uas yuav tab kaum koj		
ntshe kuv yuav ua luam dej hla tus dej tsis tau		
phooj ywg lwm teb chaws feem ntau tsis nkag siab lus thaib		
tsis pub kom cheb loj nres haum tsev kawm ntawv		
nws tsis tau mus xyuas nws txiv thiab niam los 3 xyoo	nws tsis tau mus xyuas nws txiv thiab nws niam yog 3 xyoo	
ntshe kuv tsis them nyiaj 		
nws tsis tau ntxuav tais	lawv tsis tau ntxuav tais kiag li	
kuv ntseeg tias tsis muaj dab		
nws pw khaws zog tsis txaus haum hmo uas daug los	nws pw tsis tsaus haum hmo uas daug los	


    """

    text_test = """
Tsis zoo kiag li. 
Tsis li kuv, peb muaj yeej tsis ntsib. 
Kuv tsis xav tias peb tuaj ua ntej. 
Tsis yog, kuv kuj nkaus xwb. 
Kuv muaj cov kwv tij tsis txhua. 
Tsis niam ntawm kuv tsev 
Thov txim kuv tsis paub. 
Tsam kuv tej zaum yuav pab koj. 
Ntsoos ntsoos tsis tau 
tsis ua li cas 
Kuv thov txim, kuv tsis tau mus. 
tsis ua li cas Kuv yog tibneeg hu tauj coob 
Tsis uas yog ib qho teeb meem. 
tsis ua li cas 
Tsis dhau Ntawm no yog tus mob khaub thuas. 
Ntuj pos huab 
Kuv tsis nyiam caij ntuj no. 
Tsis muaj mov noj. 
Khoom noj khoom haus kuv yuam mus tsis txhua. 
Qhov no yog ib qho chaw rau txim tsis. 
Thov txim, tab sis peb tsis muaj chaw seem twg tamsim. 
kuv tsis paub tseeb thiab  
Noj tshais yog tsis tso cai muaj. 
Nws tsi muaj koj li. 
Nws yeej tsis to taub txog nws. 
Kuv tsis tau noj mov qab. 
Koj yuav tsum tsis tau ua li ntawd. 
Tau lawm os. 
Kuv tsis muaj dabtsi rau koj saib. 
Kuv thov txim. Kuv tsis pom zoo nrog koj. 
Tsis tau. 
Kuv tsis tsav lub tsheb mus. 
Nws tseem tsis tau noj Kuv xav txog nws. 
Tsam tsis 
Kuv muaj cov kwv tij tsis txhua. 
Kuv tseem tsis tau txiav txim siab 
Kuv tsis muaj me nyuam. 
tsis ua li cas 
Tau lawm os. 
Tau lawm os. Tau txais tam sim no nws 
Kuv thov txim, kuv ntshai koj yuav tsis tau ua uas rau koj tau. 
Thov txim, tab sis nws tseem tsis tau. 
Kuv txawm ntshai tias kuv yeej tsis hnov ntawd. 
Tab sis kuv tsis npaj siab yuav ua ntawd. 
Tau lawm os.  
Tau lawm os. Kuv nyuam qhuav tuaj nyob rau hauv. 
Kuv kuj tsis ntau pes tsawg li no lub twg. 
Tsis txhob noj txhua yam thiab ua koj tsaug 
Tsis ntab 
Thov txim, peb tsis pub muag nqaij nyug. 
Tsis far from qhov no 
Tsis yog, kuv tus me nyuam xwb. 
Kuv tsis tau xav txog nws. 
Dej yog tsis dawb txhua. 
Luav tsis noj nqaij. 
Nab tsis muaj ko taw 
Tsis tag ntiav. 
Tsis tag ntiav. Kuv tsis paub lub sij hawm teem tseg. 
Kuv ntshai tsis tau tuaj. 
Tsis yog, lawm tsaug 
Nws tsi muaj tam sim no. 
Tsaug, tsis yog tam sim no.  
Tsis muaj. Kuv tsav kuv tus kheej. 
kuv tsis paub tseeb thiab  
Ua tsaug, xyua. 
Tsis tau li 10 feeb. 
Tau lawm os. 
Kuv tsis paub nws, tab sis kuv xav hais tias kuv tus muam paub lawm. 
Tias kev txaus siab rau koj mus txawv tebchaws. 
Kuv tseem tsis tau txiav txim. 
Tsis paub, tsis tau. Thaum pib mob ua? 
Tab sis kuv tsis nyiam no cov xim. 
Kuv tsis nyiam caij ntuj no. 
Tsis tau!  
Tab sis kuv ntshai tias kuv mus tsis tau. 
Kuv tsis pom koj mus li 2-3 lub hlis.  
Kuv yuav tsis ua tiag piav txog nws. 
Kuv tsis nyiam cov nab. 
Kuv tsis muaj sij hawm dawb npaum li cas. 
Kuv yuav tsum tsis muaj sij hawm nyeem cov phau ntawv. 
Kuv puas tas ua ntej nws. 
Nws yog tibneeg hu tauj coob heev. Nws tuaj tsis tau. 
Nws yuav tsis nyob lub tsev kawm ntawv nag hmo. 
Tsis txhob ntshai miv. 
Niam txiv yeej tsis ncaim lawv cov me nyuam nyob tom tsev. 
Cov lus nug no nyuaj heev. Kuv teb tsis tau. 
Ceg ris no yog tsis rau kuv. 
Nws yeej tsis pw tamsim. Nws tsim kom tsaug taus zog. 
Qhov no nws yog ib tug txiv nkhaus taw phem.  
Peb tsis tau tuav ib pa ntev. 
Dej yuav tsis ntshiab. 
Peb yuav tsis pom dab tsi. 
Tus xib fwb hais zaj dabneeg tsis dhau. 
Kuv yuav tsis nco qab txog cov hnub ntawd. 
Kuv tsis paub lub ntsiab txhais lo lus no. 
Tsis muaj leej twg paub nws hmoo. 
Nws tsis muaj ib lub nplhaib. 
Cov tsiaj no tsis tsis muaj zaub mov. 
Nws twb tsis muaj dab tsi ua. 
Nws muaj kev tsis zoo thaum ib tug phooj ywg nyob deb. 
Nws seeb.  
Hnub no nws yuav tsis mus kawm ntawv. 
Tus kws kho mob yuav tsis paub ua kom muaj tus mob no. 
Dab no tsis haum rau kuv. 
Nws tsis tau mus kawm ntawv vim hais tias nws muaj mob. 
Tseem tsis tau tias tus ntses yuav ya. 
Tsis muaj leej twg puas muaj. 
Nws yuav tsis nthuav. 
Qhov no yog ib tug poj niam viv tsis. 
Peb tsis nyiam mloog nkauj. 
Nyiaj yog tsis tsim nyog. 
Nws yeej tsis mus nowhere. 
Nws tsis nyiam tsav thaum hmo ntuj. 
Kuv tsis mloog lus kuv niam thiab txiv. 
Kuv tsis muaj ib tug saib. 
Qhov zoo tshaj yog tsis sau tseg qhia. 
Tsis muaj me nyuam kawm ntawv cov lus nug 
Kuv kuj tsis yog ib tug me nyuam kawm ntawv 
Nws tsis yog npaj rau cov tub ntxhais. 
Qhov no yuav tsis tau ib tug ntawm 
Kuv tsis tau txais ntawv ntawm nws. 
Koj cov lus teb tsis tau raws li cov lus teb. 
Nws yuav tsis nco qab nws tus xov tooj. 
Tsis muaj leej twg yuav hais tau tias. 
Kuv tsis pom nws. 
Nws yeej tsis muaj kev paub txaj muag rau nws ua dab tsi. 
Kuv yeej tsis npaj siab yuav mus thab koj. 
Kuv tsis tau da dej hla tus dej. 
Phooj ywg tseev tsim ntiaj teb feem coob tsis to taub cov lus thaib. 
Lawv yuav tsis pub nyob rau hauv lub tsev kawm ntawv. 
Nws puas tau tsis mus ntsib niam leej txiv rau peb xyoos. 
Kuv tsis tau them nyiaj ntsuab 
Nws yeej tsis ntxuav phaj. 
Kuv ntseeg hais tias yog tsis muaj dab. 
Nws muaj tsis txaus los pw hauv cov nag hmo. 


    """

    text_test = text_test.strip()
    sentence_test = text_test.splitlines()

    text_true = text_true.strip()
    text_true = text_true.splitlines()
    sentence_true = []
    for sen in text_true:
        sen = sen.split("\t")
        total_sen = []
        for sentence in sen:
            sentence = sentence.strip()
            if (sentence != ''):
                total_sen.append(sentence)
        # print(total_sen)
        sentence_true.append(total_sen)

    print(sentence_true)
    print(sentence_test)
    print("\n")
    a = f_measure()
    f_m = []
    count = 0
    for sentence in sentence_true:
        point = []
        for j in range(len(sentence)):
            tt = a.dff(sentence[j], sentence_test[count])
            point.append(tt[0]['f_measure'])
            print("xx--",tt[0]['f_measure'])
        print("p : ", point)
        max_point = max(point)
        f_m.append(max_point)
        print("max point : ", max_point)
        count += 1
        print("\n")
    print("\n---------------------\n")
    for i in f_m:
        print('%.2f ' % (i))
