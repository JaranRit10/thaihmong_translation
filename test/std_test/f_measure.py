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
zoo li cas lawm os	nyob li cas law os	zoo li cas
paus nyob zoo thiab		
es koj neb	koj neb	
koj nyob zoo ua tsaug es koj neb		
nyob zoo koj zoo li cas lawm os		
nyob zoo kuv nyob zoo ua tsaub es koj neb		
koj nyob zoo ua tsaug koj yuav mus qhov twg		
kuv tab tom mus tom tsav ntawv koj paus mus		
nyob zoo ua taaug es koj neb		
koj nyob qhov twg tuaj	koj tuaj qhov twg tuaj	
nov yog		
nov yog thiam ntawv yog		
ntawv yog leej twg		
pev paus tau sib ntsib dua		
nyob zoo tus poj nyiam no yog leej twg		
peb qhai rau kuv paub me ntsis puas tau		
koj tuaj qhov twg tuaj		
koj li hnub yug yog hnub twg		
koj yug thaum twg		
kuv yug nyoo		
hnub koj yug yog thaum twg		
nws yug thaum twg		
koj npe hu li cas		
koj lub npe yog		
koj lub npe ua si hu yog		
koj yog leej twg		
koj lub xeem yog		
koj hais nws li cas		
koj hnub yug puas tsawg		
koj yug hnub twg		
koj yug hnub dab tsi		
koj yug thaum twg		
Koj yug qhov twg		
Koj siab puas tsawg		
Koj nyav puas tsawg		
Koj tuaj qhov twg tuaj		
koj muaj neeg dab tsi		
koj puas tau sib nyuav		
koj puas muaj me nyuam thiab		
koj muaj me nyuam puas tsawg leeg	koj muaj me nyuam puas tsawg leej	
lawv kawm ntawv qhov twg		
koj tus txiv ua hauj lwm dab tsi		
lub tsev yug nyog qhov twg		
tam sim no koj so qhov twg		
Koj lub tsev nyob qhov twg		
koj qhov tsaw nyob yog qhov twg		
koj tsev neeg muaj pes tsawg leeg		
koj muaj kwv tig puas tsawg leeg		
koj puas muaj kwv tig		
koj nyiam koj tsiv puas ua hauj lwm 		
peb ua hauj lwm dab tsi		
tam sim no koj puas nyob nrog koj nyiam thiab koj tsiv		
koj ib leeg los		
 koj nyiam thiab koj tsiv puas tseem muaj txoj sia		
