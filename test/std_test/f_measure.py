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
nyob zoo		
nyob zoo thaum sawv ntxov		
nyob zoo tav su		
nyob zoo thaum tsaus ntuj		
npau suav zoo		
sib ntsib dua		
cia mam ntsib nawb		
nyob zoo thaum sawv ntxov		
Pab nyeem rau Kuv me ntsis paus tau		
thov paub koj li chaw nyob  paus tau		
thov qhia Koj tus chaw nyob paus tau		
thov Koj tus chaw nyob me ntsis paus tau		
ua tsaug nawb , txog sij hawm mus lawm , es ntsib dua		
es sib ntsib dua , mus lawm		
thov qhia tias  kuv yuav mus qhov ntawv tau li cas		
thov qhia txoj kev mus qhov ntawd rau kuv me ntsis paus tau 		
thov qhia kuv me ntsis tias qhov ntawd nyob qhov twg 		
koj pab qhia kuv me ntsis paus tau tias qhov ntawd nyob qhov twg 		
koj pab qhia txoj kev mus qhov ntawd rau kuv me ntsis  		
pab qhia kuv me ntsis tau paus tias chaw nyob no nyob nyob ncaj twg 	pab qhia kuv me ntsis tau paus tias chaw nyob no nyob nyob qhov twg 	
pab thiab  kuv yuag kev 		
mus xa kuv tim chaw ua hauj lwm 		
pab qhib nkauj paus tau 		
koj pab nres qhov no paus tau 		
los nrog kuv me ntsis paus tau 	los nrog kuv paus tau	
kuv thov hais lus nrog koj me ntsis 		
koj pab yees duab rau kuv me ntsis paus tau 		
kuv thov yees duab me ntsis paus tau 		
kuv xav kom koj xa neeg coj ncig teb chaws nrog kuv 		
kuv xav tau neeg coj ua si uas hais thaib tau 		
thov txim thov hais tshiab 	thov txim thov hais dua tshiab	
koj yuav hais tshiab me ntsis paus tau 	thov koj hais tshiab me ntsis paus tau	
thov hais qeeb me ntsis 		
kuv xav tau hom rooj 		
kuv xav tau rooj ua ntej 		
thov txim  pab so rooj  paus tau 	thov txim pab so rooj me ntsis paus tau	
thov txim   thov phaj faib me ntsis paus tau 		
thov txim  thov daim ntawv me ntsis paus tau 		
kuv xav tau rooj noj zaub mov tag kis 	kuv xav tau rooj noj mov tag kis 	
kuv xav tau rooj ze qhov rai 		
kuv xav tau tsev so 5 lub  hnub qub		
tab nkaum koj pab sau lub npe me ntsis 		
peb xav tau chav uas muaj dej sov 		
pab luv nqe rau kuv me ntsis paus tau 		
thov saib chaw nyob me ntsis paus tau 		
qhia tawm qeeb me ntsis paus tau 		
kuv xav tau ncua hnub qhia nkag chaw nyob 		
yog tsis xav yuav chaw nyob		
kuv xav tau chav rau 2 neeg 		
kuv xav mus tsev kawm ntawv 		
nyob zoo os kuv xav zawv  plaub hau		
thov txim os , kuv xav txiav plaub hau thiab 		
thov xa thoob puab uas nyob ntawm ntawv rau kuv me ntsis os 		
pab hu kws kho mob rau kuv me ntsis 		
thov Pab Kuv me ntsis 		
kuv thov dej ntxiv me ntsis Yuav paus tau 		
Koj thov Pab dab tsi? kuv me ntsis paus tau 		
tab sis Koj thov Pab kuv me ntsis paus tau 		
Koj ua ua yam ntawd tau , tias Koj xav tau 		
tab sis Kuv dab tsi? hauj lwm Tag kis 		
Kuv xav tau plaub hau tshiab 		
Kuv xav tau dab tsi? uas nws tshiab 		
Txiav kos luv tshaj no me ntsis 		
thov Saib yam lwm yam me ntsis 		
kuv xav tau nyias yam uas sib 		
thov Saib nqi me ntsis 		
Kuv xav tau 2 Hnub qub lub tsev so os 		
Kuv xav tau tsev so		
Kuv xav tau so hauv nroog 		
Kuv xav tau hloov nyiaj 		
Koj Pab qhia txoj kev mus qhov ntawd me ntsis 		
tsav kos Qeeb nqes me ntsis paus tau 		
Pab Kuv xaiv me ntsis paus tau 		
tau os , thov tos ib pliag 		
thov chav uas haus luam yeeb tsis os 		
thov txim os Pab qhia txoj kev kuv me ntsis os 		
Kuv xav tau Saib vaub kib		
peb xav tau mus tsev kawm ntawv 		
Kuv yuav tsum mus Tam sim no 		
Kuv xav tau yog Koj li,ntawm,khoom None 		
Kuv xav tau Haus npias 		
nws xav tau kev pab,Pab chawm nrog tam sim ntawv 		
thov kos npe yuav ก yam no me ntsis os 		
kuv thov siv xov tooj me ntsis paus tau 		
thov paub Lub npe Koj me ntsis paus tau 		
Pab khaws ntwav no kos kuv me ntsis os 		
kuv tseem yuav tsum mus lawm 		
Thov xav txog yuav ua li cas tam sim no.		
Nws yog kim me ntsis		
Thov koj qhia kuv txoj kev?		
Kuv xav zaws taw		
Kuv yuav tsum ntxuav koj txhais taw ua ntej.		
Thov hais nrov nrov		
Cia kuv saib daim ntawv hla tebchaws.		
Kuv xav nug tswv yim ua ntej		
Zoo, pheej yig, thov qhwv nws thiab.		
Kuv xav yuav kas fes thiab dej.		
Kuv xav tau khoom qab zib 		
txwv tsis pub tsav tsheb 1 xyoo 		
peb tsis ntxim hais lus hauv tsev kawm		
tsis hla kev thaum lub teeb yog xim liab 		
koj yuav tsum hnav ris tsho mus tsev kawm ntawv		

    """

    text_test = """
