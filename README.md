# lk_religion

Analyses of Sri Lanka's religious demographics, comparing the **2012 Census** and **2024 Census**.

Each analysis now lives in its own folder under [`analyses/`](analyses/), together with its own README, workflow script, and related data files. The sections below are copied from those child READMEs.

- [`analyses/a1_national_totals/`](analyses/a1_national_totals/)
- [`analyses/a2_by_district/`](analyses/a2_by_district/)
- [`analyses/a3_proportion_change/`](analyses/a3_proportion_change/)
- [`analyses/a4_by_dsd/`](analyses/a4_by_dsd/)
- [`analyses/a5_proportion_change_by_dsd/`](analyses/a5_proportion_change_by_dsd/)
- [`analyses/a6_by_province/`](analyses/a6_by_province/)
- [`analyses/a7_by_dsd/`](analyses/a7_by_dsd/)

---

## A1. National Population by Religion

![A1 representative chart](analyses/a1_national_totals/chart.png)

| Religion | 2012 | 2024 | Change | Annual Growth | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Buddhist | 14,271,183 | 15,199,093 | +927,910 🟩 | +0.53% 🟩 | 70.1% | 69.8% | -0.3 🟥 pp |
| Hindu | 2,561,142 | 2,734,839 | +173,697 🟩 | +0.55% 🟩 | 12.6% | 12.6% | 0.0 pp |
| Islam | 1,967,008 | 2,337,379 | +370,371 🟩 | +1.45% 🟩 | 9.7% | 10.7% | +1.1 🟩 pp |
| RomanCatholic | 1,261,136 | 1,224,348 | -36,788 🟥 | -0.25% 🟥 | 6.2% | 5.6% | -0.6 🟥 pp |
| OtherChristian | 290,920 | 282,185 | -8,735 🟥 | -0.25% 🟥 | 1.4% | 1.3% | -0.1 🟥 pp |
| Other | 6,387 | 3,956 | -2,431 🟥 | -3.91% 🟥 | 0.0% | 0.0% | 0.0 pp |
| **Total** | **20,357,776** | **21,781,800** | **+1,424,024 🟩** | **+0.57% 🟩** | **100.0%** | **100.0%** | **0.0 pp** |

### Commentary

- Sri Lanka's total population grew from **20,357,776** (2012) to **21,781,800** (2024), an increase of **+1,424,024** at an annual rate of **+0.57%**.
- **Buddhism** remains the dominant religion, accounting for **69.8%** of the population in 2024, growing at **+0.53%** per year.
- **Islam** has the fastest growth rate among major religions at **+1.45%** per year, reaching a share of **10.7%** in 2024.
- **Roman Catholic** and **Other Christian** communities show slight declines over the period.

---

## A2. Religion by District: Key Trends

![A2 district change maps](analyses/a2_by_district/chart.png)

District labels show the **district name** and **change in share of population (pp)**. Districts are shaded by **change in share of population (pp)** from **red (decline)** to **green (growth)**. Districts with religion population **< 1,000 (2024)** are shown in **grey**.

### Buddhist

| District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Puttalam `LK-62` | 2.4% | 329,705 | 361,148 | +31,443 🟩 | 43.2% | 44.1% | +0.9 🟩 pp |
| Vavuniya `LK-43` | 0.1% | 16,799 | 18,292 | +1,493 🟩 | 9.8% | 10.6% | +0.9 🟩 pp |
| Colombo `LK-11` | 11.1% | 1,632,125 | 1,682,524 | +50,399 🟩 | 70.2% | 70.8% | +0.6 🟩 pp |
| Ratnapura `LK-91` | 6.6% | 943,464 | 999,682 | +56,218 🟩 | 86.7% | 87.3% | +0.6 🟩 pp |
| Badulla `LK-81` | 4.2% | 591,799 | 636,988 | +45,189 🟩 | 72.6% | 73.0% | +0.4 🟩 pp |
| Gampaha `LK-12` | 11.5% | 1,642,767 | 1,744,475 | +101,708 🟩 | 71.3% | 71.6% | +0.3 🟩 pp |
| Jaffna `LK-41` | 0.0% | 2,168 | 2,788 | +620 🟩 | 0.4% | 0.5% | +0.1 🟩 pp |
| Hambantota `LK-33` | 4.3% | 580,344 | 649,736 | +69,392 🟩 | 96.7% | 96.8% | 0.0 pp |
| Kilinochchi `LK-45` | 0.0% | 1,275 | 1,533 | +258 🟩 | 1.1% | 1.1% | 0.0 pp |
| Matale `LK-22` | 2.8% | 385,151 | 418,608 | +33,457 🟩 | 79.5% | 79.5% | 0.0 pp |
| Monaragala `LK-82` | 3.3% | 426,762 | 498,436 | +71,674 🟩 | 94.6% | 94.5% | -0.1 🟥 pp |
| Matara `LK-32` | 5.2% | 766,323 | 787,303 | +20,980 🟩 | 94.1% | 94.0% | -0.2 🟥 pp |
| Batticaloa `LK-51` | 0.0% | 6,281 | 6,024 | -257 🟥 | 1.2% | 1.0% | -0.2 🟥 pp |
| Anuradhapura `LK-71` | 5.7% | 775,366 | 862,807 | +87,441 🟩 | 90.1% | 89.9% | -0.2 🟥 pp |
| Kurunegala `LK-61` | 10.2% | 1,430,958 | 1,557,554 | +126,596 🟩 | 88.5% | 88.1% | -0.4 🟥 pp |
| Galle `LK-31` | 6.8% | 998,647 | 1,026,031 | +27,384 🟩 | 93.9% | 93.5% | -0.4 🟥 pp |
| Polonnaruwa `LK-72` | 2.6% | 364,229 | 399,488 | +35,259 🟩 | 89.7% | 89.3% | -0.4 🟥 pp |
| Mullaitivu `LK-44` | 0.1% | 8,140 | 10,293 | +2,153 🟩 | 8.8% | 8.4% | -0.4 🟥 pp |
| Kalutara `LK-13` | 7.1% | 1,018,909 | 1,080,638 | +61,729 🟩 | 83.4% | 82.8% | -0.6 🟥 pp |
| Kandy `LK-21` | 7.0% | 1,009,220 | 1,063,511 | +54,291 🟩 | 73.4% | 72.7% | -0.6 🟥 pp |
| Nuwara Eliya `LK-23` | 1.8% | 278,254 | 278,828 | +574 🟩 | 39.1% | 38.4% | -0.7 🟥 pp |
| Kegalle `LK-92` | 4.8% | 709,917 | 728,929 | +19,012 🟩 | 84.4% | 83.7% | -0.7 🟥 pp |
| Mannar `LK-42` | 0.0% | 1,809 | 382 | -1,427 🟥 | 1.8% | 0.3% | -1.5 🟥 pp |
| Ampara `LK-52` | 1.8% | 251,427 | 276,176 | +24,749 🟩 | 38.7% | 37.1% | -1.6 🟥 pp |
| Trincomalee `LK-53` | 0.7% | 99,344 | 106,919 | +7,575 🟩 | 26.2% | 24.1% | -2.0 🟥 pp |

***Puttalam** gained the most share at **+0.9pp**. **Trincomalee** saw the steepest share decline at **-2.0pp**. **Kurunegala** had the largest absolute increase (**+126,596**).*

### Hindu

| District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Nuwara Eliya `LK-23` | 13.8% | 363,163 | 377,266 | +14,103 🟩 | 51.0% | 52.0% | +1.0 🟩 pp |
| Gampaha `LK-12` | 2.5% | 52,973 | 69,429 | +16,456 🟩 | 2.3% | 2.9% | +0.6 🟩 pp |
| Colombo `LK-11` | 7.2% | 186,303 | 197,759 | +11,456 🟩 | 8.0% | 8.3% | +0.3 🟩 pp |
| Monaragala `LK-82` | 0.5% | 11,997 | 14,974 | +2,977 🟩 | 2.7% | 2.8% | +0.2 🟩 pp |
| Kandy `LK-21` | 5.3% | 133,744 | 144,618 | +10,874 🟩 | 9.7% | 9.9% | +0.2 🟩 pp |
| Kurunegala `LK-61` | 0.6% | 14,716 | 17,487 | +2,771 🟩 | 0.9% | 1.0% | +0.1 🟩 pp |
| Kalutara `LK-13` | 1.6% | 39,541 | 42,528 | +2,987 🟩 | 3.2% | 3.3% | 0.0 pp |
| Anuradhapura `LK-71` | 0.1% | 3,231 | 3,755 | +524 🟩 | 0.4% | 0.4% | 0.0 pp |
| Hambantota `LK-33` | 0.1% | 1,222 | 1,401 | +179 🟩 | 0.2% | 0.2% | 0.0 pp |
| Kegalle `LK-92` | 2.1% | 54,350 | 56,199 | +1,849 🟩 | 6.5% | 6.5% | 0.0 pp |
| Galle `LK-31` | 0.6% | 15,584 | 15,600 | +16 🟩 | 1.5% | 1.4% | 0.0 pp |
| Polonnaruwa `LK-72` | 0.3% | 6,886 | 7,215 | +329 🟩 | 1.7% | 1.6% | -0.1 🟥 pp |
| Matale `LK-22` | 1.7% | 43,432 | 46,181 | +2,749 🟩 | 9.0% | 8.8% | -0.2 🟥 pp |
| Badulla `LK-81` | 6.1% | 157,608 | 166,380 | +8,772 🟩 | 19.3% | 19.1% | -0.3 🟥 pp |
| Puttalam `LK-62` | 1.1% | 28,811 | 28,832 | +21 🟩 | 3.8% | 3.5% | -0.3 🟥 pp |
| Matara `LK-32` | 0.5% | 16,421 | 14,625 | -1,796 🟥 | 2.0% | 1.7% | -0.3 🟥 pp |
| Ratnapura `LK-91` | 3.8% | 101,962 | 103,883 | +1,921 🟩 | 9.4% | 9.1% | -0.3 🟥 pp |
| Ampara `LK-52` | 4.2% | 102,829 | 114,586 | +11,757 🟩 | 15.8% | 15.4% | -0.4 🟥 pp |
| Jaffna `LK-41` | 17.9% | 483,255 | 489,521 | +6,266 🟩 | 82.8% | 82.3% | -0.5 🟥 pp |
| Kilinochchi `LK-45` | 4.0% | 92,986 | 110,258 | +17,272 🟩 | 81.9% | 80.7% | -1.3 🟥 pp |
| Batticaloa `LK-51` | 13.7% | 338,882 | 374,836 | +35,954 🟩 | 64.4% | 62.9% | -1.5 🟥 pp |
| Trincomalee `LK-53` | 4.0% | 98,442 | 108,050 | +9,608 🟩 | 25.9% | 24.4% | -1.5 🟥 pp |
| Mullaitivu `LK-44` | 3.2% | 69,377 | 88,738 | +19,361 🟩 | 75.3% | 72.4% | -2.9 🟥 pp |
| Vavuniya `LK-43` | 4.2% | 119,400 | 114,504 | -4,896 🟥 | 69.4% | 66.5% | -2.9 🟥 pp |
| Mannar `LK-42` | 1.0% | 24,027 | 26,214 | +2,187 🟩 | 24.1% | 21.2% | -2.9 🟥 pp |

***Nuwara Eliya** gained the most share at **+1.0pp**. **Mannar** saw the steepest share decline at **-2.9pp**. **Batticaloa** had the largest absolute increase (**+35,954**).*

### Islam

| District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Mannar `LK-42` | 1.4% | 16,512 | 33,883 | +17,371 🟩 | 16.6% | 27.4% | +10.8 🟩 pp |
| Trincomalee `LK-53` | 8.8% | 159,418 | 205,664 | +46,246 🟩 | 42.0% | 46.5% | +4.4 🟩 pp |
| Vavuniya `LK-43` | 0.8% | 11,972 | 17,775 | +5,803 🟩 | 7.0% | 10.3% | +3.4 🟩 pp |
| Ampara `LK-52` | 14.5% | 281,987 | 339,896 | +57,909 🟩 | 43.4% | 45.7% | +2.2 🟩 pp |
| Puttalam `LK-62` | 7.6% | 150,404 | 176,963 | +26,559 🟩 | 19.7% | 21.6% | +1.9 🟩 pp |
| Batticaloa `LK-51` | 6.9% | 134,065 | 161,494 | +27,429 🟩 | 25.5% | 27.1% | +1.6 🟩 pp |
| Kalutara `LK-13` | 5.9% | 114,556 | 138,230 | +23,674 🟩 | 9.4% | 10.6% | +1.2 🟩 pp |
| Kegalle `LK-92` | 3.1% | 61,164 | 72,616 | +11,452 🟩 | 7.3% | 8.3% | +1.1 🟩 pp |
| Kandy `LK-21` | 9.6% | 197,076 | 223,997 | +26,921 🟩 | 14.3% | 15.3% | +1.0 🟩 pp |
| Kurunegala `LK-61` | 6.1% | 117,810 | 143,299 | +25,489 🟩 | 7.3% | 8.1% | +0.8 🟩 pp |
| Polonnaruwa `LK-72` | 1.6% | 30,465 | 37,097 | +6,632 🟩 | 7.5% | 8.3% | +0.8 🟩 pp |
| Colombo `LK-11` | 12.8% | 274,067 | 298,422 | +24,355 🟩 | 11.8% | 12.6% | +0.8 🟩 pp |
| Mullaitivu `LK-44` | 0.1% | 1,880 | 3,279 | +1,399 🟩 | 2.0% | 2.7% | +0.6 🟩 pp |
| Gampaha `LK-12` | 5.8% | 112,746 | 134,422 | +21,676 🟩 | 4.9% | 5.5% | +0.6 🟩 pp |
| Galle `LK-31` | 2.0% | 39,267 | 46,038 | +6,771 🟩 | 3.7% | 4.2% | +0.5 🟩 pp |
| Matale `LK-22` | 2.2% | 45,682 | 52,224 | +6,542 🟩 | 9.4% | 9.9% | +0.5 🟩 pp |
| Anuradhapura `LK-71` | 3.6% | 71,493 | 83,979 | +12,486 🟩 | 8.3% | 8.7% | +0.4 🟩 pp |
| Matara `LK-32` | 1.3% | 25,614 | 29,858 | +4,244 🟩 | 3.1% | 3.6% | +0.4 🟩 pp |
| Kilinochchi `LK-45` | 0.1% | 700 | 1,394 | +694 🟩 | 0.6% | 1.0% | +0.4 🟩 pp |
| Badulla `LK-81` | 2.3% | 47,192 | 53,563 | +6,371 🟩 | 5.8% | 6.1% | +0.4 🟩 pp |
| Jaffna `LK-41` | 0.2% | 2,363 | 4,352 | +1,989 🟩 | 0.4% | 0.7% | +0.3 🟩 pp |
| Monaragala `LK-82` | 0.5% | 9,809 | 12,262 | +2,453 🟩 | 2.2% | 2.3% | +0.1 🟩 pp |
| Hambantota `LK-33` | 0.8% | 15,204 | 17,947 | +2,743 🟩 | 2.5% | 2.7% | +0.1 🟩 pp |
| Ratnapura `LK-91` | 1.1% | 24,446 | 26,796 | +2,350 🟩 | 2.2% | 2.3% | +0.1 🟩 pp |
| Nuwara Eliya `LK-23` | 0.9% | 21,116 | 21,929 | +813 🟩 | 3.0% | 3.0% | +0.1 🟩 pp |

***Mannar** gained the most share at **+10.8pp**. **Nuwara Eliya** had the smallest share gain at **+0.1pp**. **Ampara** had the largest absolute increase (**+57,909**).*

### Roman Catholic

| District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Mullaitivu `LK-44` | 1.1% | 9,063 | 13,982 | +4,919 🟩 | 9.8% | 11.4% | +1.6 🟩 pp |
| Jaffna `LK-41` | 6.3% | 75,474 | 77,197 | +1,723 🟩 | 12.9% | 13.0% | +0.1 🟩 pp |
| Matara `LK-32` | 0.2% | 2,432 | 2,445 | +13 🟩 | 0.3% | 0.3% | 0.0 pp |
| Galle `LK-31` | 0.3% | 4,415 | 4,207 | -208 🟥 | 0.4% | 0.4% | 0.0 pp |
| Hambantota `LK-33` | 0.1% | 1,139 | 1,017 | -122 🟥 | 0.2% | 0.2% | 0.0 pp |
| Kilinochchi `LK-45` | 1.2% | 12,063 | 14,446 | +2,383 🟩 | 10.6% | 10.6% | -0.1 🟥 pp |
| Monaragala `LK-82` | 0.1% | 1,601 | 1,181 | -420 🟥 | 0.4% | 0.2% | -0.1 🟥 pp |
| Matale `LK-22` | 0.6% | 7,899 | 7,797 | -102 🟥 | 1.6% | 1.5% | -0.2 🟥 pp |
| Ampara `LK-52` | 0.6% | 7,588 | 7,351 | -237 🟥 | 1.2% | 1.0% | -0.2 🟥 pp |
| Anuradhapura `LK-71` | 0.5% | 6,747 | 5,760 | -987 🟥 | 0.8% | 0.6% | -0.2 🟥 pp |
| Kegalle `LK-92` | 0.6% | 8,777 | 7,292 | -1,485 🟥 | 1.0% | 0.8% | -0.2 🟥 pp |
| Polonnaruwa `LK-72` | 0.2% | 3,192 | 2,560 | -632 🟥 | 0.8% | 0.6% | -0.2 🟥 pp |
| Ratnapura `LK-91` | 0.7% | 10,844 | 8,607 | -2,237 🟥 | 1.0% | 0.8% | -0.2 🟥 pp |
| Batticaloa `LK-51` | 2.1% | 24,454 | 25,803 | +1,349 🟩 | 4.6% | 4.3% | -0.3 🟥 pp |
| Nuwara Eliya `LK-23` | 2.6% | 33,476 | 31,705 | -1,771 🟥 | 4.7% | 4.4% | -0.3 🟥 pp |
| Kandy `LK-21` | 1.5% | 22,379 | 18,623 | -3,756 🟥 | 1.6% | 1.3% | -0.4 🟥 pp |
| Badulla `LK-81` | 0.8% | 12,020 | 9,593 | -2,427 🟥 | 1.5% | 1.1% | -0.4 🟥 pp |
| Kurunegala `LK-61` | 3.3% | 43,707 | 40,273 | -3,434 🟥 | 2.7% | 2.3% | -0.4 🟥 pp |
| Kalutara `LK-13` | 3.0% | 39,774 | 36,510 | -3,264 🟥 | 3.3% | 2.8% | -0.5 🟥 pp |
| Trincomalee `LK-53` | 1.2% | 14,493 | 14,353 | -140 🟥 | 3.8% | 3.2% | -0.6 🟥 pp |
| Colombo `LK-11` | 11.4% | 162,260 | 139,882 | -22,378 🟥 | 7.0% | 5.9% | -1.1 🟥 pp |
| Gampaha `LK-12` | 36.1% | 449,398 | 442,291 | -7,107 🟥 | 19.5% | 18.2% | -1.3 🟥 pp |
| Vavuniya `LK-43` | 1.0% | 15,305 | 12,785 | -2,520 🟥 | 8.9% | 7.4% | -1.5 🟥 pp |
| Puttalam `LK-62` | 19.7% | 240,221 | 240,975 | +754 🟩 | 31.5% | 29.4% | -2.1 🟥 pp |
| Mannar `LK-42` | 4.7% | 52,415 | 57,713 | +5,298 🟩 | 52.6% | 46.6% | -6.0 🟥 pp |

***Mullaitivu** gained the most share at **+1.6pp**. **Mannar** saw the steepest share decline at **-6.0pp**. **Mannar** had the largest absolute increase (**+5,298**).*

### Other Christian

| District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Mullaitivu `LK-44` | 2.2% | 3,664 | 6,315 | +2,651 🟩 | 4.0% | 5.2% | +1.2 🟩 pp |
| Kilinochchi `LK-45` | 3.2% | 6,436 | 9,074 | +2,638 🟩 | 5.7% | 6.6% | +1.0 🟩 pp |
| Batticaloa `LK-51` | 9.8% | 22,833 | 27,728 | +4,895 🟩 | 4.3% | 4.7% | +0.3 🟩 pp |
| Vavuniya `LK-43` | 3.2% | 8,498 | 8,895 | +397 🟩 | 4.9% | 5.2% | +0.2 🟩 pp |
| Matara `LK-32` | 1.3% | 3,208 | 3,619 | +411 🟩 | 0.4% | 0.4% | 0.0 pp |
| Ampara `LK-52` | 2.3% | 5,541 | 6,486 | +945 🟩 | 0.9% | 0.9% | 0.0 pp |
| Jaffna `LK-41` | 7.4% | 20,511 | 20,857 | +346 🟩 | 3.5% | 3.5% | 0.0 pp |
| Galle `LK-31` | 1.9% | 5,315 | 5,377 | +62 🟩 | 0.5% | 0.5% | 0.0 pp |
| Anuradhapura `LK-71` | 1.3% | 3,660 | 3,656 | -4 🟥 | 0.4% | 0.4% | 0.0 pp |
| Nuwara Eliya `LK-23` | 5.5% | 15,508 | 15,474 | -34 🟥 | 2.2% | 2.1% | 0.0 pp |
| Monaragala `LK-82` | 0.3% | 859 | 713 | -146 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Polonnaruwa `LK-72` | 0.4% | 1,276 | 1,086 | -190 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Kurunegala `LK-61` | 3.3% | 9,926 | 9,413 | -513 🟥 | 0.6% | 0.5% | -0.1 🟥 pp |
| Hambantota `LK-33` | 0.4% | 1,692 | 1,247 | -445 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Matale `LK-22` | 0.7% | 2,342 | 2,026 | -316 🟥 | 0.5% | 0.4% | -0.1 🟥 pp |
| Ratnapura `LK-91` | 2.3% | 7,212 | 6,394 | -818 🟥 | 0.7% | 0.6% | -0.1 🟥 pp |
| Kalutara `LK-13` | 2.7% | 8,956 | 7,733 | -1,223 🟥 | 0.7% | 0.6% | -0.1 🟥 pp |
| Kegalle `LK-92` | 1.9% | 6,386 | 5,387 | -999 🟥 | 0.8% | 0.6% | -0.1 🟥 pp |
| Badulla `LK-81` | 2.0% | 6,615 | 5,729 | -886 🟥 | 0.8% | 0.7% | -0.2 🟥 pp |
| Gampaha `LK-12` | 15.8% | 46,080 | 44,540 | -1,540 🟥 | 2.0% | 1.8% | -0.2 🟥 pp |
| Kandy `LK-21` | 3.9% | 12,798 | 10,919 | -1,879 🟥 | 0.9% | 0.7% | -0.2 🟥 pp |
| Puttalam `LK-62` | 3.8% | 12,093 | 10,619 | -1,474 🟥 | 1.6% | 1.3% | -0.3 🟥 pp |
| Trincomalee `LK-53` | 2.7% | 7,774 | 7,714 | -60 🟥 | 2.0% | 1.7% | -0.3 🟥 pp |
| Mannar `LK-42` | 2.0% | 4,790 | 5,560 | +770 🟩 | 4.8% | 4.5% | -0.3 🟥 pp |
| Colombo `LK-11` | 19.7% | 66,947 | 55,624 | -11,323 🟥 | 2.9% | 2.3% | -0.5 🟥 pp |

***Mullaitivu** gained the most share at **+1.2pp**. **Colombo** saw the steepest share decline at **-0.5pp**. **Batticaloa** had the largest absolute increase (**+4,895**).*

### Other

| District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Polonnaruwa `LK-72` | 2.1% | 40 | 84 | +44 🟩 | 0.0% | 0.0% | 0.0 pp |
| Anuradhapura `LK-71` | 3.1% | 78 | 123 | +45 🟩 | 0.0% | 0.0% | 0.0 pp |
| Kandy `LK-21` | 5.7% | 165 | 227 | +62 🟩 | 0.0% | 0.0% | 0.0 pp |
| Ampara `LK-52` | 1.4% | 30 | 56 | +26 🟩 | 0.0% | 0.0% | 0.0 pp |
| Gampaha `LK-12` | 24.9% | 869 | 985 | +116 🟩 | 0.0% | 0.0% | 0.0 pp |
| Matale `LK-22` | 0.9% | 25 | 34 | +9 🟩 | 0.0% | 0.0% | 0.0 pp |
| Galle `LK-31` | 3.0% | 106 | 119 | +13 🟩 | 0.0% | 0.0% | 0.0 pp |
| Kegalle `LK-92` | 1.3% | 54 | 53 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Matara `LK-32` | 1.0% | 50 | 39 | -11 🟥 | 0.0% | 0.0% | 0.0 pp |
| Ratnapura `LK-91` | 1.5% | 79 | 61 | -18 🟥 | 0.0% | 0.0% | 0.0 pp |
| Monaragala `LK-82` | 0.5% | 30 | 19 | -11 🟥 | 0.0% | 0.0% | 0.0 pp |
| Kurunegala `LK-61` | 3.3% | 170 | 130 | -40 🟥 | 0.0% | 0.0% | 0.0 pp |
| Batticaloa `LK-51` | 0.8% | 52 | 33 | -19 🟥 | 0.0% | 0.0% | 0.0 pp |
| Kalutara `LK-13` | 3.7% | 212 | 145 | -67 🟥 | 0.0% | 0.0% | 0.0 pp |
| Nuwara Eliya `LK-23` | 2.0% | 127 | 78 | -49 🟥 | 0.0% | 0.0% | 0.0 pp |
| Trincomalee `LK-53` | 1.1% | 70 | 45 | -25 🟥 | 0.0% | 0.0% | 0.0 pp |
| Jaffna `LK-41` | 0.9% | 111 | 36 | -75 🟥 | 0.0% | 0.0% | 0.0 pp |
| Mannar `LK-42` | 0.1% | 17 | 4 | -13 🟥 | 0.0% | 0.0% | 0.0 pp |
| Vavuniya `LK-43` | 1.5% | 86 | 61 | -25 🟥 | 0.1% | 0.0% | 0.0 pp |
| Badulla `LK-81` | 1.4% | 171 | 54 | -117 🟥 | 0.0% | 0.0% | 0.0 pp |
| Hambantota `LK-33` | 1.8% | 302 | 70 | -232 🟥 | 0.1% | 0.0% | 0.0 pp |
| Kilinochchi `LK-45` | 0.1% | 50 | 5 | -45 🟥 | 0.0% | 0.0% | 0.0 pp |
| Colombo `LK-11` | 30.4% | 2,262 | 1,204 | -1,058 🟥 | 0.1% | 0.1% | 0.0 pp |
| Mullaitivu `LK-44` | 0.3% | 69 | 12 | -57 🟥 | 0.1% | 0.0% | -0.1 🟥 pp |
| Puttalam `LK-62` | 7.1% | 1,162 | 279 | -883 🟥 | 0.2% | 0.0% | -0.1 🟥 pp |

***Polonnaruwa** gained the most share at **0.0pp**. **Puttalam** saw the steepest share decline at **-0.1pp**. **Gampaha** had the largest absolute increase (**+116**).*

---

## A3. Largest Change in Religious Proportion

![A3 increase/decrease maps](analyses/a3_proportion_change/chart.png)

For each district, the religion whose share of the local population changed most between 2012 and 2024, showing only rows with absolute change > 1%. Largest increases and largest decreases are shown on separate maps.

### Hindu

| District | Share 2012 | Share 2024 | Change (pp) |
|---|---:|---:|---:|
| Kilinochchi `LK-45` | 81.9% | 80.7% | -1.3pp 🟥 |
| Mullaitivu `LK-44` | 75.3% | 72.4% | -2.9pp 🟥 |

### Islam

| District | Share 2012 | Share 2024 | Change (pp) |
|---|---:|---:|---:|
| Mannar `LK-42` | 16.6% | 27.4% | +10.8pp 🟩 |
| Trincomalee `LK-53` | 42.0% | 46.5% | +4.4pp 🟩 |
| Vavuniya `LK-43` | 7.0% | 10.3% | +3.4pp 🟩 |
| Ampara `LK-52` | 43.4% | 45.7% | +2.2pp 🟩 |
| Batticaloa `LK-51` | 25.5% | 27.1% | +1.6pp 🟩 |
| Kalutara `LK-13` | 9.4% | 10.6% | +1.2pp 🟩 |
| Kegalle `LK-92` | 7.3% | 8.3% | +1.1pp 🟩 |

### RomanCatholic

| District | Share 2012 | Share 2024 | Change (pp) |
|---|---:|---:|---:|
| Colombo `LK-11` | 7.0% | 5.9% | -1.1pp 🟥 |
| Gampaha `LK-12` | 19.5% | 18.2% | -1.3pp 🟥 |
| Puttalam `LK-62` | 31.5% | 29.4% | -2.1pp 🟥 |

---

## A4. DSD Boundary Changes

![A4 representative chart](analyses/a4_by_dsd/chart.png)

Districts where the number of DSDs changed between censuses are listed below. Within those districts, DSDs whose population growth deviates from the national rate (+6.99% over 2012–2024) by more than 2× are flagged as **Altered** — their apparent demographic shifts likely reflect re-demarcation rather than genuine change.

**Districts with changed DSD boundaries:**

| District | DSDs 2012 | DSDs 2024 | Δ |
|---|---:|---:|---:|
| Nuwara Eliya `LK-23` | 5 | 10 | +5 🟩 |
| Galle `LK-31` | 19 | 22 | +3 🟩 |
| Batticaloa `LK-51` | 14 | 13 | -1 🟥 |
| Ampara `LK-52` | 20 | 19 | -1 🟥 |
| Ratnapura `LK-91` | 17 | 18 | +1 🟩 |

**New, Altered, and Removed DSDs:**

| Status | DSD | District | Pop 2012 | Pop 2024 | Pop Change |
|---|---|---|---:|---:|---:|
| Removed | LK-5224 `LK-5224` | Ampara `LK-52` | 44,632 | — | — |
| Altered | Addalaichenai `LK-5233` | Ampara `LK-52` | 41,968 | 53,214 | +26.8% 🟩 |
| Altered | Irakkamam `LK-5234` | Ampara `LK-52` | 14,383 | 17,671 | +22.9% 🟩 |
| Altered | Kalmunai `LK-5221` | Ampara `LK-52` | 29,800 | 52,798 | +77.2% 🟩 |
| Altered | Pottuvil `LK-5248` | Ampara `LK-52` | 34,809 | 42,908 | +23.3% 🟩 |
| Removed | Koralai Pattu `LK-5109` | Batticaloa `LK-51` | 23,376 | — | — |
| Removed | LK-5112 `LK-5112` | Batticaloa `LK-51` | 75,478 | — | — |
| Altered | Eravur Pattu `LK-5115` | Batticaloa `LK-51` | 24,643 | 94,237 | +282.4% 🟩 |
| New | Eravur Town `LK-5139` | Batticaloa `LK-51` | — | 26,468 | — |
| Altered | Baddegama `LK-3127` | Galle `LK-31` | 75,008 | 50,956 | -32.1% 🟥 |
| Altered | Hikkaduwa `LK-3136` | Galle `LK-31` | 101,909 | 26,216 | -74.3% 🟥 |
| New | Madampagama `LK-3138` | Galle `LK-31` | — | 33,408 | — |
| New | Rathgama `LK-3137` | Galle `LK-31` | — | 41,456 | — |
| New | Wanduramba `LK-3128` | Galle `LK-31` | — | 27,702 | — |
| Altered | Ambagamuwa Korale `LK-2315` | Nuwara Eliya `LK-23` | 205,723 | 42,538 | -79.3% 🟥 |
| Altered | Hanguranketa `LK-2306` | Nuwara Eliya `LK-23` | 88,528 | 58,931 | -33.4% 🟥 |
| Altered | Kothmale East `LK-2303` | Nuwara Eliya `LK-23` | 101,180 | 61,742 | -39.0% 🟥 |
| Altered | Nuwara Eliya `LK-2312` | Nuwara Eliya `LK-23` | 212,094 | 88,332 | -58.4% 🟥 |
| Altered | Walapane `LK-2309` | Nuwara Eliya `LK-23` | 104,119 | 65,287 | -37.3% 🟥 |
| New | Kothmale West `LK-2304` | Nuwara Eliya `LK-23` | — | 41,955 | — |
| New | Mathurata `LK-2307` | Nuwara Eliya `LK-23` | — | 33,175 | — |
| New | Nildandahinna `LK-2310` | Nuwara Eliya `LK-23` | — | 42,422 | — |
| New | Norwood `LK-2316` | Nuwara Eliya `LK-23` | — | 161,367 | — |
| New | Thalawakele `LK-2313` | Nuwara Eliya `LK-23` | — | 129,531 | — |
| Altered | Balangoda `LK-9118` | Ratnapura `LK-91` | 81,563 | 74,893 | -8.2% 🟥 |
| Altered | Eheliyagoda `LK-9103` | Ratnapura `LK-91` | 88,022 | 74,071 | -15.8% 🟥 |
| Altered | Kuruvita `LK-9106` | Ratnapura `LK-91` | 75,104 | 97,966 | +30.4% 🟩 |
| New | Kalthota `LK-9119` | Ratnapura `LK-91` | — | 13,018 | — |

---

## A5. Largest Change in Religious Proportion by DSD

For each DSD, the religion whose share of the local population changed most between 2012 and 2024, showing only rows with absolute change > 1%.

*Altered, new, and removed DSDs excluded. Religions with <1% of national count or <1,000 people in the DSD are excluded.*

### Buddhist

| DSD | District | Share 2012 | Share 2024 | Change (pp) |
|---|---|---:|---:|---:|
| Kaduwela `LK-1109` | Colombo `LK-11` | 90.4% | 92.3% | +1.9pp 🟩 |
| Gampaha `LK-1224` | Gampaha `LK-12` | 87.6% | 88.8% | +1.2pp 🟩 |
| Maharagama `LK-1121` | Colombo `LK-11` | 92.0% | 93.2% | +1.2pp 🟩 |

### Hindu

| DSD | District | Share 2012 | Share 2024 | Change (pp) |
|---|---|---:|---:|---:|
| Wattala `LK-1218` | Gampaha `LK-12` | 13.0% | 16.9% | +3.9pp 🟩 |
| Vadamaradchi North (Point Pedro) `LK-4127` | Jaffna `LK-41` | 83.9% | 86.4% | +2.5pp 🟩 |
| Thimbirigasyaya `LK-1127` | Colombo `LK-11` | 22.5% | 24.4% | +1.9pp 🟩 |
| Colombo `LK-1103` | Colombo `LK-11` | 22.7% | 24.6% | +1.9pp 🟩 |
| Manmunai South & Eruvil Pattu `LK-5136` | Batticaloa `LK-51` | 93.9% | 95.4% | +1.4pp 🟩 |
| Karachchi `LK-4509` | Kilinochchi `LK-45` | 83.1% | 81.4% | -1.7pp 🟥 |
| Vavuniya `LK-4309` | Vavuniya `LK-43` | 78.3% | 75.8% | -2.5pp 🟥 |
| Nallur `LK-4133` | Jaffna `LK-41` | 90.4% | 85.9% | -4.5pp 🟥 |
| Puthukkudiyiruppu `LK-4409` | Mullaitivu `LK-44` | 84.8% | 78.6% | -6.2pp 🟥 |

### Islam

| DSD | District | Share 2012 | Share 2024 | Change (pp) |
|---|---|---:|---:|---:|
| Kolonnawa `LK-1106` | Colombo `LK-11` | 23.1% | 31.3% | +8.3pp 🟩 |
| Dehiwala `LK-1130` | Colombo `LK-11` | 22.6% | 30.4% | +7.8pp 🟩 |
| Galle 4 Gravets `LK-3139` | Galle `LK-31` | 32.3% | 36.0% | +3.7pp 🟩 |
| Beruwala `LK-1324` | Kalutara `LK-13` | 34.7% | 38.2% | +3.5pp 🟩 |
| Mundel `LK-6218` | Puttalam `LK-62` | 38.6% | 41.9% | +3.3pp 🟩 |
| Akurana `LK-2109` | Kandy `LK-21` | 64.9% | 67.9% | +3.0pp 🟩 |
| Negombo `LK-1203` | Gampaha `LK-12` | 14.3% | 17.2% | +2.9pp 🟩 |
| Mawanella `LK-9206` | Kegalle `LK-92` | 30.4% | 33.3% | +2.8pp 🟩 |
| Panadura `LK-1303` | Kalutara `LK-13` | 14.4% | 17.2% | +2.8pp 🟩 |
| Puttalam `LK-6215` | Puttalam `LK-62` | 64.2% | 66.6% | +2.4pp 🟩 |
| Attanagalla `LK-1227` | Gampaha `LK-12` | 12.4% | 14.4% | +1.9pp 🟩 |
| Udunuwara `LK-2139` | Kandy `LK-21` | 24.5% | 26.4% | +1.9pp 🟩 |
| Udapalatha `LK-2151` | Kandy `LK-21` | 22.7% | 24.4% | +1.8pp 🟩 |
| Kuchchaweli `LK-5306` | Trincomalee `LK-53` | 64.1% | 65.8% | +1.7pp 🟩 |
| Muthur `LK-5327` | Trincomalee `LK-53` | 62.0% | 63.5% | +1.5pp 🟩 |
| Kinniya `LK-5324` | Trincomalee `LK-53` | 95.8% | 97.1% | +1.4pp 🟩 |
| Koralai Pattu Central `LK-5104` | Batticaloa `LK-51` | 97.2% | 0.3% | -96.9pp 🟥 |

### RomanCatholic

| DSD | District | Share 2012 | Share 2024 | Change (pp) |
|---|---|---:|---:|---:|
| Katana `LK-1206` | Gampaha `LK-12` | 32.0% | 34.0% | +1.9pp 🟩 |
| Kalpitiya `LK-6203` | Puttalam `LK-62` | 32.3% | 33.6% | +1.4pp 🟩 |
| Mahara `LK-1233` | Gampaha `LK-12` | 8.8% | 7.6% | -1.2pp 🟥 |
| Chilaw `LK-6233` | Puttalam `LK-62` | 45.7% | 44.4% | -1.3pp 🟥 |
| Mahawewa `LK-6239` | Puttalam `LK-62` | 51.8% | 50.4% | -1.4pp 🟥 |
| Manmunai North `LK-5118` | Batticaloa `LK-51` | 19.0% | 17.4% | -1.6pp 🟥 |
| Dankotuwa `LK-6248` | Puttalam `LK-62` | 29.8% | 27.9% | -1.9pp 🟥 |
| Nanaddan `LK-4212` | Mannar `LK-42` | 68.4% | 66.4% | -2.0pp 🟥 |
| Kelaniya `LK-1236` | Gampaha `LK-12` | 9.8% | 7.7% | -2.1pp 🟥 |
| Jaffna `LK-4136` | Jaffna `LK-41` | 52.9% | 50.6% | -2.3pp 🟥 |
| Nattandiya `LK-6242` | Puttalam `LK-62` | 40.6% | 38.2% | -2.4pp 🟥 |
| Mannar Town `LK-4203` | Mannar `LK-42` | 54.8% | 50.6% | -4.1pp 🟥 |

### OtherChristian

| DSD | District | Share 2012 | Share 2024 | Change (pp) |
|---|---|---:|---:|---:|
| Koralai Pattu North `LK-5103` | Batticaloa `LK-51` | 12.1% | 13.5% | +1.4pp 🟩 |
| Sri Jayawardanapura Kotte `LK-1124` | Colombo `LK-11` | 4.7% | 3.5% | -1.2pp 🟥 |

---

## A6. Religion by Province: Key Trends

![A6 province change maps](analyses/a6_by_province/chart.png)

Province labels show the **province name** and **change in share of population (pp)**. Provinces are shaded by **change in share of population (pp)** from **red (decline)** to **green (growth)**. Provinces with religion population **< 1,000 (2024)** are shown in **grey**.

### Buddhist

| Province | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Uva `LK-8` | 7.5% | 1,018,561 | 1,135,424 | +116,863 🟩 | 80.4% | 81.1% | +0.7 🟩 pp |
| Western `LK-1` | 29.7% | 4,293,801 | 4,507,637 | +213,836 🟩 | 73.4% | 73.7% | +0.3 🟩 pp |
| North Western `LK-6` | 12.6% | 1,760,663 | 1,918,702 | +158,039 🟩 | 74.0% | 74.2% | +0.2 🟩 pp |
| Northern `LK-4` | 0.2% | 30,191 | 33,288 | +3,097 🟩 | 2.8% | 2.9% | 0.0 pp |
| Sabaragamuwa `LK-9` | 11.4% | 1,653,381 | 1,728,611 | +75,230 🟩 | 85.7% | 85.7% | 0.0 pp |
| Central `LK-2` | 11.6% | 1,672,625 | 1,760,947 | +88,322 🟩 | 65.0% | 64.9% | -0.2 🟥 pp |
| Southern `LK-3` | 16.2% | 2,345,314 | 2,463,070 | +117,756 🟩 | 94.7% | 94.5% | -0.2 🟥 pp |
| North Central `LK-7` | 8.3% | 1,139,595 | 1,262,295 | +122,700 🟩 | 90.0% | 89.7% | -0.3 🟥 pp |
| Eastern `LK-5` | 2.6% | 357,052 | 389,119 | +32,067 🟩 | 23.0% | 21.8% | -1.1 🟥 pp |

***Uva** gained the most share at **+0.7pp**. **Eastern** saw the steepest share decline at **-1.1pp**. **Western** had the largest absolute increase (**+213,836**).*

### Hindu

| Province | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Western `LK-1` | 11.3% | 278,817 | 309,716 | +30,899 🟩 | 4.8% | 5.1% | +0.3 🟩 pp |
| North Central `LK-7` | 0.4% | 10,117 | 10,970 | +853 🟩 | 0.8% | 0.8% | 0.0 pp |
| North Western `LK-6` | 1.7% | 43,527 | 46,319 | +2,792 🟩 | 1.8% | 1.8% | 0.0 pp |
| Central `LK-2` | 20.8% | 540,339 | 568,065 | +27,726 🟩 | 21.0% | 20.9% | -0.1 🟥 pp |
| Southern `LK-3` | 1.2% | 33,227 | 31,626 | -1,601 🟥 | 1.3% | 1.2% | -0.1 🟥 pp |
| Sabaragamuwa `LK-9` | 5.9% | 156,312 | 160,082 | +3,770 🟩 | 8.1% | 7.9% | -0.2 🟥 pp |
| Uva `LK-8` | 6.6% | 169,605 | 181,354 | +11,749 🟩 | 13.4% | 13.0% | -0.4 🟥 pp |
| Eastern `LK-5` | 21.8% | 540,153 | 597,472 | +57,319 🟩 | 34.7% | 33.5% | -1.2 🟥 pp |
| Northern `LK-4` | 30.3% | 789,045 | 829,235 | +40,190 🟩 | 74.4% | 72.1% | -2.3 🟥 pp |

***Western** gained the most share at **+0.3pp**. **Northern** saw the steepest share decline at **-2.3pp**. **Eastern** had the largest absolute increase (**+57,319**).*

### Islam

| Province | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Eastern `LK-5` | 30.2% | 575,470 | 707,054 | +131,584 🟩 | 37.0% | 39.7% | +2.7 🟩 pp |
| Northern `LK-4` | 2.6% | 33,427 | 60,683 | +27,256 🟩 | 3.1% | 5.3% | +2.1 🟩 pp |
| North Western `LK-6` | 13.7% | 268,214 | 320,262 | +52,048 🟩 | 11.3% | 12.4% | +1.1 🟩 pp |
| Western `LK-1` | 24.4% | 501,369 | 571,074 | +69,705 🟩 | 8.6% | 9.3% | +0.8 🟩 pp |
| Central `LK-2` | 12.8% | 263,874 | 298,150 | +34,276 🟩 | 10.3% | 11.0% | +0.7 🟩 pp |
| North Central `LK-7` | 5.2% | 101,958 | 121,076 | +19,118 🟩 | 8.0% | 8.6% | +0.6 🟩 pp |
| Sabaragamuwa `LK-9` | 4.3% | 85,610 | 99,412 | +13,802 🟩 | 4.4% | 4.9% | +0.5 🟩 pp |
| Southern `LK-3` | 4.0% | 80,085 | 93,843 | +13,758 🟩 | 3.2% | 3.6% | +0.4 🟩 pp |
| Uva `LK-8` | 2.8% | 57,001 | 65,825 | +8,824 🟩 | 4.5% | 4.7% | +0.2 🟩 pp |

***Eastern** gained the most share at **+2.7pp**. **Uva** had the smallest share gain at **+0.2pp**.*

### Roman Catholic

| Province | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Southern `LK-3` | 0.6% | 7,986 | 7,669 | -317 🟥 | 0.3% | 0.3% | 0.0 pp |
| Northern `LK-4` | 14.4% | 164,320 | 176,123 | +11,803 🟩 | 15.5% | 15.3% | -0.2 🟥 pp |
| North Central `LK-7` | 0.7% | 9,939 | 8,320 | -1,619 🟥 | 0.8% | 0.6% | -0.2 🟥 pp |
| Sabaragamuwa `LK-9` | 1.3% | 19,621 | 15,899 | -3,722 🟥 | 1.0% | 0.8% | -0.2 🟥 pp |
| Uva `LK-8` | 0.9% | 13,621 | 10,774 | -2,847 🟥 | 1.1% | 0.8% | -0.3 🟥 pp |
| Eastern `LK-5` | 3.9% | 46,535 | 47,507 | +972 🟩 | 3.0% | 2.7% | -0.3 🟥 pp |
| Central `LK-2` | 4.7% | 63,754 | 58,125 | -5,629 🟥 | 2.5% | 2.1% | -0.3 🟥 pp |
| Western `LK-1` | 50.5% | 651,432 | 618,683 | -32,749 🟥 | 11.1% | 10.1% | -1.0 🟥 pp |
| North Western `LK-6` | 23.0% | 283,928 | 281,248 | -2,680 🟥 | 11.9% | 10.9% | -1.1 🟥 pp |

***North Western** saw the steepest share decline at **-1.1pp**. **Northern** had the largest absolute increase (**+11,803**).*

### Other Christian

| Province | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Northern `LK-4` | 18.0% | 43,899 | 50,701 | +6,802 🟩 | 4.1% | 4.4% | +0.3 🟩 pp |
| Eastern `LK-5` | 14.9% | 36,148 | 41,928 | +5,780 🟩 | 2.3% | 2.4% | 0.0 pp |
| Southern `LK-3` | 3.6% | 10,215 | 10,243 | +28 🟩 | 0.4% | 0.4% | 0.0 pp |
| North Central `LK-7` | 1.7% | 4,936 | 4,742 | -194 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Sabaragamuwa `LK-9` | 4.2% | 13,598 | 11,781 | -1,817 🟥 | 0.7% | 0.6% | -0.1 🟥 pp |
| Uva `LK-8` | 2.3% | 7,474 | 6,442 | -1,032 🟥 | 0.6% | 0.5% | -0.1 🟥 pp |
| Central `LK-2` | 10.1% | 30,648 | 28,419 | -2,229 🟥 | 1.2% | 1.0% | -0.1 🟥 pp |
| North Western `LK-6` | 7.1% | 22,019 | 20,032 | -1,987 🟥 | 0.9% | 0.8% | -0.2 🟥 pp |
| Western `LK-1` | 38.2% | 121,983 | 107,897 | -14,086 🟥 | 2.1% | 1.8% | -0.3 🟥 pp |

***Northern** gained the most share at **+0.3pp**. **Western** saw the steepest share decline at **-0.3pp**.*

### Other

| Province | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| North Central `LK-7` | 5.2% | 118 | 207 | +89 🟩 | 0.0% | 0.0% | 0.0 pp |
| Central `LK-2` | 8.6% | 317 | 339 | +22 🟩 | 0.0% | 0.0% | 0.0 pp |
| Sabaragamuwa `LK-9` | 2.9% | 133 | 114 | -19 🟥 | 0.0% | 0.0% | 0.0 pp |
| Eastern `LK-5` | 3.4% | 152 | 134 | -18 🟥 | 0.0% | 0.0% | 0.0 pp |
| Southern `LK-3` | 5.8% | 458 | 228 | -230 🟥 | 0.0% | 0.0% | 0.0 pp |
| Uva `LK-8` | 1.8% | 201 | 73 | -128 🟥 | 0.0% | 0.0% | 0.0 pp |
| Western `LK-1` | 59.0% | 3,343 | 2,334 | -1,009 🟥 | 0.1% | 0.0% | 0.0 pp |
| Northern `LK-4` | 3.0% | 333 | 118 | -215 🟥 | 0.0% | 0.0% | 0.0 pp |
| North Western `LK-6` | 10.3% | 1,332 | 409 | -923 🟥 | 0.1% | 0.0% | 0.0 pp |

***North Central** gained the most share at **0.0pp**. **North Western** saw the steepest share decline at **0.0pp**.*

---

## A7. Religion by DSD: Key Trends

![A7 DSD change maps](analyses/a7_by_dsd/chart.png)

DSDs are shaded by **change in share of population (pp)** from **red (decline)** to **green (growth)**. DSD labels are omitted due to map density. DSDs with religion population **< 1,000 (2024)** are shown in **grey**.

*New, removed, and altered DSDs from A4 are excluded to avoid boundary-change artifacts.*

### Buddhist

| DSD | District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Vavuniya North `LK-4303` | Vavuniya | 0.0% | 511 | 1,149 | +638 🟩 | 4.4% | 7.8% | +3.4 🟩 pp |
| Haldummulla `LK-8142` | Badulla | 0.1% | 19,698 | 21,455 | +1,757 🟩 | 52.4% | 55.3% | +2.9 🟩 pp |
| Kotapola `LK-3206` | Matara | 0.4% | 51,188 | 50,977 | -211 🟥 | 80.9% | 83.6% | +2.6 🟩 pp |
| Kalawana `LK-9133` | Ratnapura | 0.3% | 43,847 | 44,599 | +752 🟩 | 85.5% | 87.9% | +2.4 🟩 pp |
| Meegahakiula `LK-8109` | Badulla | 0.1% | 17,640 | 20,824 | +3,184 🟩 | 89.5% | 91.8% | +2.3 🟩 pp |
| Karuwalagaswewa `LK-6209` | Puttalam | 0.2% | 21,391 | 24,542 | +3,151 🟩 | 91.3% | 93.6% | +2.3 🟩 pp |
| Rambewa `LK-7118` | Anuradhapura | 0.2% | 30,904 | 34,412 | +3,508 🟩 | 84.0% | 86.3% | +2.3 🟩 pp |
| Chilaw `LK-6233` | Puttalam | 0.2% | 22,855 | 24,717 | +1,862 🟩 | 36.6% | 38.8% | +2.3 🟩 pp |
| Dankotuwa `LK-6248` | Puttalam | 0.3% | 41,674 | 43,375 | +1,701 🟩 | 66.8% | 69.0% | +2.2 🟩 pp |
| Nallur `LK-4133` | Jaffna | 0.0% | 273 | 1,718 | +1,445 🟩 | 0.4% | 2.4% | +2.0 🟩 pp |
| Kaduwela `LK-1109` | Colombo | 1.8% | 227,939 | 256,548 | +28,609 🟩 | 90.4% | 92.3% | +1.9 🟩 pp |
| Mahawewa `LK-6239` | Puttalam | 0.2% | 23,204 | 23,033 | -171 🟥 | 45.4% | 47.2% | +1.7 🟩 pp |
| Koralai Pattu Central `LK-5104` | Batticaloa | 0.0% | 67 | 569 | +502 🟩 | 0.3% | 2.0% | +1.7 🟩 pp |
| Kuchchaweli `LK-5306` | Trincomalee | 0.0% | 783 | 1,534 | +751 🟩 | 2.4% | 3.8% | +1.5 🟩 pp |
| Laggala `LK-2224` | Matale | 0.1% | 11,897 | 16,253 | +4,356 🟩 | 98.2% | 99.7% | +1.5 🟩 pp |
| Gangawata Korale `LK-2130` | Kandy | 0.8% | 112,495 | 110,984 | -1,511 🟥 | 70.9% | 72.4% | +1.4 🟩 pp |
| Madampe `LK-6236` | Puttalam | 0.2% | 34,803 | 36,282 | +1,479 🟩 | 72.6% | 74.1% | +1.4 🟩 pp |
| Kurunegala `LK-6154` | Kurunegala | 0.5% | 64,117 | 71,927 | +7,810 🟩 | 79.4% | 80.8% | +1.4 🟩 pp |
| Ayagama `LK-9130` | Ratnapura | 0.2% | 26,626 | 26,217 | -409 🟥 | 86.2% | 87.6% | +1.4 🟩 pp |
| Gampaha `LK-1224` | Gampaha | 1.3% | 173,095 | 182,606 | +9,511 🟩 | 87.6% | 88.8% | +1.2 🟩 pp |
| Thawalama `LK-3118` | Galle | 0.2% | 30,335 | 29,207 | -1,128 🟥 | 93.0% | 94.2% | +1.2 🟩 pp |
| Maharagama `LK-1121` | Colombo | 1.3% | 180,631 | 183,093 | +2,462 🟩 | 92.0% | 93.2% | +1.2 🟩 pp |
| Nuwaragam Palatha East `LK-7133` | Anuradhapura | 0.5% | 64,681 | 71,538 | +6,857 🟩 | 92.7% | 94.0% | +1.2 🟩 pp |
| Pitabaddara `LK-3203` | Matara | 0.3% | 47,583 | 45,984 | -1,599 🟥 | 93.0% | 94.1% | +1.1 🟩 pp |
| Nivithigala `LK-9136` | Ratnapura | 0.3% | 49,161 | 49,271 | +110 🟩 | 81.8% | 82.9% | +1.1 🟩 pp |
| Imbulpe `LK-9115` | Ratnapura | 0.4% | 50,082 | 55,075 | +4,993 🟩 | 84.2% | 85.3% | +1.1 🟩 pp |
| Katharagama `LK-8227` | Monaragala | 0.1% | 17,342 | 17,477 | +135 🟩 | 95.2% | 96.2% | +1.1 🟩 pp |
| Lunugamwehera `LK-3306` | Hambantota | 0.2% | 30,516 | 36,059 | +5,543 🟩 | 96.7% | 97.7% | +1.0 🟩 pp |
| Arachchikattuwa `LK-6230` | Puttalam | 0.2% | 24,853 | 26,320 | +1,467 🟩 | 60.6% | 61.6% | +1.0 🟩 pp |
| Elapatha `LK-9127` | Ratnapura | 0.3% | 35,614 | 36,520 | +906 🟩 | 94.1% | 95.0% | +0.9 🟩 pp |
| Palindanuwara `LK-1336` | Kalutara | 0.3% | 45,795 | 46,610 | +815 🟩 | 90.1% | 91.1% | +0.9 🟩 pp |
| Opanayake `LK-9121` | Ratnapura | 0.2% | 24,284 | 25,134 | +850 🟩 | 91.3% | 92.3% | +0.9 🟩 pp |
| Wennappuwa `LK-6245` | Puttalam | 0.1% | 12,278 | 12,250 | -28 🟥 | 18.0% | 18.9% | +0.9 🟩 pp |
| Manmunai South West `LK-5130` | Batticaloa | 0.0% | 1,039 | 1,349 | +310 🟩 | 4.2% | 5.1% | +0.9 🟩 pp |
| Nattandiya `LK-6242` | Puttalam | 0.2% | 28,213 | 30,286 | +2,073 🟩 | 45.4% | 46.2% | +0.8 🟩 pp |
| Jaffna `LK-4136` | Jaffna | 0.0% | 136 | 529 | +393 🟩 | 0.3% | 1.1% | +0.8 🟩 pp |
| Pasbagekorale `LK-2157` | Kandy | 0.2% | 27,943 | 31,091 | +3,148 🟩 | 46.6% | 47.4% | +0.8 🟩 pp |
| Nachchaduwa `LK-7136` | Anuradhapura | 0.2% | 21,801 | 24,506 | +2,705 🟩 | 85.9% | 86.7% | +0.8 🟩 pp |
| Mahara `LK-1233` | Gampaha | 1.3% | 176,491 | 191,215 | +14,724 🟩 | 84.9% | 85.7% | +0.8 🟩 pp |
| Uvaparanagama `LK-8127` | Badulla | 0.5% | 65,338 | 69,390 | +4,052 🟩 | 83.8% | 84.6% | +0.8 🟩 pp |
| Higurakgoda `LK-7203` | Polonnaruwa | 0.5% | 62,071 | 68,762 | +6,691 🟩 | 96.5% | 97.3% | +0.8 🟩 pp |
| Pallepola `LK-2212` | Matale | 0.2% | 27,223 | 29,369 | +2,146 🟩 | 92.1% | 92.9% | +0.8 🟩 pp |
| Karachchi `LK-4509` | Kilinochchi | 0.0% | 747 | 1,482 | +735 🟩 | 1.2% | 2.0% | +0.8 🟩 pp |
| Dodangoda `LK-1327` | Kalutara | 0.4% | 55,657 | 58,894 | +3,237 🟩 | 87.0% | 87.8% | +0.8 🟩 pp |
| Ampara `LK-5215` | Ampara | 0.3% | 42,584 | 46,871 | +4,287 🟩 | 97.2% | 97.9% | +0.8 🟩 pp |
| Kandeketiya `LK-8112` | Badulla | 0.2% | 21,654 | 25,458 | +3,804 🟩 | 93.8% | 94.6% | +0.8 🟩 pp |
| Sri Jayawardanapura Kotte `LK-1124` | Colombo | 0.5% | 83,139 | 74,848 | -8,291 🟥 | 77.1% | 77.8% | +0.7 🟩 pp |
| Bingiriya `LK-6142` | Kurunegala | 0.4% | 53,272 | 57,503 | +4,231 🟩 | 85.4% | 86.2% | +0.7 🟩 pp |
| Dehiattakandiya `LK-5203` | Ampara | 0.5% | 59,492 | 66,971 | +7,479 🟩 | 98.9% | 99.5% | +0.7 🟩 pp |
| Yakkalamulla `LK-3148` | Galle | 0.3% | 42,941 | 43,954 | +1,013 🟩 | 93.5% | 94.1% | +0.7 🟩 pp |
| Nawagattegama `LK-6212` | Puttalam | 0.1% | 14,239 | 17,390 | +3,151 🟩 | 98.3% | 99.0% | +0.7 🟩 pp |
| Soranathota `LK-8115` | Badulla | 0.1% | 18,082 | 19,709 | +1,627 🟩 | 80.1% | 80.8% | +0.6 🟩 pp |
| Doluwa `LK-2142` | Kandy | 0.3% | 36,702 | 39,190 | +2,488 🟩 | 73.6% | 74.2% | +0.6 🟩 pp |
| Kegalle `LK-9212` | Kegalle | 0.6% | 85,380 | 89,192 | +3,812 🟩 | 94.0% | 94.6% | +0.6 🟩 pp |
| Udubaddawa `LK-6175` | Kurunegala | 0.3% | 38,640 | 40,616 | +1,976 🟩 | 74.0% | 74.6% | +0.6 🟩 pp |
| Thissamaharama `LK-3309` | Hambantota | 0.5% | 65,858 | 71,643 | +5,785 🟩 | 96.0% | 96.6% | +0.6 🟩 pp |
| Kolonna `LK-9151` | Ratnapura | 0.3% | 41,370 | 45,356 | +3,986 🟩 | 90.0% | 90.6% | +0.6 🟩 pp |
| Ja Ela `LK-1221` | Gampaha | 0.6% | 87,772 | 90,297 | +2,525 🟩 | 43.6% | 44.1% | +0.5 🟩 pp |
| Bulathkohipitiya `LK-9224` | Kegalle | 0.3% | 38,623 | 37,337 | -1,286 🟥 | 82.0% | 82.5% | +0.5 🟩 pp |
| Hatharaliyadda `LK-2134` | Kandy | 0.2% | 27,862 | 29,096 | +1,234 🟩 | 92.9% | 93.4% | +0.5 🟩 pp |
| Dompe `LK-1230` | Gampaha | 1.1% | 145,586 | 161,461 | +15,875 🟩 | 94.5% | 95.0% | +0.5 🟩 pp |
| Mundel `LK-6218` | Puttalam | 0.1% | 10,264 | 12,452 | +2,188 🟩 | 16.7% | 17.2% | +0.5 🟩 pp |
| Anamaduwa `LK-6224` | Puttalam | 0.3% | 35,961 | 41,078 | +5,117 🟩 | 93.9% | 94.4% | +0.4 🟩 pp |
| Minuwangoda `LK-1215` | Gampaha | 1.2% | 157,739 | 176,692 | +18,953 🟩 | 88.5% | 88.9% | +0.4 🟩 pp |
| Yatinuwara `LK-2136` | Kandy | 0.7% | 94,149 | 100,496 | +6,347 🟩 | 88.8% | 89.2% | +0.4 🟩 pp |
| Ganga Ihala Korale `LK-2154` | Kandy | 0.3% | 44,364 | 47,735 | +3,371 🟩 | 80.3% | 80.7% | +0.4 🟩 pp |
| Wellawaya `LK-8221` | Monaragala | 0.5% | 58,180 | 71,292 | +13,112 🟩 | 96.9% | 97.3% | +0.4 🟩 pp |
| Deraniyagala `LK-9233` | Kegalle | 0.2% | 35,862 | 34,585 | -1,277 🟥 | 78.2% | 78.6% | +0.4 🟩 pp |
| Ambanpola `LK-6112` | Kurunegala | 0.2% | 22,314 | 24,990 | +2,676 🟩 | 97.5% | 97.9% | +0.4 🟩 pp |
| Pelmadulla `LK-9124` | Ratnapura | 0.6% | 76,321 | 80,404 | +4,083 🟩 | 85.3% | 85.7% | +0.4 🟩 pp |
| Puttalam `LK-6215` | Puttalam | 0.1% | 15,027 | 17,652 | +2,625 🟩 | 18.2% | 18.6% | +0.4 🟩 pp |
| Padaviya `LK-7103` | Anuradhapura | 0.2% | 22,724 | 24,293 | +1,569 🟩 | 98.8% | 99.2% | +0.4 🟩 pp |
| Mahakumbukkadawala `LK-6221` | Puttalam | 0.1% | 15,857 | 18,690 | +2,833 🟩 | 85.1% | 85.5% | +0.4 🟩 pp |
| Thalawa `LK-7148` | Anuradhapura | 0.4% | 56,554 | 60,125 | +3,571 🟩 | 97.9% | 98.2% | +0.4 🟩 pp |
| Dambulla `LK-2206` | Matale | 0.5% | 68,323 | 77,050 | +8,727 🟩 | 94.5% | 94.8% | +0.4 🟩 pp |
| Town & Gravets `LK-5315` | Trincomalee | 0.1% | 20,197 | 21,115 | +918 🟩 | 20.7% | 21.1% | +0.3 🟩 pp |
| Nagoda `LK-3124` | Galle | 0.3% | 49,306 | 47,836 | -1,470 🟥 | 91.6% | 91.9% | +0.3 🟩 pp |
| Kesbewa `LK-1136` | Colombo | 1.7% | 228,138 | 246,021 | +17,883 🟩 | 93.0% | 93.4% | +0.3 🟩 pp |
| Homagama `LK-1112` | Colombo | 1.9% | 228,829 | 270,923 | +42,094 🟩 | 96.2% | 96.5% | +0.3 🟩 pp |
| Tangalle `LK-3333` | Hambantota | 0.5% | 70,859 | 77,974 | +7,115 🟩 | 97.7% | 98.0% | +0.3 🟩 pp |
| Moratuwa `LK-1133` | Colombo | 0.8% | 114,784 | 109,743 | -5,041 🟥 | 68.2% | 68.5% | +0.3 🟩 pp |
| Kiriella `LK-9109` | Ratnapura | 0.2% | 34,638 | 32,480 | -2,158 🟥 | 96.3% | 96.6% | +0.3 🟩 pp |
| Elpitiya `LK-3112` | Galle | 0.4% | 62,688 | 64,758 | +2,070 🟩 | 96.9% | 97.1% | +0.3 🟩 pp |
| Mahaoya `LK-5209` | Ampara | 0.2% | 20,691 | 23,625 | +2,934 🟩 | 99.3% | 99.6% | +0.3 🟩 pp |
| Divulapitiya `LK-1209` | Gampaha | 0.9% | 122,905 | 133,909 | +11,004 🟩 | 85.1% | 85.3% | +0.3 🟩 pp |
| Agalawatta `LK-1333` | Kalutara | 0.2% | 35,475 | 35,487 | +12 🟩 | 96.7% | 97.0% | +0.2 🟩 pp |
| Nuwaragam Palatha Central `LK-7115` | Anuradhapura | 0.4% | 54,331 | 63,651 | +9,320 🟩 | 88.7% | 89.0% | +0.2 🟩 pp |
| Rambukkana `LK-9203` | Kegalle | 0.5% | 75,323 | 79,429 | +4,106 🟩 | 91.0% | 91.2% | +0.2 🟩 pp |
| Thambuththegama `LK-7145` | Anuradhapura | 0.3% | 41,073 | 45,654 | +4,581 🟩 | 96.8% | 97.0% | +0.2 🟩 pp |
| Padiyathalawa `LK-5206` | Ampara | 0.1% | 18,141 | 20,711 | +2,570 🟩 | 99.2% | 99.4% | +0.2 🟩 pp |
| Ududumbara `LK-2118` | Kandy | 0.1% | 20,574 | 21,119 | +545 🟩 | 91.4% | 91.6% | +0.2 🟩 pp |
| Buttala `LK-8224` | Monaragala | 0.4% | 52,042 | 59,547 | +7,505 🟩 | 98.0% | 98.3% | +0.2 🟩 pp |
| Padavi Sri Pura `LK-5303` | Trincomalee | 0.1% | 11,697 | 11,918 | +221 🟩 | 98.4% | 98.7% | +0.2 🟩 pp |
| Nochchiyagama `LK-7139` | Anuradhapura | 0.4% | 46,917 | 52,281 | +5,364 🟩 | 94.0% | 94.2% | +0.2 🟩 pp |
| Lahugala `LK-5251` | Ampara | 0.1% | 8,293 | 9,711 | +1,418 🟩 | 93.0% | 93.2% | +0.2 🟩 pp |
| Kuliyapitiya West `LK-6172` | Kurunegala | 0.5% | 69,513 | 74,412 | +4,899 🟩 | 89.9% | 90.1% | +0.2 🟩 pp |
| Weerabugedara `LK-6166` | Kurunegala | 0.2% | 33,276 | 35,523 | +2,247 🟩 | 96.9% | 97.1% | +0.2 🟩 pp |
| Dimbulagala `LK-7212` | Polonnaruwa | 0.6% | 76,487 | 82,634 | +6,147 🟩 | 96.0% | 96.2% | +0.2 🟩 pp |
| Nikaweratiya `LK-6121` | Kurunegala | 0.3% | 37,994 | 40,838 | +2,844 🟩 | 93.9% | 94.1% | +0.2 🟩 pp |
| Bentota `LK-3103` | Galle | 0.3% | 48,544 | 48,312 | -232 🟥 | 97.1% | 97.3% | +0.2 🟩 pp |
| Galigamuwa `LK-9215` | Kegalle | 0.5% | 70,040 | 69,494 | -546 🟥 | 94.0% | 94.2% | +0.2 🟩 pp |
| Weligepola `LK-9145` | Ratnapura | 0.2% | 30,577 | 33,774 | +3,197 🟩 | 98.7% | 98.8% | +0.2 🟩 pp |
| Millaniya `LK-1318` | Kalutara | 0.4% | 50,122 | 54,041 | +3,919 🟩 | 96.1% | 96.2% | +0.2 🟩 pp |
| Wariyapola `LK-6136` | Kurunegala | 0.4% | 59,466 | 64,464 | +4,998 🟩 | 96.8% | 97.0% | +0.1 🟩 pp |
| Rideemaliyadda `LK-8106` | Badulla | 0.4% | 51,351 | 60,652 | +9,301 🟩 | 99.5% | 99.6% | +0.1 🟩 pp |
| Padukka `LK-1118` | Colombo | 0.5% | 61,756 | 69,188 | +7,432 🟩 | 94.6% | 94.8% | +0.1 🟩 pp |
| Minipe `LK-2121` | Kandy | 0.4% | 51,422 | 54,927 | +3,505 🟩 | 99.1% | 99.3% | +0.1 🟩 pp |
| Mahawilachchiya `LK-7112` | Anuradhapura | 0.2% | 22,209 | 23,947 | +1,738 🟩 | 98.9% | 99.0% | +0.1 🟩 pp |
| Damana `LK-5242` | Ampara | 0.3% | 38,312 | 39,977 | +1,665 🟩 | 99.0% | 99.1% | +0.1 🟩 pp |
| Pathahewaheta `LK-2145` | Kandy | 0.4% | 52,105 | 54,367 | +2,262 🟩 | 89.5% | 89.7% | +0.1 🟩 pp |
| Madulla `LK-8206` | Monaragala | 0.2% | 31,062 | 36,280 | +5,218 🟩 | 99.4% | 99.5% | +0.1 🟩 pp |
| Beliatta `LK-3330` | Hambantota | 0.4% | 55,746 | 58,480 | +2,734 🟩 | 99.6% | 99.7% | +0.1 🟩 pp |
| Kalpitiya `LK-6203` | Puttalam | 0.0% | 5,547 | 6,329 | +782 🟩 | 6.4% | 6.5% | +0.1 🟩 pp |
| Embilipitiya `LK-9148` | Ratnapura | 1.1% | 134,041 | 159,374 | +25,333 🟩 | 99.5% | 99.6% | +0.1 🟩 pp |
| Sammanthurai `LK-5218` | Ampara | 0.0% | 392 | 539 | +147 🟩 | 0.6% | 0.7% | +0.1 🟩 pp |
| Alawwa `LK-6184` | Kurunegala | 0.4% | 63,075 | 65,134 | +2,059 🟩 | 99.1% | 99.2% | +0.1 🟩 pp |
| Mahiyanganaya `LK-8103` | Badulla | 0.6% | 73,410 | 86,376 | +12,966 🟩 | 96.9% | 97.0% | +0.1 🟩 pp |
| Madurawala `LK-1315` | Kalutara | 0.2% | 31,384 | 33,551 | +2,167 🟩 | 91.3% | 91.4% | +0.1 🟩 pp |
| Manmunai Pattu `LK-5127` | Batticaloa | 0.0% | 63 | 101 | +38 🟩 | 0.2% | 0.3% | +0.1 🟩 pp |
| Vavuniya `LK-4309` | Vavuniya | 0.0% | 3,084 | 3,151 | +67 🟩 | 2.6% | 2.7% | +0.1 🟩 pp |
| Polpitigama `LK-6127` | Kurunegala | 0.6% | 75,509 | 85,752 | +10,243 🟩 | 99.2% | 99.2% | +0.1 🟩 pp |
| Narammala `LK-6181` | Kurunegala | 0.4% | 51,763 | 55,045 | +3,282 🟩 | 92.0% | 92.0% | +0.1 🟩 pp |
| Vanathavilluwa `LK-6206` | Puttalam | 0.1% | 6,826 | 7,828 | +1,002 🟩 | 39.1% | 39.2% | +0.1 🟩 pp |
| Bibile `LK-8203` | Monaragala | 0.3% | 38,222 | 44,824 | +6,602 🟩 | 94.8% | 94.8% | +0.1 🟩 pp |
| Bope-Poddala `LK-3142` | Galle | 0.4% | 47,868 | 55,087 | +7,219 🟩 | 95.1% | 95.2% | +0.1 🟩 pp |
| Balapitiya `LK-3106` | Galle | 0.5% | 65,993 | 66,727 | +734 🟩 | 97.9% | 97.9% | 0.0 pp |
| Kirinda Puhulwella `LK-3233` | Matara | 0.1% | 19,602 | 19,936 | +334 🟩 | 96.6% | 96.7% | 0.0 pp |
| Sooriyawewa `LK-3303` | Hambantota | 0.4% | 42,959 | 52,554 | +9,595 🟩 | 99.7% | 99.7% | 0.0 pp |
| Okewela `LK-3327` | Hambantota | 0.1% | 18,979 | 19,956 | +977 🟩 | 99.8% | 99.8% | 0.0 pp |
| Matara Four Gravets `LK-3242` | Matara | 0.8% | 110,335 | 118,046 | +7,711 🟩 | 95.3% | 95.3% | 0.0 pp |
| Walasmulla `LK-3325` | Hambantota | 0.3% | 42,184 | 47,778 | +5,594 🟩 | 99.8% | 99.8% | 0.0 pp |
| Ehetuwewa `LK-6109` | Kurunegala | 0.2% | 24,958 | 27,418 | +2,460 🟩 | 96.8% | 96.8% | 0.0 pp |
| Ambalangoda `LK-3133` | Galle | 0.4% | 56,563 | 59,209 | +2,646 🟩 | 99.3% | 99.3% | 0.0 pp |
| Sainthamaruthu `LK-5225` | Ampara | 0.0% | 18 | 19 | +1 🟩 | 0.1% | 0.1% | 0.0 pp |
| Uhana `LK-5212` | Ampara | 0.4% | 58,095 | 61,966 | +3,871 🟩 | 99.6% | 99.6% | 0.0 pp |
| Karainagar `LK-4104` | Jaffna | 0.0% | 6 | 5 | -1 🟥 | 0.1% | 0.1% | 0.0 pp |
| Ambanganga `LK-2221` | Matale | 0.1% | 11,714 | 11,887 | +173 🟩 | 74.9% | 74.9% | 0.0 pp |
| Nintavur `LK-5230` | Ampara | 0.0% | 17 | 16 | -1 🟥 | 0.1% | 0.1% | 0.0 pp |
| Sevanagala `LK-8233` | Monaragala | 0.3% | 41,801 | 49,252 | +7,451 🟩 | 99.8% | 99.7% | 0.0 pp |
| Wilgamuwa `LK-2227` | Matale | 0.2% | 29,446 | 33,653 | +4,207 🟩 | 99.8% | 99.8% | 0.0 pp |
| Kalutara `LK-1321` | Kalutara | 1.0% | 134,970 | 140,789 | +5,819 🟩 | 84.5% | 84.5% | 0.0 pp |
| Thenmaradchi (Chavakachcheri) `LK-4130` | Jaffna | 0.0% | 153 | 145 | -8 🟥 | 0.2% | 0.2% | 0.0 pp |
| Kotawehera `LK-6115` | Kurunegala | 0.2% | 21,090 | 23,830 | +2,740 🟩 | 99.2% | 99.2% | 0.0 pp |
| Kattankudy `LK-5124` | Batticaloa | 0.0% | 38 | 31 | -7 🟥 | 0.1% | 0.1% | 0.0 pp |
| Thanamalwila `LK-8230` | Monaragala | 0.2% | 26,547 | 31,070 | +4,523 🟩 | 99.5% | 99.5% | 0.0 pp |
| Islands North (Kayts) `LK-4103` | Jaffna | 0.0% | 20 | 17 | -3 🟥 | 0.2% | 0.2% | 0.0 pp |
| Katuwana `LK-3324` | Hambantota | 0.4% | 46,707 | 52,070 | +5,363 🟩 | 99.9% | 99.8% | -0.1 🟥 pp |
| Siyambalanduwa `LK-8212` | Monaragala | 0.4% | 53,861 | 62,813 | +8,952 🟩 | 99.7% | 99.6% | -0.1 🟥 pp |
| Habaraduwa `LK-3154` | Galle | 0.4% | 61,847 | 62,715 | +868 🟩 | 99.1% | 99.1% | -0.1 🟥 pp |
| Ambalantota `LK-3315` | Hambantota | 0.5% | 70,759 | 78,046 | +7,287 🟩 | 97.0% | 96.9% | -0.1 🟥 pp |
| Karaitivu `LK-5227` | Ampara | 0.0% | 30 | 22 | -8 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Koralai Pattu West `LK-5106` | Batticaloa | 0.0% | 22 | 6 | -16 🟥 | 0.1% | 0.0% | -0.1 🟥 pp |
| Panvila `LK-2115` | Kandy | 0.1% | 9,963 | 9,699 | -264 🟥 | 37.9% | 37.8% | -0.1 🟥 pp |
| Puthukkudiyiruppu `LK-4409` | Mullaitivu | 0.0% | 44 | 41 | -3 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Angunakolapelessa `LK-3318` | Hambantota | 0.4% | 48,243 | 53,299 | +5,056 🟩 | 99.9% | 99.8% | -0.1 🟥 pp |
| Thihagoda `LK-3236` | Matara | 0.2% | 33,437 | 34,176 | +739 🟩 | 99.7% | 99.6% | -0.1 🟥 pp |
| Rajanganaya `LK-7142` | Anuradhapura | 0.2% | 33,022 | 35,641 | +2,619 🟩 | 98.4% | 98.4% | -0.1 🟥 pp |
| Elahera `LK-7218` | Polonnaruwa | 0.3% | 43,714 | 48,299 | +4,585 🟩 | 99.5% | 99.5% | -0.1 🟥 pp |
| Horana `LK-1309` | Kalutara | 0.9% | 109,930 | 129,510 | +19,580 🟩 | 97.0% | 96.9% | -0.1 🟥 pp |
| Niyagama `LK-3115` | Galle | 0.2% | 35,174 | 35,315 | +141 🟩 | 98.9% | 98.8% | -0.1 🟥 pp |
| Hakmana `LK-3230` | Matara | 0.2% | 30,633 | 31,894 | +1,261 🟩 | 96.8% | 96.7% | -0.1 🟥 pp |
| Imaduwa `LK-3151` | Galle | 0.3% | 44,652 | 47,909 | +3,257 🟩 | 99.5% | 99.4% | -0.1 🟥 pp |
| Devinuwara `LK-3245` | Matara | 0.3% | 47,320 | 48,267 | +947 🟩 | 98.1% | 98.0% | -0.1 🟥 pp |
| Vadamaradchchi East `LK-4124` | Jaffna | 0.0% | 16 | 2 | -14 🟥 | 0.1% | 0.0% | -0.1 🟥 pp |
| Kahawattha `LK-9139` | Ratnapura | 0.2% | 33,092 | 33,355 | +263 🟩 | 76.4% | 76.3% | -0.1 🟥 pp |
| Godakawela `LK-9142` | Ratnapura | 0.4% | 59,074 | 60,584 | +1,510 🟩 | 77.3% | 77.1% | -0.1 🟥 pp |
| Welivitiya-Divitura `LK-3130` | Galle | 0.2% | 28,022 | 27,996 | -26 🟥 | 95.5% | 95.4% | -0.1 🟥 pp |
| Valikamam East (Kopay) `LK-4118` | Jaffna | 0.0% | 176 | 90 | -86 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Vadamaradchchi South-West (Karaveddy) `LK-4121` | Jaffna | 0.0% | 83 | 23 | -60 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Seethawaka `LK-1115` | Colombo | 0.7% | 92,746 | 99,364 | +6,618 🟩 | 81.5% | 81.4% | -0.1 🟥 pp |
| Mulatiyana `LK-3212` | Matara | 0.4% | 50,004 | 51,488 | +1,484 🟩 | 99.5% | 99.3% | -0.2 🟥 pp |
| Panduwasnuwara East `LK-6148` | Kurunegala | 0.2% | 28,711 | 30,369 | +1,658 🟩 | 95.7% | 95.5% | -0.2 🟥 pp |
| Galnewa `LK-7163` | Anuradhapura | 0.3% | 32,269 | 36,572 | +4,303 🟩 | 92.8% | 92.7% | -0.2 🟥 pp |
| Gomarankadawala `LK-5309` | Trincomalee | 0.1% | 7,341 | 8,338 | +997 🟩 | 99.4% | 99.3% | -0.2 🟥 pp |
| Valikamam West (Chankanai) `LK-4106` | Jaffna | 0.0% | 109 | 32 | -77 🟥 | 0.2% | 0.1% | -0.2 🟥 pp |
| Weeraketiya `LK-3321` | Hambantota | 0.3% | 40,714 | 47,170 | +6,456 🟩 | 98.0% | 97.8% | -0.2 🟥 pp |
| Medirigiriya `LK-7206` | Polonnaruwa | 0.5% | 64,078 | 70,700 | +6,622 🟩 | 97.7% | 97.5% | -0.2 🟥 pp |
| Matale `LK-2218` | Matale | 0.3% | 45,871 | 49,101 | +3,230 🟩 | 61.3% | 61.1% | -0.2 🟥 pp |
| Rattota `LK-2230` | Matale | 0.3% | 36,659 | 38,198 | +1,539 🟩 | 71.4% | 71.2% | -0.2 🟥 pp |
| Mirigama `LK-1212` | Gampaha | 1.1% | 153,905 | 164,914 | +11,009 🟩 | 93.5% | 93.3% | -0.2 🟥 pp |
| Malimbada `LK-3224` | Matara | 0.2% | 34,219 | 35,392 | +1,173 🟩 | 98.2% | 98.0% | -0.2 🟥 pp |
| Matugama `LK-1330` | Kalutara | 0.5% | 70,792 | 74,770 | +3,978 🟩 | 87.1% | 86.9% | -0.2 🟥 pp |
| Palugaswewa `LK-7157` | Anuradhapura | 0.1% | 15,251 | 17,713 | +2,462 🟩 | 97.9% | 97.7% | -0.2 🟥 pp |
| Manmunai South & Eruvil Pattu `LK-5136` | Batticaloa | 0.0% | 236 | 103 | -133 🟥 | 0.4% | 0.2% | -0.2 🟥 pp |
| Valikamam South West (Sandilipay) `LK-4109` | Jaffna | 0.0% | 137 | 16 | -121 🟥 | 0.3% | 0.0% | -0.2 🟥 pp |
| Maho `LK-6124` | Kurunegala | 0.4% | 53,668 | 59,715 | +6,047 🟩 | 93.4% | 93.1% | -0.2 🟥 pp |
| Verugal `LK-5333` | Trincomalee | 0.0% | 51 | 30 | -21 🟥 | 0.4% | 0.2% | -0.2 🟥 pp |
| Walallawita `LK-1339` | Kalutara | 0.4% | 52,880 | 53,425 | +545 🟩 | 96.8% | 96.6% | -0.2 🟥 pp |
| Thirappane `LK-7151` | Anuradhapura | 0.2% | 24,554 | 28,176 | +3,622 🟩 | 90.8% | 90.5% | -0.3 🟥 pp |
| Ratnapura `LK-9112` | Ratnapura | 0.7% | 93,970 | 94,405 | +435 🟩 | 78.2% | 77.9% | -0.3 🟥 pp |
| Yatiyantota `LK-9227` | Kegalle | 0.3% | 44,639 | 45,325 | +686 🟩 | 73.1% | 72.8% | -0.3 🟥 pp |
| Karandeniya `LK-3109` | Galle | 0.4% | 61,436 | 62,611 | +1,175 🟩 | 98.3% | 98.0% | -0.3 🟥 pp |
| Akkaraipattu `LK-5236` | Ampara | 0.0% | 173 | 76 | -97 🟥 | 0.4% | 0.2% | -0.3 🟥 pp |
| Galgamuwa `LK-6106` | Kurunegala | 0.4% | 50,475 | 56,429 | +5,954 🟩 | 91.6% | 91.4% | -0.3 🟥 pp |
| Kaburupitiya `LK-3227` | Matara | 0.3% | 40,853 | 42,577 | +1,724 🟩 | 99.7% | 99.4% | -0.3 🟥 pp |
| Koralai Pattu South `LK-5110` | Batticaloa | 0.0% | 123 | 54 | -69 🟥 | 0.5% | 0.2% | -0.3 🟥 pp |
| Alayadivembu `LK-5239` | Ampara | 0.0% | 237 | 192 | -45 🟥 | 1.1% | 0.8% | -0.3 🟥 pp |
| Gonapinuwala `LK-3134` | Galle | 0.2% | 21,491 | 22,922 | +1,431 🟩 | 98.8% | 98.5% | -0.3 🟥 pp |
| Aranayake `LK-9209` | Kegalle | 0.4% | 61,625 | 61,972 | +347 🟩 | 90.0% | 89.7% | -0.3 🟥 pp |
| Neluwa `LK-3121` | Galle | 0.2% | 27,132 | 26,202 | -930 🟥 | 94.7% | 94.4% | -0.3 🟥 pp |
| Tirukkovil `LK-5245` | Ampara | 0.0% | 119 | 47 | -72 🟥 | 0.5% | 0.2% | -0.3 🟥 pp |
| Kinniya `LK-5324` | Trincomalee | 0.0% | 253 | 61 | -192 🟥 | 0.4% | 0.1% | -0.3 🟥 pp |
| Yatawatta `LK-2215` | Matale | 0.2% | 25,085 | 26,782 | +1,697 🟩 | 82.9% | 82.6% | -0.3 🟥 pp |
| Bandarawela `LK-8133` | Badulla | 0.3% | 47,274 | 47,050 | -224 🟥 | 72.2% | 71.8% | -0.3 🟥 pp |
| Pannala `LK-6178` | Kurunegala | 0.8% | 107,649 | 117,261 | +9,612 🟩 | 86.7% | 86.3% | -0.3 🟥 pp |
| Harispattuwa `LK-2133` | Kandy | 0.6% | 75,442 | 80,125 | +4,683 🟩 | 85.6% | 85.2% | -0.3 🟥 pp |
| Ingiriya `LK-1310` | Kalutara | 0.4% | 48,168 | 51,949 | +3,781 🟩 | 89.4% | 89.0% | -0.4 🟥 pp |
| Hambantota `LK-3312` | Hambantota | 0.4% | 46,820 | 54,707 | +7,887 🟩 | 81.8% | 81.4% | -0.4 🟥 pp |
| Islands South (Velanai) `LK-4139` | Jaffna | 0.0% | 75 | 14 | -61 🟥 | 0.4% | 0.1% | -0.4 🟥 pp |
| Valikamam South (Uduvil) `LK-4115` | Jaffna | 0.0% | 257 | 61 | -196 🟥 | 0.5% | 0.1% | -0.4 🟥 pp |
| Muthur `LK-5327` | Trincomalee | 0.0% | 459 | 315 | -144 🟥 | 0.8% | 0.4% | -0.4 🟥 pp |
| Vadamaradchi North (Point Pedro) `LK-4127` | Jaffna | 0.0% | 256 | 68 | -188 🟥 | 0.5% | 0.2% | -0.4 🟥 pp |
| Deltota `LK-2148` | Kandy | 0.1% | 12,103 | 12,602 | +499 🟩 | 39.9% | 39.5% | -0.4 🟥 pp |
| Biyagama `LK-1239` | Gampaha | 1.2% | 161,364 | 178,329 | +16,965 🟩 | 86.5% | 86.1% | -0.4 🟥 pp |
| Giribawa `LK-6103` | Kurunegala | 0.2% | 28,639 | 31,704 | +3,065 🟩 | 91.2% | 90.8% | -0.4 🟥 pp |
| Bamunakotuwa `LK-6149` | Kurunegala | 0.3% | 34,774 | 37,709 | +2,935 🟩 | 96.0% | 95.6% | -0.4 🟥 pp |
| Galenbidunuwewa `LK-7127` | Anuradhapura | 0.3% | 45,433 | 50,009 | +4,576 🟩 | 96.7% | 96.3% | -0.4 🟥 pp |
| Porativu Pattu `LK-5133` | Batticaloa | 0.0% | 375 | 226 | -149 🟥 | 1.0% | 0.6% | -0.5 🟥 pp |
| Dehiowita `LK-9230` | Kegalle | 0.5% | 64,423 | 66,913 | +2,490 🟩 | 79.2% | 78.8% | -0.5 🟥 pp |
| Kandavalai `LK-4506` | Kilinochchi | 0.0% | 117 | 7 | -110 🟥 | 0.5% | 0.0% | -0.5 🟥 pp |
| Dikwella `LK-3248` | Matara | 0.4% | 51,739 | 53,168 | +1,429 🟩 | 94.6% | 94.2% | -0.5 🟥 pp |
| Koralai Pattu North `LK-5103` | Batticaloa | 0.0% | 244 | 166 | -78 🟥 | 1.1% | 0.7% | -0.5 🟥 pp |
| Kekirawa `LK-7154` | Anuradhapura | 0.3% | 46,174 | 50,581 | +4,407 🟩 | 77.9% | 77.4% | -0.5 🟥 pp |
| Welikanda `LK-7210` | Polonnaruwa | 0.2% | 24,924 | 27,995 | +3,071 🟩 | 73.8% | 73.3% | -0.5 🟥 pp |
| Medawachchiya `LK-7109` | Anuradhapura | 0.3% | 43,592 | 48,517 | +4,925 🟩 | 92.9% | 92.4% | -0.5 🟥 pp |
| Polgahawela `LK-6187` | Kurunegala | 0.4% | 56,492 | 58,139 | +1,647 🟩 | 86.7% | 86.2% | -0.5 🟥 pp |
| Bulathsinhala `LK-1312` | Kalutara | 0.4% | 54,770 | 55,217 | +447 🟩 | 84.8% | 84.2% | -0.5 🟥 pp |
| Ganewatta `LK-6133` | Kurunegala | 0.3% | 37,627 | 40,474 | +2,847 🟩 | 93.7% | 93.2% | -0.6 🟥 pp |
| Rasnayakapura `LK-6118` | Kurunegala | 0.1% | 17,320 | 19,566 | +2,246 🟩 | 79.1% | 78.5% | -0.6 🟥 pp |
| Navithanveli `LK-5216` | Ampara | 0.0% | 182 | 83 | -99 🟥 | 1.0% | 0.4% | -0.6 🟥 pp |
| Monaragala `LK-8215` | Monaragala | 0.3% | 42,571 | 48,622 | +6,051 🟩 | 86.0% | 85.4% | -0.6 🟥 pp |
| Akuressa `LK-3218` | Matara | 0.4% | 51,529 | 51,918 | +389 🟩 | 97.4% | 96.8% | -0.6 🟥 pp |
| Manmunai West `LK-5121` | Batticaloa | 0.0% | 192 | 26 | -166 🟥 | 0.7% | 0.1% | -0.6 🟥 pp |
| Badulla `LK-8121` | Badulla | 0.4% | 51,643 | 56,647 | +5,004 🟩 | 68.8% | 68.2% | -0.6 🟥 pp |
| Kebithigollewa `LK-7106` | Anuradhapura | 0.2% | 20,178 | 23,731 | +3,553 🟩 | 90.4% | 89.8% | -0.6 🟥 pp |
| Badalkumbura `LK-8218` | Monaragala | 0.3% | 34,324 | 39,597 | +5,273 🟩 | 85.6% | 85.0% | -0.6 🟥 pp |
| Hali-Ela `LK-8124` | Badulla | 0.4% | 58,154 | 59,899 | +1,745 🟩 | 64.2% | 63.6% | -0.6 🟥 pp |
| Pallama `LK-6227` | Puttalam | 0.1% | 16,713 | 18,924 | +2,211 🟩 | 68.4% | 67.7% | -0.6 🟥 pp |
| Maspotha `LK-6151` | Kurunegala | 0.3% | 31,542 | 38,268 | +6,726 🟩 | 92.1% | 91.4% | -0.7 🟥 pp |
| Medadumbara `LK-2124` | Kandy | 0.3% | 45,641 | 47,828 | +2,187 🟩 | 74.8% | 74.1% | -0.7 🟥 pp |
| Pasgoda `LK-3209` | Matara | 0.4% | 57,462 | 58,982 | +1,520 🟩 | 97.1% | 96.4% | -0.7 🟥 pp |
| Bandaragama `LK-1306` | Kalutara | 0.7% | 93,708 | 105,601 | +11,893 🟩 | 85.8% | 85.1% | -0.7 🟥 pp |
| Poonakary `LK-4512` | Kilinochchi | 0.0% | 174 | 31 | -143 🟥 | 0.9% | 0.1% | -0.7 🟥 pp |
| Galewela `LK-2203` | Matale | 0.4% | 56,346 | 62,683 | +6,337 🟩 | 80.4% | 79.7% | -0.7 🟥 pp |
| Akmeemana `LK-3145` | Galle | 0.6% | 74,622 | 82,001 | +7,379 🟩 | 95.9% | 95.2% | -0.7 🟥 pp |
| Mawathagama `LK-6160` | Kurunegala | 0.4% | 52,308 | 57,291 | +4,983 🟩 | 81.6% | 80.8% | -0.8 🟥 pp |
| Ruwanwella `LK-9221` | Kegalle | 0.4% | 55,217 | 56,321 | +1,104 🟩 | 86.4% | 85.6% | -0.8 🟥 pp |
| Athuraliya `LK-3215` | Matara | 0.2% | 29,842 | 30,049 | +207 🟩 | 92.4% | 91.6% | -0.8 🟥 pp |
| Palagala `LK-7166` | Anuradhapura | 0.2% | 28,952 | 32,444 | +3,492 🟩 | 85.1% | 84.3% | -0.8 🟥 pp |
| Welioya `LK-4418` | Mullaitivu | 0.1% | 6,843 | 9,894 | +3,051 🟩 | 99.1% | 98.3% | -0.8 🟥 pp |
| Thamankaduwa `LK-7215` | Polonnaruwa | 0.5% | 67,106 | 74,194 | +7,088 🟩 | 81.4% | 80.6% | -0.8 🟥 pp |
| Ella `LK-8136` | Badulla | 0.2% | 29,951 | 32,363 | +2,412 🟩 | 66.3% | 65.5% | -0.8 🟥 pp |
| Manmunai North `LK-5118` | Batticaloa | 0.0% | 1,293 | 625 | -668 🟥 | 1.5% | 0.7% | -0.8 🟥 pp |
| Poojapitiya `LK-2106` | Kandy | 0.3% | 46,318 | 47,728 | +1,410 🟩 | 80.0% | 79.1% | -0.8 🟥 pp |
| Tumpane `LK-2103` | Kandy | 0.2% | 34,574 | 35,275 | +701 🟩 | 91.8% | 91.0% | -0.9 🟥 pp |
| Maritimepattu `LK-4415` | Mullaitivu | 0.0% | 300 | 48 | -252 🟥 | 1.0% | 0.1% | -0.9 🟥 pp |
| Naula `LK-2209` | Matale | 0.2% | 28,843 | 28,407 | -436 🟥 | 93.4% | 92.5% | -0.9 🟥 pp |
| Delft `LK-4142` | Jaffna | 0.0% | 40 | 4 | -36 🟥 | 1.0% | 0.1% | -0.9 🟥 pp |
| Ibbagamuwa `LK-6130` | Kurunegala | 0.6% | 76,728 | 84,174 | +7,446 🟩 | 90.3% | 89.4% | -0.9 🟥 pp |
| Ipalogama `LK-7160` | Anuradhapura | 0.2% | 32,964 | 35,204 | +2,240 🟩 | 84.8% | 83.9% | -0.9 🟥 pp |
| Kantale `LK-5321` | Trincomalee | 0.3% | 37,262 | 39,988 | +2,726 🟩 | 79.6% | 78.7% | -1.0 🟥 pp |
| Warakapola `LK-9218` | Kegalle | 0.7% | 102,661 | 105,968 | +3,307 🟩 | 90.8% | 89.8% | -1.0 🟥 pp |
| Nanaddan `LK-4212` | Mannar | 0.0% | 251 | 83 | -168 🟥 | 1.4% | 0.4% | -1.0 🟥 pp |
| Passara `LK-8118` | Badulla | 0.2% | 27,201 | 27,171 | -30 🟥 | 55.7% | 54.7% | -1.0 🟥 pp |
| Thimbirigasyaya `LK-1127` | Colombo | 0.7% | 113,810 | 101,553 | -12,257 🟥 | 47.9% | 46.8% | -1.1 🟥 pp |
| Mihinthale `LK-7130` | Anuradhapura | 0.3% | 33,046 | 40,807 | +7,761 🟩 | 93.6% | 92.5% | -1.1 🟥 pp |
| Musali `LK-4215` | Mannar | 0.0% | 129 | 83 | -46 🟥 | 1.6% | 0.5% | -1.1 🟥 pp |
| Lunugala `LK-8119` | Badulla | 0.1% | 12,976 | 12,807 | -169 🟥 | 41.3% | 40.2% | -1.2 🟥 pp |
| Mallawapitiya `LK-6157` | Kurunegala | 0.3% | 41,729 | 46,464 | +4,735 🟩 | 79.3% | 78.1% | -1.2 🟥 pp |
| Negombo `LK-1203` | Gampaha | 0.1% | 15,732 | 13,506 | -2,226 🟥 | 11.1% | 9.8% | -1.3 🟥 pp |
| Valikamam North (Thllippalai) `LK-4112` | Jaffna | 0.0% | 431 | 64 | -367 🟥 | 1.5% | 0.1% | -1.3 🟥 pp |
| Weligama `LK-3239` | Matara | 0.5% | 65,046 | 66,983 | +1,937 🟩 | 89.3% | 88.0% | -1.3 🟥 pp |
| Kundasale `LK-2127` | Kandy | 0.8% | 103,484 | 115,594 | +12,110 🟩 | 81.4% | 80.1% | -1.4 🟥 pp |
| Mannar Town `LK-4203` | Mannar | 0.0% | 811 | 96 | -715 🟥 | 1.6% | 0.2% | -1.4 🟥 pp |
| Thunukkai `LK-4403` | Mullaitivu | 0.0% | 168 | 31 | -137 🟥 | 1.7% | 0.3% | -1.4 🟥 pp |
| Panduwasnuwara West `LK-6145` | Kurunegala | 0.4% | 55,271 | 58,481 | +3,210 🟩 | 83.6% | 82.2% | -1.4 🟥 pp |
| Medagama `LK-8209` | Monaragala | 0.3% | 30,810 | 37,662 | +6,852 🟩 | 85.9% | 84.4% | -1.4 🟥 pp |
| Kelaniya `LK-1236` | Gampaha | 0.7% | 102,634 | 97,990 | -4,644 🟥 | 74.7% | 73.3% | -1.5 🟥 pp |
| Attanagalla `LK-1227` | Gampaha | 1.1% | 151,786 | 164,206 | +12,420 🟩 | 84.5% | 83.0% | -1.5 🟥 pp |
| Panadura `LK-1303` | Kalutara | 1.0% | 143,301 | 144,521 | +1,220 🟩 | 78.6% | 77.1% | -1.5 🟥 pp |
| Rideegama `LK-6163` | Kurunegala | 0.6% | 75,598 | 80,308 | +4,710 🟩 | 85.2% | 83.7% | -1.5 🟥 pp |
| Udunuwara `LK-2139` | Kandy | 0.6% | 79,869 | 85,290 | +5,421 🟩 | 72.0% | 70.5% | -1.5 🟥 pp |
| Vavuniya South `LK-4306` | Vavuniya | 0.1% | 12,532 | 13,946 | +1,414 🟩 | 95.5% | 94.0% | -1.6 🟥 pp |
| Thambalagamuwa `LK-5318` | Trincomalee | 0.1% | 6,760 | 7,440 | +680 🟩 | 23.7% | 22.1% | -1.6 🟥 pp |
| Wattala `LK-1218` | Gampaha | 0.4% | 52,405 | 51,544 | -861 🟥 | 29.9% | 28.2% | -1.6 🟥 pp |
| Welimada `LK-8130` | Badulla | 0.5% | 71,215 | 72,755 | +1,540 🟩 | 70.6% | 69.0% | -1.7 🟥 pp |
| Ukuwela `LK-2233` | Matale | 0.3% | 43,744 | 45,225 | +1,481 🟩 | 64.3% | 62.5% | -1.8 🟥 pp |
| Manthai East `LK-4406` | Mullaitivu | 0.0% | 163 | 34 | -129 🟥 | 2.3% | 0.4% | -1.8 🟥 pp |
| Haputale `LK-8139` | Badulla | 0.2% | 26,212 | 24,432 | -1,780 🟥 | 52.6% | 50.6% | -2.0 🟥 pp |
| Udapalatha `LK-2151` | Kandy | 0.4% | 50,471 | 54,676 | +4,205 🟩 | 55.0% | 53.0% | -2.0 🟥 pp |
| Vengalacheddikulam `LK-4312` | Vavuniya | 0.0% | 672 | 46 | -626 🟥 | 2.2% | 0.2% | -2.1 🟥 pp |
| Pathadumbara `LK-2112` | Kandy | 0.5% | 65,000 | 66,522 | +1,522 🟩 | 73.3% | 71.2% | -2.1 🟥 pp |
| Kobeigane `LK-6139` | Kurunegala | 0.2% | 31,165 | 34,325 | +3,160 🟩 | 86.6% | 84.4% | -2.2 🟥 pp |
| Manthai West `LK-4206` | Mannar | 0.0% | 350 | 19 | -331 🟥 | 2.4% | 0.1% | -2.3 🟥 pp |
| Madhu `LK-4209` | Mannar | 0.0% | 268 | 101 | -167 🟥 | 3.5% | 1.1% | -2.4 🟥 pp |
| Morawewa `LK-5312` | Trincomalee | 0.0% | 5,736 | 6,393 | +657 🟩 | 72.0% | 69.5% | -2.4 🟥 pp |
| Beruwala `LK-1324` | Kalutara | 0.7% | 91,957 | 96,273 | +4,316 🟩 | 55.7% | 53.2% | -2.5 🟥 pp |
| Akurana `LK-2109` | Kandy | 0.1% | 18,739 | 19,167 | +428 🟩 | 29.6% | 27.0% | -2.6 🟥 pp |
| Welipitiya `LK-3221` | Matara | 0.3% | 45,531 | 47,466 | +1,935 🟩 | 87.4% | 84.8% | -2.6 🟥 pp |
| Oddusuddan `LK-4412` | Mullaitivu | 0.0% | 622 | 245 | -377 🟥 | 4.0% | 1.3% | -2.6 🟥 pp |
| Colombo `LK-1103` | Colombo | 0.3% | 61,448 | 47,726 | -13,722 🟥 | 19.0% | 16.3% | -2.7 🟥 pp |
| Pachchilaipalli `LK-4503` | Kilinochchi | 0.0% | 237 | 13 | -224 🟥 | 2.8% | 0.1% | -2.7 🟥 pp |
| Kuliyapitiya East `LK-6169` | Kurunegala | 0.3% | 36,275 | 39,425 | +3,150 🟩 | 67.1% | 64.4% | -2.7 🟥 pp |
| Mawanella `LK-9206` | Kegalle | 0.6% | 76,124 | 82,393 | +6,269 🟩 | 68.1% | 65.4% | -2.8 🟥 pp |
| Horowpathana `LK-7124` | Anuradhapura | 0.2% | 26,965 | 28,932 | +1,967 🟩 | 72.9% | 70.1% | -2.8 🟥 pp |
| Kahatagasdigiliya `LK-7121` | Anuradhapura | 0.2% | 31,772 | 34,073 | +2,301 🟩 | 78.8% | 75.9% | -2.9 🟥 pp |
| Katana `LK-1206` | Gampaha | 0.9% | 141,353 | 137,806 | -3,547 🟥 | 60.1% | 57.1% | -2.9 🟥 pp |
| Lankapura `LK-7209` | Polonnaruwa | 0.2% | 25,849 | 26,904 | +1,055 🟩 | 70.9% | 67.8% | -3.1 🟥 pp |
| Galle 4 Gravets `LK-3139` | Galle | 0.5% | 66,840 | 67,502 | +662 🟩 | 65.7% | 62.3% | -3.4 🟥 pp |
| Seruvila `LK-5330` | Trincomalee | 0.1% | 8,805 | 9,787 | +982 🟩 | 64.6% | 61.1% | -3.4 🟥 pp |
| Ratmalana `LK-1131` | Colombo | 0.4% | 66,808 | 57,385 | -9,423 🟥 | 70.0% | 65.2% | -4.8 🟥 pp |
| Kolonnawa `LK-1106` | Colombo | 0.8% | 123,787 | 122,559 | -1,228 🟥 | 64.6% | 57.3% | -7.3 🟥 pp |
| Dehiwala `LK-1130` | Colombo | 0.3% | 48,310 | 43,573 | -4,737 🟥 | 54.3% | 46.4% | -7.9 🟥 pp |

***Vavuniya North** gained the most share at **+3.4pp**. **Dehiwala** saw the steepest share decline at **-7.9pp**. **Homagama** had the largest absolute increase (**+42,094**).*

### Hindu

| DSD | District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Koralai Pattu Central `LK-5104` | Batticaloa | 1.0% | 580 | 23,383 | +22,803 🟩 | 2.3% | 81.3% | +79.0 🟩 pp |
| Wattala `LK-1218` | Gampaha | 1.4% | 22,782 | 30,805 | +8,023 🟩 | 13.0% | 16.9% | +3.9 🟩 pp |
| Dehiwala `LK-1130` | Colombo | 0.6% | 10,783 | 14,406 | +3,623 🟩 | 12.1% | 15.4% | +3.2 🟩 pp |
| Morawewa `LK-5312` | Trincomalee | 0.1% | 833 | 1,200 | +367 🟩 | 10.5% | 13.1% | +2.6 🟩 pp |
| Vadamaradchi North (Point Pedro) `LK-4127` | Jaffna | 1.7% | 39,886 | 37,472 | -2,414 🟥 | 83.9% | 86.4% | +2.5 🟩 pp |
| Ratmalana `LK-1131` | Colombo | 0.3% | 5,739 | 7,316 | +1,577 🟩 | 6.0% | 8.3% | +2.3 🟩 pp |
| Pachchilaipalli `LK-4503` | Kilinochchi | 0.5% | 7,176 | 11,271 | +4,095 🟩 | 84.1% | 86.4% | +2.3 🟩 pp |
| Kelaniya `LK-1236` | Gampaha | 0.4% | 6,415 | 8,886 | +2,471 🟩 | 4.7% | 6.6% | +2.0 🟩 pp |
| Lunugala `LK-8119` | Badulla | 0.7% | 15,284 | 16,140 | +856 🟩 | 48.7% | 50.6% | +1.9 🟩 pp |
| Thimbirigasyaya `LK-1127` | Colombo | 2.4% | 53,469 | 52,962 | -507 🟥 | 22.5% | 24.4% | +1.9 🟩 pp |
| Colombo `LK-1103` | Colombo | 3.2% | 73,374 | 71,811 | -1,563 🟥 | 22.7% | 24.6% | +1.9 🟩 pp |
| Haputale `LK-8139` | Badulla | 0.8% | 17,312 | 17,674 | +362 🟩 | 34.8% | 36.6% | +1.8 🟩 pp |
| Passara `LK-8118` | Badulla | 0.8% | 17,178 | 18,256 | +1,078 🟩 | 35.2% | 36.8% | +1.6 🟩 pp |
| Kundasale `LK-2127` | Kandy | 0.7% | 12,216 | 16,116 | +3,900 🟩 | 9.6% | 11.2% | +1.5 🟩 pp |
| Manmunai South & Eruvil Pattu `LK-5136` | Batticaloa | 2.7% | 57,103 | 59,997 | +2,894 🟩 | 93.9% | 95.4% | +1.4 🟩 pp |
| Panvila `LK-2115` | Kandy | 0.6% | 13,720 | 13,754 | +34 🟩 | 52.2% | 53.6% | +1.4 🟩 pp |
| Monaragala `LK-8215` | Monaragala | 0.3% | 5,927 | 7,625 | +1,698 🟩 | 12.0% | 13.4% | +1.4 🟩 pp |
| Seethawaka `LK-1115` | Colombo | 0.5% | 9,690 | 12,066 | +2,376 🟩 | 8.5% | 9.9% | +1.4 🟩 pp |
| Ella `LK-8136` | Badulla | 0.6% | 12,338 | 14,108 | +1,770 🟩 | 27.3% | 28.5% | +1.2 🟩 pp |
| Oddusuddan `LK-4412` | Mullaitivu | 0.7% | 13,421 | 15,685 | +2,264 🟩 | 85.4% | 86.4% | +1.1 🟩 pp |
| Manthai East `LK-4406` | Mullaitivu | 0.3% | 6,351 | 6,898 | +547 🟩 | 89.2% | 90.2% | +0.9 🟩 pp |
| Valikamam South West (Sandilipay) `LK-4109` | Jaffna | 1.8% | 39,278 | 39,652 | +374 🟩 | 75.1% | 76.1% | +0.9 🟩 pp |
| Bulathsinhala `LK-1312` | Kalutara | 0.3% | 6,584 | 7,218 | +634 🟩 | 10.2% | 11.0% | +0.8 🟩 pp |
| Udapalatha `LK-2151` | Kandy | 0.9% | 17,909 | 20,988 | +3,079 🟩 | 19.5% | 20.3% | +0.8 🟩 pp |
| Bandarawela `LK-8133` | Badulla | 0.5% | 11,519 | 12,044 | +525 🟩 | 17.6% | 18.4% | +0.8 🟩 pp |
| Naula `LK-2209` | Matale | 0.1% | 1,390 | 1,625 | +235 🟩 | 4.5% | 5.3% | +0.8 🟩 pp |
| Hali-Ela `LK-8124` | Badulla | 1.3% | 26,229 | 28,031 | +1,802 🟩 | 29.0% | 29.7% | +0.8 🟩 pp |
| Dehiowita `LK-9230` | Kegalle | 0.5% | 10,909 | 12,066 | +1,157 🟩 | 13.4% | 14.2% | +0.8 🟩 pp |
| Madhu `LK-4209` | Mannar | 0.2% | 3,709 | 4,637 | +928 🟩 | 48.1% | 48.8% | +0.7 🟩 pp |
| Manmunai West `LK-5121` | Batticaloa | 1.4% | 27,680 | 32,137 | +4,457 🟩 | 97.2% | 97.9% | +0.7 🟩 pp |
| Katana `LK-1206` | Gampaha | 0.3% | 3,923 | 5,728 | +1,805 🟩 | 1.7% | 2.4% | +0.7 🟩 pp |
| Ingiriya `LK-1310` | Kalutara | 0.2% | 4,736 | 5,540 | +804 🟩 | 8.8% | 9.5% | +0.7 🟩 pp |
| Biyagama `LK-1239` | Gampaha | 0.1% | 1,565 | 3,125 | +1,560 🟩 | 0.8% | 1.5% | +0.7 🟩 pp |
| Karainagar `LK-4104` | Jaffna | 0.4% | 9,153 | 8,786 | -367 🟥 | 95.6% | 96.2% | +0.6 🟩 pp |
| Sri Jayawardanapura Kotte `LK-1124` | Colombo | 0.2% | 4,880 | 4,957 | +77 🟩 | 4.5% | 5.2% | +0.6 🟩 pp |
| Badulla `LK-8121` | Badulla | 0.7% | 13,496 | 15,442 | +1,946 🟩 | 18.0% | 18.6% | +0.6 🟩 pp |
| Moratuwa `LK-1133` | Colombo | 0.2% | 3,549 | 4,317 | +768 🟩 | 2.1% | 2.7% | +0.6 🟩 pp |
| Badalkumbura `LK-8218` | Monaragala | 0.2% | 3,624 | 4,483 | +859 🟩 | 9.0% | 9.6% | +0.6 🟩 pp |
| Welioya `LK-4418` | Mullaitivu | 0.0% | 5 | 65 | +60 🟩 | 0.1% | 0.6% | +0.6 🟩 pp |
| Valikamam South (Uduvil) `LK-4115` | Jaffna | 2.0% | 46,855 | 44,954 | -1,901 🟥 | 88.4% | 88.9% | +0.6 🟩 pp |
| Verugal `LK-5333` | Trincomalee | 0.6% | 10,858 | 13,459 | +2,601 🟩 | 95.2% | 95.7% | +0.5 🟩 pp |
| Yatawatta `LK-2215` | Matale | 0.1% | 2,691 | 3,055 | +364 🟩 | 8.9% | 9.4% | +0.5 🟩 pp |
| Seruvila `LK-5330` | Trincomalee | 0.1% | 2,260 | 2,731 | +471 🟩 | 16.6% | 17.1% | +0.5 🟩 pp |
| Mahakumbukkadawala `LK-6221` | Puttalam | 0.0% | 371 | 540 | +169 🟩 | 2.0% | 2.5% | +0.5 🟩 pp |
| Deltota `LK-2148` | Kandy | 0.5% | 10,078 | 10,738 | +660 🟩 | 33.2% | 33.7% | +0.4 🟩 pp |
| Yatiyantota `LK-9227` | Kegalle | 0.6% | 12,118 | 12,613 | +495 🟩 | 19.8% | 20.3% | +0.4 🟩 pp |
| Kahawattha `LK-9139` | Ratnapura | 0.4% | 7,650 | 7,906 | +256 🟩 | 17.7% | 18.1% | +0.4 🟩 pp |
| Vadamaradchchi South-West (Karaveddy) `LK-4121` | Jaffna | 1.8% | 43,870 | 39,599 | -4,271 🟥 | 95.9% | 96.3% | +0.4 🟩 pp |
| Pasgoda `LK-3209` | Matara | 0.1% | 1,336 | 1,629 | +293 🟩 | 2.3% | 2.7% | +0.4 🟩 pp |
| Ruwanwella `LK-9221` | Kegalle | 0.2% | 3,950 | 4,327 | +377 🟩 | 6.2% | 6.6% | +0.4 🟩 pp |
| Walallawita `LK-1339` | Kalutara | 0.1% | 1,456 | 1,686 | +230 🟩 | 2.7% | 3.0% | +0.4 🟩 pp |
| Ambanganga `LK-2221` | Matale | 0.2% | 3,613 | 3,726 | +113 🟩 | 23.1% | 23.5% | +0.4 🟩 pp |
| Mihinthale `LK-7130` | Anuradhapura | 0.0% | 84 | 266 | +182 🟩 | 0.2% | 0.6% | +0.4 🟩 pp |
| Kesbewa `LK-1136` | Colombo | 0.2% | 2,260 | 3,388 | +1,128 🟩 | 0.9% | 1.3% | +0.4 🟩 pp |
| Ratnapura `LK-9112` | Ratnapura | 0.8% | 16,888 | 17,447 | +559 🟩 | 14.0% | 14.4% | +0.4 🟩 pp |
| Alayadivembu `LK-5239` | Ampara | 1.0% | 19,196 | 21,312 | +2,116 🟩 | 85.5% | 85.8% | +0.3 🟩 pp |
| Bingiriya `LK-6142` | Kurunegala | 0.0% | 182 | 410 | +228 🟩 | 0.3% | 0.6% | +0.3 🟩 pp |
| Akuressa `LK-3218` | Matara | 0.1% | 1,083 | 1,269 | +186 🟩 | 2.0% | 2.4% | +0.3 🟩 pp |
| Udubaddawa `LK-6175` | Kurunegala | 0.0% | 223 | 402 | +179 🟩 | 0.4% | 0.7% | +0.3 🟩 pp |
| Negombo `LK-1203` | Gampaha | 0.4% | 8,317 | 8,471 | +154 🟩 | 5.9% | 6.1% | +0.3 🟩 pp |
| Neluwa `LK-3121` | Galle | 0.1% | 1,094 | 1,139 | +45 🟩 | 3.8% | 4.1% | +0.3 🟩 pp |
| Anamaduwa `LK-6224` | Puttalam | 0.0% | 67 | 194 | +127 🟩 | 0.2% | 0.4% | +0.3 🟩 pp |
| Tumpane `LK-2103` | Kandy | 0.0% | 191 | 298 | +107 🟩 | 0.5% | 0.8% | +0.3 🟩 pp |
| Imaduwa `LK-3151` | Galle | 0.0% | 31 | 156 | +125 🟩 | 0.1% | 0.3% | +0.3 🟩 pp |
| Homagama `LK-1112` | Colombo | 0.1% | 1,827 | 2,854 | +1,027 🟩 | 0.8% | 1.0% | +0.2 🟩 pp |
| Vavuniya South `LK-4306` | Vavuniya | 0.0% | 323 | 402 | +79 🟩 | 2.5% | 2.7% | +0.2 🟩 pp |
| Bamunakotuwa `LK-6149` | Kurunegala | 0.0% | 53 | 154 | +101 🟩 | 0.1% | 0.4% | +0.2 🟩 pp |
| Maharagama `LK-1121` | Colombo | 0.2% | 2,921 | 3,381 | +460 🟩 | 1.5% | 1.7% | +0.2 🟩 pp |
| Warakapola `LK-9218` | Kegalle | 0.2% | 3,065 | 3,471 | +406 🟩 | 2.7% | 2.9% | +0.2 🟩 pp |
| Maspotha `LK-6151` | Kurunegala | 0.0% | 349 | 521 | +172 🟩 | 1.0% | 1.2% | +0.2 🟩 pp |
| Mahara `LK-1233` | Gampaha | 0.1% | 1,333 | 1,911 | +578 🟩 | 0.6% | 0.9% | +0.2 🟩 pp |
| Pannala `LK-6178` | Kurunegala | 0.1% | 835 | 1,202 | +367 🟩 | 0.7% | 0.9% | +0.2 🟩 pp |
| Porativu Pattu `LK-5133` | Batticaloa | 1.7% | 35,305 | 37,730 | +2,425 🟩 | 97.5% | 97.7% | +0.2 🟩 pp |
| Manmunai North `LK-5118` | Batticaloa | 2.8% | 56,040 | 62,008 | +5,968 🟩 | 65.0% | 65.2% | +0.2 🟩 pp |
| Divulapitiya `LK-1209` | Gampaha | 0.0% | 616 | 985 | +369 🟩 | 0.4% | 0.6% | +0.2 🟩 pp |
| Matale `LK-2218` | Matale | 0.6% | 12,480 | 13,559 | +1,079 🟩 | 16.7% | 16.9% | +0.2 🟩 pp |
| Nattandiya `LK-6242` | Puttalam | 0.1% | 1,079 | 1,262 | +183 🟩 | 1.7% | 1.9% | +0.2 🟩 pp |
| Akmeemana `LK-3145` | Galle | 0.0% | 661 | 896 | +235 🟩 | 0.8% | 1.0% | +0.2 🟩 pp |
| Kobeigane `LK-6139` | Kurunegala | 0.0% | 20 | 99 | +79 🟩 | 0.1% | 0.2% | +0.2 🟩 pp |
| Kaburupitiya `LK-3227` | Matara | 0.0% | 24 | 104 | +80 🟩 | 0.1% | 0.2% | +0.2 🟩 pp |
| Deraniyagala `LK-9233` | Kegalle | 0.4% | 9,028 | 8,742 | -286 🟥 | 19.7% | 19.9% | +0.2 🟩 pp |
| Gomarankadawala `LK-5309` | Trincomalee | 0.0% | 26 | 45 | +19 🟩 | 0.4% | 0.5% | +0.2 🟩 pp |
| Akkaraipattu `LK-5236` | Ampara | 0.0% | 60 | 150 | +90 🟩 | 0.2% | 0.3% | +0.2 🟩 pp |
| Thamankaduwa `LK-7215` | Polonnaruwa | 0.0% | 735 | 981 | +246 🟩 | 0.9% | 1.1% | +0.2 🟩 pp |
| Polpitigama `LK-6127` | Kurunegala | 0.0% | 47 | 203 | +156 🟩 | 0.1% | 0.2% | +0.2 🟩 pp |
| Mahawewa `LK-6239` | Puttalam | 0.0% | 390 | 456 | +66 🟩 | 0.8% | 0.9% | +0.2 🟩 pp |
| Pathadumbara `LK-2112` | Kandy | 0.1% | 2,113 | 2,377 | +264 🟩 | 2.4% | 2.5% | +0.2 🟩 pp |
| Niyagama `LK-3115` | Galle | 0.0% | 283 | 341 | +58 🟩 | 0.8% | 1.0% | +0.2 🟩 pp |
| Mirigama `LK-1212` | Gampaha | 0.0% | 651 | 973 | +322 🟩 | 0.4% | 0.6% | +0.2 🟩 pp |
| Rideegama `LK-6163` | Kurunegala | 0.1% | 2,346 | 2,685 | +339 🟩 | 2.6% | 2.8% | +0.2 🟩 pp |
| Attanagalla `LK-1227` | Gampaha | 0.1% | 1,105 | 1,491 | +386 🟩 | 0.6% | 0.8% | +0.1 🟩 pp |
| Panduwasnuwara West `LK-6145` | Kurunegala | 0.0% | 230 | 346 | +116 🟩 | 0.3% | 0.5% | +0.1 🟩 pp |
| Kalutara `LK-1321` | Kalutara | 0.1% | 1,451 | 1,741 | +290 🟩 | 0.9% | 1.0% | +0.1 🟩 pp |
| Karandeniya `LK-3109` | Galle | 0.0% | 84 | 172 | +88 🟩 | 0.1% | 0.3% | +0.1 🟩 pp |
| Elahera `LK-7218` | Polonnaruwa | 0.0% | 35 | 102 | +67 🟩 | 0.1% | 0.2% | +0.1 🟩 pp |
| Gonapinuwala `LK-3134` | Galle | 0.0% | 10 | 41 | +31 🟩 | 0.0% | 0.2% | +0.1 🟩 pp |
| Pathahewaheta `LK-2145` | Kandy | 0.2% | 3,602 | 3,829 | +227 🟩 | 6.2% | 6.3% | +0.1 🟩 pp |
| Madampe `LK-6236` | Puttalam | 0.0% | 652 | 726 | +74 🟩 | 1.4% | 1.5% | +0.1 🟩 pp |
| Nikaweratiya `LK-6121` | Kurunegala | 0.0% | 229 | 298 | +69 🟩 | 0.6% | 0.7% | +0.1 🟩 pp |
| Buttala `LK-8224` | Monaragala | 0.0% | 340 | 461 | +121 🟩 | 0.6% | 0.8% | +0.1 🟩 pp |
| Kaduwela `LK-1109` | Colombo | 0.2% | 3,524 | 4,210 | +686 🟩 | 1.4% | 1.5% | +0.1 🟩 pp |
| Mulatiyana `LK-3212` | Matara | 0.0% | 238 | 304 | +66 🟩 | 0.5% | 0.6% | +0.1 🟩 pp |
| Weeraketiya `LK-3321` | Hambantota | 0.0% | 16 | 73 | +57 🟩 | 0.0% | 0.2% | +0.1 🟩 pp |
| Kuliyapitiya East `LK-6169` | Kurunegala | 0.0% | 146 | 234 | +88 🟩 | 0.3% | 0.4% | +0.1 🟩 pp |
| Ja Ela `LK-1221` | Gampaha | 0.2% | 4,235 | 4,533 | +298 🟩 | 2.1% | 2.2% | +0.1 🟩 pp |
| Dompe `LK-1230` | Gampaha | 0.0% | 514 | 754 | +240 🟩 | 0.3% | 0.4% | +0.1 🟩 pp |
| Doluwa `LK-2142` | Kandy | 0.4% | 9,274 | 9,879 | +605 🟩 | 18.6% | 18.7% | +0.1 🟩 pp |
| Weerabugedara `LK-6166` | Kurunegala | 0.0% | 66 | 110 | +44 🟩 | 0.2% | 0.3% | +0.1 🟩 pp |
| Nuwaragam Palatha Central `LK-7115` | Anuradhapura | 0.0% | 402 | 546 | +144 🟩 | 0.7% | 0.8% | +0.1 🟩 pp |
| Rambewa `LK-7118` | Anuradhapura | 0.0% | 19 | 63 | +44 🟩 | 0.1% | 0.2% | +0.1 🟩 pp |
| Rattota `LK-2230` | Matale | 0.5% | 11,467 | 12,036 | +569 🟩 | 22.3% | 22.4% | +0.1 🟩 pp |
| Balapitiya `LK-3106` | Galle | 0.0% | 77 | 149 | +72 🟩 | 0.1% | 0.2% | +0.1 🟩 pp |
| Ampara `LK-5215` | Ampara | 0.0% | 145 | 207 | +62 🟩 | 0.3% | 0.4% | +0.1 🟩 pp |
| Devinuwara `LK-3245` | Matara | 0.0% | 51 | 101 | +50 🟩 | 0.1% | 0.2% | +0.1 🟩 pp |
| Habaraduwa `LK-3154` | Galle | 0.0% | 55 | 118 | +63 🟩 | 0.1% | 0.2% | +0.1 🟩 pp |
| Horana `LK-1309` | Kalutara | 0.1% | 1,530 | 1,935 | +405 🟩 | 1.3% | 1.4% | +0.1 🟩 pp |
| Wilgamuwa `LK-2227` | Matale | 0.0% | 8 | 41 | +33 🟩 | 0.0% | 0.1% | +0.1 🟩 pp |
| Ganewatta `LK-6133` | Kurunegala | 0.0% | 64 | 109 | +45 🟩 | 0.2% | 0.3% | +0.1 🟩 pp |
| Athuraliya `LK-3215` | Matara | 0.0% | 514 | 552 | +38 🟩 | 1.6% | 1.7% | +0.1 🟩 pp |
| Angunakolapelessa `LK-3318` | Hambantota | 0.0% | 6 | 54 | +48 🟩 | 0.0% | 0.1% | +0.1 🟩 pp |
| Mahawilachchiya `LK-7112` | Anuradhapura | 0.0% | 6 | 27 | +21 🟩 | 0.0% | 0.1% | +0.1 🟩 pp |
| Kotawehera `LK-6115` | Kurunegala | 0.0% | 7 | 28 | +21 🟩 | 0.0% | 0.1% | +0.1 🟩 pp |
| Padukka `LK-1118` | Colombo | 0.1% | 1,237 | 1,444 | +207 🟩 | 1.9% | 2.0% | +0.1 🟩 pp |
| Galigamuwa `LK-9215` | Kegalle | 0.1% | 2,487 | 2,524 | +37 🟩 | 3.3% | 3.4% | +0.1 🟩 pp |
| Mahaoya `LK-5209` | Ampara | 0.0% | 14 | 35 | +21 🟩 | 0.1% | 0.1% | +0.1 🟩 pp |
| Medagama `LK-8209` | Monaragala | 0.0% | 36 | 80 | +44 🟩 | 0.1% | 0.2% | +0.1 🟩 pp |
| Medawachchiya `LK-7109` | Anuradhapura | 0.0% | 86 | 137 | +51 🟩 | 0.2% | 0.3% | +0.1 🟩 pp |
| Dimbulagala `LK-7212` | Polonnaruwa | 0.1% | 2,367 | 2,618 | +251 🟩 | 3.0% | 3.0% | +0.1 🟩 pp |
| Sooriyawewa `LK-3303` | Hambantota | 0.0% | 16 | 59 | +43 🟩 | 0.0% | 0.1% | +0.1 🟩 pp |
| Minuwangoda `LK-1215` | Gampaha | 0.0% | 662 | 884 | +222 🟩 | 0.4% | 0.4% | +0.1 🟩 pp |
| Ambanpola `LK-6112` | Kurunegala | 0.0% | 13 | 33 | +20 🟩 | 0.1% | 0.1% | +0.1 🟩 pp |
| Giribawa `LK-6103` | Kurunegala | 0.0% | 14 | 40 | +26 🟩 | 0.0% | 0.1% | +0.1 🟩 pp |
| Siyambalanduwa `LK-8212` | Monaragala | 0.0% | 40 | 90 | +50 🟩 | 0.1% | 0.1% | +0.1 🟩 pp |
| Madulla `LK-8206` | Monaragala | 0.0% | 19 | 47 | +28 🟩 | 0.1% | 0.1% | +0.1 🟩 pp |
| Ududumbara `LK-2118` | Kandy | 0.1% | 1,639 | 1,694 | +55 🟩 | 7.3% | 7.4% | +0.1 🟩 pp |
| Padiyathalawa `LK-5206` | Ampara | 0.0% | 22 | 38 | +16 🟩 | 0.1% | 0.2% | +0.1 🟩 pp |
| Thanamalwila `LK-8230` | Monaragala | 0.0% | 17 | 38 | +21 🟩 | 0.1% | 0.1% | +0.1 🟩 pp |
| Ibbagamuwa `LK-6130` | Kurunegala | 0.0% | 689 | 818 | +129 🟩 | 0.8% | 0.9% | +0.1 🟩 pp |
| Thambuththegama `LK-7145` | Anuradhapura | 0.0% | 17 | 46 | +29 🟩 | 0.0% | 0.1% | +0.1 🟩 pp |
| Katuwana `LK-3324` | Hambantota | 0.0% | 25 | 57 | +32 🟩 | 0.1% | 0.1% | +0.1 🟩 pp |
| Beruwala `LK-1324` | Kalutara | 0.1% | 1,286 | 1,509 | +223 🟩 | 0.8% | 0.8% | +0.1 🟩 pp |
| Bope-Poddala `LK-3142` | Galle | 0.0% | 410 | 503 | +93 🟩 | 0.8% | 0.9% | +0.1 🟩 pp |
| Weligama `LK-3239` | Matara | 0.0% | 158 | 206 | +48 🟩 | 0.2% | 0.3% | +0.1 🟩 pp |
| Thirappane `LK-7151` | Anuradhapura | 0.0% | 42 | 65 | +23 🟩 | 0.2% | 0.2% | +0.1 🟩 pp |
| Ehetuwewa `LK-6109` | Kurunegala | 0.0% | 10 | 26 | +16 🟩 | 0.0% | 0.1% | +0.1 🟩 pp |
| Galewela `LK-2203` | Matale | 0.0% | 875 | 1,024 | +149 🟩 | 1.2% | 1.3% | +0.1 🟩 pp |
| Kirinda Puhulwella `LK-3233` | Matara | 0.0% | 6 | 17 | +11 🟩 | 0.0% | 0.1% | +0.1 🟩 pp |
| Medirigiriya `LK-7206` | Polonnaruwa | 0.0% | 26 | 67 | +41 🟩 | 0.0% | 0.1% | +0.1 🟩 pp |
| Vadamaradchchi East `LK-4124` | Jaffna | 0.4% | 8,741 | 9,276 | +535 🟩 | 68.5% | 68.5% | +0.1 🟩 pp |
| Matara Four Gravets `LK-3242` | Matara | 0.0% | 271 | 354 | +83 🟩 | 0.2% | 0.3% | +0.1 🟩 pp |
| Gangawata Korale `LK-2130` | Kandy | 0.7% | 16,127 | 15,674 | -453 🟥 | 10.2% | 10.2% | +0.1 🟩 pp |
| Galenbidunuwewa `LK-7127` | Anuradhapura | 0.0% | 43 | 74 | +31 🟩 | 0.1% | 0.1% | +0.1 🟩 pp |
| Palugaswewa `LK-7157` | Anuradhapura | 0.0% | 61 | 80 | +19 🟩 | 0.4% | 0.4% | 0.0 pp |
| Padavi Sri Pura `LK-5303` | Trincomalee | 0.0% | 8 | 14 | +6 🟩 | 0.1% | 0.1% | 0.0 pp |
| Sevanagala `LK-8233` | Monaragala | 0.0% | 19 | 46 | +27 🟩 | 0.0% | 0.1% | 0.0 pp |
| Kebithigollewa `LK-7106` | Anuradhapura | 0.0% | 14 | 29 | +15 🟩 | 0.1% | 0.1% | 0.0 pp |
| Bandaragama `LK-1306` | Kalutara | 0.0% | 321 | 422 | +101 🟩 | 0.3% | 0.3% | 0.0 pp |
| Rasnayakapura `LK-6118` | Kurunegala | 0.0% | 26 | 41 | +15 🟩 | 0.1% | 0.2% | 0.0 pp |
| Harispattuwa `LK-2133` | Kandy | 0.1% | 1,591 | 1,739 | +148 🟩 | 1.8% | 1.8% | 0.0 pp |
| Hakmana `LK-3230` | Matara | 0.0% | 9 | 24 | +15 🟩 | 0.0% | 0.1% | 0.0 pp |
| Rajanganaya `LK-7142` | Anuradhapura | 0.0% | 13 | 30 | +17 🟩 | 0.0% | 0.1% | 0.0 pp |
| Pasbagekorale `LK-2157` | Kandy | 0.9% | 19,043 | 20,863 | +1,820 🟩 | 31.8% | 31.8% | 0.0 pp |
| Mawathagama `LK-6160` | Kurunegala | 0.1% | 2,706 | 3,024 | +318 🟩 | 4.2% | 4.3% | 0.0 pp |
| Thihagoda `LK-3236` | Matara | 0.0% | 20 | 35 | +15 🟩 | 0.1% | 0.1% | 0.0 pp |
| Walasmulla `LK-3325` | Hambantota | 0.0% | 15 | 36 | +21 🟩 | 0.0% | 0.1% | 0.0 pp |
| Panadura `LK-1303` | Kalutara | 0.0% | 969 | 1,069 | +100 🟩 | 0.5% | 0.6% | 0.0 pp |
| Uhana `LK-5212` | Ampara | 0.0% | 22 | 47 | +25 🟩 | 0.0% | 0.1% | 0.0 pp |
| Bentota `LK-3103` | Galle | 0.0% | 88 | 105 | +17 🟩 | 0.2% | 0.2% | 0.0 pp |
| Kolonnawa `LK-1106` | Colombo | 0.7% | 13,050 | 14,647 | +1,597 🟩 | 6.8% | 6.8% | 0.0 pp |
| Horowpathana `LK-7124` | Anuradhapura | 0.0% | 38 | 56 | +18 🟩 | 0.1% | 0.1% | 0.0 pp |
| Embilipitiya `LK-9148` | Ratnapura | 0.0% | 93 | 158 | +65 🟩 | 0.1% | 0.1% | 0.0 pp |
| Maho `LK-6124` | Kurunegala | 0.0% | 234 | 279 | +45 🟩 | 0.4% | 0.4% | 0.0 pp |
| Damana `LK-5242` | Ampara | 0.0% | 33 | 44 | +11 🟩 | 0.1% | 0.1% | 0.0 pp |
| Tirukkovil `LK-5245` | Ampara | 1.2% | 23,952 | 27,725 | +3,773 🟩 | 94.8% | 94.8% | 0.0 pp |
| Thalawa `LK-7148` | Anuradhapura | 0.0% | 95 | 114 | +19 🟩 | 0.2% | 0.2% | 0.0 pp |
| Lankapura `LK-7209` | Polonnaruwa | 0.0% | 18 | 28 | +10 🟩 | 0.0% | 0.1% | 0.0 pp |
| Galnewa `LK-7163` | Anuradhapura | 0.0% | 80 | 99 | +19 🟩 | 0.2% | 0.3% | 0.0 pp |
| Welipitiya `LK-3221` | Matara | 0.0% | 69 | 84 | +15 🟩 | 0.1% | 0.2% | 0.0 pp |
| Ambalantota `LK-3315` | Hambantota | 0.0% | 197 | 231 | +34 🟩 | 0.3% | 0.3% | 0.0 pp |
| Kuliyapitiya West `LK-6172` | Kurunegala | 0.0% | 626 | 681 | +55 🟩 | 0.8% | 0.8% | 0.0 pp |
| Vanathavilluwa `LK-6206` | Puttalam | 0.0% | 727 | 835 | +108 🟩 | 4.2% | 4.2% | 0.0 pp |
| Hatharaliyadda `LK-2134` | Kandy | 0.0% | 448 | 469 | +21 🟩 | 1.5% | 1.5% | 0.0 pp |
| Palagala `LK-7166` | Anuradhapura | 0.0% | 95 | 112 | +17 🟩 | 0.3% | 0.3% | 0.0 pp |
| Lunugamwehera `LK-3306` | Hambantota | 0.0% | 35 | 45 | +10 🟩 | 0.1% | 0.1% | 0.0 pp |
| Okewela `LK-3327` | Hambantota | 0.0% | 4 | 6 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Bibile `LK-8203` | Monaragala | 0.0% | 888 | 1,045 | +157 🟩 | 2.2% | 2.2% | 0.0 pp |
| Nochchiyagama `LK-7139` | Anuradhapura | 0.0% | 215 | 244 | +29 🟩 | 0.4% | 0.4% | 0.0 pp |
| Karuwalagaswewa `LK-6209` | Puttalam | 0.0% | 49 | 57 | +8 🟩 | 0.2% | 0.2% | 0.0 pp |
| Minipe `LK-2121` | Kandy | 0.0% | 32 | 38 | +6 🟩 | 0.1% | 0.1% | 0.0 pp |
| Welimada `LK-8130` | Badulla | 0.5% | 11,383 | 11,919 | +536 🟩 | 11.3% | 11.3% | 0.0 pp |
| Dikwella `LK-3248` | Matara | 0.0% | 68 | 72 | +4 🟩 | 0.1% | 0.1% | 0.0 pp |
| Mahiyanganaya `LK-8103` | Badulla | 0.0% | 81 | 97 | +16 🟩 | 0.1% | 0.1% | 0.0 pp |
| Wellawaya `LK-8221` | Monaragala | 0.0% | 413 | 505 | +92 🟩 | 0.7% | 0.7% | 0.0 pp |
| Panduwasnuwara East `LK-6148` | Kurunegala | 0.0% | 59 | 62 | +3 🟩 | 0.2% | 0.2% | 0.0 pp |
| Gampaha `LK-1224` | Gampaha | 0.0% | 855 | 883 | +28 🟩 | 0.4% | 0.4% | 0.0 pp |
| Dehiattakandiya `LK-5203` | Ampara | 0.0% | 55 | 59 | +4 🟩 | 0.1% | 0.1% | 0.0 pp |
| Ambalangoda `LK-3133` | Galle | 0.0% | 128 | 131 | +3 🟩 | 0.2% | 0.2% | 0.0 pp |
| Matugama `LK-1330` | Kalutara | 0.3% | 6,357 | 6,725 | +368 🟩 | 7.8% | 7.8% | 0.0 pp |
| Wariyapola `LK-6136` | Kurunegala | 0.0% | 212 | 225 | +13 🟩 | 0.3% | 0.3% | 0.0 pp |
| Madurawala `LK-1315` | Kalutara | 0.1% | 2,669 | 2,848 | +179 🟩 | 7.8% | 7.8% | 0.0 pp |
| Rideemaliyadda `LK-8106` | Badulla | 0.0% | 101 | 114 | +13 🟩 | 0.2% | 0.2% | 0.0 pp |
| Nawagattegama `LK-6212` | Puttalam | 0.0% | 22 | 25 | +3 🟩 | 0.2% | 0.1% | 0.0 pp |
| Mallawapitiya `LK-6157` | Kurunegala | 0.0% | 923 | 1,035 | +112 🟩 | 1.8% | 1.7% | 0.0 pp |
| Mawanella `LK-9206` | Kegalle | 0.1% | 1,049 | 1,164 | +115 🟩 | 0.9% | 0.9% | 0.0 pp |
| Rambukkana `LK-9203` | Kegalle | 0.0% | 811 | 838 | +27 🟩 | 1.0% | 1.0% | 0.0 pp |
| Beliatta `LK-3330` | Hambantota | 0.0% | 56 | 48 | -8 🟥 | 0.1% | 0.1% | 0.0 pp |
| Padaviya `LK-7103` | Anuradhapura | 0.0% | 14 | 9 | -5 🟥 | 0.1% | 0.0% | 0.0 pp |
| Godakawela `LK-9142` | Ratnapura | 0.6% | 12,287 | 12,597 | +310 🟩 | 16.1% | 16.0% | 0.0 pp |
| Dankotuwa `LK-6248` | Puttalam | 0.0% | 734 | 719 | -15 🟥 | 1.2% | 1.1% | 0.0 pp |
| Alawwa `LK-6184` | Kurunegala | 0.0% | 120 | 101 | -19 🟥 | 0.2% | 0.2% | 0.0 pp |
| Ukuwela `LK-2233` | Matale | 0.4% | 8,890 | 9,424 | +534 🟩 | 13.1% | 13.0% | 0.0 pp |
| Kahatagasdigiliya `LK-7121` | Anuradhapura | 0.0% | 145 | 145 | +0 | 0.4% | 0.3% | 0.0 pp |
| Millaniya `LK-1318` | Kalutara | 0.1% | 1,264 | 1,340 | +76 🟩 | 2.4% | 2.4% | 0.0 pp |
| Polgahawela `LK-6187` | Kurunegala | 0.1% | 1,285 | 1,305 | +20 🟩 | 2.0% | 1.9% | 0.0 pp |
| Tangalle `LK-3333` | Hambantota | 0.0% | 114 | 94 | -20 🟥 | 0.2% | 0.1% | 0.0 pp |
| Welivitiya-Divitura `LK-3130` | Galle | 0.0% | 935 | 923 | -12 🟥 | 3.2% | 3.1% | 0.0 pp |
| Pallama `LK-6227` | Puttalam | 0.0% | 243 | 264 | +21 🟩 | 1.0% | 0.9% | 0.0 pp |
| Sainthamaruthu `LK-5225` | Ampara | 0.0% | 30 | 20 | -10 🟥 | 0.1% | 0.1% | -0.1 🟥 pp |
| Udunuwara `LK-2139` | Kandy | 0.1% | 2,535 | 2,695 | +160 🟩 | 2.3% | 2.2% | -0.1 🟥 pp |
| Higurakgoda `LK-7203` | Polonnaruwa | 0.0% | 197 | 174 | -23 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Malimbada `LK-3224` | Matara | 0.0% | 52 | 31 | -21 🟥 | 0.1% | 0.1% | -0.1 🟥 pp |
| Galgamuwa `LK-6106` | Kurunegala | 0.0% | 177 | 159 | -18 🟥 | 0.3% | 0.3% | -0.1 🟥 pp |
| Nachchaduwa `LK-7136` | Anuradhapura | 0.0% | 32 | 17 | -15 🟥 | 0.1% | 0.1% | -0.1 🟥 pp |
| Agalawatta `LK-1333` | Kalutara | 0.0% | 782 | 755 | -27 🟥 | 2.1% | 2.1% | -0.1 🟥 pp |
| Kattankudy `LK-5124` | Batticaloa | 0.0% | 50 | 23 | -27 🟥 | 0.1% | 0.1% | -0.1 🟥 pp |
| Kegalle `LK-9212` | Kegalle | 0.1% | 2,020 | 2,027 | +7 🟩 | 2.2% | 2.1% | -0.1 🟥 pp |
| Wennappuwa `LK-6245` | Puttalam | 0.0% | 789 | 698 | -91 🟥 | 1.2% | 1.1% | -0.1 🟥 pp |
| Arachchikattuwa `LK-6230` | Puttalam | 0.1% | 1,263 | 1,278 | +15 🟩 | 3.1% | 3.0% | -0.1 🟥 pp |
| Narammala `LK-6181` | Kurunegala | 0.0% | 325 | 289 | -36 🟥 | 0.6% | 0.5% | -0.1 🟥 pp |
| Valikamam West (Chankanai) `LK-4106` | Jaffna | 1.9% | 43,591 | 42,348 | -1,243 🟥 | 93.9% | 93.8% | -0.1 🟥 pp |
| Thissamaharama `LK-3309` | Hambantota | 0.0% | 300 | 252 | -48 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Galle 4 Gravets `LK-3139` | Galle | 0.0% | 724 | 661 | -63 🟥 | 0.7% | 0.6% | -0.1 🟥 pp |
| Hambantota `LK-3312` | Hambantota | 0.0% | 438 | 446 | +8 🟩 | 0.8% | 0.7% | -0.1 🟥 pp |
| Kekirawa `LK-7154` | Anuradhapura | 0.1% | 1,232 | 1,276 | +44 🟩 | 2.1% | 2.0% | -0.1 🟥 pp |
| Elpitiya `LK-3112` | Galle | 0.1% | 1,475 | 1,434 | -41 🟥 | 2.3% | 2.2% | -0.1 🟥 pp |
| Weligepola `LK-9145` | Ratnapura | 0.0% | 348 | 339 | -9 🟥 | 1.1% | 1.0% | -0.1 🟥 pp |
| Ipalogama `LK-7160` | Anuradhapura | 0.0% | 134 | 82 | -52 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Bulathkohipitiya `LK-9224` | Kegalle | 0.3% | 7,621 | 7,247 | -374 🟥 | 16.2% | 16.0% | -0.2 🟥 pp |
| Aranayake `LK-9209` | Kegalle | 0.1% | 1,292 | 1,180 | -112 🟥 | 1.9% | 1.7% | -0.2 🟥 pp |
| Nanaddan `LK-4212` | Mannar | 0.2% | 3,436 | 3,743 | +307 🟩 | 19.2% | 19.0% | -0.2 🟥 pp |
| Soranathota `LK-8115` | Badulla | 0.2% | 3,977 | 4,256 | +279 🟩 | 17.6% | 17.4% | -0.2 🟥 pp |
| Yatinuwara `LK-2136` | Kandy | 0.1% | 2,310 | 2,227 | -83 🟥 | 2.2% | 2.0% | -0.2 🟥 pp |
| Sammanthurai `LK-5218` | Ampara | 0.4% | 7,051 | 8,342 | +1,291 🟩 | 11.7% | 11.5% | -0.2 🟥 pp |
| Nuwaragam Palatha East `LK-7133` | Anuradhapura | 0.0% | 364 | 238 | -126 🟥 | 0.5% | 0.3% | -0.2 🟥 pp |
| Kurunegala `LK-6154` | Kurunegala | 0.1% | 2,500 | 2,568 | +68 🟩 | 3.1% | 2.9% | -0.2 🟥 pp |
| Dambulla `LK-2206` | Matale | 0.0% | 741 | 659 | -82 🟥 | 1.0% | 0.8% | -0.2 🟥 pp |
| Poojapitiya `LK-2106` | Kandy | 0.1% | 1,585 | 1,521 | -64 🟥 | 2.7% | 2.5% | -0.2 🟥 pp |
| Koralai Pattu West `LK-5106` | Batticaloa | 0.0% | 72 | 26 | -46 🟥 | 0.3% | 0.1% | -0.2 🟥 pp |
| Lahugala `LK-5251` | Ampara | 0.0% | 566 | 638 | +72 🟩 | 6.3% | 6.1% | -0.2 🟥 pp |
| Pelmadulla `LK-9124` | Ratnapura | 0.5% | 11,306 | 11,641 | +335 🟩 | 12.6% | 12.4% | -0.2 🟥 pp |
| Akurana `LK-2109` | Kandy | 0.2% | 3,211 | 3,430 | +219 🟩 | 5.1% | 4.8% | -0.2 🟥 pp |
| Kantale `LK-5321` | Trincomalee | 0.1% | 1,514 | 1,525 | +11 🟩 | 3.2% | 3.0% | -0.2 🟥 pp |
| Kandavalai `LK-4506` | Kilinochchi | 1.0% | 20,504 | 21,966 | +1,462 🟩 | 88.4% | 88.1% | -0.3 🟥 pp |
| Kiriella `LK-9109` | Ratnapura | 0.0% | 1,064 | 907 | -157 🟥 | 3.0% | 2.7% | -0.3 🟥 pp |
| Medadumbara `LK-2124` | Kandy | 0.5% | 9,891 | 10,271 | +380 🟩 | 16.2% | 15.9% | -0.3 🟥 pp |
| Imbulpe `LK-9115` | Ratnapura | 0.4% | 7,563 | 8,019 | +456 🟩 | 12.7% | 12.4% | -0.3 🟥 pp |
| Yakkalamulla `LK-3148` | Galle | 0.1% | 2,470 | 2,366 | -104 🟥 | 5.4% | 5.1% | -0.3 🟥 pp |
| Opanayake `LK-9121` | Ratnapura | 0.1% | 1,764 | 1,717 | -47 🟥 | 6.6% | 6.3% | -0.3 🟥 pp |
| Kalpitiya `LK-6203` | Puttalam | 0.2% | 3,955 | 4,107 | +152 🟩 | 4.6% | 4.2% | -0.3 🟥 pp |
| Nagoda `LK-3124` | Galle | 0.1% | 3,506 | 3,185 | -321 🟥 | 6.5% | 6.1% | -0.4 🟥 pp |
| Kandeketiya `LK-8112` | Badulla | 0.0% | 768 | 780 | +12 🟩 | 3.3% | 2.9% | -0.4 🟥 pp |
| Nintavur `LK-5230` | Ampara | 0.0% | 976 | 1,002 | +26 🟩 | 3.7% | 3.3% | -0.4 🟥 pp |
| Valikamam East (Kopay) `LK-4118` | Jaffna | 3.1% | 66,581 | 68,751 | +2,170 🟩 | 90.9% | 90.5% | -0.4 🟥 pp |
| Pallepola `LK-2212` | Matale | 0.0% | 1,071 | 996 | -75 🟥 | 3.6% | 3.1% | -0.5 🟥 pp |
| Kolonna `LK-9151` | Ratnapura | 0.2% | 3,986 | 4,105 | +119 🟩 | 8.7% | 8.2% | -0.5 🟥 pp |
| Elapatha `LK-9127` | Ratnapura | 0.1% | 1,780 | 1,594 | -186 🟥 | 4.7% | 4.1% | -0.6 🟥 pp |
| Palindanuwara `LK-1336` | Kalutara | 0.2% | 3,758 | 3,492 | -266 🟥 | 7.4% | 6.8% | -0.6 🟥 pp |
| Chilaw `LK-6233` | Puttalam | 0.2% | 4,288 | 3,981 | -307 🟥 | 6.9% | 6.3% | -0.6 🟥 pp |
| Uvaparanagama `LK-8127` | Badulla | 0.4% | 9,614 | 9,612 | -2 🟥 | 12.3% | 11.7% | -0.6 🟥 pp |
| Katharagama `LK-8227` | Monaragala | 0.0% | 674 | 554 | -120 🟥 | 3.7% | 3.1% | -0.6 🟥 pp |
| Nivithigala `LK-9136` | Ratnapura | 0.4% | 9,430 | 8,934 | -496 🟥 | 15.7% | 15.0% | -0.7 🟥 pp |
| Dodangoda `LK-1327` | Kalutara | 0.3% | 6,378 | 6,248 | -130 🟥 | 10.0% | 9.3% | -0.7 🟥 pp |
| Manmunai South West `LK-5130` | Batticaloa | 1.1% | 23,436 | 25,073 | +1,637 🟩 | 94.8% | 94.0% | -0.8 🟥 pp |
| Ayagama `LK-9130` | Ratnapura | 0.2% | 3,840 | 3,483 | -357 🟥 | 12.4% | 11.6% | -0.8 🟥 pp |
| Muthur `LK-5327` | Trincomalee | 1.0% | 18,687 | 23,131 | +4,444 🟩 | 33.0% | 32.2% | -0.8 🟥 pp |
| Town & Gravets `LK-5315` | Trincomalee | 2.2% | 47,792 | 48,282 | +490 🟩 | 49.0% | 48.2% | -0.9 🟥 pp |
| Valikamam North (Thllippalai) `LK-4112` | Jaffna | 1.7% | 25,325 | 38,119 | +12,794 🟩 | 85.8% | 84.9% | -0.9 🟥 pp |
| Thenmaradchi (Chavakachcheri) `LK-4130` | Jaffna | 2.8% | 59,949 | 62,137 | +2,188 🟩 | 92.7% | 91.7% | -1.0 🟥 pp |
| Jaffna `LK-4136` | Jaffna | 0.8% | 19,033 | 17,820 | -1,213 🟥 | 37.7% | 36.7% | -1.0 🟥 pp |
| Kinniya `LK-5324` | Trincomalee | 0.1% | 2,439 | 2,378 | -61 🟥 | 3.8% | 2.7% | -1.0 🟥 pp |
| Ganga Ihala Korale `LK-2154` | Kandy | 0.3% | 6,229 | 6,018 | -211 🟥 | 11.3% | 10.2% | -1.1 🟥 pp |
| Puttalam `LK-6215` | Puttalam | 0.2% | 4,854 | 4,446 | -408 🟥 | 5.9% | 4.7% | -1.2 🟥 pp |
| Thunukkai `LK-4403` | Mullaitivu | 0.4% | 8,682 | 9,188 | +506 🟩 | 89.5% | 88.3% | -1.3 🟥 pp |
| Thawalama `LK-3118` | Galle | 0.1% | 1,661 | 1,183 | -478 🟥 | 5.1% | 3.8% | -1.3 🟥 pp |
| Manthai West `LK-4206` | Mannar | 0.3% | 6,127 | 7,488 | +1,361 🟩 | 41.5% | 40.1% | -1.4 🟥 pp |
| Maritimepattu `LK-4415` | Mullaitivu | 1.2% | 20,709 | 25,829 | +5,120 🟩 | 71.6% | 70.2% | -1.4 🟥 pp |
| Laggala `LK-2224` | Matale | 0.0% | 206 | 36 | -170 🟥 | 1.7% | 0.2% | -1.5 🟥 pp |
| Koralai Pattu North `LK-5103` | Batticaloa | 0.9% | 17,356 | 20,144 | +2,788 🟩 | 80.6% | 79.1% | -1.5 🟥 pp |
| Navithanveli `LK-5216` | Ampara | 0.5% | 10,271 | 11,635 | +1,364 🟩 | 54.8% | 53.2% | -1.6 🟥 pp |
| Karachchi `LK-4509` | Kilinochchi | 2.7% | 51,086 | 60,727 | +9,641 🟩 | 83.1% | 81.4% | -1.7 🟥 pp |
| Pitabaddara `LK-3203` | Matara | 0.1% | 3,092 | 2,094 | -998 🟥 | 6.0% | 4.3% | -1.8 🟥 pp |
| Meegahakiula `LK-8109` | Badulla | 0.1% | 1,883 | 1,767 | -116 🟥 | 9.5% | 7.8% | -1.8 🟥 pp |
| Welikanda `LK-7210` | Polonnaruwa | 0.1% | 3,508 | 3,245 | -263 🟥 | 10.4% | 8.5% | -1.9 🟥 pp |
| Thambalagamuwa `LK-5318` | Trincomalee | 0.2% | 4,873 | 5,089 | +216 🟩 | 17.1% | 15.1% | -2.0 🟥 pp |
| Kuchchaweli `LK-5306` | Trincomalee | 0.5% | 9,152 | 10,196 | +1,044 🟩 | 27.6% | 25.6% | -2.0 🟥 pp |
| Musali `LK-4215` | Mannar | 0.0% | 354 | 419 | +65 🟩 | 4.4% | 2.3% | -2.1 🟥 pp |
| Karaitivu `LK-5227` | Ampara | 0.5% | 9,788 | 10,919 | +1,131 🟩 | 58.1% | 56.0% | -2.1 🟥 pp |
| Haldummulla `LK-8142` | Badulla | 0.7% | 16,445 | 16,140 | -305 🟥 | 43.8% | 41.6% | -2.2 🟥 pp |
| Kotapola `LK-3206` | Matara | 0.3% | 9,430 | 7,749 | -1,681 🟥 | 14.9% | 12.7% | -2.2 🟥 pp |
| Kalawana `LK-9133` | Ratnapura | 0.2% | 6,789 | 5,584 | -1,205 🟥 | 13.2% | 11.0% | -2.2 🟥 pp |
| Mundel `LK-6218` | Puttalam | 0.4% | 9,328 | 9,244 | -84 🟥 | 15.1% | 12.7% | -2.4 🟥 pp |
| Poonakary `LK-4512` | Kilinochchi | 0.7% | 14,220 | 16,294 | +2,074 🟩 | 70.0% | 67.6% | -2.5 🟥 pp |
| Vavuniya `LK-4309` | Vavuniya | 4.0% | 92,034 | 88,683 | -3,351 🟥 | 78.3% | 75.8% | -2.5 🟥 pp |
| Islands North (Kayts) `LK-4103` | Jaffna | 0.2% | 5,401 | 5,170 | -231 🟥 | 54.7% | 52.1% | -2.6 🟥 pp |
| Koralai Pattu South `LK-5110` | Batticaloa | 1.1% | 24,280 | 25,536 | +1,256 🟩 | 92.9% | 90.2% | -2.6 🟥 pp |
| Mannar Town `LK-4203` | Mannar | 0.4% | 10,401 | 9,927 | -474 🟥 | 20.4% | 17.2% | -3.2 🟥 pp |
| Islands South (Velanai) `LK-4139` | Jaffna | 0.5% | 12,584 | 11,846 | -738 🟥 | 75.2% | 71.4% | -3.8 🟥 pp |
| Vavuniya North `LK-4303` | Vavuniya | 0.6% | 10,363 | 12,616 | +2,253 🟩 | 89.9% | 85.8% | -4.2 🟥 pp |
| Nallur `LK-4133` | Jaffna | 2.8% | 61,569 | 62,589 | +1,020 🟩 | 90.4% | 85.9% | -4.5 🟥 pp |
| Delft `LK-4142` | Jaffna | 0.0% | 1,439 | 1,002 | -437 🟥 | 37.6% | 31.7% | -5.9 🟥 pp |
| Vengalacheddikulam `LK-4312` | Vavuniya | 0.6% | 16,680 | 12,803 | -3,877 🟥 | 55.8% | 49.7% | -6.1 🟥 pp |
| Manmunai Pattu `LK-5127` | Batticaloa | 1.0% | 21,350 | 23,159 | +1,809 🟩 | 69.6% | 63.4% | -6.2 🟥 pp |
| Puthukkudiyiruppu `LK-4409` | Mullaitivu | 1.4% | 20,209 | 31,073 | +10,864 🟩 | 84.8% | 78.6% | -6.2 🟥 pp |

***Koralai Pattu Central** gained the most share at **+79.0pp**. **Puthukkudiyiruppu** saw the steepest share decline at **-6.2pp**.*

### Islam

| DSD | District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Musali `LK-4215` | Mannar | 0.7% | 4,848 | 13,581 | +8,733 🟩 | 59.7% | 74.9% | +15.1 🟩 pp |
| Vengalacheddikulam `LK-4312` | Vavuniya | 0.4% | 6,909 | 9,146 | +2,237 🟩 | 23.1% | 35.5% | +12.4 🟩 pp |
| Mannar Town `LK-4203` | Mannar | 0.7% | 9,098 | 15,373 | +6,275 🟩 | 17.8% | 26.6% | +8.8 🟩 pp |
| Kolonnawa `LK-1106` | Colombo | 3.2% | 44,189 | 67,100 | +22,911 🟩 | 23.1% | 31.3% | +8.3 🟩 pp |
| Dehiwala `LK-1130` | Colombo | 1.4% | 20,109 | 28,538 | +8,429 🟩 | 22.6% | 30.4% | +7.8 🟩 pp |
| Manmunai Pattu `LK-5127` | Batticaloa | 0.5% | 7,565 | 11,254 | +3,689 🟩 | 24.6% | 30.8% | +6.2 🟩 pp |
| Madhu `LK-4209` | Mannar | 0.1% | 559 | 1,196 | +637 🟩 | 7.2% | 12.6% | +5.3 🟩 pp |
| Ratmalana `LK-1131` | Colombo | 0.7% | 10,837 | 13,852 | +3,015 🟩 | 11.3% | 15.7% | +4.4 🟩 pp |
| Galle 4 Gravets `LK-3139` | Galle | 1.9% | 32,865 | 39,021 | +6,156 🟩 | 32.3% | 36.0% | +3.7 🟩 pp |
| Beruwala `LK-1324` | Kalutara | 3.3% | 57,228 | 69,141 | +11,913 🟩 | 34.7% | 38.2% | +3.5 🟩 pp |
| Nanaddan `LK-4212` | Mannar | 0.1% | 668 | 1,405 | +737 🟩 | 3.7% | 7.1% | +3.4 🟩 pp |
| Manthai West `LK-4206` | Mannar | 0.1% | 1,339 | 2,328 | +989 🟩 | 9.1% | 12.5% | +3.4 🟩 pp |
| Thambalagamuwa `LK-5318` | Trincomalee | 1.0% | 16,256 | 20,286 | +4,030 🟩 | 57.0% | 60.3% | +3.3 🟩 pp |
| Mundel `LK-6218` | Puttalam | 1.5% | 23,770 | 30,384 | +6,614 🟩 | 38.6% | 41.9% | +3.3 🟩 pp |
| Lankapura `LK-7209` | Polonnaruwa | 0.6% | 10,377 | 12,589 | +2,212 🟩 | 28.5% | 31.7% | +3.3 🟩 pp |
| Vavuniya `LK-4309` | Vavuniya | 0.4% | 5,037 | 8,612 | +3,575 🟩 | 4.3% | 7.4% | +3.1 🟩 pp |
| Akurana `LK-2109` | Kandy | 2.3% | 41,117 | 48,201 | +7,084 🟩 | 64.9% | 67.9% | +3.0 🟩 pp |
| Kahatagasdigiliya `LK-7121` | Anuradhapura | 0.5% | 8,198 | 10,466 | +2,268 🟩 | 20.3% | 23.3% | +3.0 🟩 pp |
| Negombo `LK-1203` | Gampaha | 1.1% | 20,374 | 23,788 | +3,414 🟩 | 14.3% | 17.2% | +2.9 🟩 pp |
| Welikanda `LK-7210` | Polonnaruwa | 0.3% | 4,929 | 6,663 | +1,734 🟩 | 14.6% | 17.4% | +2.8 🟩 pp |
| Horowpathana `LK-7124` | Anuradhapura | 0.6% | 9,829 | 12,135 | +2,306 🟩 | 26.6% | 29.4% | +2.8 🟩 pp |
| Mawanella `LK-9206` | Kegalle | 2.0% | 34,008 | 41,933 | +7,925 🟩 | 30.4% | 33.3% | +2.8 🟩 pp |
| Kuliyapitiya East `LK-6169` | Kurunegala | 1.0% | 17,087 | 21,068 | +3,981 🟩 | 31.6% | 34.4% | +2.8 🟩 pp |
| Panadura `LK-1303` | Kalutara | 1.6% | 26,306 | 32,306 | +6,000 🟩 | 14.4% | 17.2% | +2.8 🟩 pp |
| Welipitiya `LK-3221` | Matara | 0.4% | 6,339 | 8,220 | +1,881 🟩 | 12.2% | 14.7% | +2.5 🟩 pp |
| Jaffna `LK-4136` | Jaffna | 0.1% | 1,732 | 2,881 | +1,149 🟩 | 3.4% | 5.9% | +2.5 🟩 pp |
| Pallama `LK-6227` | Puttalam | 0.3% | 3,977 | 5,235 | +1,258 🟩 | 16.3% | 18.7% | +2.5 🟩 pp |
| Seruvila `LK-5330` | Trincomalee | 0.2% | 2,430 | 3,234 | +804 🟩 | 17.8% | 20.2% | +2.4 🟩 pp |
| Puttalam `LK-6215` | Puttalam | 3.0% | 52,934 | 63,101 | +10,167 🟩 | 64.2% | 66.6% | +2.4 🟩 pp |
| Karaitivu `LK-5227` | Ampara | 0.4% | 6,760 | 8,285 | +1,525 🟩 | 40.1% | 42.5% | +2.4 🟩 pp |
| Kobeigane `LK-6139` | Kurunegala | 0.3% | 3,862 | 5,322 | +1,460 🟩 | 10.7% | 13.1% | +2.4 🟩 pp |
| Maritimepattu `LK-4415` | Mullaitivu | 0.1% | 1,766 | 3,092 | +1,326 🟩 | 6.1% | 8.4% | +2.3 🟩 pp |
| Navithanveli `LK-5216` | Ampara | 0.4% | 6,402 | 7,967 | +1,565 🟩 | 34.2% | 36.5% | +2.3 🟩 pp |
| Pathadumbara `LK-2112` | Kandy | 1.1% | 20,239 | 23,313 | +3,074 🟩 | 22.8% | 24.9% | +2.1 🟩 pp |
| Attanagalla `LK-1227` | Gampaha | 1.4% | 22,303 | 28,406 | +6,103 🟩 | 12.4% | 14.4% | +1.9 🟩 pp |
| Ukuwela `LK-2233` | Matale | 0.8% | 14,180 | 16,475 | +2,295 🟩 | 20.8% | 22.8% | +1.9 🟩 pp |
| Panduwasnuwara West `LK-6145` | Kurunegala | 0.5% | 8,452 | 10,464 | +2,012 🟩 | 12.8% | 14.7% | +1.9 🟩 pp |
| Welimada `LK-8130` | Badulla | 1.0% | 16,921 | 19,720 | +2,799 🟩 | 16.8% | 18.7% | +1.9 🟩 pp |
| Udunuwara `LK-2139` | Kandy | 1.5% | 27,186 | 31,951 | +4,765 🟩 | 24.5% | 26.4% | +1.9 🟩 pp |
| Mallawapitiya `LK-6157` | Kurunegala | 0.5% | 7,924 | 10,018 | +2,094 🟩 | 15.1% | 16.8% | +1.8 🟩 pp |
| Udapalatha `LK-2151` | Kandy | 1.2% | 20,784 | 25,206 | +4,422 🟩 | 22.7% | 24.4% | +1.8 🟩 pp |
| Town & Gravets `LK-5315` | Trincomalee | 0.8% | 13,501 | 15,605 | +2,104 🟩 | 13.8% | 15.6% | +1.7 🟩 pp |
| Kuchchaweli `LK-5306` | Trincomalee | 1.3% | 21,308 | 26,239 | +4,931 🟩 | 64.1% | 65.8% | +1.7 🟩 pp |
| Kelaniya `LK-1236` | Gampaha | 0.7% | 12,439 | 14,312 | +1,873 🟩 | 9.1% | 10.7% | +1.6 🟩 pp |
| Rideegama `LK-6163` | Kurunegala | 0.6% | 10,022 | 12,391 | +2,369 🟩 | 11.3% | 12.9% | +1.6 🟩 pp |
| Muthur `LK-5327` | Trincomalee | 2.2% | 35,088 | 45,658 | +10,570 🟩 | 62.0% | 63.5% | +1.5 🟩 pp |
| Medagama `LK-8209` | Monaragala | 0.3% | 4,939 | 6,827 | +1,888 🟩 | 13.8% | 15.3% | +1.5 🟩 pp |
| Nattandiya `LK-6242` | Puttalam | 0.4% | 6,609 | 7,939 | +1,330 🟩 | 10.6% | 12.1% | +1.5 🟩 pp |
| Poonakary `LK-4512` | Kilinochchi | 0.0% | 469 | 909 | +440 🟩 | 2.3% | 3.8% | +1.5 🟩 pp |
| Manmunai North `LK-5118` | Batticaloa | 0.3% | 4,585 | 6,424 | +1,839 🟩 | 5.3% | 6.8% | +1.4 🟩 pp |
| Kantale `LK-5321` | Trincomalee | 0.4% | 7,633 | 9,020 | +1,387 🟩 | 16.3% | 17.7% | +1.4 🟩 pp |
| Kinniya `LK-5324` | Trincomalee | 4.1% | 61,880 | 84,032 | +22,152 🟩 | 95.8% | 97.1% | +1.4 🟩 pp |
| Colombo `LK-1103` | Colombo | 6.1% | 135,000 | 125,890 | -9,110 🟥 | 41.8% | 43.1% | +1.3 🟩 pp |
| Ganga Ihala Korale `LK-2154` | Kandy | 0.2% | 3,779 | 4,795 | +1,016 🟩 | 6.8% | 8.1% | +1.3 🟩 pp |
| Haputale `LK-8139` | Badulla | 0.2% | 3,665 | 4,165 | +500 🟩 | 7.4% | 8.6% | +1.3 🟩 pp |
| Poojapitiya `LK-2106` | Kandy | 0.5% | 9,571 | 10,718 | +1,147 🟩 | 16.5% | 17.8% | +1.2 🟩 pp |
| Weligama `LK-3239` | Matara | 0.4% | 7,379 | 8,652 | +1,273 🟩 | 10.1% | 11.4% | +1.2 🟩 pp |
| Mawathagama `LK-6160` | Kurunegala | 0.4% | 7,199 | 8,803 | +1,604 🟩 | 11.2% | 12.4% | +1.2 🟩 pp |
| Udubaddawa `LK-6175` | Kurunegala | 0.3% | 5,412 | 6,270 | +858 🟩 | 10.4% | 11.5% | +1.2 🟩 pp |
| Wattala `LK-1218` | Gampaha | 0.7% | 11,407 | 13,918 | +2,511 🟩 | 6.5% | 7.6% | +1.1 🟩 pp |
| Pannala `LK-6178` | Kurunegala | 0.5% | 7,205 | 9,398 | +2,193 🟩 | 5.8% | 6.9% | +1.1 🟩 pp |
| Koralai Pattu North `LK-5103` | Batticaloa | 0.1% | 699 | 1,095 | +396 🟩 | 3.2% | 4.3% | +1.1 🟩 pp |
| Thimbirigasyaya `LK-1127` | Colombo | 1.9% | 41,447 | 40,132 | -1,315 🟥 | 17.4% | 18.5% | +1.1 🟩 pp |
| Thamankaduwa `LK-7215` | Polonnaruwa | 0.8% | 13,210 | 15,680 | +2,470 🟩 | 16.0% | 17.0% | +1.0 🟩 pp |
| Palagala `LK-7166` | Anuradhapura | 0.3% | 4,797 | 5,804 | +1,007 🟩 | 14.1% | 15.1% | +1.0 🟩 pp |
| Warakapola `LK-9218` | Kegalle | 0.4% | 6,326 | 7,750 | +1,424 🟩 | 5.6% | 6.6% | +1.0 🟩 pp |
| Medadumbara `LK-2124` | Kandy | 0.2% | 4,008 | 4,863 | +855 🟩 | 6.6% | 7.5% | +1.0 🟩 pp |
| Biyagama `LK-1239` | Gampaha | 0.8% | 13,030 | 16,468 | +3,438 🟩 | 7.0% | 7.9% | +1.0 🟩 pp |
| Bandaragama `LK-1306` | Kalutara | 0.7% | 12,252 | 15,120 | +2,868 🟩 | 11.2% | 12.2% | +1.0 🟩 pp |
| Galewela `LK-2203` | Matale | 0.5% | 9,325 | 11,221 | +1,896 🟩 | 13.3% | 14.3% | +1.0 🟩 pp |
| Ibbagamuwa `LK-6130` | Kurunegala | 0.4% | 6,551 | 8,137 | +1,586 🟩 | 7.7% | 8.6% | +0.9 🟩 pp |
| Kekirawa `LK-7154` | Anuradhapura | 0.6% | 11,044 | 12,767 | +1,723 🟩 | 18.6% | 19.5% | +0.9 🟩 pp |
| Ipalogama `LK-7160` | Anuradhapura | 0.3% | 5,421 | 6,222 | +801 🟩 | 13.9% | 14.8% | +0.9 🟩 pp |
| Polgahawela `LK-6187` | Kurunegala | 0.3% | 6,013 | 6,780 | +767 🟩 | 9.2% | 10.0% | +0.8 🟩 pp |
| Kalutara `LK-1321` | Kalutara | 0.7% | 12,530 | 14,397 | +1,867 🟩 | 7.8% | 8.6% | +0.8 🟩 pp |
| Tumpane `LK-2103` | Kandy | 0.1% | 2,610 | 2,989 | +379 🟩 | 6.9% | 7.7% | +0.8 🟩 pp |
| Ganewatta `LK-6133` | Kurunegala | 0.1% | 1,948 | 2,441 | +493 🟩 | 4.9% | 5.6% | +0.8 🟩 pp |
| Rasnayakapura `LK-6118` | Kurunegala | 0.2% | 4,138 | 4,898 | +760 🟩 | 18.9% | 19.7% | +0.8 🟩 pp |
| Maspotha `LK-6151` | Kurunegala | 0.1% | 889 | 1,388 | +499 🟩 | 2.6% | 3.3% | +0.7 🟩 pp |
| Giribawa `LK-6103` | Kurunegala | 0.1% | 2,500 | 3,027 | +527 🟩 | 8.0% | 8.7% | +0.7 🟩 pp |
| Nallur `LK-4133` | Jaffna | 0.0% | 91 | 579 | +488 🟩 | 0.1% | 0.8% | +0.7 🟩 pp |
| Ratnapura `LK-9112` | Ratnapura | 0.3% | 6,325 | 7,169 | +844 🟩 | 5.3% | 5.9% | +0.7 🟩 pp |
| Ruwanwella `LK-9221` | Kegalle | 0.2% | 3,806 | 4,325 | +519 🟩 | 6.0% | 6.6% | +0.6 🟩 pp |
| Kebithigollewa `LK-7106` | Anuradhapura | 0.1% | 2,086 | 2,631 | +545 🟩 | 9.3% | 10.0% | +0.6 🟩 pp |
| Morawewa `LK-5312` | Trincomalee | 0.1% | 1,306 | 1,561 | +255 🟩 | 16.4% | 17.0% | +0.6 🟩 pp |
| Athuraliya `LK-3215` | Matara | 0.1% | 1,736 | 1,952 | +216 🟩 | 5.4% | 5.9% | +0.6 🟩 pp |
| Matale `LK-2218` | Matale | 0.8% | 14,337 | 15,853 | +1,516 🟩 | 19.2% | 19.7% | +0.6 🟩 pp |
| Koralai Pattu South `LK-5110` | Batticaloa | 0.0% | 28 | 189 | +161 🟩 | 0.1% | 0.7% | +0.6 🟩 pp |
| Matugama `LK-1330` | Kalutara | 0.2% | 2,980 | 3,632 | +652 🟩 | 3.7% | 4.2% | +0.6 🟩 pp |
| Islands South (Velanai) `LK-4139` | Jaffna | 0.0% | 156 | 246 | +90 🟩 | 0.9% | 1.5% | +0.6 🟩 pp |
| Medawachchiya `LK-7109` | Anuradhapura | 0.2% | 2,893 | 3,526 | +633 🟩 | 6.2% | 6.7% | +0.5 🟩 pp |
| Katana `LK-1206` | Gampaha | 0.3% | 4,799 | 6,242 | +1,443 🟩 | 2.0% | 2.6% | +0.5 🟩 pp |
| Rambukkana `LK-9203` | Kegalle | 0.2% | 2,851 | 3,470 | +619 🟩 | 3.4% | 4.0% | +0.5 🟩 pp |
| Maho `LK-6124` | Kurunegala | 0.2% | 3,041 | 3,731 | +690 🟩 | 5.3% | 5.8% | +0.5 🟩 pp |
| Thirappane `LK-7151` | Anuradhapura | 0.1% | 1,662 | 2,077 | +415 🟩 | 6.1% | 6.7% | +0.5 🟩 pp |
| Pasbagekorale `LK-2157` | Kandy | 0.5% | 9,130 | 10,328 | +1,198 🟩 | 15.2% | 15.8% | +0.5 🟩 pp |
| Hambantota `LK-3312` | Hambantota | 0.5% | 9,382 | 11,352 | +1,970 🟩 | 16.4% | 16.9% | +0.5 🟩 pp |
| Sri Jayawardanapura Kotte `LK-1124` | Colombo | 0.3% | 6,798 | 6,535 | -263 🟥 | 6.3% | 6.8% | +0.5 🟩 pp |
| Galenbidunuwewa `LK-7127` | Anuradhapura | 0.1% | 1,393 | 1,794 | +401 🟩 | 3.0% | 3.5% | +0.5 🟩 pp |
| Galgamuwa `LK-6106` | Kurunegala | 0.2% | 3,484 | 4,202 | +718 🟩 | 6.3% | 6.8% | +0.5 🟩 pp |
| Dikwella `LK-3248` | Matara | 0.2% | 2,761 | 3,119 | +358 🟩 | 5.1% | 5.5% | +0.5 🟩 pp |
| Mihinthale `LK-7130` | Anuradhapura | 0.1% | 1,706 | 2,332 | +626 🟩 | 4.8% | 5.3% | +0.5 🟩 pp |
| Harispattuwa `LK-2133` | Kandy | 0.5% | 9,630 | 10,694 | +1,064 🟩 | 10.9% | 11.4% | +0.5 🟩 pp |
| Yatiyantota `LK-9227` | Kegalle | 0.1% | 2,781 | 3,110 | +329 🟩 | 4.6% | 5.0% | +0.4 🟩 pp |
| Nintavur `LK-5230` | Ampara | 1.4% | 25,342 | 29,614 | +4,272 🟩 | 96.1% | 96.6% | +0.4 🟩 pp |
| Ella `LK-8136` | Badulla | 0.1% | 1,920 | 2,300 | +380 🟩 | 4.2% | 4.7% | +0.4 🟩 pp |
| Panduwasnuwara East `LK-6148` | Kurunegala | 0.0% | 675 | 839 | +164 🟩 | 2.2% | 2.6% | +0.4 🟩 pp |
| Akmeemana `LK-3145` | Galle | 0.1% | 1,816 | 2,341 | +525 🟩 | 2.3% | 2.7% | +0.4 🟩 pp |
| Hali-Ela `LK-8124` | Badulla | 0.2% | 4,136 | 4,661 | +525 🟩 | 4.6% | 4.9% | +0.4 🟩 pp |
| Aranayake `LK-9209` | Kegalle | 0.3% | 5,233 | 5,525 | +292 🟩 | 7.6% | 8.0% | +0.4 🟩 pp |
| Chilaw `LK-6233` | Puttalam | 0.3% | 5,205 | 5,519 | +314 🟩 | 8.3% | 8.7% | +0.3 🟩 pp |
| Kuliyapitiya West `LK-6172` | Kurunegala | 0.1% | 2,059 | 2,484 | +425 🟩 | 2.7% | 3.0% | +0.3 🟩 pp |
| Koralai Pattu West `LK-5106` | Batticaloa | 1.2% | 22,076 | 24,550 | +2,474 🟩 | 99.5% | 99.9% | +0.3 🟩 pp |
| Badulla `LK-8121` | Badulla | 0.4% | 7,760 | 8,868 | +1,108 🟩 | 10.3% | 10.7% | +0.3 🟩 pp |
| Narammala `LK-6181` | Kurunegala | 0.2% | 3,425 | 3,838 | +413 🟩 | 6.1% | 6.4% | +0.3 🟩 pp |
| Nochchiyagama `LK-7139` | Anuradhapura | 0.1% | 2,010 | 2,416 | +406 🟩 | 4.0% | 4.4% | +0.3 🟩 pp |
| Bingiriya `LK-6142` | Kurunegala | 0.1% | 1,945 | 2,295 | +350 🟩 | 3.1% | 3.4% | +0.3 🟩 pp |
| Yatinuwara `LK-2136` | Kandy | 0.4% | 7,716 | 8,550 | +834 🟩 | 7.3% | 7.6% | +0.3 🟩 pp |
| Nuwaragam Palatha Central `LK-7115` | Anuradhapura | 0.3% | 5,335 | 6,452 | +1,117 🟩 | 8.7% | 9.0% | +0.3 🟩 pp |
| Medirigiriya `LK-7206` | Polonnaruwa | 0.1% | 1,166 | 1,504 | +338 🟩 | 1.8% | 2.1% | +0.3 🟩 pp |
| Mirigama `LK-1212` | Gampaha | 0.4% | 7,676 | 8,768 | +1,092 🟩 | 4.7% | 5.0% | +0.3 🟩 pp |
| Badalkumbura `LK-8218` | Monaragala | 0.1% | 1,814 | 2,243 | +429 🟩 | 4.5% | 4.8% | +0.3 🟩 pp |
| Rattota `LK-2230` | Matale | 0.1% | 2,101 | 2,344 | +243 🟩 | 4.1% | 4.4% | +0.3 🟩 pp |
| Galnewa `LK-7163` | Anuradhapura | 0.1% | 2,289 | 2,708 | +419 🟩 | 6.6% | 6.9% | +0.3 🟩 pp |
| Bulathsinhala `LK-1312` | Kalutara | 0.1% | 2,237 | 2,450 | +213 🟩 | 3.5% | 3.7% | +0.3 🟩 pp |
| Karachchi `LK-4509` | Kilinochchi | 0.0% | 195 | 440 | +245 🟩 | 0.3% | 0.6% | +0.3 🟩 pp |
| Passara `LK-8118` | Badulla | 0.1% | 2,454 | 2,625 | +171 🟩 | 5.0% | 5.3% | +0.3 🟩 pp |
| Dehiowita `LK-9230` | Kegalle | 0.2% | 3,538 | 3,916 | +378 🟩 | 4.4% | 4.6% | +0.3 🟩 pp |
| Moratuwa `LK-1133` | Colombo | 0.2% | 3,339 | 3,549 | +210 🟩 | 2.0% | 2.2% | +0.2 🟩 pp |
| Mahara `LK-1233` | Gampaha | 0.5% | 9,255 | 10,437 | +1,182 🟩 | 4.5% | 4.7% | +0.2 🟩 pp |
| Bamunakotuwa `LK-6149` | Kurunegala | 0.0% | 772 | 929 | +157 🟩 | 2.1% | 2.4% | +0.2 🟩 pp |
| Thunukkai `LK-4403` | Mullaitivu | 0.0% | 7 | 30 | +23 🟩 | 0.1% | 0.3% | +0.2 🟩 pp |
| Bandarawela `LK-8133` | Badulla | 0.2% | 3,628 | 3,761 | +133 🟩 | 5.5% | 5.7% | +0.2 🟩 pp |
| Kundasale `LK-2127` | Kandy | 0.4% | 7,496 | 8,808 | +1,312 🟩 | 5.9% | 6.1% | +0.2 🟩 pp |
| Malimbada `LK-3224` | Matara | 0.0% | 480 | 570 | +90 🟩 | 1.4% | 1.6% | +0.2 🟩 pp |
| Uvaparanagama `LK-8127` | Badulla | 0.1% | 2,239 | 2,516 | +277 🟩 | 2.9% | 3.1% | +0.2 🟩 pp |
| Valikamam South (Uduvil) `LK-4115` | Jaffna | 0.0% | 59 | 152 | +93 🟩 | 0.1% | 0.3% | +0.2 🟩 pp |
| Mahiyanganaya `LK-8103` | Badulla | 0.1% | 1,876 | 2,373 | +497 🟩 | 2.5% | 2.7% | +0.2 🟩 pp |
| Weeraketiya `LK-3321` | Hambantota | 0.0% | 760 | 968 | +208 🟩 | 1.8% | 2.0% | +0.2 🟩 pp |
| Godakawela `LK-9142` | Ratnapura | 0.2% | 2,937 | 3,138 | +201 🟩 | 3.8% | 4.0% | +0.2 🟩 pp |
| Kahawattha `LK-9139` | Ratnapura | 0.1% | 1,479 | 1,558 | +79 🟩 | 3.4% | 3.6% | +0.1 🟩 pp |
| Ambalantota `LK-3315` | Hambantota | 0.1% | 1,604 | 1,887 | +283 🟩 | 2.2% | 2.3% | +0.1 🟩 pp |
| Devinuwara `LK-3245` | Matara | 0.0% | 669 | 753 | +84 🟩 | 1.4% | 1.5% | +0.1 🟩 pp |
| Madampe `LK-6236` | Puttalam | 0.1% | 2,754 | 2,885 | +131 🟩 | 5.7% | 5.9% | +0.1 🟩 pp |
| Gangawata Korale `LK-2130` | Kandy | 0.9% | 18,985 | 18,558 | -427 🟥 | 12.0% | 12.1% | +0.1 🟩 pp |
| Wariyapola `LK-6136` | Kurunegala | 0.0% | 873 | 1,027 | +154 🟩 | 1.4% | 1.5% | +0.1 🟩 pp |
| Naula `LK-2209` | Matale | 0.0% | 408 | 443 | +35 🟩 | 1.3% | 1.4% | +0.1 🟩 pp |
| Kurunegala `LK-6154` | Kurunegala | 0.5% | 9,505 | 10,581 | +1,076 🟩 | 11.8% | 11.9% | +0.1 🟩 pp |
| Kesbewa `LK-1136` | Colombo | 0.1% | 2,160 | 2,600 | +440 🟩 | 0.9% | 1.0% | +0.1 🟩 pp |
| Alayadivembu `LK-5239` | Ampara | 0.0% | 26 | 55 | +29 🟩 | 0.1% | 0.2% | +0.1 🟩 pp |
| Palindanuwara `LK-1336` | Kalutara | 0.0% | 581 | 639 | +58 🟩 | 1.1% | 1.2% | +0.1 🟩 pp |
| Kattankudy `LK-5124` | Batticaloa | 2.2% | 40,254 | 44,725 | +4,471 🟩 | 99.7% | 99.8% | +0.1 🟩 pp |
| Sammanthurai `LK-5218` | Ampara | 3.0% | 52,350 | 63,096 | +10,746 🟩 | 86.6% | 86.7% | +0.1 🟩 pp |
| Thenmaradchi (Chavakachcheri) `LK-4130` | Jaffna | 0.0% | 63 | 132 | +69 🟩 | 0.1% | 0.2% | +0.1 🟩 pp |
| Akkaraipattu `LK-5236` | Ampara | 2.2% | 38,919 | 44,739 | +5,820 🟩 | 99.4% | 99.5% | +0.1 🟩 pp |
| Valikamam East (Kopay) `LK-4118` | Jaffna | 0.0% | 116 | 193 | +77 🟩 | 0.2% | 0.3% | +0.1 🟩 pp |
| Yatawatta `LK-2215` | Matale | 0.1% | 1,976 | 2,145 | +169 🟩 | 6.5% | 6.6% | +0.1 🟩 pp |
| Puthukkudiyiruppu `LK-4409` | Mullaitivu | 0.0% | 23 | 71 | +48 🟩 | 0.1% | 0.2% | +0.1 🟩 pp |
| Sainthamaruthu `LK-5225` | Ampara | 1.4% | 25,402 | 29,828 | +4,426 🟩 | 99.8% | 99.8% | +0.1 🟩 pp |
| Dambulla `LK-2206` | Matale | 0.1% | 2,179 | 2,509 | +330 🟩 | 3.0% | 3.1% | +0.1 🟩 pp |
| Verugal `LK-5333` | Trincomalee | 0.0% | 11 | 24 | +13 🟩 | 0.1% | 0.2% | +0.1 🟩 pp |
| Ingiriya `LK-1310` | Kalutara | 0.0% | 37 | 83 | +46 🟩 | 0.1% | 0.1% | +0.1 🟩 pp |
| Dankotuwa `LK-6248` | Puttalam | 0.0% | 384 | 433 | +49 🟩 | 0.6% | 0.7% | +0.1 🟩 pp |
| Kaburupitiya `LK-3227` | Matara | 0.0% | 14 | 45 | +31 🟩 | 0.0% | 0.1% | +0.1 🟩 pp |
| Lunugamwehera `LK-3306` | Hambantota | 0.0% | 535 | 652 | +117 🟩 | 1.7% | 1.8% | +0.1 🟩 pp |
| Weligepola `LK-9145` | Ratnapura | 0.0% | 6 | 27 | +21 🟩 | 0.0% | 0.1% | +0.1 🟩 pp |
| Ehetuwewa `LK-6109` | Kurunegala | 0.0% | 727 | 815 | +88 🟩 | 2.8% | 2.9% | +0.1 🟩 pp |
| Welioya `LK-4418` | Mullaitivu | 0.0% | 3 | 10 | +7 🟩 | 0.0% | 0.1% | +0.1 🟩 pp |
| Hakmana `LK-3230` | Matara | 0.0% | 963 | 1,022 | +59 🟩 | 3.0% | 3.1% | +0.1 🟩 pp |
| Bibile `LK-8203` | Monaragala | 0.1% | 1,020 | 1,217 | +197 🟩 | 2.5% | 2.6% | 0.0 pp |
| Damana `LK-5242` | Ampara | 0.0% | 150 | 174 | +24 🟩 | 0.4% | 0.4% | 0.0 pp |
| Karandeniya `LK-3109` | Galle | 0.0% | 567 | 606 | +39 🟩 | 0.9% | 0.9% | 0.0 pp |
| Walallawita `LK-1339` | Kalutara | 0.0% | 16 | 39 | +23 🟩 | 0.0% | 0.1% | 0.0 pp |
| Thawalama `LK-3118` | Galle | 0.0% | 9 | 20 | +11 🟩 | 0.0% | 0.1% | 0.0 pp |
| Matara Four Gravets `LK-3242` | Matara | 0.2% | 4,374 | 4,724 | +350 🟩 | 3.8% | 3.8% | 0.0 pp |
| Delft `LK-4142` | Jaffna | 0.0% | 0 | 1 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Valikamam South West (Sandilipay) `LK-4109` | Jaffna | 0.0% | 38 | 54 | +16 🟩 | 0.1% | 0.1% | 0.0 pp |
| Welivitiya-Divitura `LK-3130` | Galle | 0.0% | 5 | 13 | +8 🟩 | 0.0% | 0.0% | 0.0 pp |
| Rajanganaya `LK-7142` | Anuradhapura | 0.0% | 2 | 12 | +10 🟩 | 0.0% | 0.0% | 0.0 pp |
| Mahawewa `LK-6239` | Puttalam | 0.0% | 34 | 45 | +11 🟩 | 0.1% | 0.1% | 0.0 pp |
| Valikamam West (Chankanai) `LK-4106` | Jaffna | 0.0% | 15 | 26 | +11 🟩 | 0.0% | 0.1% | 0.0 pp |
| Manmunai West `LK-5121` | Batticaloa | 0.0% | 15 | 25 | +10 🟩 | 0.1% | 0.1% | 0.0 pp |
| Sevanagala `LK-8233` | Monaragala | 0.0% | 3 | 15 | +12 🟩 | 0.0% | 0.0% | 0.0 pp |
| Laggala `LK-2224` | Matale | 0.0% | 1 | 5 | +4 🟩 | 0.0% | 0.0% | 0.0 pp |
| Habaraduwa `LK-3154` | Galle | 0.0% | 28 | 42 | +14 🟩 | 0.0% | 0.1% | 0.0 pp |
| Pasgoda `LK-3209` | Matara | 0.0% | 2 | 15 | +13 🟩 | 0.0% | 0.0% | 0.0 pp |
| Imbulpe `LK-9115` | Ratnapura | 0.0% | 87 | 108 | +21 🟩 | 0.1% | 0.2% | 0.0 pp |
| Mahakumbukkadawala `LK-6221` | Puttalam | 0.0% | 14 | 21 | +7 🟩 | 0.1% | 0.1% | 0.0 pp |
| Mahawilachchiya `LK-7112` | Anuradhapura | 0.0% | 13 | 19 | +6 🟩 | 0.1% | 0.1% | 0.0 pp |
| Deraniyagala `LK-9233` | Kegalle | 0.0% | 48 | 55 | +7 🟩 | 0.1% | 0.1% | 0.0 pp |
| Agalawatta `LK-1333` | Kalutara | 0.0% | 84 | 91 | +7 🟩 | 0.2% | 0.2% | 0.0 pp |
| Vadamaradchchi South-West (Karaveddy) `LK-4121` | Jaffna | 0.0% | 20 | 26 | +6 🟩 | 0.0% | 0.1% | 0.0 pp |
| Madurawala `LK-1315` | Kalutara | 0.0% | 21 | 29 | +8 🟩 | 0.1% | 0.1% | 0.0 pp |
| Kalpitiya `LK-6203` | Puttalam | 2.6% | 47,178 | 52,977 | +5,799 🟩 | 54.6% | 54.6% | 0.0 pp |
| Mulatiyana `LK-3212` | Matara | 0.0% | 1 | 9 | +8 🟩 | 0.0% | 0.0% | 0.0 pp |
| Uhana `LK-5212` | Ampara | 0.0% | 10 | 20 | +10 🟩 | 0.0% | 0.0% | 0.0 pp |
| Okewela `LK-3327` | Hambantota | 0.0% | 20 | 24 | +4 🟩 | 0.1% | 0.1% | 0.0 pp |
| Tirukkovil `LK-5245` | Ampara | 0.0% | 4 | 9 | +5 🟩 | 0.0% | 0.0% | 0.0 pp |
| Nawagattegama `LK-6212` | Puttalam | 0.0% | 3 | 6 | +3 🟩 | 0.0% | 0.0% | 0.0 pp |
| Katuwana `LK-3324` | Hambantota | 0.0% | 9 | 17 | +8 🟩 | 0.0% | 0.0% | 0.0 pp |
| Manmunai South & Eruvil Pattu `LK-5136` | Batticaloa | 0.0% | 20 | 29 | +9 🟩 | 0.0% | 0.0% | 0.0 pp |
| Padaviya `LK-7103` | Anuradhapura | 0.0% | 3 | 6 | +3 🟩 | 0.0% | 0.0% | 0.0 pp |
| Karainagar `LK-4104` | Jaffna | 0.0% | 0 | 1 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Siyambalanduwa `LK-8212` | Monaragala | 0.0% | 29 | 40 | +11 🟩 | 0.1% | 0.1% | 0.0 pp |
| Kegalle `LK-9212` | Kegalle | 0.1% | 1,229 | 1,285 | +56 🟩 | 1.4% | 1.4% | 0.0 pp |
| Elahera `LK-7218` | Polonnaruwa | 0.0% | 7 | 12 | +5 🟩 | 0.0% | 0.0% | 0.0 pp |
| Padavi Sri Pura `LK-5303` | Trincomalee | 0.0% | 3 | 4 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Horana `LK-1309` | Kalutara | 0.0% | 151 | 188 | +37 🟩 | 0.1% | 0.1% | 0.0 pp |
| Elpitiya `LK-3112` | Galle | 0.0% | 14 | 19 | +5 🟩 | 0.0% | 0.0% | 0.0 pp |
| Kiriella `LK-9109` | Ratnapura | 0.0% | 14 | 15 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Niyagama `LK-3115` | Galle | 0.0% | 2 | 4 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Thihagoda `LK-3236` | Matara | 0.0% | 8 | 10 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Polpitigama `LK-6127` | Kurunegala | 0.0% | 28 | 36 | +8 🟩 | 0.0% | 0.0% | 0.0 pp |
| Angunakolapelessa `LK-3318` | Hambantota | 0.0% | 8 | 10 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Akuressa `LK-3218` | Matara | 0.0% | 14 | 15 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Kandavalai `LK-4506` | Kilinochchi | 0.0% | 23 | 25 | +2 🟩 | 0.1% | 0.1% | 0.0 pp |
| Pachchilaipalli `LK-4503` | Kilinochchi | 0.0% | 13 | 20 | +7 🟩 | 0.2% | 0.2% | 0.0 pp |
| Ambalangoda `LK-3133` | Galle | 0.0% | 17 | 18 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Thambuththegama `LK-7145` | Anuradhapura | 0.0% | 9 | 10 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Rideemaliyadda `LK-8106` | Badulla | 0.0% | 18 | 21 | +3 🟩 | 0.0% | 0.0% | 0.0 pp |
| Alawwa `LK-6184` | Kurunegala | 0.0% | 19 | 19 | +0 | 0.0% | 0.0% | 0.0 pp |
| Divulapitiya `LK-1209` | Gampaha | 0.0% | 151 | 162 | +11 🟩 | 0.1% | 0.1% | 0.0 pp |
| Wilgamuwa `LK-2227` | Matale | 0.0% | 5 | 5 | +0 | 0.0% | 0.0% | 0.0 pp |
| Gonapinuwala `LK-3134` | Galle | 0.0% | 10 | 10 | +0 | 0.0% | 0.0% | 0.0 pp |
| Homagama `LK-1112` | Colombo | 0.1% | 1,484 | 1,740 | +256 🟩 | 0.6% | 0.6% | 0.0 pp |
| Galigamuwa `LK-9215` | Kegalle | 0.1% | 1,179 | 1,164 | -15 🟥 | 1.6% | 1.6% | 0.0 pp |
| Sooriyawewa `LK-3303` | Hambantota | 0.0% | 14 | 14 | +0 | 0.0% | 0.0% | 0.0 pp |
| Nagoda `LK-3124` | Galle | 0.0% | 17 | 13 | -4 🟥 | 0.0% | 0.0% | 0.0 pp |
| Madulla `LK-8206` | Monaragala | 0.0% | 10 | 9 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Minuwangoda `LK-1215` | Gampaha | 0.3% | 6,315 | 7,022 | +707 🟩 | 3.5% | 3.5% | 0.0 pp |
| Doluwa `LK-2142` | Kandy | 0.1% | 2,636 | 2,787 | +151 🟩 | 5.3% | 5.3% | 0.0 pp |
| Vadamaradchi North (Point Pedro) `LK-4127` | Jaffna | 0.0% | 41 | 33 | -8 🟥 | 0.1% | 0.1% | 0.0 pp |
| Imaduwa `LK-3151` | Galle | 0.0% | 13 | 8 | -5 🟥 | 0.0% | 0.0% | 0.0 pp |
| Thanamalwila `LK-8230` | Monaragala | 0.0% | 11 | 9 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Beliatta `LK-3330` | Hambantota | 0.0% | 13 | 6 | -7 🟥 | 0.0% | 0.0% | 0.0 pp |
| Embilipitiya `LK-9148` | Ratnapura | 0.0% | 63 | 54 | -9 🟥 | 0.0% | 0.0% | 0.0 pp |
| Anamaduwa `LK-6224` | Puttalam | 0.0% | 740 | 835 | +95 🟩 | 1.9% | 1.9% | 0.0 pp |
| Nivithigala `LK-9136` | Ratnapura | 0.0% | 554 | 539 | -15 🟥 | 0.9% | 0.9% | 0.0 pp |
| Gomarankadawala `LK-5309` | Trincomalee | 0.0% | 2 | 1 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Valikamam North (Thllippalai) `LK-4112` | Jaffna | 0.0% | 21 | 24 | +3 🟩 | 0.1% | 0.1% | 0.0 pp |
| Meegahakiula `LK-8109` | Badulla | 0.0% | 15 | 13 | -2 🟥 | 0.1% | 0.1% | 0.0 pp |
| Millaniya `LK-1318` | Kalutara | 0.0% | 62 | 56 | -6 🟥 | 0.1% | 0.1% | 0.0 pp |
| Islands North (Kayts) `LK-4103` | Jaffna | 0.0% | 3 | 1 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Porativu Pattu `LK-5133` | Batticaloa | 0.0% | 13 | 6 | -7 🟥 | 0.0% | 0.0% | 0.0 pp |
| Pelmadulla `LK-9124` | Ratnapura | 0.0% | 652 | 663 | +11 🟩 | 0.7% | 0.7% | 0.0 pp |
| Dodangoda `LK-1327` | Kalutara | 0.0% | 71 | 59 | -12 🟥 | 0.1% | 0.1% | 0.0 pp |
| Kolonna `LK-9151` | Ratnapura | 0.0% | 41 | 33 | -8 🟥 | 0.1% | 0.1% | 0.0 pp |
| Karuwalagaswewa `LK-6209` | Puttalam | 0.0% | 12 | 7 | -5 🟥 | 0.1% | 0.0% | 0.0 pp |
| Yakkalamulla `LK-3148` | Galle | 0.0% | 20 | 8 | -12 🟥 | 0.0% | 0.0% | 0.0 pp |
| Manmunai South West `LK-5130` | Batticaloa | 0.0% | 8 | 1 | -7 🟥 | 0.0% | 0.0% | 0.0 pp |
| Wennappuwa `LK-6245` | Puttalam | 0.0% | 111 | 87 | -24 🟥 | 0.2% | 0.1% | 0.0 pp |
| Walasmulla `LK-3325` | Hambantota | 0.0% | 38 | 29 | -9 🟥 | 0.1% | 0.1% | 0.0 pp |
| Lahugala `LK-5251` | Ampara | 0.0% | 3 | 0 | -3 🟥 | 0.0% | 0.0% | 0.0 pp |
| Kalawana `LK-9133` | Ratnapura | 0.0% | 41 | 23 | -18 🟥 | 0.1% | 0.0% | 0.0 pp |
| Thissamaharama `LK-3309` | Hambantota | 0.1% | 1,834 | 1,955 | +121 🟩 | 2.7% | 2.6% | 0.0 pp |
| Haldummulla `LK-8142` | Badulla | 0.0% | 461 | 461 | +0 | 1.2% | 1.2% | 0.0 pp |
| Ambanganga `LK-2221` | Matale | 0.0% | 77 | 72 | -5 🟥 | 0.5% | 0.5% | 0.0 pp |
| Pitabaddara `LK-3203` | Matara | 0.0% | 28 | 7 | -21 🟥 | 0.1% | 0.0% | 0.0 pp |
| Vadamaradchchi East `LK-4124` | Jaffna | 0.0% | 8 | 3 | -5 🟥 | 0.1% | 0.0% | 0.0 pp |
| Manthai East `LK-4406` | Mullaitivu | 0.0% | 15 | 13 | -2 🟥 | 0.2% | 0.2% | 0.0 pp |
| Katharagama `LK-8227` | Monaragala | 0.0% | 55 | 47 | -8 🟥 | 0.3% | 0.3% | 0.0 pp |
| Neluwa `LK-3121` | Galle | 0.0% | 19 | 5 | -14 🟥 | 0.1% | 0.0% | 0.0 pp |
| Vavuniya South `LK-4306` | Vavuniya | 0.0% | 9 | 3 | -6 🟥 | 0.1% | 0.0% | 0.0 pp |
| Palugaswewa `LK-7157` | Anuradhapura | 0.0% | 25 | 20 | -5 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Ayagama `LK-9130` | Ratnapura | 0.0% | 31 | 15 | -16 🟥 | 0.1% | 0.1% | -0.1 🟥 pp |
| Vavuniya North `LK-4303` | Vavuniya | 0.0% | 17 | 14 | -3 🟥 | 0.1% | 0.1% | -0.1 🟥 pp |
| Pallepola `LK-2212` | Matale | 0.1% | 1,093 | 1,152 | +59 🟩 | 3.7% | 3.6% | -0.1 🟥 pp |
| Dompe `LK-1230` | Gampaha | 0.1% | 2,419 | 2,574 | +155 🟩 | 1.6% | 1.5% | -0.1 🟥 pp |
| Gampaha `LK-1224` | Gampaha | 0.0% | 463 | 365 | -98 🟥 | 0.2% | 0.2% | -0.1 🟥 pp |
| Balapitiya `LK-3106` | Galle | 0.1% | 1,136 | 1,109 | -27 🟥 | 1.7% | 1.6% | -0.1 🟥 pp |
| Ambanpola `LK-6112` | Kurunegala | 0.0% | 364 | 391 | +27 🟩 | 1.6% | 1.5% | -0.1 🟥 pp |
| Kotawehera `LK-6115` | Kurunegala | 0.0% | 104 | 103 | -1 🟥 | 0.5% | 0.4% | -0.1 🟥 pp |
| Tangalle `LK-3333` | Hambantota | 0.0% | 987 | 1,033 | +46 🟩 | 1.4% | 1.3% | -0.1 🟥 pp |
| Arachchikattuwa `LK-6230` | Puttalam | 0.0% | 169 | 148 | -21 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Dimbulagala `LK-7212` | Polonnaruwa | 0.0% | 105 | 54 | -51 🟥 | 0.1% | 0.1% | -0.1 🟥 pp |
| Padukka `LK-1118` | Colombo | 0.1% | 1,157 | 1,242 | +85 🟩 | 1.8% | 1.7% | -0.1 🟥 pp |
| Oddusuddan `LK-4412` | Mullaitivu | 0.0% | 66 | 63 | -3 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Thalawa `LK-7148` | Anuradhapura | 0.0% | 616 | 606 | -10 🟥 | 1.1% | 1.0% | -0.1 🟥 pp |
| Weerabugedara `LK-6166` | Kurunegala | 0.0% | 84 | 61 | -23 🟥 | 0.2% | 0.2% | -0.1 🟥 pp |
| Kaduwela `LK-1109` | Colombo | 0.2% | 3,735 | 3,898 | +163 🟩 | 1.5% | 1.4% | -0.1 🟥 pp |
| Bope-Poddala `LK-3142` | Galle | 0.1% | 1,481 | 1,650 | +169 🟩 | 2.9% | 2.9% | -0.1 🟥 pp |
| Ja Ela `LK-1221` | Gampaha | 0.1% | 2,115 | 1,960 | -155 🟥 | 1.0% | 1.0% | -0.1 🟥 pp |
| Opanayake `LK-9121` | Ratnapura | 0.0% | 258 | 238 | -20 🟥 | 1.0% | 0.9% | -0.1 🟥 pp |
| Kirinda Puhulwella `LK-3233` | Matara | 0.0% | 666 | 655 | -11 🟥 | 3.3% | 3.2% | -0.1 🟥 pp |
| Deltota `LK-2148` | Kandy | 0.4% | 7,626 | 7,983 | +357 🟩 | 25.1% | 25.0% | -0.1 🟥 pp |
| Kandeketiya `LK-8112` | Badulla | 0.0% | 551 | 611 | +60 🟩 | 2.4% | 2.3% | -0.1 🟥 pp |
| Kotapola `LK-3206` | Matara | 0.0% | 180 | 90 | -90 🟥 | 0.3% | 0.1% | -0.1 🟥 pp |
| Elapatha `LK-9127` | Ratnapura | 0.0% | 105 | 53 | -52 🟥 | 0.3% | 0.1% | -0.1 🟥 pp |
| Pathahewaheta `LK-2145` | Kandy | 0.1% | 1,399 | 1,372 | -27 🟥 | 2.4% | 2.3% | -0.1 🟥 pp |
| Minipe `LK-2121` | Kandy | 0.0% | 312 | 252 | -60 🟥 | 0.6% | 0.5% | -0.1 🟥 pp |
| Mahaoya `LK-5209` | Ampara | 0.0% | 45 | 16 | -29 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Ampara `LK-5215` | Ampara | 0.0% | 322 | 275 | -47 🟥 | 0.7% | 0.6% | -0.2 🟥 pp |
| Nikaweratiya `LK-6121` | Kurunegala | 0.1% | 1,503 | 1,543 | +40 🟩 | 3.7% | 3.6% | -0.2 🟥 pp |
| Maharagama `LK-1121` | Colombo | 0.1% | 2,780 | 2,458 | -322 🟥 | 1.4% | 1.3% | -0.2 🟥 pp |
| Bulathkohipitiya `LK-9224` | Kegalle | 0.0% | 165 | 83 | -82 🟥 | 0.4% | 0.2% | -0.2 🟥 pp |
| Seethawaka `LK-1115` | Colombo | 0.0% | 1,032 | 888 | -144 🟥 | 0.9% | 0.7% | -0.2 🟥 pp |
| Buttala `LK-8224` | Monaragala | 0.0% | 468 | 425 | -43 🟥 | 0.9% | 0.7% | -0.2 🟥 pp |
| Bentota `LK-3103` | Galle | 0.1% | 1,155 | 1,057 | -98 🟥 | 2.3% | 2.1% | -0.2 🟥 pp |
| Higurakgoda `LK-7203` | Polonnaruwa | 0.0% | 671 | 595 | -76 🟥 | 1.0% | 0.8% | -0.2 🟥 pp |
| Lunugala `LK-8119` | Badulla | 0.1% | 1,253 | 1,208 | -45 🟥 | 4.0% | 3.8% | -0.2 🟥 pp |
| Padiyathalawa `LK-5206` | Ampara | 0.0% | 88 | 56 | -32 🟥 | 0.5% | 0.3% | -0.2 🟥 pp |
| Ududumbara `LK-2118` | Kandy | 0.0% | 183 | 134 | -49 🟥 | 0.8% | 0.6% | -0.2 🟥 pp |
| Soranathota `LK-8115` | Badulla | 0.0% | 295 | 260 | -35 🟥 | 1.3% | 1.1% | -0.2 🟥 pp |
| Wellawaya `LK-8221` | Monaragala | 0.1% | 1,088 | 1,147 | +59 🟩 | 1.8% | 1.6% | -0.2 🟥 pp |
| Monaragala `LK-8215` | Monaragala | 0.0% | 372 | 283 | -89 🟥 | 0.8% | 0.5% | -0.3 🟥 pp |
| Panvila `LK-2115` | Kandy | 0.0% | 1,107 | 991 | -116 🟥 | 4.2% | 3.9% | -0.3 🟥 pp |
| Nuwaragam Palatha East `LK-7133` | Anuradhapura | 0.2% | 3,114 | 3,135 | +21 🟩 | 4.5% | 4.1% | -0.3 🟥 pp |
| Hatharaliyadda `LK-2134` | Kandy | 0.1% | 1,562 | 1,504 | -58 🟥 | 5.2% | 4.8% | -0.4 🟥 pp |
| Nachchaduwa `LK-7136` | Anuradhapura | 0.2% | 3,365 | 3,599 | +234 🟩 | 13.3% | 12.7% | -0.5 🟥 pp |
| Dehiattakandiya `LK-5203` | Ampara | 0.0% | 404 | 90 | -314 🟥 | 0.7% | 0.1% | -0.5 🟥 pp |
| Vanathavilluwa `LK-6206` | Puttalam | 0.4% | 6,510 | 7,341 | +831 🟩 | 37.3% | 36.7% | -0.6 🟥 pp |
| Rambewa `LK-7118` | Anuradhapura | 0.3% | 5,683 | 5,242 | -441 🟥 | 15.5% | 13.2% | -2.3 🟥 pp |
| Koralai Pattu Central `LK-5104` | Batticaloa | 0.0% | 24,965 | 94 | -24,871 🟥 | 97.2% | 0.3% | -96.9 🟥 pp |

***Musali** gained the most share at **+15.1pp**. **Koralai Pattu Central** saw the steepest share decline at **-96.9pp**. **Kolonnawa** had the largest absolute increase (**+22,911**).*

### Roman Catholic

| DSD | District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Delft `LK-4142` | Jaffna | 0.2% | 2,077 | 1,924 | -153 🟥 | 54.3% | 60.9% | +6.6 🟩 pp |
| Puthukkudiyiruppu `LK-4409` | Mullaitivu | 0.5% | 2,305 | 5,817 | +3,512 🟩 | 9.7% | 14.7% | +5.0 🟩 pp |
| Koralai Pattu Central `LK-5104` | Batticaloa | 0.1% | 63 | 1,257 | +1,194 🟩 | 0.2% | 4.4% | +4.1 🟩 pp |
| Islands South (Velanai) `LK-4139` | Jaffna | 0.4% | 3,619 | 4,263 | +644 🟩 | 21.6% | 25.7% | +4.1 🟩 pp |
| Nallur `LK-4133` | Jaffna | 0.4% | 3,453 | 5,310 | +1,857 🟩 | 5.1% | 7.3% | +2.2 🟩 pp |
| Katana `LK-1206` | Gampaha | 6.9% | 75,385 | 81,913 | +6,528 🟩 | 32.0% | 34.0% | +1.9 🟩 pp |
| Kalpitiya `LK-6203` | Puttalam | 2.8% | 27,880 | 32,625 | +4,745 🟩 | 32.3% | 33.6% | +1.4 🟩 pp |
| Poonakary `LK-4512` | Kilinochchi | 0.5% | 4,621 | 5,767 | +1,146 🟩 | 22.8% | 23.9% | +1.2 🟩 pp |
| Islands North (Kayts) `LK-4103` | Jaffna | 0.4% | 4,062 | 4,196 | +134 🟩 | 41.1% | 42.3% | +1.1 🟩 pp |
| Valikamam North (Thllippalai) `LK-4112` | Jaffna | 0.4% | 2,866 | 4,843 | +1,977 🟩 | 9.7% | 10.8% | +1.1 🟩 pp |
| Vavuniya North `LK-4303` | Vavuniya | 0.0% | 313 | 555 | +242 🟩 | 2.7% | 3.8% | +1.1 🟩 pp |
| Thenmaradchi (Chavakachcheri) `LK-4130` | Jaffna | 0.3% | 2,428 | 3,247 | +819 🟩 | 3.8% | 4.8% | +1.0 🟩 pp |
| Thunukkai `LK-4403` | Mullaitivu | 0.0% | 458 | 576 | +118 🟩 | 4.7% | 5.5% | +0.8 🟩 pp |
| Valikamam East (Kopay) `LK-4118` | Jaffna | 0.4% | 4,065 | 4,684 | +619 🟩 | 5.6% | 6.2% | +0.6 🟩 pp |
| Oddusuddan `LK-4412` | Mullaitivu | 0.1% | 694 | 886 | +192 🟩 | 4.4% | 4.9% | +0.5 🟩 pp |
| Vanathavilluwa `LK-6206` | Puttalam | 0.3% | 3,023 | 3,532 | +509 🟩 | 17.3% | 17.7% | +0.4 🟩 pp |
| Welivitiya-Divitura `LK-3130` | Galle | 0.0% | 118 | 210 | +92 🟩 | 0.4% | 0.7% | +0.3 🟩 pp |
| Vadamaradchchi East `LK-4124` | Jaffna | 0.3% | 3,758 | 4,018 | +260 🟩 | 29.4% | 29.7% | +0.2 🟩 pp |
| Thawalama `LK-3118` | Galle | 0.0% | 308 | 368 | +60 🟩 | 0.9% | 1.2% | +0.2 🟩 pp |
| Lahugala `LK-5251` | Ampara | 0.0% | 24 | 53 | +29 🟩 | 0.3% | 0.5% | +0.2 🟩 pp |
| Pitabaddara `LK-3203` | Matara | 0.0% | 78 | 177 | +99 🟩 | 0.2% | 0.4% | +0.2 🟩 pp |
| Manthai East `LK-4406` | Mullaitivu | 0.0% | 272 | 307 | +35 🟩 | 3.8% | 4.0% | +0.2 🟩 pp |
| Palugaswewa `LK-7157` | Anuradhapura | 0.0% | 168 | 229 | +61 🟩 | 1.1% | 1.3% | +0.2 🟩 pp |
| Rattota `LK-2230` | Matale | 0.1% | 621 | 730 | +109 🟩 | 1.2% | 1.4% | +0.2 🟩 pp |
| Porativu Pattu `LK-5133` | Batticaloa | 0.0% | 79 | 139 | +60 🟩 | 0.2% | 0.4% | +0.1 🟩 pp |
| Verugal `LK-5333` | Trincomalee | 0.0% | 20 | 44 | +24 🟩 | 0.2% | 0.3% | +0.1 🟩 pp |
| Akuressa `LK-3218` | Matara | 0.0% | 126 | 177 | +51 🟩 | 0.2% | 0.3% | +0.1 🟩 pp |
| Athuraliya `LK-3215` | Matara | 0.0% | 58 | 89 | +31 🟩 | 0.2% | 0.3% | +0.1 🟩 pp |
| Manmunai South West `LK-5130` | Batticaloa | 0.0% | 60 | 87 | +27 🟩 | 0.2% | 0.3% | +0.1 🟩 pp |
| Gonapinuwala `LK-3134` | Galle | 0.0% | 133 | 161 | +28 🟩 | 0.6% | 0.7% | +0.1 🟩 pp |
| Ayagama `LK-9130` | Ratnapura | 0.0% | 131 | 151 | +20 🟩 | 0.4% | 0.5% | +0.1 🟩 pp |
| Thihagoda `LK-3236` | Matara | 0.0% | 22 | 50 | +28 🟩 | 0.1% | 0.1% | +0.1 🟩 pp |
| Valikamam South (Uduvil) `LK-4115` | Jaffna | 0.3% | 3,522 | 3,395 | -127 🟥 | 6.6% | 6.7% | +0.1 🟩 pp |
| Lunugamwehera `LK-3306` | Hambantota | 0.0% | 48 | 83 | +35 🟩 | 0.2% | 0.2% | +0.1 🟩 pp |
| Welioya `LK-4418` | Mullaitivu | 0.0% | 41 | 67 | +26 🟩 | 0.6% | 0.7% | +0.1 🟩 pp |
| Akmeemana `LK-3145` | Galle | 0.0% | 314 | 407 | +93 🟩 | 0.4% | 0.5% | +0.1 🟩 pp |
| Aranayake `LK-9209` | Kegalle | 0.0% | 173 | 222 | +49 🟩 | 0.3% | 0.3% | +0.1 🟩 pp |
| Koralai Pattu South `LK-5110` | Batticaloa | 0.0% | 240 | 279 | +39 🟩 | 0.9% | 1.0% | +0.1 🟩 pp |
| Tirukkovil `LK-5245` | Ampara | 0.0% | 410 | 492 | +82 🟩 | 1.6% | 1.7% | +0.1 🟩 pp |
| Nintavur `LK-5230` | Ampara | 0.0% | 5 | 24 | +19 🟩 | 0.0% | 0.1% | +0.1 🟩 pp |
| Malimbada `LK-3224` | Matara | 0.0% | 49 | 68 | +19 🟩 | 0.1% | 0.2% | 0.0 pp |
| Karandeniya `LK-3109` | Galle | 0.0% | 141 | 173 | +32 🟩 | 0.2% | 0.3% | 0.0 pp |
| Ududumbara `LK-2118` | Kandy | 0.0% | 54 | 62 | +8 🟩 | 0.2% | 0.3% | 0.0 pp |
| Agalawatta `LK-1333` | Kalutara | 0.0% | 128 | 138 | +10 🟩 | 0.3% | 0.4% | 0.0 pp |
| Kalawana `LK-9133` | Ratnapura | 0.0% | 131 | 143 | +12 🟩 | 0.3% | 0.3% | 0.0 pp |
| Ambalantota `LK-3315` | Hambantota | 0.0% | 126 | 158 | +32 🟩 | 0.2% | 0.2% | 0.0 pp |
| Mawanella `LK-9206` | Kegalle | 0.0% | 338 | 406 | +68 🟩 | 0.3% | 0.3% | 0.0 pp |
| Kotawehera `LK-6115` | Kurunegala | 0.0% | 46 | 56 | +10 🟩 | 0.2% | 0.2% | 0.0 pp |
| Naula `LK-2209` | Matale | 0.0% | 159 | 163 | +4 🟩 | 0.5% | 0.5% | 0.0 pp |
| Thanamalwila `LK-8230` | Monaragala | 0.0% | 50 | 63 | +13 🟩 | 0.2% | 0.2% | 0.0 pp |
| Welipitiya `LK-3221` | Matara | 0.0% | 60 | 72 | +12 🟩 | 0.1% | 0.1% | 0.0 pp |
| Neluwa `LK-3121` | Galle | 0.0% | 61 | 62 | +1 🟩 | 0.2% | 0.2% | 0.0 pp |
| Uhana `LK-5212` | Ampara | 0.0% | 73 | 84 | +11 🟩 | 0.1% | 0.1% | 0.0 pp |
| Hakmana `LK-3230` | Matara | 0.0% | 23 | 27 | +4 🟩 | 0.1% | 0.1% | 0.0 pp |
| Kaburupitiya `LK-3227` | Matara | 0.0% | 30 | 35 | +5 🟩 | 0.1% | 0.1% | 0.0 pp |
| Angunakolapelessa `LK-3318` | Hambantota | 0.0% | 15 | 21 | +6 🟩 | 0.0% | 0.0% | 0.0 pp |
| Medawachchiya `LK-7109` | Anuradhapura | 0.0% | 219 | 249 | +30 🟩 | 0.5% | 0.5% | 0.0 pp |
| Akkaraipattu `LK-5236` | Ampara | 0.0% | 7 | 10 | +3 🟩 | 0.0% | 0.0% | 0.0 pp |
| Weligepola `LK-9145` | Ratnapura | 0.0% | 17 | 20 | +3 🟩 | 0.1% | 0.1% | 0.0 pp |
| Alawwa `LK-6184` | Kurunegala | 0.0% | 255 | 263 | +8 🟩 | 0.4% | 0.4% | 0.0 pp |
| Katuwana `LK-3324` | Hambantota | 0.0% | 16 | 17 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Walasmulla `LK-3325` | Hambantota | 0.0% | 14 | 15 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Medadumbara `LK-2124` | Kandy | 0.1% | 1,020 | 1,076 | +56 🟩 | 1.7% | 1.7% | 0.0 pp |
| Laggala `LK-2224` | Matale | 0.0% | 5 | 6 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Mulatiyana `LK-3212` | Matara | 0.0% | 11 | 9 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Karaitivu `LK-5227` | Ampara | 0.0% | 96 | 110 | +14 🟩 | 0.6% | 0.6% | 0.0 pp |
| Kirinda Puhulwella `LK-3233` | Matara | 0.0% | 13 | 12 | -1 🟥 | 0.1% | 0.1% | 0.0 pp |
| Imaduwa `LK-3151` | Galle | 0.0% | 57 | 56 | -1 🟥 | 0.1% | 0.1% | 0.0 pp |
| Kattankudy `LK-5124` | Batticaloa | 0.0% | 13 | 9 | -4 🟥 | 0.0% | 0.0% | 0.0 pp |
| Kiriella `LK-9109` | Ratnapura | 0.0% | 176 | 160 | -16 🟥 | 0.5% | 0.5% | 0.0 pp |
| Sevanagala `LK-8233` | Monaragala | 0.0% | 37 | 36 | -1 🟥 | 0.1% | 0.1% | 0.0 pp |
| Kahatagasdigiliya `LK-7121` | Anuradhapura | 0.0% | 115 | 121 | +6 🟩 | 0.3% | 0.3% | 0.0 pp |
| Okewela `LK-3327` | Hambantota | 0.0% | 9 | 6 | -3 🟥 | 0.0% | 0.0% | 0.0 pp |
| Weeraketiya `LK-3321` | Hambantota | 0.0% | 24 | 19 | -5 🟥 | 0.1% | 0.0% | 0.0 pp |
| Minipe `LK-2121` | Kandy | 0.0% | 48 | 39 | -9 🟥 | 0.1% | 0.1% | 0.0 pp |
| Walallawita `LK-1339` | Kalutara | 0.0% | 129 | 118 | -11 🟥 | 0.2% | 0.2% | 0.0 pp |
| Sainthamaruthu `LK-5225` | Ampara | 0.0% | 11 | 6 | -5 🟥 | 0.0% | 0.0% | 0.0 pp |
| Vadamaradchchi South-West (Karaveddy) `LK-4121` | Jaffna | 0.1% | 1,134 | 1,009 | -125 🟥 | 2.5% | 2.5% | 0.0 pp |
| Kuliyapitiya East `LK-6169` | Kurunegala | 0.0% | 389 | 425 | +36 🟩 | 0.7% | 0.7% | 0.0 pp |
| Ehetuwewa `LK-6109` | Kurunegala | 0.0% | 43 | 40 | -3 🟥 | 0.2% | 0.1% | 0.0 pp |
| Dikwella `LK-3248` | Matara | 0.0% | 47 | 34 | -13 🟥 | 0.1% | 0.1% | 0.0 pp |
| Padiyathalawa `LK-5206` | Ampara | 0.0% | 19 | 16 | -3 🟥 | 0.1% | 0.1% | 0.0 pp |
| Koralai Pattu West `LK-5106` | Batticaloa | 0.0% | 7 | 1 | -6 🟥 | 0.0% | 0.0% | 0.0 pp |
| Siyambalanduwa `LK-8212` | Monaragala | 0.0% | 63 | 56 | -7 🟥 | 0.1% | 0.1% | 0.0 pp |
| Gomarankadawala `LK-5309` | Trincomalee | 0.0% | 11 | 10 | -1 🟥 | 0.1% | 0.1% | 0.0 pp |
| Horowpathana `LK-7124` | Anuradhapura | 0.0% | 90 | 88 | -2 🟥 | 0.2% | 0.2% | 0.0 pp |
| Kinniya `LK-5324` | Trincomalee | 0.0% | 39 | 25 | -14 🟥 | 0.1% | 0.0% | 0.0 pp |
| Weligama `LK-3239` | Matara | 0.0% | 141 | 122 | -19 🟥 | 0.2% | 0.2% | 0.0 pp |
| Tumpane `LK-2103` | Kandy | 0.0% | 118 | 108 | -10 🟥 | 0.3% | 0.3% | 0.0 pp |
| Medagama `LK-8209` | Monaragala | 0.0% | 40 | 33 | -7 🟥 | 0.1% | 0.1% | 0.0 pp |
| Manmunai West `LK-5121` | Batticaloa | 0.0% | 265 | 293 | +28 🟩 | 0.9% | 0.9% | 0.0 pp |
| Balapitiya `LK-3106` | Galle | 0.0% | 126 | 101 | -25 🟥 | 0.2% | 0.1% | 0.0 pp |
| Galenbidunuwewa `LK-7127` | Anuradhapura | 0.0% | 58 | 44 | -14 🟥 | 0.1% | 0.1% | 0.0 pp |
| Wilgamuwa `LK-2227` | Matale | 0.0% | 17 | 6 | -11 🟥 | 0.1% | 0.0% | 0.0 pp |
| Ambalangoda `LK-3133` | Galle | 0.0% | 88 | 66 | -22 🟥 | 0.2% | 0.1% | 0.0 pp |
| Sooriyawewa `LK-3303` | Hambantota | 0.0% | 32 | 16 | -16 🟥 | 0.1% | 0.0% | 0.0 pp |
| Poojapitiya `LK-2106` | Kandy | 0.0% | 184 | 165 | -19 🟥 | 0.3% | 0.3% | 0.0 pp |
| Karainagar `LK-4104` | Jaffna | 0.0% | 42 | 36 | -6 🟥 | 0.4% | 0.4% | 0.0 pp |
| Devinuwara `LK-3245` | Matara | 0.0% | 92 | 71 | -21 🟥 | 0.2% | 0.1% | 0.0 pp |
| Rambukkana `LK-9203` | Kegalle | 0.1% | 1,326 | 1,351 | +25 🟩 | 1.6% | 1.6% | -0.1 🟥 pp |
| Habaraduwa `LK-3154` | Galle | 0.0% | 221 | 190 | -31 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Nachchaduwa `LK-7136` | Anuradhapura | 0.0% | 94 | 89 | -5 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Bentota `LK-3103` | Galle | 0.0% | 133 | 104 | -29 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Niyagama `LK-3115` | Galle | 0.0% | 56 | 36 | -20 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Harispattuwa `LK-2133` | Kandy | 0.1% | 1,099 | 1,115 | +16 🟩 | 1.2% | 1.2% | -0.1 🟥 pp |
| Matara Four Gravets `LK-3242` | Matara | 0.0% | 469 | 425 | -44 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Madulla `LK-8206` | Monaragala | 0.0% | 83 | 74 | -9 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Navithanveli `LK-5216` | Ampara | 0.2% | 1,687 | 1,955 | +268 🟩 | 9.0% | 8.9% | -0.1 🟥 pp |
| Kebithigollewa `LK-7106` | Anuradhapura | 0.0% | 25 | 12 | -13 🟥 | 0.1% | 0.0% | -0.1 🟥 pp |
| Ukuwela `LK-2233` | Matale | 0.1% | 845 | 850 | +5 🟩 | 1.2% | 1.2% | -0.1 🟥 pp |
| Bibile `LK-8203` | Monaragala | 0.0% | 137 | 129 | -8 🟥 | 0.3% | 0.3% | -0.1 🟥 pp |
| Nagoda `LK-3124` | Galle | 0.0% | 244 | 201 | -43 🟥 | 0.5% | 0.4% | -0.1 🟥 pp |
| Mahaoya `LK-5209` | Ampara | 0.0% | 29 | 17 | -12 🟥 | 0.1% | 0.1% | -0.1 🟥 pp |
| Horana `LK-1309` | Kalutara | 0.1% | 942 | 1,019 | +77 🟩 | 0.8% | 0.8% | -0.1 🟥 pp |
| Deltota `LK-2148` | Kandy | 0.0% | 205 | 193 | -12 🟥 | 0.7% | 0.6% | -0.1 🟥 pp |
| Beliatta `LK-3330` | Hambantota | 0.0% | 114 | 78 | -36 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Kotapola `LK-3206` | Matara | 0.1% | 1,093 | 1,010 | -83 🟥 | 1.7% | 1.7% | -0.1 🟥 pp |
| Galnewa `LK-7163` | Anuradhapura | 0.0% | 70 | 51 | -19 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Mahiyanganaya `LK-8103` | Badulla | 0.0% | 143 | 102 | -41 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Bulathsinhala `LK-1312` | Kalutara | 0.0% | 338 | 294 | -44 🟥 | 0.5% | 0.4% | -0.1 🟥 pp |
| Bamunakotuwa `LK-6149` | Kurunegala | 0.0% | 557 | 577 | +20 🟩 | 1.5% | 1.5% | -0.1 🟥 pp |
| Vavuniya South `LK-4306` | Vavuniya | 0.0% | 209 | 225 | +16 🟩 | 1.6% | 1.5% | -0.1 🟥 pp |
| Manmunai Pattu `LK-5127` | Batticaloa | 0.1% | 1,075 | 1,251 | +176 🟩 | 3.5% | 3.4% | -0.1 🟥 pp |
| Thissamaharama `LK-3309` | Hambantota | 0.0% | 195 | 152 | -43 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Millaniya `LK-1318` | Kalutara | 0.0% | 458 | 448 | -10 🟥 | 0.9% | 0.8% | -0.1 🟥 pp |
| Ibbagamuwa `LK-6130` | Kurunegala | 0.1% | 756 | 762 | +6 🟩 | 0.9% | 0.8% | -0.1 🟥 pp |
| Rambewa `LK-7118` | Anuradhapura | 0.0% | 150 | 130 | -20 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Elpitiya `LK-3112` | Galle | 0.0% | 262 | 215 | -47 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Rideemaliyadda `LK-8106` | Badulla | 0.0% | 95 | 61 | -34 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Rideegama `LK-6163` | Kurunegala | 0.0% | 497 | 454 | -43 🟥 | 0.6% | 0.5% | -0.1 🟥 pp |
| Nikaweratiya `LK-6121` | Kurunegala | 0.0% | 581 | 585 | +4 🟩 | 1.4% | 1.3% | -0.1 🟥 pp |
| Embilipitiya `LK-9148` | Ratnapura | 0.0% | 310 | 226 | -84 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Madurawala `LK-1315` | Kalutara | 0.0% | 143 | 120 | -23 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Dodangoda `LK-1327` | Kalutara | 0.1% | 1,268 | 1,268 | +0 | 2.0% | 1.9% | -0.1 🟥 pp |
| Pasgoda `LK-3209` | Matara | 0.0% | 120 | 67 | -53 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Thalawa `LK-7148` | Anuradhapura | 0.0% | 282 | 239 | -43 🟥 | 0.5% | 0.4% | -0.1 🟥 pp |
| Opanayake `LK-9121` | Ratnapura | 0.0% | 131 | 107 | -24 🟥 | 0.5% | 0.4% | -0.1 🟥 pp |
| Pelmadulla `LK-9124` | Ratnapura | 0.1% | 699 | 639 | -60 🟥 | 0.8% | 0.7% | -0.1 🟥 pp |
| Arachchikattuwa `LK-6230` | Puttalam | 1.2% | 13,894 | 14,443 | +549 🟩 | 33.9% | 33.8% | -0.1 🟥 pp |
| Bope-Poddala `LK-3142` | Galle | 0.0% | 314 | 301 | -13 🟥 | 0.6% | 0.5% | -0.1 🟥 pp |
| Dehiattakandiya `LK-5203` | Ampara | 0.0% | 110 | 52 | -58 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Ambanganga `LK-2221` | Matale | 0.0% | 134 | 119 | -15 🟥 | 0.9% | 0.7% | -0.1 🟥 pp |
| Hatharaliyadda `LK-2134` | Kandy | 0.0% | 88 | 58 | -30 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Buttala `LK-8224` | Monaragala | 0.0% | 163 | 121 | -42 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Mihinthale `LK-7130` | Anuradhapura | 0.0% | 326 | 360 | +34 🟩 | 0.9% | 0.8% | -0.1 🟥 pp |
| Tangalle `LK-3333` | Hambantota | 0.0% | 251 | 189 | -62 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Dimbulagala `LK-7212` | Polonnaruwa | 0.0% | 444 | 385 | -59 🟥 | 0.6% | 0.4% | -0.1 🟥 pp |
| Kahawattha `LK-9139` | Ratnapura | 0.1% | 684 | 640 | -44 🟥 | 1.6% | 1.5% | -0.1 🟥 pp |
| Galigamuwa `LK-9215` | Kegalle | 0.0% | 484 | 394 | -90 🟥 | 0.6% | 0.5% | -0.1 🟥 pp |
| Yatawatta `LK-2215` | Matale | 0.0% | 375 | 364 | -11 🟥 | 1.2% | 1.1% | -0.1 🟥 pp |
| Valikamam West (Chankanai) `LK-4106` | Jaffna | 0.1% | 761 | 687 | -74 🟥 | 1.6% | 1.5% | -0.1 🟥 pp |
| Palagala `LK-7166` | Anuradhapura | 0.0% | 120 | 90 | -30 🟥 | 0.4% | 0.2% | -0.1 🟥 pp |
| Medirigiriya `LK-7206` | Polonnaruwa | 0.0% | 202 | 136 | -66 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Hambantota `LK-3312` | Hambantota | 0.0% | 295 | 263 | -32 🟥 | 0.5% | 0.4% | -0.1 🟥 pp |
| Elahera `LK-7218` | Polonnaruwa | 0.0% | 123 | 74 | -49 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Manmunai South & Eruvil Pattu `LK-5136` | Batticaloa | 0.1% | 1,591 | 1,565 | -26 🟥 | 2.6% | 2.5% | -0.1 🟥 pp |
| Giribawa `LK-6103` | Kurunegala | 0.0% | 105 | 71 | -34 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Kandeketiya `LK-8112` | Badulla | 0.0% | 41 | 12 | -29 🟥 | 0.2% | 0.0% | -0.1 🟥 pp |
| Pallepola `LK-2212` | Matale | 0.0% | 119 | 85 | -34 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Kantale `LK-5321` | Trincomalee | 0.0% | 219 | 169 | -50 🟥 | 0.5% | 0.3% | -0.1 🟥 pp |
| Rajanganaya `LK-7142` | Anuradhapura | 0.0% | 426 | 411 | -15 🟥 | 1.3% | 1.1% | -0.1 🟥 pp |
| Lankapura `LK-7209` | Polonnaruwa | 0.0% | 181 | 143 | -38 🟥 | 0.5% | 0.4% | -0.1 🟥 pp |
| Wellawaya `LK-8221` | Monaragala | 0.0% | 189 | 129 | -60 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Yakkalamulla `LK-3148` | Galle | 0.0% | 188 | 126 | -62 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Welimada `LK-8130` | Badulla | 0.1% | 739 | 626 | -113 🟥 | 0.7% | 0.6% | -0.1 🟥 pp |
| Thambalagamuwa `LK-5318` | Trincomalee | 0.0% | 114 | 87 | -27 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Kandavalai `LK-4506` | Kilinochchi | 0.1% | 1,485 | 1,560 | +75 🟩 | 6.4% | 6.3% | -0.1 🟥 pp |
| Ipalogama `LK-7160` | Anuradhapura | 0.0% | 258 | 217 | -41 🟥 | 0.7% | 0.5% | -0.1 🟥 pp |
| Kekirawa `LK-7154` | Anuradhapura | 0.0% | 464 | 415 | -49 🟥 | 0.8% | 0.6% | -0.1 🟥 pp |
| Bulathkohipitiya `LK-9224` | Kegalle | 0.0% | 387 | 304 | -83 🟥 | 0.8% | 0.7% | -0.1 🟥 pp |
| Maho `LK-6124` | Kurunegala | 0.0% | 365 | 309 | -56 🟥 | 0.6% | 0.5% | -0.2 🟥 pp |
| Weerabugedara `LK-6166` | Kurunegala | 0.1% | 726 | 717 | -9 🟥 | 2.1% | 2.0% | -0.2 🟥 pp |
| Galgamuwa `LK-6106` | Kurunegala | 0.0% | 582 | 555 | -27 🟥 | 1.1% | 0.9% | -0.2 🟥 pp |
| Nivithigala `LK-9136` | Ratnapura | 0.0% | 570 | 469 | -101 🟥 | 0.9% | 0.8% | -0.2 🟥 pp |
| Padukka `LK-1118` | Colombo | 0.0% | 565 | 516 | -49 🟥 | 0.9% | 0.7% | -0.2 🟥 pp |
| Welikanda `LK-7210` | Polonnaruwa | 0.0% | 215 | 181 | -34 🟥 | 0.6% | 0.5% | -0.2 🟥 pp |
| Akurana `LK-2109` | Kandy | 0.0% | 252 | 164 | -88 🟥 | 0.4% | 0.2% | -0.2 🟥 pp |
| Galle 4 Gravets `LK-3139` | Galle | 0.1% | 898 | 774 | -124 🟥 | 0.9% | 0.7% | -0.2 🟥 pp |
| Kundasale `LK-2127` | Kandy | 0.2% | 2,165 | 2,210 | +45 🟩 | 1.7% | 1.5% | -0.2 🟥 pp |
| Mahawilachchiya `LK-7112` | Anuradhapura | 0.0% | 144 | 113 | -31 🟥 | 0.6% | 0.5% | -0.2 🟥 pp |
| Ruwanwella `LK-9221` | Kegalle | 0.0% | 566 | 467 | -99 🟥 | 0.9% | 0.7% | -0.2 🟥 pp |
| Meegahakiula `LK-8109` | Badulla | 0.0% | 80 | 52 | -28 🟥 | 0.4% | 0.2% | -0.2 🟥 pp |
| Mawathagama `LK-6160` | Kurunegala | 0.1% | 897 | 865 | -32 🟥 | 1.4% | 1.2% | -0.2 🟥 pp |
| Katharagama `LK-8227` | Monaragala | 0.0% | 65 | 32 | -33 🟥 | 0.4% | 0.2% | -0.2 🟥 pp |
| Polpitigama `LK-6127` | Kurunegala | 0.0% | 350 | 234 | -116 🟥 | 0.5% | 0.3% | -0.2 🟥 pp |
| Dambulla `LK-2206` | Matale | 0.1% | 895 | 851 | -44 🟥 | 1.2% | 1.0% | -0.2 🟥 pp |
| Ingiriya `LK-1310` | Kalutara | 0.0% | 324 | 239 | -85 🟥 | 0.6% | 0.4% | -0.2 🟥 pp |
| Badalkumbura `LK-8218` | Monaragala | 0.0% | 294 | 251 | -43 🟥 | 0.7% | 0.5% | -0.2 🟥 pp |
| Uvaparanagama `LK-8127` | Badulla | 0.0% | 505 | 371 | -134 🟥 | 0.6% | 0.5% | -0.2 🟥 pp |
| Udunuwara `LK-2139` | Kandy | 0.1% | 848 | 683 | -165 🟥 | 0.8% | 0.6% | -0.2 🟥 pp |
| Pathahewaheta `LK-2145` | Kandy | 0.0% | 621 | 525 | -96 🟥 | 1.1% | 0.9% | -0.2 🟥 pp |
| Soranathota `LK-8115` | Badulla | 0.0% | 126 | 87 | -39 🟥 | 0.6% | 0.4% | -0.2 🟥 pp |
| Kolonna `LK-9151` | Ratnapura | 0.0% | 272 | 195 | -77 🟥 | 0.6% | 0.4% | -0.2 🟥 pp |
| Damana `LK-5242` | Ampara | 0.0% | 126 | 47 | -79 🟥 | 0.3% | 0.1% | -0.2 🟥 pp |
| Warakapola `LK-9218` | Kegalle | 0.0% | 677 | 456 | -221 🟥 | 0.6% | 0.4% | -0.2 🟥 pp |
| Seruvila `LK-5330` | Trincomalee | 0.0% | 58 | 34 | -24 🟥 | 0.4% | 0.2% | -0.2 🟥 pp |
| Panduwasnuwara East `LK-6148` | Kurunegala | 0.0% | 519 | 479 | -40 🟥 | 1.7% | 1.5% | -0.2 🟥 pp |
| Bandaragama `LK-1306` | Kalutara | 0.2% | 2,067 | 2,070 | +3 🟩 | 1.9% | 1.7% | -0.2 🟥 pp |
| Ganewatta `LK-6133` | Kurunegala | 0.0% | 363 | 289 | -74 🟥 | 0.9% | 0.7% | -0.2 🟥 pp |
| Narammala `LK-6181` | Kurunegala | 0.0% | 609 | 502 | -107 🟥 | 1.1% | 0.8% | -0.2 🟥 pp |
| Elapatha `LK-9127` | Ratnapura | 0.0% | 291 | 202 | -89 🟥 | 0.8% | 0.5% | -0.2 🟥 pp |
| Mirigama `LK-1212` | Gampaha | 0.1% | 1,794 | 1,496 | -298 🟥 | 1.1% | 0.8% | -0.2 🟥 pp |
| Yatiyantota `LK-9227` | Kegalle | 0.1% | 800 | 663 | -137 🟥 | 1.3% | 1.1% | -0.2 🟥 pp |
| Matugama `LK-1330` | Kalutara | 0.0% | 650 | 476 | -174 🟥 | 0.8% | 0.6% | -0.2 🟥 pp |
| Homagama `LK-1112` | Colombo | 0.3% | 3,618 | 3,553 | -65 🟥 | 1.5% | 1.3% | -0.3 🟥 pp |
| Padavi Sri Pura `LK-5303` | Trincomalee | 0.0% | 70 | 40 | -30 🟥 | 0.6% | 0.3% | -0.3 🟥 pp |
| Mallawapitiya `LK-6157` | Kurunegala | 0.1% | 1,058 | 1,042 | -16 🟥 | 2.0% | 1.8% | -0.3 🟥 pp |
| Yatinuwara `LK-2136` | Kandy | 0.1% | 1,033 | 801 | -232 🟥 | 1.0% | 0.7% | -0.3 🟥 pp |
| Pathadumbara `LK-2112` | Kandy | 0.1% | 1,032 | 841 | -191 🟥 | 1.2% | 0.9% | -0.3 🟥 pp |
| Thambuththegama `LK-7145` | Anuradhapura | 0.0% | 342 | 251 | -91 🟥 | 0.8% | 0.5% | -0.3 🟥 pp |
| Ambanpola `LK-6112` | Kurunegala | 0.0% | 125 | 69 | -56 🟥 | 0.5% | 0.3% | -0.3 🟥 pp |
| Thirappane `LK-7151` | Anuradhapura | 0.1% | 728 | 751 | +23 🟩 | 2.7% | 2.4% | -0.3 🟥 pp |
| Passara `LK-8118` | Badulla | 0.1% | 1,082 | 960 | -122 🟥 | 2.2% | 1.9% | -0.3 🟥 pp |
| Polgahawela `LK-6187` | Kurunegala | 0.1% | 888 | 726 | -162 🟥 | 1.4% | 1.1% | -0.3 🟥 pp |
| Palindanuwara `LK-1336` | Kalutara | 0.0% | 296 | 144 | -152 🟥 | 0.6% | 0.3% | -0.3 🟥 pp |
| Sammanthurai `LK-5218` | Ampara | 0.0% | 281 | 118 | -163 🟥 | 0.5% | 0.2% | -0.3 🟥 pp |
| Godakawela `LK-9142` | Ratnapura | 0.1% | 1,341 | 1,132 | -209 🟥 | 1.8% | 1.4% | -0.3 🟥 pp |
| Badulla `LK-8121` | Badulla | 0.1% | 1,296 | 1,170 | -126 🟥 | 1.7% | 1.4% | -0.3 🟥 pp |
| Thamankaduwa `LK-7215` | Polonnaruwa | 0.1% | 984 | 804 | -180 🟥 | 1.2% | 0.9% | -0.3 🟥 pp |
| Galewela `LK-2203` | Matale | 0.3% | 3,287 | 3,438 | +151 🟩 | 4.7% | 4.4% | -0.3 🟥 pp |
| Rasnayakapura `LK-6118` | Kurunegala | 0.0% | 348 | 316 | -32 🟥 | 1.6% | 1.3% | -0.3 🟥 pp |
| Kobeigane `LK-6139` | Kurunegala | 0.1% | 832 | 809 | -23 🟥 | 2.3% | 2.0% | -0.3 🟥 pp |
| Doluwa `LK-2142` | Kandy | 0.0% | 584 | 445 | -139 🟥 | 1.2% | 0.8% | -0.3 🟥 pp |
| Padaviya `LK-7103` | Anuradhapura | 0.0% | 216 | 149 | -67 🟥 | 0.9% | 0.6% | -0.3 🟥 pp |
| Karachchi `LK-4509` | Kilinochchi | 0.5% | 5,015 | 5,839 | +824 🟩 | 8.2% | 7.8% | -0.3 🟥 pp |
| Wariyapola `LK-6136` | Kurunegala | 0.1% | 758 | 597 | -161 🟥 | 1.2% | 0.9% | -0.3 🟥 pp |
| Hali-Ela `LK-8124` | Badulla | 0.1% | 1,245 | 974 | -271 🟥 | 1.4% | 1.0% | -0.3 🟥 pp |
| Town & Gravets `LK-5315` | Trincomalee | 0.9% | 11,103 | 11,065 | -38 🟥 | 11.4% | 11.0% | -0.4 🟥 pp |
| Ganga Ihala Korale `LK-2154` | Kandy | 0.0% | 485 | 282 | -203 🟥 | 0.9% | 0.5% | -0.4 🟥 pp |
| Kegalle `LK-9212` | Kegalle | 0.1% | 1,576 | 1,254 | -322 🟥 | 1.7% | 1.3% | -0.4 🟥 pp |
| Ja Ela `LK-1221` | Gampaha | 8.5% | 99,515 | 100,285 | +770 🟩 | 49.4% | 49.0% | -0.4 🟥 pp |
| Nochchiyagama `LK-7139` | Anuradhapura | 0.0% | 630 | 460 | -170 🟥 | 1.3% | 0.8% | -0.4 🟥 pp |
| Higurakgoda `LK-7203` | Polonnaruwa | 0.1% | 1,043 | 837 | -206 🟥 | 1.6% | 1.2% | -0.4 🟥 pp |
| Divulapitiya `LK-1209` | Gampaha | 1.7% | 19,395 | 20,361 | +966 🟩 | 13.4% | 13.0% | -0.4 🟥 pp |
| Morawewa `LK-5312` | Trincomalee | 0.0% | 55 | 22 | -33 🟥 | 0.7% | 0.2% | -0.5 🟥 pp |
| Matale `LK-2218` | Matale | 0.1% | 1,442 | 1,185 | -257 🟥 | 1.9% | 1.5% | -0.5 🟥 pp |
| Dompe `LK-1230` | Gampaha | 0.4% | 4,691 | 4,393 | -298 🟥 | 3.0% | 2.6% | -0.5 🟥 pp |
| Minuwangoda `LK-1215` | Gampaha | 1.0% | 11,512 | 11,896 | +384 🟩 | 6.5% | 6.0% | -0.5 🟥 pp |
| Koralai Pattu North `LK-5103` | Batticaloa | 0.1% | 641 | 638 | -3 🟥 | 3.0% | 2.5% | -0.5 🟥 pp |
| Dehiowita `LK-9230` | Kegalle | 0.1% | 1,761 | 1,436 | -325 🟥 | 2.2% | 1.7% | -0.5 🟥 pp |
| Ella `LK-8136` | Badulla | 0.0% | 549 | 365 | -184 🟥 | 1.2% | 0.7% | -0.5 🟥 pp |
| Nuwaragam Palatha Central `LK-7115` | Anuradhapura | 0.0% | 623 | 383 | -240 🟥 | 1.0% | 0.5% | -0.5 🟥 pp |
| Maspotha `LK-6151` | Kurunegala | 0.1% | 1,220 | 1,286 | +66 🟩 | 3.6% | 3.1% | -0.5 🟥 pp |
| Muthur `LK-5327` | Trincomalee | 0.1% | 1,459 | 1,494 | +35 🟩 | 2.6% | 2.1% | -0.5 🟥 pp |
| Haldummulla `LK-8142` | Badulla | 0.0% | 418 | 238 | -180 🟥 | 1.1% | 0.6% | -0.5 🟥 pp |
| Attanagalla `LK-1227` | Gampaha | 0.3% | 3,685 | 3,036 | -649 🟥 | 2.1% | 1.5% | -0.5 🟥 pp |
| Monaragala `LK-8215` | Monaragala | 0.0% | 480 | 257 | -223 🟥 | 1.0% | 0.5% | -0.5 🟥 pp |
| Manthai West `LK-4206` | Mannar | 0.7% | 6,469 | 8,081 | +1,612 🟩 | 43.8% | 43.3% | -0.5 🟥 pp |
| Imbulpe `LK-9115` | Ratnapura | 0.1% | 1,135 | 894 | -241 🟥 | 1.9% | 1.4% | -0.5 🟥 pp |
| Ampara `LK-5215` | Ampara | 0.0% | 537 | 335 | -202 🟥 | 1.2% | 0.7% | -0.5 🟥 pp |
| Nuwaragam Palatha East `LK-7133` | Anuradhapura | 0.1% | 1,199 | 908 | -291 🟥 | 1.7% | 1.2% | -0.5 🟥 pp |
| Udapalatha `LK-2151` | Kandy | 0.1% | 1,598 | 1,249 | -349 🟥 | 1.7% | 1.2% | -0.5 🟥 pp |
| Nawagattegama `LK-6212` | Puttalam | 0.0% | 174 | 116 | -58 🟥 | 1.2% | 0.7% | -0.5 🟥 pp |
| Kesbewa `LK-1136` | Colombo | 0.6% | 8,297 | 7,459 | -838 🟥 | 3.4% | 2.8% | -0.6 🟥 pp |
| Anamaduwa `LK-6224` | Puttalam | 0.1% | 1,299 | 1,230 | -69 🟥 | 3.4% | 2.8% | -0.6 🟥 pp |
| Ratnapura `LK-9112` | Ratnapura | 0.1% | 1,812 | 1,139 | -673 🟥 | 1.5% | 0.9% | -0.6 🟥 pp |
| Panduwasnuwara West `LK-6145` | Kurunegala | 0.1% | 1,973 | 1,719 | -254 🟥 | 3.0% | 2.4% | -0.6 🟥 pp |
| Panvila `LK-2115` | Kandy | 0.1% | 898 | 723 | -175 🟥 | 3.4% | 2.8% | -0.6 🟥 pp |
| Kolonnawa `LK-1106` | Colombo | 0.6% | 7,360 | 6,895 | -465 🟥 | 3.8% | 3.2% | -0.6 🟥 pp |
| Kuchchaweli `LK-5306` | Trincomalee | 0.1% | 1,345 | 1,363 | +18 🟩 | 4.0% | 3.4% | -0.6 🟥 pp |
| Thimbirigasyaya `LK-1127` | Colombo | 1.3% | 18,208 | 15,209 | -2,999 🟥 | 7.7% | 7.0% | -0.7 🟥 pp |
| Moratuwa `LK-1133` | Colombo | 2.6% | 33,319 | 30,669 | -2,650 🟥 | 19.8% | 19.1% | -0.7 🟥 pp |
| Valikamam South West (Sandilipay) `LK-4109` | Jaffna | 0.9% | 10,631 | 10,258 | -373 🟥 | 20.3% | 19.7% | -0.7 🟥 pp |
| Bandarawela `LK-8133` | Badulla | 0.1% | 2,182 | 1,739 | -443 🟥 | 3.3% | 2.7% | -0.7 🟥 pp |
| Sri Jayawardanapura Kotte `LK-1124` | Colombo | 0.5% | 7,853 | 6,340 | -1,513 🟥 | 7.3% | 6.6% | -0.7 🟥 pp |
| Pasbagekorale `LK-2157` | Kandy | 0.2% | 2,490 | 2,268 | -222 🟥 | 4.2% | 3.5% | -0.7 🟥 pp |
| Maharagama `LK-1121` | Colombo | 0.4% | 6,618 | 5,252 | -1,366 🟥 | 3.4% | 2.7% | -0.7 🟥 pp |
| Kurunegala `LK-6154` | Kurunegala | 0.2% | 2,895 | 2,568 | -327 🟥 | 3.6% | 2.9% | -0.7 🟥 pp |
| Deraniyagala `LK-9233` | Kegalle | 0.0% | 689 | 339 | -350 🟥 | 1.5% | 0.8% | -0.7 🟥 pp |
| Colombo `LK-1103` | Colombo | 3.1% | 42,435 | 36,117 | -6,318 🟥 | 13.1% | 12.4% | -0.8 🟥 pp |
| Kuliyapitiya West `LK-6172` | Kurunegala | 0.3% | 4,447 | 4,114 | -333 🟥 | 5.8% | 5.0% | -0.8 🟥 pp |
| Lunugala `LK-8119` | Badulla | 0.1% | 1,494 | 1,265 | -229 🟥 | 4.8% | 4.0% | -0.8 🟥 pp |
| Kalutara `LK-1321` | Kalutara | 0.7% | 9,738 | 8,815 | -923 🟥 | 6.1% | 5.3% | -0.8 🟥 pp |
| Haputale `LK-8139` | Badulla | 0.1% | 2,025 | 1,571 | -454 🟥 | 4.1% | 3.3% | -0.8 🟥 pp |
| Alayadivembu `LK-5239` | Ampara | 0.2% | 1,983 | 1,989 | +6 🟩 | 8.8% | 8.0% | -0.8 🟥 pp |
| Wennappuwa `LK-6245` | Puttalam | 4.2% | 53,426 | 50,261 | -3,165 🟥 | 78.4% | 77.6% | -0.8 🟥 pp |
| Vavuniya `LK-4309` | Vavuniya | 0.8% | 10,219 | 9,184 | -1,035 🟥 | 8.7% | 7.9% | -0.8 🟥 pp |
| Mahakumbukkadawala `LK-6221` | Puttalam | 0.2% | 2,250 | 2,452 | +202 🟩 | 12.1% | 11.2% | -0.9 🟥 pp |
| Panadura `LK-1303` | Kalutara | 0.7% | 9,368 | 7,982 | -1,386 🟥 | 5.1% | 4.3% | -0.9 🟥 pp |
| Pannala `LK-6178` | Kurunegala | 0.6% | 7,616 | 7,048 | -568 🟥 | 6.1% | 5.2% | -0.9 🟥 pp |
| Beruwala `LK-1324` | Kalutara | 1.1% | 13,925 | 13,379 | -546 🟥 | 8.4% | 7.4% | -1.0 🟥 pp |
| Gampaha `LK-1224` | Gampaha | 1.7% | 21,085 | 19,706 | -1,379 🟥 | 10.7% | 9.6% | -1.1 🟥 pp |
| Biyagama `LK-1239` | Gampaha | 0.6% | 8,533 | 7,229 | -1,304 🟥 | 4.6% | 3.5% | -1.1 🟥 pp |
| Gangawata Korale `LK-2130` | Kandy | 0.5% | 7,557 | 5,616 | -1,941 🟥 | 4.8% | 3.7% | -1.1 🟥 pp |
| Maritimepattu `LK-4415` | Mullaitivu | 0.5% | 5,293 | 6,329 | +1,036 🟩 | 18.3% | 17.2% | -1.1 🟥 pp |
| Mundel `LK-6218` | Puttalam | 1.7% | 17,806 | 20,129 | +2,323 🟩 | 28.9% | 27.7% | -1.2 🟥 pp |
| Kaduwela `LK-1109` | Colombo | 0.9% | 12,519 | 10,576 | -1,943 🟥 | 5.0% | 3.8% | -1.2 🟥 pp |
| Bingiriya `LK-6142` | Kurunegala | 0.5% | 6,401 | 6,072 | -329 🟥 | 10.3% | 9.1% | -1.2 🟥 pp |
| Mahara `LK-1233` | Gampaha | 1.4% | 18,183 | 16,909 | -1,274 🟥 | 8.8% | 7.6% | -1.2 🟥 pp |
| Pachchilaipalli `LK-4503` | Kilinochchi | 0.1% | 942 | 1,280 | +338 🟩 | 11.0% | 9.8% | -1.2 🟥 pp |
| Chilaw `LK-6233` | Puttalam | 2.4% | 28,544 | 28,248 | -296 🟥 | 45.7% | 44.4% | -1.3 🟥 pp |
| Madampe `LK-6236` | Puttalam | 0.7% | 8,304 | 7,860 | -444 🟥 | 17.3% | 16.0% | -1.3 🟥 pp |
| Ratmalana `LK-1131` | Colombo | 0.5% | 7,183 | 5,455 | -1,728 🟥 | 7.5% | 6.2% | -1.3 🟥 pp |
| Mahawewa `LK-6239` | Puttalam | 2.1% | 26,436 | 24,602 | -1,834 🟥 | 51.8% | 50.4% | -1.4 🟥 pp |
| Seethawaka `LK-1115` | Colombo | 0.6% | 8,309 | 7,214 | -1,095 🟥 | 7.3% | 5.9% | -1.4 🟥 pp |
| Puttalam `LK-6215` | Puttalam | 0.7% | 8,302 | 8,222 | -80 🟥 | 10.1% | 8.7% | -1.4 🟥 pp |
| Manmunai North `LK-5118` | Batticaloa | 1.4% | 16,360 | 16,570 | +210 🟩 | 19.0% | 17.4% | -1.6 🟥 pp |
| Pallama `LK-6227` | Puttalam | 0.3% | 3,244 | 3,267 | +23 🟩 | 13.3% | 11.7% | -1.6 🟥 pp |
| Dehiwala `LK-1130` | Colombo | 0.4% | 5,976 | 4,627 | -1,349 🟥 | 6.7% | 4.9% | -1.8 🟥 pp |
| Negombo `LK-1203` | Gampaha | 7.4% | 92,828 | 87,605 | -5,223 🟥 | 65.3% | 63.5% | -1.8 🟥 pp |
| Dankotuwa `LK-6248` | Puttalam | 1.5% | 18,622 | 17,539 | -1,083 🟥 | 29.8% | 27.9% | -1.9 🟥 pp |
| Nanaddan `LK-4212` | Mannar | 1.1% | 12,229 | 13,056 | +827 🟩 | 68.4% | 66.4% | -2.0 🟥 pp |
| Udubaddawa `LK-6175` | Kurunegala | 0.6% | 7,506 | 6,724 | -782 🟥 | 14.4% | 12.3% | -2.0 🟥 pp |
| Kelaniya `LK-1236` | Gampaha | 0.9% | 13,458 | 10,341 | -3,117 🟥 | 9.8% | 7.7% | -2.1 🟥 pp |
| Karuwalagaswewa `LK-6209` | Puttalam | 0.1% | 1,791 | 1,447 | -344 🟥 | 7.6% | 5.5% | -2.1 🟥 pp |
| Jaffna `LK-4136` | Jaffna | 2.1% | 26,700 | 24,546 | -2,154 🟥 | 52.9% | 50.6% | -2.3 🟥 pp |
| Vadamaradchi North (Point Pedro) `LK-4127` | Jaffna | 0.4% | 6,356 | 4,781 | -1,575 🟥 | 13.4% | 11.0% | -2.3 🟥 pp |
| Nattandiya `LK-6242` | Puttalam | 2.1% | 25,226 | 25,002 | -224 🟥 | 40.6% | 38.2% | -2.4 🟥 pp |
| Wattala `LK-1218` | Gampaha | 6.5% | 79,334 | 77,121 | -2,213 🟥 | 45.2% | 42.3% | -2.9 🟥 pp |
| Madhu `LK-4209` | Mannar | 0.3% | 2,997 | 3,319 | +322 🟩 | 38.9% | 35.0% | -3.9 🟥 pp |
| Mannar Town `LK-4203` | Mannar | 2.5% | 27,970 | 29,246 | +1,276 🟩 | 54.8% | 50.6% | -4.1 🟥 pp |
| Vengalacheddikulam `LK-4312` | Vavuniya | 0.2% | 4,564 | 2,821 | -1,743 🟥 | 15.3% | 10.9% | -4.3 🟥 pp |
| Musali `LK-4215` | Mannar | 0.3% | 2,750 | 4,011 | +1,261 🟩 | 33.9% | 22.1% | -11.8 🟥 pp |

***Delft** gained the most share at **+6.6pp**. **Musali** saw the steepest share decline at **-11.8pp**. **Katana** had the largest absolute increase (**+6,528**).*

### Other Christian

| DSD | District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Koralai Pattu Central `LK-5104` | Batticaloa | 1.4% | 12 | 3,459 | +3,447 🟩 | 0.0% | 12.0% | +12.0 🟩 pp |
| Koralai Pattu South `LK-5110` | Batticaloa | 0.9% | 1,471 | 2,244 | +773 🟩 | 5.6% | 7.9% | +2.3 🟩 pp |
| Thunukkai `LK-4403` | Mullaitivu | 0.2% | 382 | 584 | +202 🟩 | 3.9% | 5.6% | +1.7 🟩 pp |
| Pachchilaipalli `LK-4503` | Kilinochchi | 0.2% | 162 | 461 | +299 🟩 | 1.9% | 3.5% | +1.6 🟩 pp |
| Islands North (Kayts) `LK-4103` | Jaffna | 0.2% | 387 | 543 | +156 🟩 | 3.9% | 5.5% | +1.5 🟩 pp |
| Vavuniya South `LK-4306` | Vavuniya | 0.1% | 45 | 265 | +220 🟩 | 0.3% | 1.8% | +1.4 🟩 pp |
| Koralai Pattu North `LK-5103` | Batticaloa | 1.3% | 2,597 | 3,432 | +835 🟩 | 12.1% | 13.5% | +1.4 🟩 pp |
| Oddusuddan `LK-4412` | Mullaitivu | 0.5% | 877 | 1,267 | +390 🟩 | 5.6% | 7.0% | +1.4 🟩 pp |
| Maritimepattu `LK-4415` | Mullaitivu | 0.6% | 838 | 1,510 | +672 🟩 | 2.9% | 4.1% | +1.2 🟩 pp |
| Puthukkudiyiruppu `LK-4409` | Mullaitivu | 1.0% | 1,239 | 2,530 | +1,291 🟩 | 5.2% | 6.4% | +1.2 🟩 pp |
| Valikamam North (Thllippalai) `LK-4112` | Jaffna | 0.7% | 869 | 1,857 | +988 🟩 | 2.9% | 4.1% | +1.2 🟩 pp |
| Karachchi `LK-4509` | Kilinochchi | 2.4% | 4,413 | 6,139 | +1,726 🟩 | 7.2% | 8.2% | +1.0 🟩 pp |
| Seruvila `LK-5330` | Trincomalee | 0.1% | 66 | 221 | +155 🟩 | 0.5% | 1.4% | +0.9 🟩 pp |
| Kandavalai `LK-4506` | Kilinochchi | 0.5% | 1,060 | 1,362 | +302 🟩 | 4.6% | 5.5% | +0.9 🟩 pp |
| Manthai West `LK-4206` | Mannar | 0.3% | 485 | 756 | +271 🟩 | 3.3% | 4.0% | +0.8 🟩 pp |
| Manthai East `LK-4406` | Mullaitivu | 0.2% | 316 | 397 | +81 🟩 | 4.4% | 5.2% | +0.7 🟩 pp |
| Manmunai North `LK-5118` | Batticaloa | 3.7% | 7,937 | 9,459 | +1,522 🟩 | 9.2% | 9.9% | +0.7 🟩 pp |
| Alayadivembu `LK-5239` | Ampara | 0.5% | 1,015 | 1,289 | +274 🟩 | 4.5% | 5.2% | +0.7 🟩 pp |
| Poonakary `LK-4512` | Kilinochchi | 0.4% | 801 | 1,112 | +311 🟩 | 3.9% | 4.6% | +0.7 🟩 pp |
| Pitabaddara `LK-3203` | Matara | 0.2% | 400 | 604 | +204 🟩 | 0.8% | 1.2% | +0.5 🟩 pp |
| Mihinthale `LK-7130` | Anuradhapura | 0.1% | 130 | 341 | +211 🟩 | 0.4% | 0.8% | +0.4 🟩 pp |
| Pasgoda `LK-3209` | Matara | 0.2% | 239 | 478 | +239 🟩 | 0.4% | 0.8% | +0.4 🟩 pp |
| Seethawaka `LK-1115` | Colombo | 1.0% | 1,993 | 2,592 | +599 🟩 | 1.8% | 2.1% | +0.4 🟩 pp |
| Thambalagamuwa `LK-5318` | Trincomalee | 0.3% | 520 | 734 | +214 🟩 | 1.8% | 2.2% | +0.4 🟩 pp |
| Ipalogama `LK-7160` | Anuradhapura | 0.1% | 79 | 235 | +156 🟩 | 0.2% | 0.6% | +0.4 🟩 pp |
| Valikamam West (Chankanai) `LK-4106` | Jaffna | 0.8% | 1,960 | 2,066 | +106 🟩 | 4.2% | 4.6% | +0.4 🟩 pp |
| Godakawela `LK-9142` | Ratnapura | 0.4% | 815 | 1,085 | +270 🟩 | 1.1% | 1.4% | +0.3 🟩 pp |
| Sammanthurai `LK-5218` | Ampara | 0.3% | 386 | 689 | +303 🟩 | 0.6% | 0.9% | +0.3 🟩 pp |
| Lunugala `LK-8119` | Badulla | 0.2% | 374 | 459 | +85 🟩 | 1.2% | 1.4% | +0.2 🟩 pp |
| Colombo `LK-1103` | Colombo | 4.1% | 10,715 | 10,381 | -334 🟥 | 3.3% | 3.6% | +0.2 🟩 pp |
| Kuliyapitiya West `LK-6172` | Kurunegala | 0.3% | 663 | 891 | +228 🟩 | 0.9% | 1.1% | +0.2 🟩 pp |
| Madhu `LK-4209` | Mannar | 0.1% | 178 | 239 | +61 🟩 | 2.3% | 2.5% | +0.2 🟩 pp |
| Vavuniya `LK-4309` | Vavuniya | 2.9% | 7,102 | 7,307 | +205 🟩 | 6.0% | 6.2% | +0.2 🟩 pp |
| Vadamaradchi North (Point Pedro) `LK-4127` | Jaffna | 0.4% | 1,016 | 1,013 | -3 🟥 | 2.1% | 2.3% | +0.2 🟩 pp |
| Tirukkovil `LK-5245` | Ampara | 0.4% | 792 | 973 | +181 🟩 | 3.1% | 3.3% | +0.2 🟩 pp |
| Maspotha `LK-6151` | Kurunegala | 0.2% | 262 | 401 | +139 🟩 | 0.8% | 1.0% | +0.2 🟩 pp |
| Akuressa `LK-3218` | Matara | 0.1% | 160 | 259 | +99 🟩 | 0.3% | 0.5% | +0.2 🟩 pp |
| Vanathavilluwa `LK-6206` | Puttalam | 0.2% | 370 | 454 | +84 🟩 | 2.1% | 2.3% | +0.2 🟩 pp |
| Muthur `LK-5327` | Trincomalee | 0.5% | 925 | 1,283 | +358 🟩 | 1.6% | 1.8% | +0.2 🟩 pp |
| Vengalacheddikulam `LK-4312` | Vavuniya | 0.4% | 1,056 | 949 | -107 🟥 | 3.5% | 3.7% | +0.1 🟩 pp |
| Hambantota `LK-3312` | Hambantota | 0.2% | 253 | 396 | +143 🟩 | 0.4% | 0.6% | +0.1 🟩 pp |
| Rajanganaya `LK-7142` | Anuradhapura | 0.1% | 79 | 137 | +58 🟩 | 0.2% | 0.4% | +0.1 🟩 pp |
| Kolonna `LK-9151` | Ratnapura | 0.1% | 284 | 379 | +95 🟩 | 0.6% | 0.8% | +0.1 🟩 pp |
| Nagoda `LK-3124` | Galle | 0.3% | 754 | 796 | +42 🟩 | 1.4% | 1.5% | +0.1 🟩 pp |
| Deltota `LK-2148` | Kandy | 0.2% | 328 | 383 | +55 🟩 | 1.1% | 1.2% | +0.1 🟩 pp |
| Porativu Pattu `LK-5133` | Batticaloa | 0.2% | 450 | 526 | +76 🟩 | 1.2% | 1.4% | +0.1 🟩 pp |
| Deraniyagala `LK-9233` | Kegalle | 0.1% | 240 | 280 | +40 🟩 | 0.5% | 0.6% | +0.1 🟩 pp |
| Pathahewaheta `LK-2145` | Kandy | 0.2% | 460 | 543 | +83 🟩 | 0.8% | 0.9% | +0.1 🟩 pp |
| Rasnayakapura `LK-6118` | Kurunegala | 0.0% | 59 | 91 | +32 🟩 | 0.3% | 0.4% | +0.1 🟩 pp |
| Welioya `LK-4418` | Mullaitivu | 0.0% | 12 | 27 | +15 🟩 | 0.2% | 0.3% | +0.1 🟩 pp |
| Bope-Poddala `LK-3142` | Galle | 0.1% | 257 | 344 | +87 🟩 | 0.5% | 0.6% | +0.1 🟩 pp |
| Wariyapola `LK-6136` | Kurunegala | 0.1% | 115 | 172 | +57 🟩 | 0.2% | 0.3% | +0.1 🟩 pp |
| Wennappuwa `LK-6245` | Puttalam | 0.6% | 1,492 | 1,465 | -27 🟥 | 2.2% | 2.3% | +0.1 🟩 pp |
| Pathadumbara `LK-2112` | Kandy | 0.2% | 339 | 419 | +80 🟩 | 0.4% | 0.4% | +0.1 🟩 pp |
| Neluwa `LK-3121` | Galle | 0.1% | 332 | 338 | +6 🟩 | 1.2% | 1.2% | +0.1 🟩 pp |
| Weligama `LK-3239` | Matara | 0.1% | 115 | 165 | +50 🟩 | 0.2% | 0.2% | +0.1 🟩 pp |
| Horana `LK-1309` | Kalutara | 0.4% | 788 | 1,007 | +219 🟩 | 0.7% | 0.8% | +0.1 🟩 pp |
| Gonapinuwala `LK-3134` | Galle | 0.1% | 111 | 132 | +21 🟩 | 0.5% | 0.6% | +0.1 🟩 pp |
| Akmeemana `LK-3145` | Galle | 0.2% | 362 | 449 | +87 🟩 | 0.5% | 0.5% | +0.1 🟩 pp |
| Aranayake `LK-9209` | Kegalle | 0.1% | 137 | 176 | +39 🟩 | 0.2% | 0.3% | +0.1 🟩 pp |
| Dodangoda `LK-1327` | Kalutara | 0.2% | 558 | 620 | +62 🟩 | 0.9% | 0.9% | +0.1 🟩 pp |
| Kalpitiya `LK-6203` | Puttalam | 0.4% | 800 | 948 | +148 🟩 | 0.9% | 1.0% | +0.1 🟩 pp |
| Karandeniya `LK-3109` | Galle | 0.1% | 268 | 300 | +32 🟩 | 0.4% | 0.5% | 0.0 pp |
| Galewela `LK-2203` | Matale | 0.1% | 205 | 259 | +54 🟩 | 0.3% | 0.3% | 0.0 pp |
| Bentota `LK-3103` | Galle | 0.0% | 52 | 69 | +17 🟩 | 0.1% | 0.1% | 0.0 pp |
| Madurawala `LK-1315` | Kalutara | 0.1% | 152 | 175 | +23 🟩 | 0.4% | 0.5% | 0.0 pp |
| Ambalangoda `LK-3133` | Galle | 0.1% | 162 | 190 | +28 🟩 | 0.3% | 0.3% | 0.0 pp |
| Welipitiya `LK-3221` | Matara | 0.0% | 91 | 115 | +24 🟩 | 0.2% | 0.2% | 0.0 pp |
| Mulatiyana `LK-3212` | Matara | 0.0% | 6 | 22 | +16 🟩 | 0.0% | 0.0% | 0.0 pp |
| Athuraliya `LK-3215` | Matara | 0.1% | 153 | 165 | +12 🟩 | 0.5% | 0.5% | 0.0 pp |
| Minipe `LK-2121` | Kandy | 0.0% | 67 | 86 | +19 🟩 | 0.1% | 0.2% | 0.0 pp |
| Polgahawela `LK-6187` | Kurunegala | 0.2% | 475 | 509 | +34 🟩 | 0.7% | 0.8% | 0.0 pp |
| Dikwella `LK-3248` | Matara | 0.0% | 55 | 71 | +16 🟩 | 0.1% | 0.1% | 0.0 pp |
| Damana `LK-5242` | Ampara | 0.0% | 71 | 83 | +12 🟩 | 0.2% | 0.2% | 0.0 pp |
| Malimbada `LK-3224` | Matara | 0.0% | 56 | 66 | +10 🟩 | 0.2% | 0.2% | 0.0 pp |
| Delft `LK-4142` | Jaffna | 0.1% | 268 | 222 | -46 🟥 | 7.0% | 7.0% | 0.0 pp |
| Gomarankadawala `LK-5309` | Trincomalee | 0.0% | 2 | 4 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Padukka `LK-1118` | Colombo | 0.2% | 540 | 618 | +78 🟩 | 0.8% | 0.8% | 0.0 pp |
| Kobeigane `LK-6139` | Kurunegala | 0.0% | 95 | 114 | +19 🟩 | 0.3% | 0.3% | 0.0 pp |
| Ibbagamuwa `LK-6130` | Kurunegala | 0.1% | 233 | 273 | +40 🟩 | 0.3% | 0.3% | 0.0 pp |
| Manmunai Pattu `LK-5127` | Batticaloa | 0.3% | 640 | 767 | +127 🟩 | 2.1% | 2.1% | 0.0 pp |
| Kirinda Puhulwella `LK-3233` | Matara | 0.0% | 4 | 7 | +3 🟩 | 0.0% | 0.0% | 0.0 pp |
| Kattankudy `LK-5124` | Batticaloa | 0.0% | 0 | 6 | +6 🟩 | 0.0% | 0.0% | 0.0 pp |
| Galgamuwa `LK-6106` | Kurunegala | 0.2% | 359 | 410 | +51 🟩 | 0.7% | 0.7% | 0.0 pp |
| Kaburupitiya `LK-3227` | Matara | 0.0% | 46 | 53 | +7 🟩 | 0.1% | 0.1% | 0.0 pp |
| Kebithigollewa `LK-7106` | Anuradhapura | 0.0% | 22 | 29 | +7 🟩 | 0.1% | 0.1% | 0.0 pp |
| Kotawehera `LK-6115` | Kurunegala | 0.0% | 11 | 14 | +3 🟩 | 0.1% | 0.1% | 0.0 pp |
| Kinniya `LK-5324` | Trincomalee | 0.0% | 2 | 7 | +5 🟩 | 0.0% | 0.0% | 0.0 pp |
| Bamunakotuwa `LK-6149` | Kurunegala | 0.0% | 61 | 68 | +7 🟩 | 0.2% | 0.2% | 0.0 pp |
| Siyambalanduwa `LK-8212` | Monaragala | 0.0% | 46 | 56 | +10 🟩 | 0.1% | 0.1% | 0.0 pp |
| Navithanveli `LK-5216` | Ampara | 0.1% | 185 | 216 | +31 🟩 | 1.0% | 1.0% | 0.0 pp |
| Sainthamaruthu `LK-5225` | Ampara | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Thambuththegama `LK-7145` | Anuradhapura | 0.4% | 992 | 1,100 | +108 🟩 | 2.3% | 2.3% | 0.0 pp |
| Beliatta `LK-3330` | Hambantota | 0.0% | 59 | 60 | +1 🟩 | 0.1% | 0.1% | 0.0 pp |
| Hakmana `LK-3230` | Matara | 0.0% | 19 | 18 | -1 🟥 | 0.1% | 0.1% | 0.0 pp |
| Padavi Sri Pura `LK-5303` | Trincomalee | 0.0% | 104 | 105 | +1 🟩 | 0.9% | 0.9% | 0.0 pp |
| Akkaraipattu `LK-5236` | Ampara | 0.0% | 6 | 4 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Habaraduwa `LK-3154` | Galle | 0.1% | 232 | 231 | -1 🟥 | 0.4% | 0.4% | 0.0 pp |
| Medadumbara `LK-2124` | Kandy | 0.2% | 470 | 492 | +22 🟩 | 0.8% | 0.8% | 0.0 pp |
| Laggala `LK-2224` | Matale | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Elapatha `LK-9127` | Ratnapura | 0.0% | 63 | 60 | -3 🟥 | 0.2% | 0.2% | 0.0 pp |
| Panduwasnuwara East `LK-6148` | Kurunegala | 0.0% | 42 | 41 | -1 🟥 | 0.1% | 0.1% | 0.0 pp |
| Niyagama `LK-3115` | Galle | 0.0% | 59 | 55 | -4 🟥 | 0.2% | 0.2% | 0.0 pp |
| Angunakolapelessa `LK-3318` | Hambantota | 0.0% | 29 | 25 | -4 🟥 | 0.1% | 0.0% | 0.0 pp |
| Jaffna `LK-4136` | Jaffna | 1.1% | 2,884 | 2,766 | -118 🟥 | 5.7% | 5.7% | 0.0 pp |
| Soranathota `LK-8115` | Badulla | 0.0% | 91 | 95 | +4 🟩 | 0.4% | 0.4% | 0.0 pp |
| Katuwana `LK-3324` | Hambantota | 0.0% | 12 | 6 | -6 🟥 | 0.0% | 0.0% | 0.0 pp |
| Millaniya `LK-1318` | Kalutara | 0.1% | 268 | 280 | +12 🟩 | 0.5% | 0.5% | 0.0 pp |
| Vavuniya North `LK-4303` | Vavuniya | 0.1% | 295 | 374 | +79 🟩 | 2.6% | 2.5% | 0.0 pp |
| Kiriella `LK-9109` | Ratnapura | 0.0% | 79 | 68 | -11 🟥 | 0.2% | 0.2% | 0.0 pp |
| Naula `LK-2209` | Matale | 0.0% | 83 | 77 | -6 🟥 | 0.3% | 0.3% | 0.0 pp |
| Divulapitiya `LK-1209` | Gampaha | 0.6% | 1,417 | 1,508 | +91 🟩 | 1.0% | 1.0% | 0.0 pp |
| Mahakumbukkadawala `LK-6221` | Puttalam | 0.1% | 141 | 161 | +20 🟩 | 0.8% | 0.7% | 0.0 pp |
| Warakapola `LK-9218` | Kegalle | 0.1% | 320 | 309 | -11 🟥 | 0.3% | 0.3% | 0.0 pp |
| Dambulla `LK-2206` | Matale | 0.1% | 164 | 167 | +3 🟩 | 0.2% | 0.2% | 0.0 pp |
| Koralai Pattu West `LK-5106` | Batticaloa | 0.0% | 5 | 0 | -5 🟥 | 0.0% | 0.0% | 0.0 pp |
| Walasmulla `LK-3325` | Hambantota | 0.0% | 20 | 11 | -9 🟥 | 0.0% | 0.0% | 0.0 pp |
| Bandarawela `LK-8133` | Badulla | 0.3% | 891 | 874 | -17 🟥 | 1.4% | 1.3% | 0.0 pp |
| Wilgamuwa `LK-2227` | Matale | 0.0% | 17 | 10 | -7 🟥 | 0.1% | 0.0% | 0.0 pp |
| Embilipitiya `LK-9148` | Ratnapura | 0.1% | 203 | 196 | -7 🟥 | 0.2% | 0.1% | 0.0 pp |
| Monaragala `LK-8215` | Monaragala | 0.1% | 155 | 161 | +6 🟩 | 0.3% | 0.3% | 0.0 pp |
| Nintavur `LK-5230` | Ampara | 0.0% | 21 | 15 | -6 🟥 | 0.1% | 0.0% | 0.0 pp |
| Thanamalwila `LK-8230` | Monaragala | 0.0% | 57 | 57 | +0 | 0.2% | 0.2% | 0.0 pp |
| Padaviya `LK-7103` | Anuradhapura | 0.0% | 41 | 36 | -5 🟥 | 0.2% | 0.1% | 0.0 pp |
| Okewela `LK-3327` | Hambantota | 0.0% | 6 | 0 | -6 🟥 | 0.0% | 0.0% | 0.0 pp |
| Thirappane `LK-7151` | Anuradhapura | 0.0% | 54 | 52 | -2 🟥 | 0.2% | 0.2% | 0.0 pp |
| Rambewa `LK-7118` | Anuradhapura | 0.0% | 25 | 14 | -11 🟥 | 0.1% | 0.0% | 0.0 pp |
| Medawachchiya `LK-7109` | Anuradhapura | 0.0% | 76 | 67 | -9 🟥 | 0.2% | 0.1% | 0.0 pp |
| Hatharaliyadda `LK-2134` | Kandy | 0.0% | 24 | 14 | -10 🟥 | 0.1% | 0.0% | 0.0 pp |
| Imaduwa `LK-3151` | Galle | 0.0% | 85 | 74 | -11 🟥 | 0.2% | 0.2% | 0.0 pp |
| Badulla `LK-8121` | Badulla | 0.3% | 834 | 892 | +58 🟩 | 1.1% | 1.1% | 0.0 pp |
| Nikaweratiya `LK-6121` | Kurunegala | 0.1% | 144 | 138 | -6 🟥 | 0.4% | 0.3% | 0.0 pp |
| Mirigama `LK-1212` | Gampaha | 0.2% | 534 | 505 | -29 🟥 | 0.3% | 0.3% | 0.0 pp |
| Udubaddawa `LK-6175` | Kurunegala | 0.2% | 447 | 445 | -2 🟥 | 0.9% | 0.8% | 0.0 pp |
| Pelmadulla `LK-9124` | Ratnapura | 0.2% | 482 | 469 | -13 🟥 | 0.5% | 0.5% | 0.0 pp |
| Thamankaduwa `LK-7215` | Polonnaruwa | 0.1% | 374 | 381 | +7 🟩 | 0.5% | 0.4% | 0.0 pp |
| Mannar Town `LK-4203` | Mannar | 1.2% | 2,787 | 3,129 | +342 🟩 | 5.5% | 5.4% | 0.0 pp |
| Wellawaya `LK-8221` | Monaragala | 0.1% | 184 | 195 | +11 🟩 | 0.3% | 0.3% | 0.0 pp |
| Sevanagala `LK-8233` | Monaragala | 0.0% | 39 | 26 | -13 🟥 | 0.1% | 0.1% | 0.0 pp |
| Ruwanwella `LK-9221` | Kegalle | 0.1% | 373 | 356 | -17 🟥 | 0.6% | 0.5% | 0.0 pp |
| Bibile `LK-8203` | Monaragala | 0.0% | 61 | 51 | -10 🟥 | 0.2% | 0.1% | 0.0 pp |
| Mahara `LK-1233` | Gampaha | 1.0% | 2,459 | 2,538 | +79 🟩 | 1.2% | 1.1% | 0.0 pp |
| Matara Four Gravets `LK-3242` | Matara | 0.1% | 341 | 307 | -34 🟥 | 0.3% | 0.2% | 0.0 pp |
| Elahera `LK-7218` | Polonnaruwa | 0.0% | 35 | 16 | -19 🟥 | 0.1% | 0.0% | 0.0 pp |
| Rideemaliyadda `LK-8106` | Badulla | 0.0% | 53 | 34 | -19 🟥 | 0.1% | 0.1% | 0.0 pp |
| Thihagoda `LK-3236` | Matara | 0.0% | 48 | 33 | -15 🟥 | 0.1% | 0.1% | 0.0 pp |
| Dehiattakandiya `LK-5203` | Ampara | 0.0% | 117 | 99 | -18 🟥 | 0.2% | 0.1% | 0.0 pp |
| Panduwasnuwara West `LK-6145` | Kurunegala | 0.1% | 192 | 173 | -19 🟥 | 0.3% | 0.2% | 0.0 pp |
| Lankapura `LK-7209` | Polonnaruwa | 0.0% | 26 | 9 | -17 🟥 | 0.1% | 0.0% | 0.0 pp |
| Weerabugedara `LK-6166` | Kurunegala | 0.1% | 181 | 175 | -6 🟥 | 0.5% | 0.5% | 0.0 pp |
| Ehetuwewa `LK-6109` | Kurunegala | 0.0% | 29 | 18 | -11 🟥 | 0.1% | 0.1% | 0.0 pp |
| Buttala `LK-8224` | Monaragala | 0.0% | 71 | 51 | -20 🟥 | 0.1% | 0.1% | 0.0 pp |
| Polpitigama `LK-6127` | Kurunegala | 0.1% | 200 | 183 | -17 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Padiyathalawa `LK-5206` | Ampara | 0.0% | 20 | 12 | -8 🟥 | 0.1% | 0.1% | -0.1 🟥 pp |
| Medirigiriya `LK-7206` | Polonnaruwa | 0.0% | 102 | 75 | -27 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Alawwa `LK-6184` | Kurunegala | 0.1% | 197 | 168 | -29 🟥 | 0.3% | 0.3% | -0.1 🟥 pp |
| Uhana `LK-5212` | Ampara | 0.0% | 124 | 98 | -26 🟥 | 0.2% | 0.2% | -0.1 🟥 pp |
| Akurana `LK-2109` | Kandy | 0.0% | 78 | 48 | -30 🟥 | 0.1% | 0.1% | -0.1 🟥 pp |
| Narammala `LK-6181` | Kurunegala | 0.1% | 155 | 131 | -24 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Kahatagasdigiliya `LK-7121` | Anuradhapura | 0.0% | 109 | 96 | -13 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Horowpathana `LK-7124` | Anuradhapura | 0.0% | 65 | 49 | -16 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Balapitiya `LK-3106` | Galle | 0.0% | 94 | 56 | -38 🟥 | 0.1% | 0.1% | -0.1 🟥 pp |
| Dimbulagala `LK-7212` | Polonnaruwa | 0.1% | 248 | 216 | -32 🟥 | 0.3% | 0.3% | -0.1 🟥 pp |
| Bandaragama `LK-1306` | Kalutara | 0.4% | 869 | 913 | +44 🟩 | 0.8% | 0.7% | -0.1 🟥 pp |
| Bulathkohipitiya `LK-9224` | Kegalle | 0.1% | 299 | 260 | -39 🟥 | 0.6% | 0.6% | -0.1 🟥 pp |
| Ganewatta `LK-6133` | Kurunegala | 0.0% | 134 | 118 | -16 🟥 | 0.3% | 0.3% | -0.1 🟥 pp |
| Kandeketiya `LK-8112` | Badulla | 0.0% | 59 | 52 | -7 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Pannala `LK-6178` | Kurunegala | 0.4% | 900 | 899 | -1 🟥 | 0.7% | 0.7% | -0.1 🟥 pp |
| Beruwala `LK-1324` | Kalutara | 0.2% | 552 | 486 | -66 🟥 | 0.3% | 0.3% | -0.1 🟥 pp |
| Galle 4 Gravets `LK-3139` | Galle | 0.1% | 402 | 355 | -47 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Galnewa `LK-7163` | Anuradhapura | 0.0% | 48 | 27 | -21 🟥 | 0.1% | 0.1% | -0.1 🟥 pp |
| Sooriyawewa `LK-3303` | Hambantota | 0.0% | 80 | 61 | -19 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Valikamam South West (Sandilipay) `LK-4109` | Jaffna | 0.8% | 2,182 | 2,139 | -43 🟥 | 4.2% | 4.1% | -0.1 🟥 pp |
| Higurakgoda `LK-7203` | Polonnaruwa | 0.1% | 298 | 277 | -21 🟥 | 0.5% | 0.4% | -0.1 🟥 pp |
| Badalkumbura `LK-8218` | Monaragala | 0.0% | 47 | 21 | -26 🟥 | 0.1% | 0.0% | -0.1 🟥 pp |
| Ukuwela `LK-2233` | Matale | 0.1% | 367 | 336 | -31 🟥 | 0.5% | 0.5% | -0.1 🟥 pp |
| Dehiowita `LK-9230` | Kegalle | 0.2% | 670 | 636 | -34 🟥 | 0.8% | 0.7% | -0.1 🟥 pp |
| Mahawilachchiya `LK-7112` | Anuradhapura | 0.0% | 95 | 84 | -11 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Weligepola `LK-9145` | Ratnapura | 0.0% | 30 | 7 | -23 🟥 | 0.1% | 0.0% | -0.1 🟥 pp |
| Welimada `LK-8130` | Badulla | 0.2% | 545 | 489 | -56 🟥 | 0.5% | 0.5% | -0.1 🟥 pp |
| Galenbidunuwewa `LK-7127` | Anuradhapura | 0.0% | 65 | 31 | -34 🟥 | 0.1% | 0.1% | -0.1 🟥 pp |
| Elpitiya `LK-3112` | Galle | 0.1% | 286 | 240 | -46 🟥 | 0.4% | 0.4% | -0.1 🟥 pp |
| Matugama `LK-1330` | Kalutara | 0.2% | 503 | 462 | -41 🟥 | 0.6% | 0.5% | -0.1 🟥 pp |
| Palagala `LK-7166` | Anuradhapura | 0.0% | 38 | 11 | -27 🟥 | 0.1% | 0.0% | -0.1 🟥 pp |
| Ududumbara `LK-2118` | Kandy | 0.0% | 55 | 37 | -18 🟥 | 0.2% | 0.2% | -0.1 🟥 pp |
| Mawanella `LK-9206` | Kegalle | 0.0% | 205 | 125 | -80 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Kelaniya `LK-1236` | Gampaha | 0.8% | 2,331 | 2,155 | -176 🟥 | 1.7% | 1.6% | -0.1 🟥 pp |
| Devinuwara `LK-3245` | Matara | 0.0% | 120 | 80 | -40 🟥 | 0.2% | 0.2% | -0.1 🟥 pp |
| Udunuwara `LK-2139` | Kandy | 0.2% | 460 | 396 | -64 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Harispattuwa `LK-2133` | Kandy | 0.1% | 399 | 339 | -60 🟥 | 0.5% | 0.4% | -0.1 🟥 pp |
| Attanagalla `LK-1227` | Gampaha | 0.2% | 677 | 561 | -116 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Udapalatha `LK-2151` | Kandy | 0.4% | 953 | 975 | +22 🟩 | 1.0% | 0.9% | -0.1 🟥 pp |
| Gampaha `LK-1224` | Gampaha | 0.8% | 2,137 | 2,028 | -109 🟥 | 1.1% | 1.0% | -0.1 🟥 pp |
| Tangalle `LK-3333` | Hambantota | 0.1% | 292 | 243 | -49 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Nattandiya `LK-6242` | Puttalam | 0.4% | 1,012 | 1,003 | -9 🟥 | 1.6% | 1.5% | -0.1 🟥 pp |
| Ja Ela `LK-1221` | Gampaha | 3.0% | 7,746 | 7,671 | -75 🟥 | 3.8% | 3.7% | -0.1 🟥 pp |
| Minuwangoda `LK-1215` | Gampaha | 0.8% | 2,084 | 2,126 | +42 🟩 | 1.2% | 1.1% | -0.1 🟥 pp |
| Weeraketiya `LK-3321` | Hambantota | 0.0% | 51 | 11 | -40 🟥 | 0.1% | 0.0% | -0.1 🟥 pp |
| Dompe `LK-1230` | Gampaha | 0.3% | 776 | 682 | -94 🟥 | 0.5% | 0.4% | -0.1 🟥 pp |
| Kantale `LK-5321` | Trincomalee | 0.1% | 173 | 135 | -38 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Nochchiyagama `LK-7139` | Anuradhapura | 0.0% | 114 | 68 | -46 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Madulla `LK-8206` | Monaragala | 0.0% | 64 | 36 | -28 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Pallepola `LK-2212` | Matale | 0.0% | 57 | 27 | -30 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Manmunai South West `LK-5130` | Batticaloa | 0.1% | 182 | 166 | -16 🟥 | 0.7% | 0.6% | -0.1 🟥 pp |
| Kalutara `LK-1321` | Kalutara | 0.3% | 988 | 841 | -147 🟥 | 0.6% | 0.5% | -0.1 🟥 pp |
| Ambalantota `LK-3315` | Hambantota | 0.1% | 249 | 183 | -66 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Negombo `LK-1203` | Gampaha | 1.7% | 4,755 | 4,455 | -300 🟥 | 3.3% | 3.2% | -0.1 🟥 pp |
| Galigamuwa `LK-9215` | Kegalle | 0.1% | 290 | 201 | -89 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Nawagattegama `LK-6212` | Puttalam | 0.0% | 45 | 34 | -11 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Anamaduwa `LK-6224` | Puttalam | 0.1% | 212 | 189 | -23 🟥 | 0.6% | 0.4% | -0.1 🟥 pp |
| Manmunai West `LK-5121` | Batticaloa | 0.1% | 337 | 349 | +12 🟩 | 1.2% | 1.1% | -0.1 🟥 pp |
| Medagama `LK-8209` | Monaragala | 0.0% | 52 | 11 | -41 🟥 | 0.1% | 0.0% | -0.1 🟥 pp |
| Nuwaragam Palatha East `LK-7133` | Anuradhapura | 0.1% | 371 | 313 | -58 🟥 | 0.5% | 0.4% | -0.1 🟥 pp |
| Tumpane `LK-2103` | Kandy | 0.0% | 148 | 104 | -44 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Maho `LK-6124` | Kurunegala | 0.0% | 150 | 86 | -64 🟥 | 0.3% | 0.1% | -0.1 🟥 pp |
| Ambanpola `LK-6112` | Kurunegala | 0.0% | 58 | 32 | -26 🟥 | 0.3% | 0.1% | -0.1 🟥 pp |
| Haldummulla `LK-8142` | Badulla | 0.2% | 515 | 482 | -33 🟥 | 1.4% | 1.2% | -0.1 🟥 pp |
| Thenmaradchi (Chavakachcheri) `LK-4130` | Jaffna | 0.8% | 2,106 | 2,119 | +13 🟩 | 3.3% | 3.1% | -0.1 🟥 pp |
| Kegalle `LK-9212` | Kegalle | 0.2% | 641 | 543 | -98 🟥 | 0.7% | 0.6% | -0.1 🟥 pp |
| Matale `LK-2218` | Matale | 0.3% | 724 | 671 | -53 🟥 | 1.0% | 0.8% | -0.1 🟥 pp |
| Mahaoya `LK-5209` | Ampara | 0.0% | 47 | 22 | -25 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Poojapitiya `LK-2106` | Kandy | 0.1% | 254 | 183 | -71 🟥 | 0.4% | 0.3% | -0.1 🟥 pp |
| Nachchaduwa `LK-7136` | Anuradhapura | 0.0% | 84 | 55 | -29 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Kekirawa `LK-7154` | Anuradhapura | 0.1% | 326 | 270 | -56 🟥 | 0.6% | 0.4% | -0.1 🟥 pp |
| Valikamam East (Kopay) `LK-4118` | Jaffna | 0.9% | 2,278 | 2,257 | -21 🟥 | 3.1% | 3.0% | -0.1 🟥 pp |
| Biyagama `LK-1239` | Gampaha | 0.8% | 2,035 | 1,965 | -70 🟥 | 1.1% | 0.9% | -0.1 🟥 pp |
| Rideegama `LK-6163` | Kurunegala | 0.0% | 240 | 122 | -118 🟥 | 0.3% | 0.1% | -0.1 🟥 pp |
| Walallawita `LK-1339` | Kalutara | 0.0% | 141 | 63 | -78 🟥 | 0.3% | 0.1% | -0.1 🟥 pp |
| Vadamaradchchi East `LK-4124` | Jaffna | 0.1% | 243 | 238 | -5 🟥 | 1.9% | 1.8% | -0.1 🟥 pp |
| Mahiyanganaya `LK-8103` | Badulla | 0.1% | 230 | 133 | -97 🟥 | 0.3% | 0.1% | -0.2 🟥 pp |
| Meegahakiula `LK-8109` | Badulla | 0.0% | 54 | 27 | -27 🟥 | 0.3% | 0.1% | -0.2 🟥 pp |
| Palindanuwara `LK-1336` | Kalutara | 0.1% | 364 | 286 | -78 🟥 | 0.7% | 0.6% | -0.2 🟥 pp |
| Ganga Ihala Korale `LK-2154` | Kandy | 0.1% | 383 | 315 | -68 🟥 | 0.7% | 0.5% | -0.2 🟥 pp |
| Uvaparanagama `LK-8127` | Badulla | 0.1% | 301 | 180 | -121 🟥 | 0.4% | 0.2% | -0.2 🟥 pp |
| Yatawatta `LK-2215` | Matale | 0.0% | 115 | 69 | -46 🟥 | 0.4% | 0.2% | -0.2 🟥 pp |
| Lahugala `LK-5251` | Ampara | 0.0% | 27 | 14 | -13 🟥 | 0.3% | 0.1% | -0.2 🟥 pp |
| Kalawana `LK-9133` | Ratnapura | 0.2% | 493 | 402 | -91 🟥 | 1.0% | 0.8% | -0.2 🟥 pp |
| Karuwalagaswewa `LK-6209` | Puttalam | 0.1% | 194 | 171 | -23 🟥 | 0.8% | 0.7% | -0.2 🟥 pp |
| Ratnapura `LK-9112` | Ratnapura | 0.4% | 1,203 | 998 | -205 🟥 | 1.0% | 0.8% | -0.2 🟥 pp |
| Islands South (Velanai) `LK-4139` | Jaffna | 0.1% | 262 | 230 | -32 🟥 | 1.6% | 1.4% | -0.2 🟥 pp |
| Karaitivu `LK-5227` | Ampara | 0.1% | 165 | 156 | -9 🟥 | 1.0% | 0.8% | -0.2 🟥 pp |
| Welivitiya-Divitura `LK-3130` | Galle | 0.1% | 267 | 213 | -54 🟥 | 0.9% | 0.7% | -0.2 🟥 pp |
| Ampara `LK-5215` | Ampara | 0.1% | 237 | 170 | -67 🟥 | 0.5% | 0.4% | -0.2 🟥 pp |
| Kuliyapitiya East `LK-6169` | Kurunegala | 0.0% | 161 | 68 | -93 🟥 | 0.3% | 0.1% | -0.2 🟥 pp |
| Pallama `LK-6227` | Puttalam | 0.1% | 262 | 247 | -15 🟥 | 1.1% | 0.9% | -0.2 🟥 pp |
| Hali-Ela `LK-8124` | Badulla | 0.3% | 798 | 652 | -146 🟥 | 0.9% | 0.7% | -0.2 🟥 pp |
| Katharagama `LK-8227` | Monaragala | 0.0% | 83 | 48 | -35 🟥 | 0.5% | 0.3% | -0.2 🟥 pp |
| Palugaswewa `LK-7157` | Anuradhapura | 0.0% | 76 | 53 | -23 🟥 | 0.5% | 0.3% | -0.2 🟥 pp |
| Kundasale `LK-2127` | Kandy | 0.6% | 1,698 | 1,645 | -53 🟥 | 1.3% | 1.1% | -0.2 🟥 pp |
| Musali `LK-4215` | Mannar | 0.0% | 38 | 49 | +11 🟩 | 0.5% | 0.3% | -0.2 🟥 pp |
| Yakkalamulla `LK-3148` | Galle | 0.1% | 326 | 233 | -93 🟥 | 0.7% | 0.5% | -0.2 🟥 pp |
| Kotapola `LK-3206` | Matara | 0.5% | 1,355 | 1,176 | -179 🟥 | 2.1% | 1.9% | -0.2 🟥 pp |
| Nuwaragam Palatha Central `LK-7115` | Anuradhapura | 0.2% | 526 | 461 | -65 🟥 | 0.9% | 0.6% | -0.2 🟥 pp |
| Thalawa `LK-7148` | Anuradhapura | 0.0% | 245 | 127 | -118 🟥 | 0.4% | 0.2% | -0.2 🟥 pp |
| Ambanganga `LK-2221` | Matale | 0.0% | 105 | 72 | -33 🟥 | 0.7% | 0.5% | -0.2 🟥 pp |
| Bingiriya `LK-6142` | Kurunegala | 0.2% | 546 | 436 | -110 🟥 | 0.9% | 0.7% | -0.2 🟥 pp |
| Agalawatta `LK-1333` | Kalutara | 0.0% | 200 | 118 | -82 🟥 | 0.5% | 0.3% | -0.2 🟥 pp |
| Thawalama `LK-3118` | Galle | 0.1% | 295 | 211 | -84 🟥 | 0.9% | 0.7% | -0.2 🟥 pp |
| Nanaddan `LK-4212` | Mannar | 0.5% | 1,302 | 1,387 | +85 🟩 | 7.3% | 7.0% | -0.2 🟥 pp |
| Kesbewa `LK-1136` | Colombo | 1.6% | 4,271 | 3,990 | -281 🟥 | 1.7% | 1.5% | -0.2 🟥 pp |
| Ingiriya `LK-1310` | Kalutara | 0.2% | 630 | 544 | -86 🟥 | 1.2% | 0.9% | -0.2 🟥 pp |
| Mawathagama `LK-6160` | Kurunegala | 0.3% | 951 | 882 | -69 🟥 | 1.5% | 1.2% | -0.2 🟥 pp |
| Giribawa `LK-6103` | Kurunegala | 0.0% | 154 | 87 | -67 🟥 | 0.5% | 0.2% | -0.2 🟥 pp |
| Haputale `LK-8139` | Badulla | 0.2% | 574 | 437 | -137 🟥 | 1.2% | 0.9% | -0.2 🟥 pp |
| Mundel `LK-6218` | Puttalam | 0.1% | 464 | 360 | -104 🟥 | 0.8% | 0.5% | -0.3 🟥 pp |
| Vadamaradchchi South-West (Karaveddy) `LK-4121` | Jaffna | 0.2% | 613 | 444 | -169 🟥 | 1.3% | 1.1% | -0.3 🟥 pp |
| Katana `LK-1206` | Gampaha | 3.6% | 9,676 | 9,268 | -408 🟥 | 4.1% | 3.8% | -0.3 🟥 pp |
| Yatinuwara `LK-2136` | Kandy | 0.2% | 811 | 557 | -254 🟥 | 0.8% | 0.5% | -0.3 🟥 pp |
| Welikanda `LK-7210` | Polonnaruwa | 0.0% | 193 | 112 | -81 🟥 | 0.6% | 0.3% | -0.3 🟥 pp |
| Homagama `LK-1112` | Colombo | 0.7% | 2,097 | 1,665 | -432 🟥 | 0.9% | 0.6% | -0.3 🟥 pp |
| Morawewa `LK-5312` | Trincomalee | 0.0% | 38 | 17 | -21 🟥 | 0.5% | 0.2% | -0.3 🟥 pp |
| Dankotuwa `LK-6248` | Puttalam | 0.3% | 981 | 797 | -184 🟥 | 1.6% | 1.3% | -0.3 🟥 pp |
| Ella `LK-8136` | Badulla | 0.1% | 412 | 299 | -113 🟥 | 0.9% | 0.6% | -0.3 🟥 pp |
| Nivithigala `LK-9136` | Ratnapura | 0.1% | 415 | 226 | -189 🟥 | 0.7% | 0.4% | -0.3 🟥 pp |
| Imbulpe `LK-9115` | Ratnapura | 0.2% | 609 | 453 | -156 🟥 | 1.0% | 0.7% | -0.3 🟥 pp |
| Kahawattha `LK-9139` | Ratnapura | 0.1% | 389 | 247 | -142 🟥 | 0.9% | 0.6% | -0.3 🟥 pp |
| Mallawapitiya `LK-6157` | Kurunegala | 0.4% | 992 | 922 | -70 🟥 | 1.9% | 1.5% | -0.3 🟥 pp |
| Rattota `LK-2230` | Matale | 0.1% | 504 | 338 | -166 🟥 | 1.0% | 0.6% | -0.4 🟥 pp |
| Nallur `LK-4133` | Jaffna | 1.1% | 2,748 | 2,682 | -66 🟥 | 4.0% | 3.7% | -0.4 🟥 pp |
| Doluwa `LK-2142` | Kandy | 0.2% | 636 | 482 | -154 🟥 | 1.3% | 0.9% | -0.4 🟥 pp |
| Yatiyantota `LK-9227` | Kegalle | 0.2% | 758 | 541 | -217 🟥 | 1.2% | 0.9% | -0.4 🟥 pp |
| Thissamaharama `LK-3309` | Hambantota | 0.1% | 416 | 167 | -249 🟥 | 0.6% | 0.2% | -0.4 🟥 pp |
| Kolonnawa `LK-1106` | Colombo | 1.1% | 3,260 | 2,809 | -451 🟥 | 1.7% | 1.3% | -0.4 🟥 pp |
| Puttalam `LK-6215` | Puttalam | 0.4% | 1,312 | 1,139 | -173 🟥 | 1.6% | 1.2% | -0.4 🟥 pp |
| Opanayake `LK-9121` | Ratnapura | 0.0% | 150 | 46 | -104 🟥 | 0.6% | 0.2% | -0.4 🟥 pp |
| Wattala `LK-1218` | Gampaha | 3.6% | 9,453 | 9,078 | -375 🟥 | 5.4% | 5.0% | -0.4 🟥 pp |
| Madampe `LK-6236` | Puttalam | 0.5% | 1,403 | 1,232 | -171 🟥 | 2.9% | 2.5% | -0.4 🟥 pp |
| Moratuwa `LK-1133` | Colombo | 4.6% | 13,059 | 11,763 | -1,296 🟥 | 7.8% | 7.3% | -0.4 🟥 pp |
| Panvila `LK-2115` | Kandy | 0.2% | 604 | 482 | -122 🟥 | 2.3% | 1.9% | -0.4 🟥 pp |
| Panadura `LK-1303` | Kalutara | 0.6% | 2,293 | 1,567 | -726 🟥 | 1.3% | 0.8% | -0.4 🟥 pp |
| Bulathsinhala `LK-1312` | Kalutara | 0.1% | 650 | 371 | -279 🟥 | 1.0% | 0.6% | -0.4 🟥 pp |
| Valikamam South (Uduvil) `LK-4115` | Jaffna | 0.8% | 2,321 | 1,978 | -343 🟥 | 4.4% | 3.9% | -0.5 🟥 pp |
| Lunugamwehera `LK-3306` | Hambantota | 0.0% | 225 | 84 | -141 🟥 | 0.7% | 0.2% | -0.5 🟥 pp |
| Gangawata Korale `LK-2130` | Kandy | 1.0% | 3,332 | 2,454 | -878 🟥 | 2.1% | 1.6% | -0.5 🟥 pp |
| Ratmalana `LK-1131` | Colombo | 1.6% | 4,847 | 4,012 | -835 🟥 | 5.1% | 4.6% | -0.5 🟥 pp |
| Verugal `LK-5333` | Trincomalee | 0.2% | 469 | 505 | +36 🟩 | 4.1% | 3.6% | -0.5 🟥 pp |
| Mahawewa `LK-6239` | Puttalam | 0.3% | 1,000 | 697 | -303 🟥 | 2.0% | 1.4% | -0.5 🟥 pp |
| Maharagama `LK-1121` | Colombo | 0.9% | 3,285 | 2,227 | -1,058 🟥 | 1.7% | 1.1% | -0.5 🟥 pp |
| Passara `LK-8118` | Badulla | 0.2% | 884 | 624 | -260 🟥 | 1.8% | 1.3% | -0.6 🟥 pp |
| Kuchchaweli `LK-5306` | Trincomalee | 0.2% | 627 | 530 | -97 🟥 | 1.9% | 1.3% | -0.6 🟥 pp |
| Karainagar `LK-4104` | Jaffna | 0.1% | 374 | 303 | -71 🟥 | 3.9% | 3.3% | -0.6 🟥 pp |
| Ayagama `LK-9130` | Ratnapura | 0.0% | 266 | 78 | -188 🟥 | 0.9% | 0.3% | -0.6 🟥 pp |
| Kaduwela `LK-1109` | Colombo | 1.0% | 3,879 | 2,595 | -1,284 🟥 | 1.5% | 0.9% | -0.6 🟥 pp |
| Kurunegala `LK-6154` | Kurunegala | 0.5% | 1,720 | 1,346 | -374 🟥 | 2.1% | 1.5% | -0.6 🟥 pp |
| Arachchikattuwa `LK-6230` | Puttalam | 0.2% | 796 | 558 | -238 🟥 | 1.9% | 1.3% | -0.6 🟥 pp |
| Pasbagekorale `LK-2157` | Kandy | 0.4% | 1,299 | 965 | -334 🟥 | 2.2% | 1.5% | -0.7 🟥 pp |
| Rambukkana `LK-9203` | Kegalle | 0.8% | 2,453 | 1,960 | -493 🟥 | 3.0% | 2.3% | -0.7 🟥 pp |
| Chilaw `LK-6233` | Puttalam | 0.5% | 1,609 | 1,164 | -445 🟥 | 2.6% | 1.8% | -0.7 🟥 pp |
| Town & Gravets `LK-5315` | Trincomalee | 1.6% | 4,848 | 4,173 | -675 🟥 | 5.0% | 4.2% | -0.8 🟥 pp |
| Thimbirigasyaya `LK-1127` | Colombo | 2.8% | 10,262 | 7,036 | -3,226 🟥 | 4.3% | 3.2% | -1.1 🟥 pp |
| Manmunai South & Eruvil Pattu `LK-5136` | Batticaloa | 0.5% | 1,836 | 1,216 | -620 🟥 | 3.0% | 1.9% | -1.1 🟥 pp |
| Sri Jayawardanapura Kotte `LK-1124` | Colombo | 1.3% | 5,055 | 3,379 | -1,676 🟥 | 4.7% | 3.5% | -1.2 🟥 pp |
| Dehiwala `LK-1130` | Colombo | 1.0% | 3,684 | 2,557 | -1,127 🟥 | 4.1% | 2.7% | -1.4 🟥 pp |

***Koralai Pattu Central** gained the most share at **+12.0pp**. **Dehiwala** saw the steepest share decline at **-1.4pp**.*

### Other

| DSD | District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Palugaswewa `LK-7157` | Anuradhapura | 1.1% | 1 | 43 | +42 🟩 | 0.0% | 0.2% | +0.2 🟩 pp |
| Puttalam `LK-6215` | Puttalam | 5.7% | 14 | 217 | +203 🟩 | 0.0% | 0.2% | +0.2 🟩 pp |
| Delft `LK-4142` | Jaffna | 0.1% | 0 | 5 | +5 🟩 | 0.0% | 0.2% | +0.2 🟩 pp |
| Elahera `LK-7218` | Polonnaruwa | 1.6% | 1 | 62 | +61 🟩 | 0.0% | 0.1% | +0.1 🟩 pp |
| Udapalatha `LK-2151` | Kandy | 2.3% | 1 | 87 | +86 🟩 | 0.0% | 0.1% | +0.1 🟩 pp |
| Minuwangoda `LK-1215` | Gampaha | 4.1% | 19 | 154 | +135 🟩 | 0.0% | 0.1% | +0.1 🟩 pp |
| Akmeemana `LK-3145` | Galle | 1.1% | 1 | 42 | +41 🟩 | 0.0% | 0.0% | 0.0 pp |
| Katana `LK-1206` | Gampaha | 6.9% | 155 | 262 | +107 🟩 | 0.1% | 0.1% | 0.0 pp |
| Nuwaragam Palatha Central `LK-7115` | Anuradhapura | 0.9% | 6 | 36 | +30 🟩 | 0.0% | 0.1% | 0.0 pp |
| Mirigama `LK-1212` | Gampaha | 2.4% | 20 | 91 | +71 🟩 | 0.0% | 0.1% | 0.0 pp |
| Pasbagekorale `LK-2157` | Kandy | 1.0% | 12 | 38 | +26 🟩 | 0.0% | 0.1% | 0.0 pp |
| Gonapinuwala `LK-3134` | Galle | 0.1% | 0 | 5 | +5 🟩 | 0.0% | 0.0% | 0.0 pp |
| Maspotha `LK-6151` | Kurunegala | 0.2% | 0 | 9 | +9 🟩 | 0.0% | 0.0% | 0.0 pp |
| Palagala `LK-7166` | Anuradhapura | 0.2% | 0 | 8 | +8 🟩 | 0.0% | 0.0% | 0.0 pp |
| Tirukkovil `LK-5245` | Ampara | 0.2% | 0 | 6 | +6 🟩 | 0.0% | 0.0% | 0.0 pp |
| Welioya `LK-4418` | Mullaitivu | 0.1% | 0 | 2 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Kuchchaweli `LK-5306` | Trincomalee | 0.3% | 3 | 11 | +8 🟩 | 0.0% | 0.0% | 0.0 pp |
| Bandarawela `LK-8133` | Badulla | 0.5% | 8 | 20 | +12 🟩 | 0.0% | 0.0% | 0.0 pp |
| Mahawilachchiya `LK-7112` | Anuradhapura | 0.1% | 0 | 4 | +4 🟩 | 0.0% | 0.0% | 0.0 pp |
| Mahakumbukkadawala `LK-6221` | Puttalam | 0.1% | 0 | 3 | +3 🟩 | 0.0% | 0.0% | 0.0 pp |
| Bulathkohipitiya `LK-9224` | Kegalle | 0.2% | 0 | 6 | +6 🟩 | 0.0% | 0.0% | 0.0 pp |
| Manthai East `LK-4406` | Mullaitivu | 0.0% | 0 | 1 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Bamunakotuwa `LK-6149` | Kurunegala | 0.1% | 0 | 5 | +5 🟩 | 0.0% | 0.0% | 0.0 pp |
| Kalutara `LK-1321` | Kalutara | 1.1% | 20 | 41 | +21 🟩 | 0.0% | 0.0% | 0.0 pp |
| Galewela `LK-2203` | Matale | 0.4% | 4 | 14 | +10 🟩 | 0.0% | 0.0% | 0.0 pp |
| Ampara `LK-5215` | Ampara | 0.3% | 4 | 10 | +6 🟩 | 0.0% | 0.0% | 0.0 pp |
| Pannala `LK-6178` | Kurunegala | 1.0% | 20 | 37 | +17 🟩 | 0.0% | 0.0% | 0.0 pp |
| Udubaddawa `LK-6175` | Kurunegala | 0.2% | 3 | 9 | +6 🟩 | 0.0% | 0.0% | 0.0 pp |
| Rajanganaya `LK-7142` | Anuradhapura | 0.1% | 1 | 5 | +4 🟩 | 0.0% | 0.0% | 0.0 pp |
| Kekirawa `LK-7154` | Anuradhapura | 0.2% | 1 | 8 | +7 🟩 | 0.0% | 0.0% | 0.0 pp |
| Madhu `LK-4209` | Mannar | 0.0% | 0 | 1 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Madampe `LK-6236` | Puttalam | 0.2% | 4 | 9 | +5 🟩 | 0.0% | 0.0% | 0.0 pp |
| Islands North (Kayts) `LK-4103` | Jaffna | 0.1% | 3 | 4 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Dankotuwa `LK-6248` | Puttalam | 0.3% | 4 | 10 | +6 🟩 | 0.0% | 0.0% | 0.0 pp |
| Dehiwala `LK-1130` | Colombo | 3.0% | 100 | 114 | +14 🟩 | 0.1% | 0.1% | 0.0 pp |
| Athuraliya `LK-3215` | Matara | 0.1% | 1 | 4 | +3 🟩 | 0.0% | 0.0% | 0.0 pp |
| Ingiriya `LK-1310` | Kalutara | 0.2% | 1 | 6 | +5 🟩 | 0.0% | 0.0% | 0.0 pp |
| Manmunai North `LK-5118` | Batticaloa | 0.6% | 12 | 21 | +9 🟩 | 0.0% | 0.0% | 0.0 pp |
| Kelaniya `LK-1236` | Gampaha | 1.9% | 62 | 71 | +9 🟩 | 0.0% | 0.1% | 0.0 pp |
| Attanagalla `LK-1227` | Gampaha | 0.7% | 9 | 25 | +16 🟩 | 0.0% | 0.0% | 0.0 pp |
| Imbulpe `LK-9115` | Ratnapura | 0.2% | 1 | 6 | +5 🟩 | 0.0% | 0.0% | 0.0 pp |
| Medadumbara `LK-2124` | Kandy | 0.2% | 4 | 9 | +5 🟩 | 0.0% | 0.0% | 0.0 pp |
| Opanayake `LK-9121` | Ratnapura | 0.1% | 0 | 2 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Sooriyawewa `LK-3303` | Hambantota | 0.1% | 1 | 5 | +4 🟩 | 0.0% | 0.0% | 0.0 pp |
| Bingiriya `LK-6142` | Kurunegala | 0.2% | 3 | 8 | +5 🟩 | 0.0% | 0.0% | 0.0 pp |
| Tangalle `LK-3333` | Hambantota | 0.3% | 4 | 10 | +6 🟩 | 0.0% | 0.0% | 0.0 pp |
| Bope-Poddala `LK-3142` | Galle | 0.1% | 1 | 5 | +4 🟩 | 0.0% | 0.0% | 0.0 pp |
| Vavuniya South `LK-4306` | Vavuniya | 0.0% | 0 | 1 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Kolonnawa `LK-1106` | Colombo | 1.6% | 41 | 60 | +19 🟩 | 0.0% | 0.0% | 0.0 pp |
| Naula `LK-2209` | Matale | 0.1% | 1 | 3 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Thalawa `LK-7148` | Anuradhapura | 0.1% | 1 | 5 | +4 🟩 | 0.0% | 0.0% | 0.0 pp |
| Wellawaya `LK-8221` | Monaragala | 0.3% | 6 | 12 | +6 🟩 | 0.0% | 0.0% | 0.0 pp |
| Lunugala `LK-8119` | Badulla | 0.1% | 0 | 2 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Elpitiya `LK-3112` | Galle | 0.1% | 1 | 5 | +4 🟩 | 0.0% | 0.0% | 0.0 pp |
| Thihagoda `LK-3236` | Matara | 0.1% | 0 | 2 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Sammanthurai `LK-5218` | Ampara | 0.3% | 5 | 10 | +5 🟩 | 0.0% | 0.0% | 0.0 pp |
| Divulapitiya `LK-1209` | Gampaha | 0.8% | 22 | 32 | +10 🟩 | 0.0% | 0.0% | 0.0 pp |
| Karaitivu `LK-5227` | Ampara | 0.0% | 0 | 1 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Beruwala `LK-1324` | Kalutara | 0.8% | 21 | 32 | +11 🟩 | 0.0% | 0.0% | 0.0 pp |
| Weligama `LK-3239` | Matara | 0.2% | 4 | 8 | +4 🟩 | 0.0% | 0.0% | 0.0 pp |
| Nivithigala `LK-9136` | Ratnapura | 0.1% | 0 | 3 | +3 🟩 | 0.0% | 0.0% | 0.0 pp |
| Kegalle `LK-9212` | Kegalle | 0.3% | 8 | 13 | +5 🟩 | 0.0% | 0.0% | 0.0 pp |
| Padiyathalawa `LK-5206` | Ampara | 0.0% | 0 | 1 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Warakapola `LK-9218` | Kegalle | 0.3% | 7 | 13 | +6 🟩 | 0.0% | 0.0% | 0.0 pp |
| Yatiyantota `LK-9227` | Kegalle | 0.1% | 0 | 3 | +3 🟩 | 0.0% | 0.0% | 0.0 pp |
| Galgamuwa `LK-6106` | Kurunegala | 0.1% | 1 | 4 | +3 🟩 | 0.0% | 0.0% | 0.0 pp |
| Deraniyagala `LK-9233` | Kegalle | 0.1% | 2 | 4 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Dehiattakandiya `LK-5203` | Ampara | 0.1% | 0 | 3 | +3 🟩 | 0.0% | 0.0% | 0.0 pp |
| Alawwa `LK-6184` | Kurunegala | 0.1% | 1 | 4 | +3 🟩 | 0.0% | 0.0% | 0.0 pp |
| Kahatagasdigiliya `LK-7121` | Anuradhapura | 0.1% | 0 | 2 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Polgahawela `LK-6187` | Kurunegala | 0.2% | 3 | 6 | +3 🟩 | 0.0% | 0.0% | 0.0 pp |
| Manthai West `LK-4206` | Mannar | 0.1% | 1 | 2 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Kantale `LK-5321` | Trincomalee | 0.1% | 1 | 3 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Thissamaharama `LK-3309` | Hambantota | 0.2% | 3 | 6 | +3 🟩 | 0.0% | 0.0% | 0.0 pp |
| Rattota `LK-2230` | Matale | 0.1% | 2 | 4 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Nochchiyagama `LK-7139` | Anuradhapura | 0.1% | 0 | 2 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Welivitiya-Divitura `LK-3130` | Galle | 0.0% | 0 | 1 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Dikwella `LK-3248` | Matara | 0.1% | 2 | 4 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Pathahewaheta `LK-2145` | Kandy | 0.1% | 1 | 3 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Manmunai West `LK-5121` | Batticaloa | 0.0% | 0 | 1 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Wariyapola `LK-6136` | Kurunegala | 0.1% | 1 | 3 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Balapitiya `LK-3106` | Galle | 0.2% | 6 | 8 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Malimbada `LK-3224` | Matara | 0.0% | 0 | 1 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Ukuwela `LK-2233` | Matale | 0.1% | 1 | 3 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Vengalacheddikulam `LK-4312` | Vavuniya | 0.1% | 5 | 5 | +0 | 0.0% | 0.0% | 0.0 pp |
| Nattandiya `LK-6242` | Puttalam | 0.2% | 6 | 8 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Tumpane `LK-2103` | Kandy | 0.1% | 1 | 2 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Galnewa `LK-7163` | Anuradhapura | 0.0% | 0 | 1 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Yatinuwara `LK-2136` | Kandy | 0.3% | 8 | 11 | +3 🟩 | 0.0% | 0.0% | 0.0 pp |
| Pathadumbara `LK-2112` | Kandy | 0.1% | 2 | 4 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Devinuwara `LK-3245` | Matara | 0.1% | 1 | 2 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Rambukkana `LK-9203` | Kegalle | 0.2% | 5 | 7 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Buttala `LK-8224` | Monaragala | 0.0% | 0 | 1 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Mallawapitiya `LK-6157` | Kurunegala | 0.3% | 8 | 10 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Mawanella `LK-9206` | Kegalle | 0.1% | 3 | 5 | +2 🟩 | 0.0% | 0.0% | 0.0 pp |
| Kinniya `LK-5324` | Trincomalee | 0.0% | 0 | 1 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Negombo `LK-1203` | Gampaha | 3.3% | 130 | 127 | -3 🟥 | 0.1% | 0.1% | 0.0 pp |
| Kiriella `LK-9109` | Ratnapura | 0.0% | 1 | 1 | +0 | 0.0% | 0.0% | 0.0 pp |
| Agalawatta `LK-1333` | Kalutara | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Akurana `LK-2109` | Kandy | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Ududumbara `LK-2118` | Kandy | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Yatawatta `LK-2215` | Matale | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Ambanganga `LK-2221` | Matale | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Laggala `LK-2224` | Matale | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Bentota `LK-3103` | Galle | 0.1% | 3 | 3 | +0 | 0.0% | 0.0% | 0.0 pp |
| Niyagama `LK-3115` | Galle | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Akuressa `LK-3218` | Matara | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Kirinda Puhulwella `LK-3233` | Matara | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Angunakolapelessa `LK-3318` | Hambantota | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Weeraketiya `LK-3321` | Hambantota | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Okewela `LK-3327` | Hambantota | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Vadamaradchchi East `LK-4124` | Jaffna | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Musali `LK-4215` | Mannar | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Pachchilaipalli `LK-4503` | Kilinochchi | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Koralai Pattu North `LK-5103` | Batticaloa | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Koralai Pattu Central `LK-5104` | Batticaloa | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Koralai Pattu West `LK-5106` | Batticaloa | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Porativu Pattu `LK-5133` | Batticaloa | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Navithanveli `LK-5216` | Ampara | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Sainthamaruthu `LK-5225` | Ampara | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Nintavur `LK-5230` | Ampara | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Damana `LK-5242` | Ampara | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Padavi Sri Pura `LK-5303` | Trincomalee | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Gomarankadawala `LK-5309` | Trincomalee | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Morawewa `LK-5312` | Trincomalee | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Verugal `LK-5333` | Trincomalee | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Giribawa `LK-6103` | Kurunegala | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Panduwasnuwara East `LK-6148` | Kurunegala | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Nawagattegama `LK-6212` | Puttalam | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Padaviya `LK-7103` | Anuradhapura | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Kebithigollewa `LK-7106` | Anuradhapura | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Galenbidunuwewa `LK-7127` | Anuradhapura | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Rideemaliyadda `LK-8106` | Badulla | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Soranathota `LK-8115` | Badulla | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Madulla `LK-8206` | Monaragala | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Badalkumbura `LK-8218` | Monaragala | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Elapatha `LK-9127` | Ratnapura | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Ayagama `LK-9130` | Ratnapura | 0.0% | 0 | 0 | +0 | 0.0% | 0.0% | 0.0 pp |
| Ruwanwella `LK-9221` | Kegalle | 0.0% | 1 | 1 | +0 | 0.0% | 0.0% | 0.0 pp |
| Habaraduwa `LK-3154` | Galle | 0.2% | 6 | 6 | +0 | 0.0% | 0.0% | 0.0 pp |
| Uhana `LK-5212` | Ampara | 0.0% | 1 | 1 | +0 | 0.0% | 0.0% | 0.0 pp |
| Ambalangoda `LK-3133` | Galle | 0.1% | 3 | 3 | +0 | 0.0% | 0.0% | 0.0 pp |
| Kaburupitiya `LK-3227` | Matara | 0.1% | 2 | 2 | +0 | 0.0% | 0.0% | 0.0 pp |
| Alayadivembu `LK-5239` | Ampara | 0.0% | 1 | 1 | +0 | 0.0% | 0.0% | 0.0 pp |
| Hali-Ela `LK-8124` | Badulla | 0.2% | 9 | 9 | +0 | 0.0% | 0.0% | 0.0 pp |
| Sevanagala `LK-8233` | Monaragala | 0.0% | 1 | 1 | +0 | 0.0% | 0.0% | 0.0 pp |
| Manmunai Pattu `LK-5127` | Batticaloa | 0.0% | 1 | 1 | +0 | 0.0% | 0.0% | 0.0 pp |
| Badulla `LK-8121` | Badulla | 0.4% | 13 | 14 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Thanamalwila `LK-8230` | Monaragala | 0.0% | 1 | 1 | +0 | 0.0% | 0.0% | 0.0 pp |
| Mihinthale `LK-7130` | Anuradhapura | 0.0% | 1 | 1 | +0 | 0.0% | 0.0% | 0.0 pp |
| Horana `LK-1309` | Kalutara | 0.7% | 23 | 26 | +3 🟩 | 0.0% | 0.0% | 0.0 pp |
| Deltota `LK-2148` | Kandy | 0.1% | 5 | 5 | +0 | 0.0% | 0.0% | 0.0 pp |
| Uvaparanagama `LK-8127` | Badulla | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Ibbagamuwa `LK-6130` | Kurunegala | 0.1% | 4 | 3 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Medirigiriya `LK-7206` | Polonnaruwa | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Kundasale `LK-2127` | Kandy | 0.3% | 11 | 10 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Pasgoda `LK-3209` | Matara | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Poojapitiya `LK-2106` | Kandy | 0.0% | 2 | 1 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Dambulla `LK-2206` | Matale | 0.1% | 4 | 3 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Panduwasnuwara West `LK-6145` | Kurunegala | 0.1% | 4 | 3 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Valikamam South West (Sandilipay) `LK-4109` | Jaffna | 0.1% | 3 | 2 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Narammala `LK-6181` | Kurunegala | 0.0% | 2 | 1 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Siyambalanduwa `LK-8212` | Monaragala | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Mulatiyana `LK-3212` | Matara | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Beliatta `LK-3330` | Hambantota | 0.1% | 4 | 3 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Millaniya `LK-1318` | Kalutara | 0.0% | 2 | 1 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Valikamam West (Chankanai) `LK-4106` | Jaffna | 0.0% | 2 | 1 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Yakkalamulla `LK-3148` | Galle | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Embilipitiya `LK-9148` | Ratnapura | 0.0% | 3 | 0 | -3 🟥 | 0.0% | 0.0% | 0.0 pp |
| Kolonna `LK-9151` | Ratnapura | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Vavuniya `LK-4309` | Vavuniya | 1.4% | 57 | 54 | -3 🟥 | 0.0% | 0.0% | 0.0 pp |
| Kattankudy `LK-5124` | Batticaloa | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Nikaweratiya `LK-6121` | Kurunegala | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Ganewatta `LK-6133` | Kurunegala | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Kuliyapitiya East `LK-6169` | Kurunegala | 0.1% | 4 | 3 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Bibile `LK-8203` | Monaragala | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Katuwana `LK-3324` | Hambantota | 0.1% | 3 | 2 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Akkaraipattu `LK-5236` | Ampara | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Rambewa `LK-7118` | Anuradhapura | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Lankapura `LK-7209` | Polonnaruwa | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Kobeigane `LK-6139` | Kurunegala | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Welikanda `LK-7210` | Polonnaruwa | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Thawalama `LK-3118` | Galle | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Polpitigama `LK-6127` | Kurunegala | 0.1% | 5 | 3 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Karandeniya `LK-3109` | Galle | 0.0% | 2 | 0 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Hakmana `LK-3230` | Matara | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Thamankaduwa `LK-7215` | Polonnaruwa | 0.4% | 17 | 16 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Matara Four Gravets `LK-3242` | Matara | 0.3% | 15 | 12 | -3 🟥 | 0.0% | 0.0% | 0.0 pp |
| Wilgamuwa `LK-2227` | Matale | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Nallur `LK-4133` | Jaffna | 0.2% | 8 | 6 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Nuwaragam Palatha East `LK-7133` | Anuradhapura | 0.2% | 8 | 6 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Panvila `LK-2115` | Kandy | 0.0% | 2 | 1 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Nagoda `LK-3124` | Galle | 0.0% | 2 | 0 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Udunuwara `LK-2139` | Kandy | 0.1% | 7 | 3 | -4 🟥 | 0.0% | 0.0% | 0.0 pp |
| Valikamam South (Uduvil) `LK-4115` | Jaffna | 0.0% | 2 | 0 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Koralai Pattu South `LK-5110` | Batticaloa | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Minipe `LK-2121` | Kandy | 0.0% | 2 | 0 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Nachchaduwa `LK-7136` | Anuradhapura | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Manmunai South West `LK-5130` | Batticaloa | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Welimada `LK-8130` | Badulla | 0.0% | 5 | 1 | -4 🟥 | 0.0% | 0.0% | 0.0 pp |
| Kuliyapitiya West `LK-6172` | Kurunegala | 0.1% | 8 | 5 | -3 🟥 | 0.0% | 0.0% | 0.0 pp |
| Matale `LK-2218` | Matale | 0.2% | 10 | 7 | -3 🟥 | 0.0% | 0.0% | 0.0 pp |
| Pallama `LK-6227` | Puttalam | 0.0% | 2 | 1 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Dompe `LK-1230` | Gampaha | 0.3% | 19 | 13 | -6 🟥 | 0.0% | 0.0% | 0.0 pp |
| Valikamam North (Thllippalai) `LK-4112` | Jaffna | 0.2% | 6 | 7 | +1 🟩 | 0.0% | 0.0% | 0.0 pp |
| Kahawattha `LK-9139` | Ratnapura | 0.1% | 4 | 2 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Thenmaradchi (Chavakachcheri) `LK-4130` | Jaffna | 0.1% | 5 | 2 | -3 🟥 | 0.0% | 0.0% | 0.0 pp |
| Matugama `LK-1330` | Kalutara | 0.0% | 4 | 0 | -4 🟥 | 0.0% | 0.0% | 0.0 pp |
| Ratnapura `LK-9112` | Ratnapura | 0.2% | 14 | 8 | -6 🟥 | 0.0% | 0.0% | 0.0 pp |
| Muthur `LK-5327` | Trincomalee | 0.0% | 3 | 0 | -3 🟥 | 0.0% | 0.0% | 0.0 pp |
| Gampaha `LK-1224` | Gampaha | 0.6% | 32 | 22 | -10 🟥 | 0.0% | 0.0% | 0.0 pp |
| Higurakgoda `LK-7203` | Polonnaruwa | 0.2% | 9 | 6 | -3 🟥 | 0.0% | 0.0% | 0.0 pp |
| Katharagama `LK-8227` | Monaragala | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Horowpathana `LK-7124` | Anuradhapura | 0.0% | 3 | 1 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Aranayake `LK-9209` | Kegalle | 0.0% | 4 | 0 | -4 🟥 | 0.0% | 0.0% | 0.0 pp |
| Weerabugedara `LK-6166` | Kurunegala | 0.1% | 6 | 4 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Hatharaliyadda `LK-2134` | Kandy | 0.0% | 2 | 0 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Chilaw `LK-6233` | Puttalam | 0.3% | 14 | 10 | -4 🟥 | 0.0% | 0.0% | 0.0 pp |
| Pallepola `LK-2212` | Matale | 0.0% | 2 | 0 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Mahara `LK-1233` | Gampaha | 1.3% | 61 | 50 | -11 🟥 | 0.0% | 0.0% | 0.0 pp |
| Neluwa `LK-3121` | Galle | 0.0% | 2 | 0 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Valikamam East (Kopay) `LK-4118` | Jaffna | 0.1% | 9 | 4 | -5 🟥 | 0.0% | 0.0% | 0.0 pp |
| Walasmulla `LK-3325` | Hambantota | 0.0% | 3 | 0 | -3 🟥 | 0.0% | 0.0% | 0.0 pp |
| Walallawita `LK-1339` | Kalutara | 0.1% | 6 | 2 | -4 🟥 | 0.0% | 0.0% | 0.0 pp |
| Pitabaddara `LK-3203` | Matara | 0.0% | 5 | 1 | -4 🟥 | 0.0% | 0.0% | 0.0 pp |
| Kalawana `LK-9133` | Ratnapura | 0.1% | 6 | 2 | -4 🟥 | 0.0% | 0.0% | 0.0 pp |
| Pelmadulla `LK-9124` | Ratnapura | 0.1% | 9 | 2 | -7 🟥 | 0.0% | 0.0% | 0.0 pp |
| Homagama `LK-1112` | Colombo | 0.9% | 50 | 36 | -14 🟥 | 0.0% | 0.0% | 0.0 pp |
| Mundel `LK-6218` | Puttalam | 0.0% | 6 | 1 | -5 🟥 | 0.0% | 0.0% | 0.0 pp |
| Harispattuwa `LK-2133` | Kandy | 0.2% | 16 | 9 | -7 🟥 | 0.0% | 0.0% | 0.0 pp |
| Kandeketiya `LK-8112` | Badulla | 0.0% | 2 | 0 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Medagama `LK-8209` | Monaragala | 0.0% | 4 | 1 | -3 🟥 | 0.0% | 0.0% | 0.0 pp |
| Karuwalagaswewa `LK-6209` | Puttalam | 0.0% | 3 | 1 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Rasnayakapura `LK-6118` | Kurunegala | 0.0% | 2 | 0 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Thambuththegama `LK-7145` | Anuradhapura | 0.0% | 4 | 0 | -4 🟥 | 0.0% | 0.0% | 0.0 pp |
| Mahaoya `LK-5209` | Ampara | 0.0% | 2 | 0 | -2 🟥 | 0.0% | 0.0% | 0.0 pp |
| Ambalantota `LK-3315` | Hambantota | 0.0% | 8 | 1 | -7 🟥 | 0.0% | 0.0% | 0.0 pp |
| Jaffna `LK-4136` | Jaffna | 0.0% | 6 | 1 | -5 🟥 | 0.0% | 0.0% | 0.0 pp |
| Welipitiya `LK-3221` | Matara | 0.1% | 8 | 3 | -5 🟥 | 0.0% | 0.0% | 0.0 pp |
| Padukka `LK-1118` | Colombo | 0.2% | 12 | 6 | -6 🟥 | 0.0% | 0.0% | 0.0 pp |
| Panadura `LK-1303` | Kalutara | 0.8% | 48 | 30 | -18 🟥 | 0.0% | 0.0% | 0.0 pp |
| Karainagar `LK-4104` | Jaffna | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Thunukkai `LK-4403` | Mullaitivu | 0.0% | 2 | 1 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Lahugala `LK-5251` | Ampara | 0.0% | 1 | 0 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Wennappuwa `LK-6245` | Puttalam | 0.2% | 15 | 7 | -8 🟥 | 0.0% | 0.0% | 0.0 pp |
| Sri Jayawardanapura Kotte `LK-1124` | Colombo | 3.4% | 158 | 130 | -28 🟥 | 0.1% | 0.1% | 0.0 pp |
| Kesbewa `LK-1136` | Colombo | 2.2% | 106 | 83 | -23 🟥 | 0.0% | 0.0% | 0.0 pp |
| Bandaragama `LK-1306` | Kalutara | 0.2% | 19 | 7 | -12 🟥 | 0.0% | 0.0% | 0.0 pp |
| Galigamuwa `LK-9215` | Kegalle | 0.0% | 10 | 1 | -9 🟥 | 0.0% | 0.0% | 0.0 pp |
| Kurunegala `LK-6154` | Kurunegala | 0.2% | 18 | 9 | -9 🟥 | 0.0% | 0.0% | 0.0 pp |
| Biyagama `LK-1239` | Gampaha | 1.0% | 58 | 39 | -19 🟥 | 0.0% | 0.0% | 0.0 pp |
| Galle 4 Gravets `LK-3139` | Galle | 0.2% | 20 | 8 | -12 🟥 | 0.0% | 0.0% | 0.0 pp |
| Rideegama `LK-6163` | Kurunegala | 0.0% | 11 | 0 | -11 🟥 | 0.0% | 0.0% | 0.0 pp |
| Dimbulagala `LK-7212` | Polonnaruwa | 0.0% | 10 | 0 | -10 🟥 | 0.0% | 0.0% | 0.0 pp |
| Gangawata Korale `LK-2130` | Kandy | 1.1% | 65 | 43 | -22 🟥 | 0.0% | 0.0% | 0.0 pp |
| Ipalogama `LK-7160` | Anuradhapura | 0.0% | 6 | 1 | -5 🟥 | 0.0% | 0.0% | 0.0 pp |
| Godakawela `LK-9142` | Ratnapura | 0.1% | 15 | 5 | -10 🟥 | 0.0% | 0.0% | 0.0 pp |
| Weligepola `LK-9145` | Ratnapura | 0.0% | 5 | 1 | -4 🟥 | 0.0% | 0.0% | 0.0 pp |
| Palindanuwara `LK-1336` | Kalutara | 0.0% | 7 | 0 | -7 🟥 | 0.0% | 0.0% | 0.0 pp |
| Thambalagamuwa `LK-5318` | Trincomalee | 0.0% | 4 | 0 | -4 🟥 | 0.0% | 0.0% | 0.0 pp |
| Kotapola `LK-3206` | Matara | 0.0% | 9 | 0 | -9 🟥 | 0.0% | 0.0% | 0.0 pp |
| Thirappane `LK-7151` | Anuradhapura | 0.0% | 4 | 0 | -4 🟥 | 0.0% | 0.0% | 0.0 pp |
| Ella `LK-8136` | Badulla | 0.1% | 11 | 4 | -7 🟥 | 0.0% | 0.0% | 0.0 pp |
| Vadamaradchi North (Point Pedro) `LK-4127` | Jaffna | 0.1% | 10 | 2 | -8 🟥 | 0.0% | 0.0% | 0.0 pp |
| Passara `LK-8118` | Badulla | 0.0% | 8 | 0 | -8 🟥 | 0.0% | 0.0% | 0.0 pp |
| Puthukkudiyiruppu `LK-4409` | Mullaitivu | 0.0% | 4 | 0 | -4 🟥 | 0.0% | 0.0% | 0.0 pp |
| Dehiowita `LK-9230` | Kegalle | 0.0% | 14 | 0 | -14 🟥 | 0.0% | 0.0% | 0.0 pp |
| Town & Gravets `LK-5315` | Trincomalee | 0.8% | 46 | 30 | -16 🟥 | 0.0% | 0.0% | 0.0 pp |
| Kandavalai `LK-4506` | Kilinochchi | 0.0% | 5 | 1 | -4 🟥 | 0.0% | 0.0% | 0.0 pp |
| Ambanpola `LK-6112` | Kurunegala | 0.0% | 4 | 0 | -4 🟥 | 0.0% | 0.0% | 0.0 pp |
| Mawathagama `LK-6160` | Kurunegala | 0.1% | 13 | 2 | -11 🟥 | 0.0% | 0.0% | 0.0 pp |
| Vanathavilluwa `LK-6206` | Puttalam | 0.0% | 4 | 1 | -3 🟥 | 0.0% | 0.0% | 0.0 pp |
| Haputale `LK-8139` | Badulla | 0.0% | 10 | 1 | -9 🟥 | 0.0% | 0.0% | 0.0 pp |
| Doluwa `LK-2142` | Kandy | 0.0% | 10 | 1 | -9 🟥 | 0.0% | 0.0% | 0.0 pp |
| Anamaduwa `LK-6224` | Puttalam | 0.0% | 7 | 0 | -7 🟥 | 0.0% | 0.0% | 0.0 pp |
| Manmunai South & Eruvil Pattu `LK-5136` | Batticaloa | 0.3% | 21 | 10 | -11 🟥 | 0.0% | 0.0% | 0.0 pp |
| Vadamaradchchi South-West (Karaveddy) `LK-4121` | Jaffna | 0.0% | 10 | 1 | -9 🟥 | 0.0% | 0.0% | 0.0 pp |
| Mannar Town `LK-4203` | Mannar | 0.0% | 11 | 1 | -10 🟥 | 0.0% | 0.0% | 0.0 pp |
| Colombo `LK-1103` | Colombo | 4.3% | 251 | 164 | -87 🟥 | 0.1% | 0.1% | 0.0 pp |
| Kotawehera `LK-6115` | Kurunegala | 0.0% | 5 | 0 | -5 🟥 | 0.0% | 0.0% | 0.0 pp |
| Monaragala `LK-8215` | Monaragala | 0.1% | 15 | 3 | -12 🟥 | 0.0% | 0.0% | 0.0 pp |
| Ganga Ihala Korale `LK-2154` | Kandy | 0.0% | 14 | 0 | -14 🟥 | 0.0% | 0.0% | 0.0 pp |
| Mahawewa `LK-6239` | Puttalam | 0.0% | 14 | 0 | -14 🟥 | 0.0% | 0.0% | 0.0 pp |
| Nanaddan `LK-4212` | Mannar | 0.0% | 5 | 0 | -5 🟥 | 0.0% | 0.0% | 0.0 pp |
| Seethawaka `LK-1115` | Colombo | 0.1% | 37 | 4 | -33 🟥 | 0.0% | 0.0% | 0.0 pp |
| Bulathsinhala `LK-1312` | Kalutara | 0.0% | 21 | 0 | -21 🟥 | 0.0% | 0.0% | 0.0 pp |
| Madurawala `LK-1315` | Kalutara | 0.0% | 12 | 0 | -12 🟥 | 0.0% | 0.0% | 0.0 pp |
| Moratuwa `LK-1133` | Colombo | 4.2% | 230 | 158 | -72 🟥 | 0.1% | 0.1% | 0.0 pp |
| Ja Ela `LK-1221` | Gampaha | 1.6% | 138 | 60 | -78 🟥 | 0.1% | 0.0% | 0.0 pp |
| Karachchi `LK-4509` | Kilinochchi | 0.1% | 28 | 4 | -24 🟥 | 0.0% | 0.0% | 0.0 pp |
| Dodangoda `LK-1327` | Kalutara | 0.0% | 28 | 0 | -28 🟥 | 0.0% | 0.0% | 0.0 pp |
| Maho `LK-6124` | Kurunegala | 0.1% | 27 | 2 | -25 🟥 | 0.0% | 0.0% | 0.0 pp |
| Mahiyanganaya `LK-8103` | Badulla | 0.0% | 36 | 1 | -35 🟥 | 0.0% | 0.0% | 0.0 pp |
| Ratmalana `LK-1131` | Colombo | 1.1% | 92 | 43 | -49 🟥 | 0.1% | 0.0% | 0.0 pp |
| Maharagama `LK-1121` | Colombo | 2.3% | 188 | 89 | -99 🟥 | 0.1% | 0.0% | -0.1 🟥 pp |
| Haldummulla `LK-8142` | Badulla | 0.1% | 21 | 2 | -19 🟥 | 0.1% | 0.0% | -0.1 🟥 pp |
| Arachchikattuwa `LK-6230` | Puttalam | 0.1% | 24 | 2 | -22 🟥 | 0.1% | 0.0% | -0.1 🟥 pp |
| Ehetuwewa `LK-6109` | Kurunegala | 0.0% | 14 | 0 | -14 🟥 | 0.1% | 0.0% | -0.1 🟥 pp |
| Wattala `LK-1218` | Gampaha | 1.0% | 144 | 39 | -105 🟥 | 0.1% | 0.0% | -0.1 🟥 pp |
| Maritimepattu `LK-4415` | Mullaitivu | 0.1% | 22 | 5 | -17 🟥 | 0.1% | 0.0% | -0.1 🟥 pp |
| Hambantota `LK-3312` | Hambantota | 1.1% | 76 | 43 | -33 🟥 | 0.1% | 0.1% | -0.1 🟥 pp |
| Poonakary `LK-4512` | Kilinochchi | 0.0% | 17 | 0 | -17 🟥 | 0.1% | 0.0% | -0.1 🟥 pp |
| Medawachchiya `LK-7109` | Anuradhapura | 0.0% | 40 | 0 | -40 🟥 | 0.1% | 0.0% | -0.1 🟥 pp |
| Imaduwa `LK-3151` | Galle | 0.0% | 42 | 1 | -41 🟥 | 0.1% | 0.0% | -0.1 🟥 pp |
| Seruvila `LK-5330` | Trincomalee | 0.0% | 13 | 0 | -13 🟥 | 0.1% | 0.0% | -0.1 🟥 pp |
| Thimbirigasyaya `LK-1127` | Colombo | 6.0% | 552 | 226 | -326 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Kaduwela `LK-1109` | Colombo | 2.4% | 445 | 91 | -354 🟥 | 0.2% | 0.0% | -0.1 🟥 pp |
| Vavuniya North `LK-4303` | Vavuniya | 0.0% | 24 | 1 | -23 🟥 | 0.2% | 0.0% | -0.2 🟥 pp |
| Meegahakiula `LK-8109` | Badulla | 0.0% | 47 | 0 | -47 🟥 | 0.2% | 0.0% | -0.2 🟥 pp |
| Oddusuddan `LK-4412` | Mullaitivu | 0.1% | 41 | 3 | -38 🟥 | 0.3% | 0.0% | -0.2 🟥 pp |
| Islands South (Velanai) `LK-4139` | Jaffna | 0.0% | 46 | 1 | -45 🟥 | 0.3% | 0.0% | -0.3 🟥 pp |
| Lunugamwehera `LK-3306` | Hambantota | 0.0% | 200 | 0 | -200 🟥 | 0.6% | 0.0% | -0.6 🟥 pp |
| Kalpitiya `LK-6203` | Puttalam | 0.2% | 1,045 | 9 | -1,036 🟥 | 1.2% | 0.0% | -1.2 🟥 pp |

***Palugaswewa** gained the most share at **+0.2pp**. **Kalpitiya** saw the steepest share decline at **-1.2pp**. **Puttalam** had the largest absolute increase (**+203**).*

---

*Data from the 2012 and 2024 Sri Lanka Census, accessed via [lanka_data](https://pypi.org/project/lanka-data/). Raw data and derived tables live in the corresponding directories under [`analyses/`](analyses/).*