kuv nyiam nyob zoo		
koj nyob qhov twg		
koj nyob lub nroog dab tsi		
koj nyob hauv lub ntsoog dab tsi		
Koj lub tsev nyob qhov twg		
Koj ua hauj lwm dab tsi		
Koj ua hauj lwm dab tsi		
Tam sim no Koj ua dab tsi		
Koj txoj hauj lwm yog dab tsi		
Koj yog , puas yog		
Koj ua hauj lwm qhov twg		
koj li nyiaj hli npaum cas		
Koj tau nyiaj hli npaum cas		
Koj muaj nyiaj hli npaum cas		
Koj tau nqe ntiav ib hnub npaum cas	Koj tau nqe ntiav ib hnub li cas	
Koj nyiam dab tsi hauv lub hauj lwm uas tab tom ua		
es yog Koj tau hauj lwm uas nyob deb tsev		
nyob zoo , hnub so zoo li cas thiab		
Zoo tshaj li , es koj lub tsev yug koj nyob twg		
nyob qhov twg		
es koj naim thiab koj txiv neb zoo li cas thiab 		
tu siab thiab nawb , Tam sim no koj nyiam kuj nyob tim tsev		
tsis tau ntsib ua ke los ntev  , Tam sim no ua hauj lwm dab tsi		
Koj ua hauj lwm dab tsi swb		
koj xav yog dab tsi thaum koj loj hlob		
thov txim , Koj paub paus tias nyob qhov twg		
Koj paus paub txoj kev mus		
txoj kev no puas mus txog		
Kuv Yuav mus qhov ntawd tau li cas		
ntawm no paus yog txoj kev mus tim tnawv		
qhov ntawd nyob qhov twg		
txoj kev twg yog txoj kev mus		
kom kuv coj koj mus qhov twg		
Koj tab tom Yuav mus qhov twg		
nqe tsheb npaum cas		
thov txim txoj kev no paus yog mus qhov ntawv		
Hmo no paus mus noj mov ua ke 		
tag kis mus noj mov qhov twg 		
Hmo no Koj paus xav mus noj mov nrog kuv 		
tau maj , peb Yuav mus qhov twg Zoo 		
koj paus mus koom nrog peb 		
peb paus mus nrhiav dab tsi haus 		
paus Haus dej 		
nyob zoo , ua tsaug ,es Koj neb 		
nyob zoo , Koj xav noj mov nrog kuv 		
Yuav kom mus tos tsawg teev 		
Koj paus xav  so 		
peb mus puas tau tau		
Koj paus nyob ntawv		
Koj kawm qhov twg		
Koj tus xib hwb yog leej twg		
Koj tus xib hwb Lub npe hu li cas		
Koj kawm xyuam tim dab tsi		
xuj dab tsi uas Koj nyiam		
xuj uas Koj nyiam thaum kawg yog xuj dab tsi		
Koj nyiam ua dab tsi hauv sib hawm vaaj		
hauj lwm uas Koj txaus siab yog dab tsi	hauj lwm uas Koj nyiam yog dab tsi	
Koj muaj kawm ntau npaum li cas		
koj tsav kawm pib tsawg teev		
Koj lawb ntawv thaum tsawg teev		
tav su no koj puas muaj kawm		
Koj paus mus tsev kawm ntawv txhua hnub		
Koj sawv kev mus tsev kawm ntawv li cas		
Koj kawm tiav lawm los tsis tau tiav		
kev kawm siab kawg nkaus ntawm koj yog dab tsi		
Koj kawm kev kawm dab tsi		
Koj mus tsev kawm ntawv hom twg		
Kuv kawm tiav qhov	Kuv kawm xaus qhov	
Koj kawm tiav qhov twg los		
Koj kawm Xyoo twg		
koj paus muaj teeb meem dab tsi		
nws yog dab tsi		
koj nyob chav twg		
Koj puas tau mus tim tsev kawm ntawv los		
Koj paus tau mus tim tsev kawm ntawv		
Koj tab tom yuav mus tim tsev kawm ntawv  paus yog		
peb yuav mus twg		


    """

    text_test = """
