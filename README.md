# lk_religion

Analyses of Sri Lanka's religious demographics, comparing the **2012 Census** and **2024 Census**.

Each analysis now lives in its own folder under [`analyses/`](analyses/), together with its own README, workflow script, and related data files. The sections below are copied from those child READMEs.

- [`analyses/a1_national_totals/`](analyses/a1_national_totals/)
- [`analyses/a2_by_district/`](analyses/a2_by_district/)
- [`analyses/a3_proportion_change/`](analyses/a3_proportion_change/)
- [`analyses/a4_by_dsd/`](analyses/a4_by_dsd/)
- [`analyses/a5_proportion_change_by_dsd/`](analyses/a5_proportion_change_by_dsd/)

---

## A1. National Population by Religion

![A1 representative chart](analyses/a1_national_totals/chart.png)

| Religion | 2012 | 2024 | Change | Annual Growth | % of Population |
|---|---:|---:|---:|---:|---:|
| Buddhist | 14,271,183 | 15,199,093 | +927,910 | +0.53% | 69.8% |
| Hindu | 2,561,142 | 2,734,839 | +173,697 | +0.55% | 12.6% |
| Islam | 1,967,008 | 2,337,379 | +370,371 | +1.45% | 10.7% |
| RomanCatholic | 1,261,136 | 1,224,348 | -36,788 | -0.25% | 5.6% |
| OtherChristian | 290,920 | 282,185 | -8,735 | -0.25% | 1.3% |
| Other | 6,387 | 3,956 | -2,431 | -3.91% | 0.0% |
| **Total** | **20,357,776** | **21,781,800** | **+1,424,024** | **+0.57%** |

### Commentary

- Sri Lanka's total population grew from **20,357,776** (2012) to **21,781,800** (2024), an increase of **+1,424,024** at an annual rate of **+0.57%**.
- **Buddhism** remains the dominant religion, accounting for **69.8%** of the population in 2024, growing at **+0.53%** per year.
- **Islam** has the fastest growth rate among major religions at **+1.45%** per year, reaching a share of **10.7%** in 2024.
- **Roman Catholic** and **Other Christian** communities show slight declines over the period.

---

## A2. Religion by District: Key Trends

![A2 representative chart](analyses/a2_by_district/chart.png)

### Buddhist

| District | 2012 | 2024 | Change | Annual Growth | % of Natl |
|---|---:|---:|---:|---:|---:|
| Monaragala | 426,762 | 498,436 | +71,674 | +1.30% | 3.3% |
| Hambantota | 580,344 | 649,736 | +69,392 | +0.95% | 4.3% |
| Anuradhapura | 775,366 | 862,807 | +87,441 | +0.89% | 5.7% |
| Ampara | 251,427 | 276,176 | +24,749 | +0.79% | 1.8% |
| Polonnaruwa | 364,229 | 399,488 | +35,259 | +0.77% | 2.6% |
| Puttalam | 329,705 | 361,148 | +31,443 | +0.76% | 2.4% |
| Kurunegala | 1,430,958 | 1,557,554 | +126,596 | +0.71% | 10.2% |
| Matale | 385,151 | 418,608 | +33,457 | +0.70% | 2.8% |
| Badulla | 591,799 | 636,988 | +45,189 | +0.62% | 4.2% |
| Gampaha | 1,642,767 | 1,744,475 | +101,708 | +0.50% | 11.5% |
| Kalutara | 1,018,909 | 1,080,638 | +61,729 | +0.49% | 7.1% |
| Ratnapura | 943,464 | 999,682 | +56,218 | +0.48% | 6.6% |
| Kandy | 1,009,220 | 1,063,511 | +54,291 | +0.44% | 7.0% |
| Colombo | 1,632,125 | 1,682,524 | +50,399 | +0.25% | 11.1% |
| Galle | 998,647 | 1,026,031 | +27,384 | +0.23% | 6.8% |
| Matara | 766,323 | 787,303 | +20,980 | +0.23% | 5.2% |
| Kegalle | 709,917 | 728,929 | +19,012 | +0.22% | 4.8% |
| Nuwara Eliya | 278,254 | 278,828 | +574 | +0.02% | 1.8% |
| *Other (<1% or <1,000)* | *135,816* | *146,231* | *+10,415* | *+0.62%* | |

