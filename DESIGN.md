---
name: Begynder Investor Design System (Snowball Slate Edition)
colors:
  dark:
    canvas: '#14171f'                # Dyb neutral mørkegrå baggrund
    surface: '#1d222e'               # Bento-kort & containere
    surface_elevated: '#262d3d'      # Modaler, tooltips og dropdowns
    surface_active: '#2d364a'        # Hover og aktive flader
    border: '#2a3245'                # 1px afdæmpet kort-kant
    border_subtle: 'rgba(255, 255, 255, 0.07)'
    text_primary: '#f1f5f9'          # Slate 100
    text_secondary: '#94a3b8'        # Slate 400
    text_muted: '#64748b'            # Slate 500
    accent_primary: '#6366f1'        # Indigo 500 (Brand)
    accent_cyan: '#06b6d4'           # Cyan 500 (Knapper & Grafer)
    accent_emerald: '#10b981'        # Positiv vækst
    accent_amber: '#f59e0b'          # Advarsel / Supporter Guld
    accent_rose: '#f43f5e'           # Kritisk / Tab
  light:
    canvas: '#f8fafc'
    surface: '#ffffff'
    surface_elevated: '#f1f5f9'
    border: '#e2e8f0'
    text_primary: '#0f172a'
    text_secondary: '#475569'
    accent_primary: '#312e81'
typography:
  metric-xl:
    fontFamily: IBM Plex Sans
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 48px
    letterSpacing: -0.02em
  metric-lg:
    fontFamily: IBM Plex Sans
    fontSize: 30px
    fontWeight: '600'
    lineHeight: 38px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: IBM Plex Sans
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
  headline-md:
    fontFamily: IBM Plex Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
    letterSpacing: 0.02em
  label-xs:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
spacing:
  container-max: 1280px
  gutter: 1.5rem
---

## Brand & Guidelines
- **Koncept & Manifest**: Platformen er et "Åbent Læringslaboratorium" (bygget af en begynder — til den seriøse begynder investor). Et transparent lærings- og simuleringsværktøj skabt for at demokratisere investering. Platformen er baseret på research, personlige erfaringer og AI som byggefundament. Det er IKKE et finanshus eller et rådgivningsorgan.
- **Tone-of-Voice**: Sproget er roligt, autoritativt, analytisk og letforståeligt. Vi taler til voksne, nysgerrige og seriøse mennesker i øjenhøjde – aldrig nedad.
- **Forbudte Termer**: Udtryk som "skåret ud i pap", "i børnehøjde", "skåret ind til benet" samt metaforer, der associerer til børn eller skolebænke, er STRENGT FORBUDTE.
- **Anbefalede Termer**: Brug faglige og respektfulde alternativer som "Kerneanalyse", "Nøgleindsigt", "Fokuspunkt" eller "Strategisk overblik".
- High-End Fintech Minimalism combined with Analytical Clarity.
- Bento Box layout with clean 1px slate-borders (#E2E8F0) and no heavy shadows.
- Primary font for data/metrics is 'IBM Plex Sans' and body copy is 'Inter'.
- Completely independent from legacy Begynder Investor implementations.

## Retningslinjer for UI Balance:
1. Navigation: Slank, transparent top-navigation (h-16, backdrop-blur-md, max-w-[1400px]) i stedet for tung sidebar.
2. Bento-kort: Subtilt mørkegrå (`#1d222e`) med 1px diskret kant (`#2a3245`) og `rounded-2xl`. Ingen overmættede blå flader.
3. Call-To-Actions: Stilrene knapper i cyan/indigo med afrundede hjørner (`rounded-xl`), god luft og skarp typografi.
4. Supporter Integration: Diskret, eksklusivt guldemblem i topbaren (`#f59e0b`) ved profilen.