yog dab tsi? 
koj nyob li cas lawm 
es koj ne 
Kuv nyiam heev, thank you. 
Nyob zoo, yog dab tsi koj? 
Nyob zoo, kuv zoo, thank you ces. 
Kuv nyiam heev, thank you. 
Koj mus rau lub tsev qiv ntawv? 
Nyob zoo ua tsaug. 
Nws tawm tuaj nyob qhov twg puas tau? 
Qhov no yog 
Qhov no yog, thiab that's 
Ntawd yog leej twg? 
Muaj peb puas ntsib? 
Nyob zoo, leej twg yog tus pojniam no?  
Koj yuav kom kuv yuav tsum paub kuv? 
Nws tawm tuaj nyob qhov twg puas tau? 
Koj lub hnub yug yog li cas? 
Koj tshwm sim thaum twg? 
Kuv yug 
koj lub hnub yug yog thaum twg? 
Nws yug thaum twg? 
koj lub npe hu li cas 
koj npe yog li cas 
Yog koj lub npe menyuam yaus 
koj yog leej twg 
Koj lub xeem yog 
Koj yuav tsiaj ua nws li cas? 
koj muaj pes tsawg xyoo? 
Koj lub hnub yug yog li cas? 
Cas hnub no muaj koj tshwm sim? 
Koj tshwm sim thaum twg? 
Koj yog yug nyob qhov twg? 
Koj muaj siab npaum li cas? 
Koj puas hnov li cas? 
koj nyob qhov twg tuaj 
Koj muaj haiv neeg dab tsi? 
koj puas tau yuav txiv 
Koj puas muaj cov me nyuam? 
Koj muaj me nyuam coob npaum li cas? 
Lawv tsis paub qhov twg? 
Ua li cas ua yus tus txiv? 
Koj hometown nyob qhov twg? 
Koj nyob qhov twg? 
Koj lub tsev nyob qhov twg? 
Koj nyob qhov twg? 
Koj muaj pes tsawg leej? 
Koj muaj kwv tij coob npaum li cas? 
Koj puas muaj tej kwvtij? 
Cas koj niam thiab txiv ua hauj lwm? 
Peb ua num rau dab tsi? 
Koj nyob tam sim no nrog koj txiv? 
koj puas nyob ib leeg? 
Cas koj niam txiv nyob twj ywm ciaj sia? 
Kuv niam tau zoo nyob heev. 
Koj nyob qhov twg? 
Cas lub zos koj nyob rau hauv? 
Cas atherosclerosis koj nyob rau hauv? 
Nws lub tsev nyob qhov twg? 
koj ua hauj lwm dab tsi 
Koj ua dab tsi profession puas tau? 
koj tab tom ua dab tsi? 
Koj hauj lwm yog dab tsi? 
Koj puas yog? 
Koj ua haujlwm qhovtwg? 
Koj lub nyiaj hli yog dab tsi? 
Koj lub nyiaj hli yog dab tsi? 
Yog koj cov nyiaj hli tau li cas? 
Koj tsis them ib hnub ntau npaum li cas? 
Koj puas nyiam txog cov hauj lwm zoo li cas? 
Thiab yog hais tias koj tau ib txoj hauj lwm nyob deb deb, 
Cov nyiaj so koobtsheej yog dab tsi? 
Zoo, qhov twg koj hometown? 
Nws yog qhov twg? 
Koj txiv yog dab tsi? 
Thov txim. Koj niam yog tam sim no nyob rau tom tsev. 
tau ntev lawm tsis tau sib ntsib Dab tsi ua hauj lwm tam sim no? 
Koj tsis xa li cas? 
Nws xav ua ib yam dab tsi thaum nws loj los. 
Thov txim, koj paub tias qhov twg? 
Koj puas paub koj txoj kev? 
Yog no txoj kev txog? 
Li cas es kuv thiaj muaj? 
Qhov no puas yog qhov uas yuav muaj mus? 
Nws yog qhov twg? 
Qhov uas yuav yog dab tsi 
Kuv yuav coj tau koj nyob qhov twg? 
koj mus qhov twg? 
Puas muaj ib lub tsheb raug nqi ntau npaum li cas? 
Excuse li no, muaj cai? 
Yog hmo ntuj no mus noj mov ua ke? 
Qhov twg noj thaum sawv ntxov? 
Koj puas xav noj mov nrog kuv? 
Peb mus qhov twg? 
Nws yuav tuaj ntsib peb? 
Peb tsis nrhiav kev haus zoo li cas? 
Ua koj cov dej haus tau li? 
Nyob zoo ua tsaug. 
Nyob zoo Koj puas xav noj mov nrog kuv? 
Nws siv sij hawm ntau npaum li cas yuav? 
Koj puas xav nyob? 
Peb mus? 
koj puas tau txog? 
Koj puas tau kawm nyob qhov twg? 
Leej twg yog koj xib fwb? 
Lub npe ntawm koj cov xib fwb yog dab tsi? 
Koj thiaj paub yuav ua li cas? 
Koj nyiam dab tsi qhia? 
Hais koj nyiam tshaj plaws yog dab tsi? 
Koj puas nyiam ua tau nyob rau lub sij hawm pub dawb zoo li cas? 
Tej yam koj xav nyob rau nraum no zoo li cas? 
Koj kawm heev npaum li cas? 
Koj pib li cas lub sij hawm twg? 
Koj rho cov teev dab tsi? 
Koj puas muaj ib tav su tsev kawm ntawv? 
Ua koj mus kawm ntawv txhua hnub? 
Koj puas mus kawm ntawv li cas? 
Koj puas tau tag tus? 
Koj kev kawm ntawv saum toj kawg nkaus yog dab tsi? 
Koj kawm thaum kawg li cas? 
Koj mus kawm ntawv zoo li cas? 
Kuv kawm tiav nyob 
Koj puas tau tag qhov twg? 
Koj kawm cov xyoo zoo li cas? 
Nws puas muaj tej teeb meem no? 
yog dab tsi? 
Nws nyob qhov twg? 
Koj twb mus kawm ntawv? 
Koj puas tau mus kawm ntawv? 
Koj yuav mus kawm ntawv? 
Peb mus qhov twg?


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
        print("p : ", point)
        max_point = max(point)
        f_m.append(max_point)
        print("max point : ", max_point)
        count += 1
        print("\n")
    print("\n---------------------\n")
    for i in f_m:
        print('%.2f ' % (i))