Kuv tuaj ntawm no 
Nyob zoo sawv ntxov 
Nyob zoo tav su 
Nyob zoo hmo 
pw zoo os 
sib ntsib dua 
. 
Sawasdee thaum sawv ntxov  
Yuav koj tsiaj kuv tus haum? 
Koj yuav tau txais lub ceeb toom los ntawm koj qhov chaw nyob? 
Thov qhia txog koj qhov chaw nyob? 
Koj yuav hais kom koj qhov chaw nyob? 
Tsaug rau lub sijhawm ntawd, kuv tau ntsib. 
Thiab raws li goodbye. 
Thov koj qhia kuv yog vim li cas kuv thiaj muaj? 
Thov qhia rau kuv qhov uas muaj rau kuv. 
Thov koj qhia kuv muaj. 
Koj thiaj paub kuv lawv nyob qhov twg? 
Koj thiaj paub kuv txoj kev uas muaj rau kuv? 
Qhia kuv, thov koj, uas yog qhov chaw nyob? 
Pab nrog Kuv txoj kev poob kuv 
Mus xa kuv tuaj ua haujlwm 
Koj tau ua suab paj nruag? 
Thov koj pab kuv nres ntawm no? 
Koj yuav tuaj nrog kuv? 
Kuv nrog koj tham me ntsis. 
Koj yuav muab ib Diam duab rau kuv? 
Kuv yuav mus yees duab ntawv tso cai? 
Kuv xav kom nej xa kuv ncig saib rau kuv. 
Kuv xav tau ib ncig xyuas hais lus thaib 
Thov txim, thov koj hais dua. 
Yuav thov hais tej yam tshiab? 
Thov hais ib yam nkaus thiab maj mam. 
Kuv xav tam ib rooj 
Kuv xav tam saum ib lub rooj ua ntej 
thov txim os Kuv yuav rho tawm qhov rooj cheese? 
Koj yuav excuse kuv lov ib phaj? 
Kuv yuav thov txim rau daim ntawv? 
Kuv xav kom muaj tagkis book ib lub rooj noj mov. 
Kuv xav tau ib lub rooj nyob ze ntawm lub qhov rais. 
Kuv xav tau ib lub tsev so 5-hnub qub 
Koj yuav tau pab tsiaj koj lub npe. 
Peb xav tau ib chav dej kub. 
Koj puas kam luv nqi? 
Koj yuav tau txais ib chav tsev? 
Koj thiaj paub kuv me ntsis lig? 
Kuv xav mus ncua hnub kuv booking 
Kom ib chav tsev 
Kuv xav book ib yig neeg 2. 
Kuv xav mus kawm ntawv. 
Nyob zoo Kuv xav ntxuav kuv cov plaub hau. 
Kuv thov txim. Kuv yuav txiav kuv cov plaub hau thiab. 
Thov xa kuv ib lub hnab nyob qhov qub chaw. 
Pab kuv ua tau ib tus kws kho mob me. 
Thov koj pab kuv. 
Kuv yuav tau dej ntau me ntsis? 
Koj thov pab tau kuv? 
Tab sis koj thov pab tau kuv? 
Koj yuav ua li ntawd. Yog hais tias koj xav 
Tab sis kuv yuav tsum mus tag kis. 
Kuv xav kom muaj hairstyle tshiab. 
Kuv xav tau tej yam tshiab. 
Qhov ntuag yog luv. 
Peb saib me ntsis ntxiv. 
Kuv xav tej yam sib zog. 
Tau ib tug nqi 
Kuv xav tau ib lub tsev so 2 hnub qub 
Kuv xav book ib chav tsev 
Kuv xav nyob hauv lub nroog 
Kuv yuav tau nyiaj ntxiv rov los. 
Ua koj qhia qhov uas muaj? 
Tau kuv kom nws? 
Pab kuv xaiv me ntsis? 
. thov tos ib pliag 
Kuv tsis tau nug rau ib chav tsev haus luam yeeb. 
Kuv thov txim tias, thov koj qhia kuv yog vim kuv txoj kev. 
Kuv xav pom vaub kib 
Peb yuav tau mus kawm ntawv. 
kuv yuav tau mus tam sim no 
Kuv xav ua koj tus phooj ywg 
Kuv xav haus npias. 
Nws yuav tsum tau kev pab tam sid. 
Thov kos npe no slurry tau. 
Kuv siv kuv cov xov tooj? 
Koj yuav paub koj lub npe? 
Pab kuv khaws daim ntawv no. 
Kuv yuav tau mus. 
Kuv xav txog tam sim no ua li cas pab. 
Nws yog ib yam nkaus thiab kim heev. 
Thov qhia rau kuv li. 
Kuv xav tau ib tug ko taw zaws 
Kuv tau los so koj ob txhais ua ntej. 
Thov hais me ntsis.  
Cia kuv saib rau phau passport. 
Kuv xav nug txog ib qhov suggestion thawj zaug. 
Qhov zoo, yog cov nqi pheej yig Thov koj ua ib nras. 
Kuv xav yuav ua kasfes haus thiab dej 
Kuv xav kom cov khoom qab zib. 
Tsis txhob tsav 1 xyoo 
Peb tsis hais nyob rau hauv chav kawm ntawv. 
Tsis tau hla kev thaum lub teeb liab. 
Nws yuav tsum hnav khaub ncaws rau tsev kawm ntawv. 


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