***Monaragala** grew fastest at **+1.30%/yr**. **Nuwara Eliya** had the slowest growth at **+0.02%/yr**. **Kurunegala** had the largest absolute increase (**+126,596**).*

### Hindu

| District | 2012 | 2024 | Change | Annual Growth | % of Natl |
|---|---:|---:|---:|---:|---:|
| Gampaha | 52,973 | 69,429 | +16,456 | +2.28% | 2.5% |
| Mullaitivu | 69,377 | 88,738 | +19,361 | +2.07% | 3.2% |
| Kilinochchi | 92,986 | 110,258 | +17,272 | +1.43% | 4.0% |
| Ampara | 102,829 | 114,586 | +11,757 | +0.91% | 4.2% |
| Batticaloa | 338,882 | 374,836 | +35,954 | +0.84% | 13.7% |
| Trincomalee | 98,442 | 108,050 | +9,608 | +0.78% | 4.0% |
| Kandy | 133,744 | 144,618 | +10,874 | +0.65% | 5.3% |
| Kalutara | 39,541 | 42,528 | +2,987 | +0.61% | 1.6% |
| Matale | 43,432 | 46,181 | +2,749 | +0.51% | 1.7% |
| Colombo | 186,303 | 197,759 | +11,456 | +0.50% | 7.2% |
| Badulla | 157,608 | 166,380 | +8,772 | +0.45% | 6.1% |
| Nuwara Eliya | 363,163 | 377,266 | +14,103 | +0.32% | 13.8% |
| Kegalle | 54,350 | 56,199 | +1,849 | +0.28% | 2.1% |
| Ratnapura | 101,962 | 103,883 | +1,921 | +0.16% | 3.8% |
| Jaffna | 483,255 | 489,521 | +6,266 | +0.11% | 17.9% |
| Puttalam | 28,811 | 28,832 | +21 | +0.01% | 1.1% |
| Vavuniya | 119,400 | 114,504 | -4,896 | -0.35% | 4.2% |
| *Other (<1% or <1,000)* | *94,084* | *101,271* | *+7,187* | *+0.62%* | |

***Gampaha** grew fastest at **+2.28%/yr**. **Vavuniya** saw the steepest decline at **-0.35%/yr**. **Batticaloa** had the largest absolute increase (**+35,954**).*

### Islam

| District | 2012 | 2024 | Change | Annual Growth | % of Natl |
|---|---:|---:|---:|---:|---:|
| Mannar | 16,512 | 33,883 | +17,371 | +6.17% | 1.4% |
| Trincomalee | 159,418 | 205,664 | +46,246 | +2.15% | 8.8% |
| Polonnaruwa | 30,465 | 37,097 | +6,632 | +1.65% | 1.6% |
| Kurunegala | 117,810 | 143,299 | +25,489 | +1.65% | 6.1% |
| Kalutara | 114,556 | 138,230 | +23,674 | +1.58% | 5.9% |
| Ampara | 281,987 | 339,896 | +57,909 | +1.57% | 14.5% |
| Batticaloa | 134,065 | 161,494 | +27,429 | +1.56% | 6.9% |
| Gampaha | 112,746 | 134,422 | +21,676 | +1.48% | 5.8% |
| Kegalle | 61,164 | 72,616 | +11,452 | +1.44% | 3.1% |
| Puttalam | 150,404 | 176,963 | +26,559 | +1.36% | 7.6% |
| Anuradhapura | 71,493 | 83,979 | +12,486 | +1.35% | 3.6% |
| Galle | 39,267 | 46,038 | +6,771 | +1.33% | 2.0% |
| Matara | 25,614 | 29,858 | +4,244 | +1.29% | 1.3% |
| Matale | 45,682 | 52,224 | +6,542 | +1.12% | 2.2% |
| Kandy | 197,076 | 223,997 | +26,921 | +1.07% | 9.6% |
| Badulla | 47,192 | 53,563 | +6,371 | +1.06% | 2.3% |
| Ratnapura | 24,446 | 26,796 | +2,350 | +0.77% | 1.1% |
| Colombo | 274,067 | 298,422 | +24,355 | +0.71% | 12.8% |
| *Other (<1% or <1,000)* | *63,044* | *78,938* | *+15,894* | *+1.89%* | |

