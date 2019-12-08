from jiwer import wer

"""
    wer = (การแทนที่ + การแทรก + การลบ)/ จำนวนประโยคอ้างอิง
"""

class Wer :
    def readysen(self, sentence):
        # ตัดเครื่องหมายออก
        split = [',', '?', "!", '.']
        for i in split:
            sentence = sentence.split(i)
            sentence = " ".join(sentence)

        # เปลี่ยนเป็นอักษรตัวเล็กให้หมด
        sentence = sentence.lower()

        return sentence

if __name__ == '__main__':

    text_true =  """
tsis zoo li	tsis zoo	Tsis zoo hlo li	Tsis zoo kiag li. 	
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
tsis nawb ntawm no huab cua no	tsis tim no huab cua no			
ntuj tsis muaj huab	lub ntuj tsis muj huab			
kuv tsis nyiam ntuj no				
tseem tsis tau zaub mov na	tseem tsis tau zaub mov nawb		tsis tau zaub mov li	
cov zaub mov uas kuv xaiv tseg tseem tsis tau nawb	cov khoom noj kuv tau hais tseg tseem tsis tau 			
no tsis yog yam kuv tau hais tseg na	qhov no tsis yog  yam uas kuv xaiv 		no tsis yog qhov xaiv tseg nawb	
thov txim vim peb tsis tau muaj chaw khoom tam sim no li	thov txim peb tsis muaj chaw khoom tam sim no			
kuv tsis paub tseeb				
tsis hais txog noj tshais	tsis hais koom txog mov sawv ntxov		tsis koom zaub mov sawv ntxov	
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
kuv tsis ntseeg txiv thiab niam	kuv tsis moog niam txiv lus		kuv tsis moog niam txiv 	
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
tsis Zoo li
tsis yog , Kuv tias peb tseem tsis tau ntsib ua ke nawb
Kuv tsis Xav tias peb tau ntsib ua ke los ua ntej nawb
tsis , Kuv tseem tsis tau sib yuav
Kuv tsis muaj kwv tij li
tsis , niam nyob tim kuv tsev
tu siab , Kuv tsis sib paub
ntshai tias Kuv ua tsum Pab Koj tsis tau
tsis yuav  tsum rho
tsis txawj dab tsi
Kuv thov txim , Kuv tseem mus tsis tau
tsis txawj dab tsi , Kuv tsis khoob
ntawv tsis txawj teeb meem
tsis nawb , qhov ntawm no huab cua no
lub ntuj tsis muaj huab
kuv tsis nyiam caij ntuj no li
tseem tsis tau zaub mov li
zaub mov uas Kuv hais mus tseem tsis tau li
ntawm no tsis yog uas hais mus ntawm no
yuav  tsum thov txim , tab sis peb tseem tsis muaj chaws seem Tam sim no li
kuv tsis paub meej
tsis koom tshais
nws tsis yog Koj li
nws tsis nkag siab nws
Kuv noj zaub mov tsis qab li
Koj yuav  tsum tsis ua txhob yog li ntawv
tsis txawj dab tsi li
kuv tsis muaj dab tsi uas Yuav pom zoo
thov txim os , Kuv tsis pom zoo rau Koj
ua tsis txawj os
kuv tsav tsheb tsis txawj
tseem tsis tau noj , Kuv tab tom Xav nyob zoo li yam
ntshai tias Yuav tsis tau
kuv tsis muaj kwv tij li
tseem tsis tau Txiav txim siab
Kuv tsis muaj me nyuam
tsis txawj dab tsi os
tsis txawj dab tsi os , nrhiav tau li
Kuv tu siab os , Kuv ntshai tias Yuav tsis yuav ua yam ntawv pub Koj tau
thov txim os , tab sis ntawv txawj mus tsis tau
kuv ntshai tias kuv tsis hnov yam ntawv
tab sis kuv tsis tau rau siab uas Yuav ua เช่นนั้น
tsis txawj dab tsi os
tsis txawj dab tsi os , kuv nyuam qhuav nkag los
Kuv tsis tshuag nyiam xim no li cas
tsis yuav hu li cas lawm , ua tsaug
tsis yuav  tsum rov
thov txim , peb tsis muag nqaij nyuj
tsis deb ntawm ntawm no
tsis muaj , kuv txawj leeg me nyuam ib
Kuv Xav tsis tawm li
dej tsis muaj xim li
luav tsis noj nqaij tsiaj
Nab tsis muaj ko taw
tsis muaj os
tsis os , kuv tsis tau teem cia
Kuv ntshai tias Yuav tsis cuag os
tsis lawm os , ua tsaug
nws Tam sim no tsis nyob
ua tsaug , tsis yog Tam sim no
tsis yog os , Kuv tsav tsheb mus xwb
Kuv tsis paub meej
ua tsaug , tsis txawj dab tsi
tsis ntev li ,10, feeb
tsis txawj dab tsi os
kuv tsis sib paub nws tab sis kuv Xav tias kuv tus muam paub
tsis txawj dab tsi os , thov kom muaj kev zoo siab rau kev sawv kev
Kuv tseem Txiav txim siab tsis tau
tsis muaj li nawb , pib mob thaum twg
tab sis kuv tsis nyiam xim no
kuv tsis nyiam caij ntuj no
tsis tau nawb
tab sis kuv ntshai tias , kuv Yuav mus tsis tau
kuv tsis tau ntsib Koj los ,2-3, hli lawm
Kuv Yuav tsis sim piav qhia li
Kuv tsis nyiam Nab
Kuv tsis tshuag muaj sij hawm vaaj
Kuv tsis muaj sij hawm nyeem ntawv li
Kuv tsis tau noj nws los ua ntej li
koj tsis seej heev , nws tsis ua los tau
koj tsis nyob tsev kawm ntawv nag hmo
tsis yuav  tsum ntshai miv
naim thiab txiv tsis tau pov tseg me nyuam , cia neeg ib tim tsev
lus nug nyuaj heev , Kuv tsis ua xaus tau
tus ris no tsis phim nrog Kuv
koj tsis tau pw tsaug zog tam sim no , koj sawv
no txawj txiv txhais uas tsis Zoo
peb tsis ua npo Ua tsis taus pa cia tau ntev
dej tsis ntshiab
peb tsis ua ntsia pom dab tsi tau
xib hwb hais zaj tseem tsis Xaus
Kuv Yuav tsis Tsis nco qab Hnub ntawv
kuv tsis paub lo lus txhais lo li no
tsis muaj leej twg paub koj tus Txoj hmoo
koj tsis tau muaj nplhaib
tsiaj nyob tsis tau yog tsis muaj zaub mov
koj tsis muaj dab tsi Yuav ua
koj xav tias tsis Zoo thaum npawg tsis nyob
nws tsis nyob zoo
Hnub no nws tsis ua mus tsev kawm ntawv tau
kws kho mob tsis ua nrhiav kev tus teeb meem mob koj li tau
tiab no tsis phim rau Kuv
koj tsis ua mus tsev kawm ntawv tau vim koj mob
nws txawj mus tsis tau uas ntses Yuav yag
tsis muaj leej twg nyob hauv ntawv
zaj no tsis txawj qhov txhim saib
no tsis yog tsav daj poj niam
peb tsis nyiam mloog nkauj
nyiaj tsis yog yam uas tseem ceeb
koj tsis tau mus qhov twg li
nws tsis nyiam kev tsav tsheb hauv sij hawm hmo ntuj
Kuv tsis mloog lus naim thiab txiv
Kuv tsis muaj kev pom zoo
tsis tau qhia tias muaj Zoo
tsis muaj lus nug ntawm tub kawm
Kuv tsis tau txawj tub kawm
nws tseem tsis txhij rau kev xeem
no tiag tus tsis yog
Kuv tseem tsis tau txhais tsab ntawv ntawm koj
Koj tus lus teb tsis Ncaj Raws lus teb
koj tsis ua cim leb koj tus xov tooj
tsis muaj leej twg ua hais yam no tau
Kuv tsis ua ntsia pom koj tau
nws tsis tau xav tias txaj muag hauv yam uas nws ua
Kuv tsis tau rau siab uas Yuav tab nkaum Koj
Kuv tsis ua Ua luam dej hla tus dej
npawg txawv tab chaws feem ntau tsis nkag siab lus thaib
tsis txo cai kom nres tsheb loj hauv tsev kawm ntawv
nws tsis tau mus xyuas koj txiv thiab koj niam txawj sij hawm 3 xyoo
Kuv tsis ua Them nyiaj
nws tsis tau ntxuav Phaj
kuv ntseeg tias tsis muaj dab
nws pw so tsis txaus hauv hmo qhov uas dhaug los


    """

    text_true = text_true.strip()
    text_true = text_true.splitlines()

    text_test = text_test.strip()
    text_test = text_test.splitlines()
    print("\n----------------------------------\n")

    w = Wer()
    all_sentence_true = []
    for sen in text_true:
        sen = sen.split("\t")
        total = []
        for sentence in sen:
            sentence = sentence.strip()
            if sentence != "":
                # print(sentence)
                total.append(w.readysen(sentence))
        all_sentence_true.append(total)
    # print(all_sentence_true)

    all_sentence_test = []
    for sentence_t in text_test:
        sentence_t = sentence_t.strip()
        if (sentence_t != ''):
            all_sentence_test.append(w.readysen(sentence_t))
    # print(all_sentence_test)



    print("\n-----calculate point-------------\n")
    count =0
    count_point =[]
    for sentence_true in all_sentence_true:
        sub_point = []
        for sen in sentence_true:
            # print(sentence_true)
            # print(sen," --> ",all_sentence_test[count])
            p = wer(sen,all_sentence_test[count],standardize=True)
            if(1-p<0):
                print(sen,"-->",all_sentence_test[count]," -- ",p)
            sub_point.append(p)
        count_point.append(min(sub_point))
        # print(sub_point)
        # count_point.append(sub_point[0])
        count+=1


    print("\n--------all point WERcc--------\n")
    for point in count_point:
        print(1-point)
