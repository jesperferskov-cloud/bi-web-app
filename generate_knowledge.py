import re

with open('ai-assistant.js', 'r', encoding='utf-8') as f:
    content = f.read()

new_local_knowledge = """    const localKnowledge = [
        {
            keywords: ['pe', 'p e', 'price to earnings', 'kurs indtjening', 'vaerdiansaettelse', 'p e tallet'],
            answer: "P/E står for Price/Earnings (Pris/Indtjening). Det viser, hvor meget du betaler for 1 krone af virksomhedens overskud. Et lavt tal kan indikere en billig eller moden aktie, mens et højt tal indikerer markedets forventning om kraftig fremtidig vækst."
        },
        {
            keywords: ['80 20', 'core satellite', 'kerne satellit', 'allokering', '80 20 balancen'],
            answer: "I Begynder Investor-metodikken anbefaler vi 80/20-fordelingen: Mindst 80% placeres i brede, passive globale indeksfonde (Core) for stabilitet og renters rente, mens maks. 20% investeres i analyserede enkeltaktier (Satellit) til læring."
        },
        {
            keywords: ['saldo', 'kontant', 'penge', 'balance', 'hvor mange penge'],
            getDynamicAnswer: () => {
                const cash = localStorage.getItem('bi_cash_balance') || '50000';
                return `Du har i øjeblikket ${Number(cash).toLocaleString('da-DK')} kr. i din simulerede kontantbeholdning.`;
            }
        },
        {
            keywords: ['profil', 'hvem er jeg', 'min profil'],
            getDynamicAnswer: () => {
                const profile = localStorage.getItem('bi_user_profile');
                if (profile) {
                    try {
                        const data = JSON.parse(profile);
                        return `Din nuværende profil er sat op som: **${data.risk || 'Ukendt'}** risikoprofil, med en tidshorisont på **${data.horizon || 'Ukendt'}**.`;
                    } catch(e) {}
                }
                return 'Jeg kan se, at du ikke har udfyldt din investeringsprofil endnu. Det kan du gøre under "Profil" i menuen.';
            }
        },
        {
            keywords: ['moat', 'voldgrav', 'konkurrencefordel', 'primære voldgrav'],
            answer: "En økonomisk voldgrav (Moat) er en virksomheds varige konkurrencefordel (f.eks. patenter, stærke brands som Novo Nordisk eller høje skifteomkostninger), som forhindrer konkurrenter i at æde dens overskud."
        },
        {
            keywords: ['etf', 'passiv fond', 'indeksfond', 'åop'],
            answer: "En ETF (Exchange Traded Fund) er en børsnoteret fond, der følger et indeks passivt. Fordelen er lave årlige omkostninger (ÅOP) og øjeblikkelig global risikospredning."
        },
        {
            keywords: ['volatilitet', 'svingninger', 'udsving', 'risiko', 'største risiko'],
            answer: "Risiko og volatilitet måler, hvor kraftigt og hurtigt kursen svinger. Den største risiko ved aktier er permanent tab af kapital, hvilket vi minimerer gennem 80/20-spredning, analyse af Moat og anti-FOMO regler."
        },
        {
            keywords: ['karantæne', 'fomo', '48 timer', '48t karantæne', '48t', 'anti-fomo', 'anti fomo'],
            answer: "Anti-FOMO karantænen på 48 timer er en obligatorisk tænkepause for satellit-køb. Den tvinger dig til at sove på beslutningen og modvirker impulskøb drevet af markedsstøj."
        },
        {
            keywords: ['renters rente', 'rente'],
            answer: "Renters rente er effekten af at geninvestere dit afkast. Over tid begynder dit afkast at skabe sit eget afkast, hvilket giver en sneboldeffekt der vokser eksponentielt."
        },
        {
            keywords: ['aktiesparekonto', 'aktiespare konto', 'ask', 'aktiesparekonti'],
            answer: "En Aktiesparekonto (ASK) er en lukrativ investeringskonto med kun 17% lagerskat mod normalt 27/42%. I 2026 er indskudsloftet 174.200 kr. (beregnet ud fra samlet saldo pr. 31/12 året før). Den er særligt velegnet til brede aktieindeks og ETF'er."
        },
        {
            keywords: ['aldersopsparing', 'ao', 'pension', 'pal', 'pensionsopsparing'],
            answer: "En Aldersopsparing har Danmarks laveste skattesats på kun 15,3% (PAL-skat). Udbetalingen modregnes ikke i folkepensionens tillæg. I 2026 er grænsen 9.900 kr./år, hvis du har over 7 år til pensionsalderen, og 64.200 kr./år, hvis du har 7 år eller mindre."
        },
        {
            keywords: ['frit depot', 'almindeligt depot', 'aktiedepot', 'aktieindkomst'],
            answer: "Et almindeligt frit depot beskattes efter realisationsprincippet (skat ved salg eller udbytte). I 2026 er progressionsgrænsen 79.400 kr. for enlige (158.800 kr. for gifte), hvor du betaler 27% i skat under grænsen og 42% af gevinst herover."
        },
        {
            keywords: ['månedsopsparing', 'maanedlig opsparing', 'automatisk opsparing'],
            answer: "En månedsopsparing lader dig købe brede fonde eller ETF'er automatisk hver måned uden kurtage (handelsgebyr) – ideelt til passiv Core-investering."
        },
        {
            keywords: ['aktie', 'aktier'],
            answer: "En aktie er en ejerandel i en virksomhed, som giver andel i dens fremtidige værdiskabelse."
        },
        {
            keywords: ['aktiekurs', 'kurs'],
            answer: "Aktiekurs er den aktuelle pris en aktie handles til på børsen, styret af udbud og efterspørgsel."
        },
        {
            keywords: ['børs', 'børsen'],
            answer: "En børs er den regulerede markedsplads for værdipapirer (f.eks. Nasdaq Copenhagen eller NYSE)."
        },
        {
            keywords: ['afkast'],
            answer: "Afkast er det samlede økonomiske resultat over en periode (kursændringer + eventuelt udbytte)."
        },
        {
            keywords: ['portefølje', 'beholdning'],
            getDynamicAnswer: () => {
                const baseText = "En portefølje er den samlede beholdning af aktier, fonde og andre aktiver, som en investor ejer. ";
                const holdings = localStorage.getItem('bi_portfolio_holdings');
                if (holdings && holdings !== '[]') {
                    return baseText + 'Du har allerede aktiver i din portefølje. Gå til "Portefølje" for at se et detaljeret overblik over fordelingen.';
                } else {
                    return baseText + 'Din portefølje er tom lige nu. Prøv at gå til "Markeder" for at finde din første aktie eller fond.';
                }
            }
        },
        {
            keywords: ['kurtage', 'gebyr', 'handelsgebyr'],
            answer: "Kurtage er handelsgebyret eller kommissionen, som din mægler/bank tager for at udføre en ordre."
        },
        {
            keywords: ['realiseret', 'urealiseret', 'realisere'],
            answer: "Urealiseret gevinst/tab eksisterer kun på papiret. Det realiseres først skattemæssigt den dag, du sælger."
        },
        {
            keywords: ['udbud', 'efterspørgsel'],
            answer: "Udbud og efterspørgsel er prismekanismen på børsen; overstiger købernes efterspørgsel udbuddet, stiger kursen."
        },
        {
            keywords: ['ordrebog', 'bid', 'ask', 'spread'],
            answer: "I ordrebogen er Bid den højeste købspris og Ask er den laveste salgspris. Differencen kaldes spread."
        },
        {
            keywords: ['diversifikation', 'risikospredning', 'sprede'],
            answer: "Diversifikation er risikospredning – princippet om ikke at lægge alle æg i én kurv ved at sprede på sektorer og markeder."
        },
        {
            keywords: ['investeringsfond', 'ucits', 'fond'],
            answer: "En investeringsfond (fx UCITS) er en fælles pulje forvaltet af professionelle, hvor investorer samler midler for bred spredning."
        },
        {
            keywords: ['aktieindeks', 'indeks'],
            answer: "Et aktieindeks er en udvalgt kurv af aktier, der måler et samlet marked (f.eks. C25 eller S&P 500)."
        },
        {
            keywords: ['markedsværdi', 'market cap'],
            answer: "Markedsværdi (Market Cap) er den samlede børsværdi af et selskab (aktiekurs × udestående aktier)."
        },
        {
            keywords: ['regnskab', 'årsregnskab', 'kvartalsregnskab'],
            answer: "Et regnskab er officielle finansielle rapporter (kvartal/år) med omsætning, overskud, pengestrømme og guidance."
        },
        {
            keywords: ['bull', 'bear', 'bull-marked', 'bear-marked'],
            answer: "Bull og Bear: Bull-marked betyder længerevarende optur og optimisme; Bear-marked dækker over fald (typisk 20%+) og pessimisme."
        }
    ];"""

# Replace between `const localKnowledge = [` and `    ];`
# Regular expression to match the localKnowledge declaration.
pattern = re.compile(r'    const localKnowledge = \[.*?    \];', re.DOTALL)
content = pattern.sub(new_local_knowledge, content)

with open('ai-assistant.js', 'w', encoding='utf-8') as f:
    f.write(content)