***Mannar** grew fastest at **+6.17%/yr**. **Colombo** had the slowest growth at **+0.71%/yr**. **Ampara** had the largest absolute increase (**+57,909**).*

### RomanCatholic

| District | 2012 | 2024 | Change | Annual Growth | % of Natl |
|---|---:|---:|---:|---:|---:|
| Mullaitivu | 9,063 | 13,982 | +4,919 | +3.68% | 1.1% |
| Kilinochchi | 12,063 | 14,446 | +2,383 | +1.51% | 1.2% |
| Mannar | 52,415 | 57,713 | +5,298 | +0.81% | 4.7% |
| Batticaloa | 24,454 | 25,803 | +1,349 | +0.45% | 2.1% |
| Jaffna | 75,474 | 77,197 | +1,723 | +0.19% | 6.3% |
| Puttalam | 240,221 | 240,975 | +754 | +0.03% | 19.7% |
| Trincomalee | 14,493 | 14,353 | -140 | -0.08% | 1.2% |
| Gampaha | 449,398 | 442,291 | -7,107 | -0.13% | 36.1% |
| Nuwara Eliya | 33,476 | 31,705 | -1,771 | -0.45% | 2.6% |
| Kurunegala | 43,707 | 40,273 | -3,434 | -0.68% | 3.3% |
| Kalutara | 39,774 | 36,510 | -3,264 | -0.71% | 3.0% |
| Colombo | 162,260 | 139,882 | -22,378 | -1.23% | 11.4% |
| Vavuniya | 15,305 | 12,785 | -2,520 | -1.49% | 1.0% |
| Kandy | 22,379 | 18,623 | -3,756 | -1.52% | 1.5% |
| *Other (<1% or <1,000)* | *66,654* | *57,810* | *-8,844* | *-1.18%* | |

***Mullaitivu** grew fastest at **+3.68%/yr**. **Kandy** saw the steepest decline at **-1.52%/yr**. **Mannar** had the largest absolute increase (**+5,298**).*

### OtherChristian

| District | 2012 | 2024 | Change | Annual Growth | % of Natl |
|---|---:|---:|---:|---:|---:|
| Mullaitivu | 3,664 | 6,315 | +2,651 | +4.64% | 2.2% |
| Kilinochchi | 6,436 | 9,074 | +2,638 | +2.90% | 3.2% |
| Batticaloa | 22,833 | 27,728 | +4,895 | +1.63% | 9.8% |
| Ampara | 5,541 | 6,486 | +945 | +1.32% | 2.3% |
| Mannar | 4,790 | 5,560 | +770 | +1.25% | 2.0% |
| Matara | 3,208 | 3,619 | +411 | +1.01% | 1.3% |
| Vavuniya | 8,498 | 8,895 | +397 | +0.38% | 3.2% |
| Jaffna | 20,511 | 20,857 | +346 | +0.14% | 7.4% |
| Galle | 5,315 | 5,377 | +62 | +0.10% | 1.9% |
| Anuradhapura | 3,660 | 3,656 | -4 | -0.01% | 1.3% |
| Nuwara Eliya | 15,508 | 15,474 | -34 | -0.02% | 5.5% |
| Trincomalee | 7,774 | 7,714 | -60 | -0.06% | 2.7% |
| Gampaha | 46,080 | 44,540 | -1,540 | -0.28% | 15.8% |
| Kurunegala | 9,926 | 9,413 | -513 | -0.44% | 3.3% |
| Ratnapura | 7,212 | 6,394 | -818 | -1.00% | 2.3% |
| Puttalam | 12,093 | 10,619 | -1,474 | -1.08% | 3.8% |
| Badulla | 6,615 | 5,729 | -886 | -1.19% | 2.0% |
| Kalutara | 8,956 | 7,733 | -1,223 | -1.22% | 2.7% |
| Kandy | 12,798 | 10,919 | -1,879 | -1.31% | 3.9% |
| Kegalle | 6,386 | 5,387 | -999 | -1.41% | 1.9% |
| Colombo | 66,947 | 55,624 | -11,323 | -1.53% | 19.7% |
| *Other (<1% or <1,000)* | *6,169* | *5,072* | *-1,097* | *-1.62%* | |

