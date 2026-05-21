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

District labels show the religion share of each district population in **2012 → 2024**. Districts are shaded by **change in share of population (pp)** from **red (decline)** to **green (growth)**. Districts with religion population **< 1,000 (2024)** are shown in **grey**.

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

![A3 representative chart](analyses/a3_proportion_change/chart.png)

For each district, the religion whose share of the local population changed most between 2012 and 2024, showing only rows with absolute change > 1%.

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

*Data from the 2012 and 2024 Sri Lanka Census, accessed via [lanka_data](https://pypi.org/project/lanka-data/). Raw data and derived tables live in the corresponding directories under [`analyses/`](analyses/).*
