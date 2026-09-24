# Begynder Investor - System Instructions

## 1. Core Philosophy, Tone & Design
- **Manifest**: Platformen drives som et "Åbent Læringslaboratorium" (bygget af en begynder — til den seriøse begynder investor). Det er et transparent lærings- og simuleringsværktøj, der bidrager til at demokratisere investering baseret på research, erfaringer og AI.
- **Ansvarsfraskrivelse**: Det skal altid fremgå tydeligt, at platformen IKKE er et finanshus eller et rådgivningsorgan.
- **Tone-of-Voice**: Sprogstilen skal være rolig, autoritativ, analytisk og letforståelig. Vi taler til voksne, nysgerrige og seriøse mennesker i øjenhøjde – aldrig nedad.
- **Forbudte Termer**: Undgå konsekvent udtryk som "skåret ud i pap", "i børnehøjde", "skåret ind til benet" og børne- eller skolemetaforer. Brug i stedet "Kerneanalyse", "Nøgleindsigt", "Fokuspunkt" eller "Strategisk overblik".
- Finansiel strategi: Baseret på 80/20 Core-Satellite filosofien.
- Følg altid tokens i DESIGN.md (Deep Indigo #312E81, Slate Surface #F8FAFC, Slate Border #E2E8F0, Emerald #059669, Rose #E11D48).
- Fonte: IBM Plex Sans (overskrifter/tal), Inter (brødtekst). Ingen tunge skygger.

## 2. Tech Stack & Kodekrav
- Ren semantisk HTML5, Tailwind CSS via CDN og letvægts Vanilla JS.
- Ingen eksterne frameworks (React, Vue) eller tunge JS-biblioteker medmindre eksplicit angivet.
- Al data gemmes client-side i browserens localStorage.

## 3. Faste Datamodeller & localStorage Nøgler
- Profil: `bi_user_name` (string), `bi_user_profile` (JSON: navn, alder, risiko, maal, horisont).
- Portefølje/Saldo: `bi_cash_balance` (f.eks. '10000').
- Modulprogression: `bi_module_core_completed`, `bi_module_fomo_completed`, `bi_module_rebalance_completed`, osv. (boolean som 'true'/'false').

## 4. Agent Adfærd
- Gæt aldrig på variabelnavne eller styling – brug altid ovenstående nøgler og DESIGN.md.
- Bevar altid eksisterende sidebar-navigation og disclaimere intakte.