***Mullaitivu** grew fastest at **+4.64%/yr**. **Colombo** saw the steepest decline at **-1.53%/yr**. **Batticaloa** had the largest absolute increase (**+4,895**).*

### Other

| District | 2012 | 2024 | Change | Annual Growth | % of Natl |
|---|---:|---:|---:|---:|---:|
| Colombo | 2,262 | 1,204 | -1,058 | -5.12% | 30.4% |
| Puttalam | 1,162 | 279 | -883 | -11.21% | 7.1% |
| *Other (<1% or <1,000)* | *2,963* | *2,473* | *-490* | *-1.50%* | |

***Puttalam** saw the steepest decline at **-11.21%/yr**.*

---

## A3. Largest Change in Religious Proportion

![A3 representative chart](analyses/a3_proportion_change/chart.png)

For each district, the religion whose share of the local population changed most between 2012 and 2024.

### By District

| District | Religion | Share 2012 | Share 2024 | Change |
|---|---|---:|---:|---:|
| Mannar | Islam | 16.6% | 27.4% | +10.8% |
| Trincomalee | Islam | 42.0% | 46.5% | +4.4% |
| Vavuniya | Islam | 7.0% | 10.3% | +3.4% |
| Mullaitivu | Hindu | 75.3% | 72.4% | -2.9% |
| Ampara | Islam | 43.4% | 45.7% | +2.2% |
| Puttalam | RomanCatholic | 31.5% | 29.4% | -2.1% |
| Batticaloa | Islam | 25.5% | 27.1% | +1.6% |
| Gampaha | RomanCatholic | 19.5% | 18.2% | -1.3% |
| Kilinochchi | Hindu | 81.9% | 80.7% | -1.3% |
| Kalutara | Islam | 9.4% | 10.6% | +1.2% |
| Colombo | RomanCatholic | 7.0% | 5.9% | -1.1% |
| Kegalle | Islam | 7.3% | 8.3% | +1.1% |
| Kandy | Islam | 14.3% | 15.3% | +1.0% |
| Nuwara Eliya | Hindu | 51.0% | 52.0% | +1.0% |
| Kurunegala | Islam | 7.3% | 8.1% | +0.8% |
| Polonnaruwa | Islam | 7.5% | 8.3% | +0.8% |
| Ratnapura | Buddhist | 86.7% | 87.3% | +0.6% |
| Galle | Islam | 3.7% | 4.2% | +0.5% |
| Matale | Islam | 9.4% | 9.9% | +0.5% |
| Jaffna | Hindu | 82.8% | 82.3% | -0.5% |
| Badulla | Buddhist | 72.6% | 73.0% | +0.4% |
| Anuradhapura | Islam | 8.3% | 8.7% | +0.4% |
| Matara | Islam | 3.1% | 3.6% | +0.4% |
| Monaragala | Hindu | 2.7% | 2.8% | +0.2% |
| Hambantota | Islam | 2.5% | 2.7% | +0.1% |

---

## A4. DSD Boundary Changes

![A4 representative chart](analyses/a4_by_dsd/chart.png)

Districts where the number of DSDs changed between censuses are listed below. Within those districts, DSDs whose population growth deviates from the national rate (+6.99% over 2012–2024) by more than 2× are flagged as **Altered** — their apparent demographic shifts likely reflect re-demarcation rather than genuine change.

**Districts with changed DSD boundaries:**

| District | DSDs 2012 | DSDs 2024 | Δ |
|---|---:|---:|---:|
| Nuwara Eliya | 5 | 10 | +5 |
| Galle | 19 | 22 | +3 |
| Batticaloa | 14 | 13 | -1 |
| Ampara | 20 | 19 | -1 |
| Ratnapura | 17 | 18 | +1 |

**New, Altered, and Removed DSDs:**

