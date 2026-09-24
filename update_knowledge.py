import re

with open('ai-assistant.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Append the new entries to localKnowledge.
# Find the end of the localKnowledge array
knowledge_end_idx = content.find("];\n\n    function processQuery(query)")

new_entries = """        },
        {
            keywords: ['aktiesparekonto', 'aktiespare konto', 'ask', 'aktiesparekonti'],
            answer: "En Aktiesparekonto (ASK) er en særlig investeringskonto med en fordelagtig skattesats på kun 17% (mod normalt 27-42% aktieskat). Den beskattes efter lagerprincippet én gang årligt, og der gælder et lovbestemt indskudsloft. Den er ideel til begyndere, der vil handle aktier eller udvalgte ETF'er med lav skat."
        },
        {
            keywords: ['aldersopsparing', 'ao', 'pensionsopsparing'],
            answer: "En aldersopsparing er en pensionsordning med lav beskatning (15,3% PAL-skat) af afkastet. Du får intet fradrag for indskud, men udbetalingerne modregnes ikke i folkepensionens tillægsprocent, hvilket gør den særlig attraktiv tæt på pensionsalderen."
        },
        {
            keywords: ['månedsopsparing', 'maanedlig opsparing', 'automatisk opsparing'],
            answer: "En månedsopsparing lader dig automatisk købe brede fonde eller ETF'er hver måned uden kurtage (handelsgebyr), hvilket er ideelt til passiv 80/20 Core-opsparing."
        }"""

# Replace the last `}` with the new entries.
# Wait, the last item ends with `    }` followed by `    ];`
content = content.replace("        }\n    ];\n", new_entries + "\n    ];\n")


# Now replace processQuery
old_process_query = """    function processQuery(query) {
        const q = normalizeText(query);
        
        for (const item of localKnowledge) {
            if (item.keywords.some(keyword => q.includes(keyword))) {
                if (item.getDynamicAnswer) {
                    return item.getDynamicAnswer();
                }
                return item.answer;
            }
        }

        return 'Dette kræver dybere markedsanalyse eller ligger uden for min lokale viden. Opgrader til Supporter for live web-research, eller stil et spørgsmål om investeringsbegreber.';
    }"""

new_process_query = """    function processQuery(query) {
        const q = normalizeText(query);
        const userWords = q.split(' ').filter(w => w.length > 2); // Ignore very short words for token matching
        
        let bestMatch = null;
        let highestScore = 0;

        for (const item of localKnowledge) {
            let score = 0;
            for (const keyword of item.keywords) {
                // Exact phrase match (like previously)
                if (q.includes(keyword)) {
                    score += 10;
                }
                
                // Flexible token matching
                const keywordWords = keyword.split(' ');
                let matchCount = 0;
                for (const kw of keywordWords) {
                    if (kw.length > 2 && userWords.some(uw => uw.includes(kw) || kw.includes(uw))) {
                        matchCount++;
                    }
                }
                if (matchCount > 0 && matchCount === keywordWords.length) {
                    score += 5; // Good match if all parts of the keyword matched somewhere
                } else if (matchCount > 0) {
                    score += matchCount; // Partial match
                }
            }
            
            if (score > highestScore) {
                highestScore = score;
                bestMatch = item;
            }
        }

        if (bestMatch && highestScore > 0) {
            if (bestMatch.getDynamicAnswer) {
                return bestMatch.getDynamicAnswer();
            }
            return bestMatch.answer;
        }

        return 'Dette kræver dybere markedsanalyse eller ligger uden for min lokale viden. Opgrader til Supporter for live web-research, eller stil et spørgsmål om investeringsbegreber.';
    }"""

content = content.replace(old_process_query, new_process_query)

with open('ai-assistant.js', 'w', encoding='utf-8') as f:
    f.write(content)