| Status | Code | DSD | District | Pop 2012 | Pop 2024 | Pop Change |
|---|---|---|---|---:|---:|---:|
| Removed | LK-5224 | LK-5224 | Ampara | 44,632 | — | — |
| Altered | LK-5233 | Addalaichenai | Ampara | 41,968 | 53,214 | +26.8% |
| Altered | LK-5234 | Irakkamam | Ampara | 14,383 | 17,671 | +22.9% |
| Altered | LK-5221 | Kalmunai | Ampara | 29,800 | 52,798 | +77.2% |
| Altered | LK-5248 | Pottuvil | Ampara | 34,809 | 42,908 | +23.3% |
| Removed | LK-5109 | Koralai Pattu | Batticaloa | 23,376 | — | — |
| Removed | LK-5112 | LK-5112 | Batticaloa | 75,478 | — | — |
| Altered | LK-5115 | Eravur Pattu | Batticaloa | 24,643 | 94,237 | +282.4% |
| New | LK-5139 | Eravur Town | Batticaloa | — | 26,468 | — |
| Altered | LK-3127 | Baddegama | Galle | 75,008 | 50,956 | -32.1% |
| Altered | LK-3136 | Hikkaduwa | Galle | 101,909 | 26,216 | -74.3% |
| New | LK-3138 | Madampagama | Galle | — | 33,408 | — |
| New | LK-3137 | Rathgama | Galle | — | 41,456 | — |
| New | LK-3128 | Wanduramba | Galle | — | 27,702 | — |
| Altered | LK-2315 | Ambagamuwa Korale | Nuwara Eliya | 205,723 | 42,538 | -79.3% |
| Altered | LK-2306 | Hanguranketa | Nuwara Eliya | 88,528 | 58,931 | -33.4% |
| Altered | LK-2303 | Kothmale East | Nuwara Eliya | 101,180 | 61,742 | -39.0% |
| Altered | LK-2312 | Nuwara Eliya | Nuwara Eliya | 212,094 | 88,332 | -58.4% |
| Altered | LK-2309 | Walapane | Nuwara Eliya | 104,119 | 65,287 | -37.3% |
| New | LK-2304 | Kothmale West | Nuwara Eliya | — | 41,955 | — |
| New | LK-2307 | Mathurata | Nuwara Eliya | — | 33,175 | — |
| New | LK-2310 | Nildandahinna | Nuwara Eliya | — | 42,422 | — |
| New | LK-2316 | Norwood | Nuwara Eliya | — | 161,367 | — |
| New | LK-2313 | Thalawakele | Nuwara Eliya | — | 129,531 | — |
| Altered | LK-9118 | Balangoda | Ratnapura | 81,563 | 74,893 | -8.2% |
| Altered | LK-9103 | Eheliyagoda | Ratnapura | 88,022 | 74,071 | -15.8% |
| Altered | LK-9106 | Kuruvita | Ratnapura | 75,104 | 97,966 | +30.4% |
| New | LK-9119 | Kalthota | Ratnapura | — | 13,018 | — |

---

## A5. Largest Change in Religious Proportion by DSD

For each DSD, the religion whose share of the local population changed most between 2012 and 2024.

*Altered, new, and removed DSDs excluded. Religions with <1% of national count or <1,000 people in the DSD are excluded.*

### Buddhist

| DSD | District | Share 2012 | Share 2024 | Change |
|---|---|---:|---:|---:|
| Kaduwela | Colombo | 90.4% | 92.3% | +1.9% |
| Gampaha | Gampaha | 87.6% | 88.8% | +1.2% |
| Maharagama | Colombo | 92.0% | 93.2% | +1.2% |

### Hindu

| DSD | District | Share 2012 | Share 2024 | Change |
|---|---|---:|---:|---:|
| Puthukkudiyiruppu | Mullaitivu | 84.8% | 78.6% | -6.2% |
| Nallur | Jaffna | 90.4% | 85.9% | -4.5% |
| Wattala | Gampaha | 13.0% | 16.9% | +3.9% |
| Vadamaradchi North (Point Pedro) | Jaffna | 83.9% | 86.4% | +2.5% |
| Vavuniya | Vavuniya | 78.3% | 75.8% | -2.5% |
| Thimbirigasyaya | Colombo | 22.5% | 24.4% | +1.9% |
| Colombo | Colombo | 22.7% | 24.6% | +1.9% |
| Karachchi | Kilinochchi | 83.1% | 81.4% | -1.7% |
| Manmunai South & Eruvil Pattu | Batticaloa | 93.9% | 95.4% | +1.4% |
| Thenmaradchi (Chavakachcheri) | Jaffna | 92.7% | 91.7% | -1.0% |
| Valikamam South West (Sandilipay) | Jaffna | 75.1% | 76.1% | +0.9% |
| Valikamam North (Thllippalai) | Jaffna | 85.8% | 84.9% | -0.9% |
| Town & Gravets | Trincomalee | 49.0% | 48.2% | -0.9% |
| Hali-Ela | Badulla | 29.0% | 29.7% | +0.8% |
| Manmunai West | Batticaloa | 97.2% | 97.9% | +0.7% |

### Islam

| DSD | District | Share 2012 | Share 2024 | Change |
|---|---|---:|---:|---:|
| Koralai Pattu Central | Batticaloa | 97.2% | 0.3% | -96.9% |
| Kolonnawa | Colombo | 23.1% | 31.3% | +8.3% |
| Dehiwala | Colombo | 22.6% | 30.4% | +7.8% |
| Galle 4 Gravets | Galle | 32.3% | 36.0% | +3.7% |
| Beruwala | Kalutara | 34.7% | 38.2% | +3.5% |
| Mundel | Puttalam | 38.6% | 41.9% | +3.3% |
| Akurana | Kandy | 64.9% | 67.9% | +3.0% |
| Negombo | Gampaha | 14.3% | 17.2% | +2.9% |
| Mawanella | Kegalle | 30.4% | 33.3% | +2.8% |
| Panadura | Kalutara | 14.4% | 17.2% | +2.8% |
| Puttalam | Puttalam | 64.2% | 66.6% | +2.4% |
| Attanagalla | Gampaha | 12.4% | 14.4% | +1.9% |
| Udunuwara | Kandy | 24.5% | 26.4% | +1.9% |
| Udapalatha | Kandy | 22.7% | 24.4% | +1.8% |
| Kuchchaweli | Trincomalee | 64.1% | 65.8% | +1.7% |
| Muthur | Trincomalee | 62.0% | 63.5% | +1.5% |
| Kinniya | Trincomalee | 95.8% | 97.1% | +1.4% |

### RomanCatholic

| DSD | District | Share 2012 | Share 2024 | Change |
|---|---|---:|---:|---:|
| Mannar Town | Mannar | 54.8% | 50.6% | -4.1% |
| Nattandiya | Puttalam | 40.6% | 38.2% | -2.4% |
| Jaffna | Jaffna | 52.9% | 50.6% | -2.3% |
| Kelaniya | Gampaha | 9.8% | 7.7% | -2.1% |
| Nanaddan | Mannar | 68.4% | 66.4% | -2.0% |
| Dankotuwa | Puttalam | 29.8% | 27.9% | -1.9% |
| Katana | Gampaha | 32.0% | 34.0% | +1.9% |
| Manmunai North | Batticaloa | 19.0% | 17.4% | -1.6% |
| Mahawewa | Puttalam | 51.8% | 50.4% | -1.4% |
| Kalpitiya | Puttalam | 32.3% | 33.6% | +1.4% |
| Chilaw | Puttalam | 45.7% | 44.4% | -1.3% |
| Mahara | Gampaha | 8.8% | 7.6% | -1.2% |
| Wennappuwa | Puttalam | 78.4% | 77.6% | -0.8% |

### OtherChristian

| DSD | District | Share 2012 | Share 2024 | Change |
|---|---|---:|---:|---:|
| Koralai Pattu North | Batticaloa | 12.1% | 13.5% | +1.4% |
| Sri Jayawardanapura Kotte | Colombo | 4.7% | 3.5% | -1.2% |

---

*Data from the 2012 and 2024 Sri Lanka Census, accessed via [lanka_data](https://pypi.org/project/lanka-data/). Raw data and derived tables live in the corresponding directories under [`analyses/`](analyses/).*
