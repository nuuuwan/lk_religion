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

District labels show the **district name** and **change in share of population (pp)**. Districts are shaded by **change in share of population (pp)** from **red (decline)** to **green (growth)**. Districts with religion population **< 1,000 (2024)** are shown in **grey**.

### Buddhist

| District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Puttalam | 2.4% | 329,705 | 361,148 | +31,443 🟩 | 43.2% | 44.1% | +0.9 🟩 pp |
| Vavuniya | 0.1% | 16,799 | 18,292 | +1,493 🟩 | 9.8% | 10.6% | +0.9 🟩 pp |
| Colombo | 11.1% | 1,632,125 | 1,682,524 | +50,399 🟩 | 70.2% | 70.8% | +0.6 🟩 pp |
| Ratnapura | 6.6% | 943,464 | 999,682 | +56,218 🟩 | 86.7% | 87.3% | +0.6 🟩 pp |
| Badulla | 4.2% | 591,799 | 636,988 | +45,189 🟩 | 72.6% | 73.0% | +0.4 🟩 pp |
| Gampaha | 11.5% | 1,642,767 | 1,744,475 | +101,708 🟩 | 71.3% | 71.6% | +0.3 🟩 pp |
| Jaffna | 0.0% | 2,168 | 2,788 | +620 🟩 | 0.4% | 0.5% | +0.1 🟩 pp |
| Hambantota | 4.3% | 580,344 | 649,736 | +69,392 🟩 | 96.7% | 96.8% | 0.0 pp |
| Kilinochchi | 0.0% | 1,275 | 1,533 | +258 🟩 | 1.1% | 1.1% | 0.0 pp |
| Matale | 2.8% | 385,151 | 418,608 | +33,457 🟩 | 79.5% | 79.5% | 0.0 pp |
| Monaragala | 3.3% | 426,762 | 498,436 | +71,674 🟩 | 94.6% | 94.5% | -0.1 🟥 pp |
| Matara | 5.2% | 766,323 | 787,303 | +20,980 🟩 | 94.1% | 94.0% | -0.2 🟥 pp |
| Batticaloa | 0.0% | 6,281 | 6,024 | -257 🟥 | 1.2% | 1.0% | -0.2 🟥 pp |
| Anuradhapura | 5.7% | 775,366 | 862,807 | +87,441 🟩 | 90.1% | 89.9% | -0.2 🟥 pp |
| Kurunegala | 10.2% | 1,430,958 | 1,557,554 | +126,596 🟩 | 88.5% | 88.1% | -0.4 🟥 pp |
| Galle | 6.8% | 998,647 | 1,026,031 | +27,384 🟩 | 93.9% | 93.5% | -0.4 🟥 pp |
| Polonnaruwa | 2.6% | 364,229 | 399,488 | +35,259 🟩 | 89.7% | 89.3% | -0.4 🟥 pp |
| Mullaitivu | 0.1% | 8,140 | 10,293 | +2,153 🟩 | 8.8% | 8.4% | -0.4 🟥 pp |
| Kalutara | 7.1% | 1,018,909 | 1,080,638 | +61,729 🟩 | 83.4% | 82.8% | -0.6 🟥 pp |
| Kandy | 7.0% | 1,009,220 | 1,063,511 | +54,291 🟩 | 73.4% | 72.7% | -0.6 🟥 pp |
| Nuwara Eliya | 1.8% | 278,254 | 278,828 | +574 🟩 | 39.1% | 38.4% | -0.7 🟥 pp |
| Kegalle | 4.8% | 709,917 | 728,929 | +19,012 🟩 | 84.4% | 83.7% | -0.7 🟥 pp |
| Mannar | 0.0% | 1,809 | 382 | -1,427 🟥 | 1.8% | 0.3% | -1.5 🟥 pp |
| Ampara | 1.8% | 251,427 | 276,176 | +24,749 🟩 | 38.7% | 37.1% | -1.6 🟥 pp |
| Trincomalee | 0.7% | 99,344 | 106,919 | +7,575 🟩 | 26.2% | 24.1% | -2.0 🟥 pp |

***Puttalam** gained the most share at **+0.9pp**. **Trincomalee** saw the steepest share decline at **-2.0pp**. **Kurunegala** had the largest absolute increase (**+126,596**).*

### Hindu

| District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Nuwara Eliya | 13.8% | 363,163 | 377,266 | +14,103 🟩 | 51.0% | 52.0% | +1.0 🟩 pp |
| Gampaha | 2.5% | 52,973 | 69,429 | +16,456 🟩 | 2.3% | 2.9% | +0.6 🟩 pp |
| Colombo | 7.2% | 186,303 | 197,759 | +11,456 🟩 | 8.0% | 8.3% | +0.3 🟩 pp |
| Monaragala | 0.5% | 11,997 | 14,974 | +2,977 🟩 | 2.7% | 2.8% | +0.2 🟩 pp |
| Kandy | 5.3% | 133,744 | 144,618 | +10,874 🟩 | 9.7% | 9.9% | +0.2 🟩 pp |
| Kurunegala | 0.6% | 14,716 | 17,487 | +2,771 🟩 | 0.9% | 1.0% | +0.1 🟩 pp |
| Kalutara | 1.6% | 39,541 | 42,528 | +2,987 🟩 | 3.2% | 3.3% | 0.0 pp |
| Anuradhapura | 0.1% | 3,231 | 3,755 | +524 🟩 | 0.4% | 0.4% | 0.0 pp |
| Hambantota | 0.1% | 1,222 | 1,401 | +179 🟩 | 0.2% | 0.2% | 0.0 pp |
| Kegalle | 2.1% | 54,350 | 56,199 | +1,849 🟩 | 6.5% | 6.5% | 0.0 pp |
| Galle | 0.6% | 15,584 | 15,600 | +16 🟩 | 1.5% | 1.4% | 0.0 pp |
| Polonnaruwa | 0.3% | 6,886 | 7,215 | +329 🟩 | 1.7% | 1.6% | -0.1 🟥 pp |
| Matale | 1.7% | 43,432 | 46,181 | +2,749 🟩 | 9.0% | 8.8% | -0.2 🟥 pp |
| Badulla | 6.1% | 157,608 | 166,380 | +8,772 🟩 | 19.3% | 19.1% | -0.3 🟥 pp |
| Puttalam | 1.1% | 28,811 | 28,832 | +21 🟩 | 3.8% | 3.5% | -0.3 🟥 pp |
| Matara | 0.5% | 16,421 | 14,625 | -1,796 🟥 | 2.0% | 1.7% | -0.3 🟥 pp |
| Ratnapura | 3.8% | 101,962 | 103,883 | +1,921 🟩 | 9.4% | 9.1% | -0.3 🟥 pp |
| Ampara | 4.2% | 102,829 | 114,586 | +11,757 🟩 | 15.8% | 15.4% | -0.4 🟥 pp |
| Jaffna | 17.9% | 483,255 | 489,521 | +6,266 🟩 | 82.8% | 82.3% | -0.5 🟥 pp |
| Kilinochchi | 4.0% | 92,986 | 110,258 | +17,272 🟩 | 81.9% | 80.7% | -1.3 🟥 pp |
| Batticaloa | 13.7% | 338,882 | 374,836 | +35,954 🟩 | 64.4% | 62.9% | -1.5 🟥 pp |
| Trincomalee | 4.0% | 98,442 | 108,050 | +9,608 🟩 | 25.9% | 24.4% | -1.5 🟥 pp |
| Mullaitivu | 3.2% | 69,377 | 88,738 | +19,361 🟩 | 75.3% | 72.4% | -2.9 🟥 pp |
| Vavuniya | 4.2% | 119,400 | 114,504 | -4,896 🟥 | 69.4% | 66.5% | -2.9 🟥 pp |
| Mannar | 1.0% | 24,027 | 26,214 | +2,187 🟩 | 24.1% | 21.2% | -2.9 🟥 pp |

***Nuwara Eliya** gained the most share at **+1.0pp**. **Mannar** saw the steepest share decline at **-2.9pp**. **Batticaloa** had the largest absolute increase (**+35,954**).*

### Islam

| District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Mannar | 1.4% | 16,512 | 33,883 | +17,371 🟩 | 16.6% | 27.4% | +10.8 🟩 pp |
| Trincomalee | 8.8% | 159,418 | 205,664 | +46,246 🟩 | 42.0% | 46.5% | +4.4 🟩 pp |
| Vavuniya | 0.8% | 11,972 | 17,775 | +5,803 🟩 | 7.0% | 10.3% | +3.4 🟩 pp |
| Ampara | 14.5% | 281,987 | 339,896 | +57,909 🟩 | 43.4% | 45.7% | +2.2 🟩 pp |
| Puttalam | 7.6% | 150,404 | 176,963 | +26,559 🟩 | 19.7% | 21.6% | +1.9 🟩 pp |
| Batticaloa | 6.9% | 134,065 | 161,494 | +27,429 🟩 | 25.5% | 27.1% | +1.6 🟩 pp |
| Kalutara | 5.9% | 114,556 | 138,230 | +23,674 🟩 | 9.4% | 10.6% | +1.2 🟩 pp |
| Kegalle | 3.1% | 61,164 | 72,616 | +11,452 🟩 | 7.3% | 8.3% | +1.1 🟩 pp |
| Kandy | 9.6% | 197,076 | 223,997 | +26,921 🟩 | 14.3% | 15.3% | +1.0 🟩 pp |
| Kurunegala | 6.1% | 117,810 | 143,299 | +25,489 🟩 | 7.3% | 8.1% | +0.8 🟩 pp |
| Polonnaruwa | 1.6% | 30,465 | 37,097 | +6,632 🟩 | 7.5% | 8.3% | +0.8 🟩 pp |
| Colombo | 12.8% | 274,067 | 298,422 | +24,355 🟩 | 11.8% | 12.6% | +0.8 🟩 pp |
| Mullaitivu | 0.1% | 1,880 | 3,279 | +1,399 🟩 | 2.0% | 2.7% | +0.6 🟩 pp |
| Gampaha | 5.8% | 112,746 | 134,422 | +21,676 🟩 | 4.9% | 5.5% | +0.6 🟩 pp |
| Galle | 2.0% | 39,267 | 46,038 | +6,771 🟩 | 3.7% | 4.2% | +0.5 🟩 pp |
| Matale | 2.2% | 45,682 | 52,224 | +6,542 🟩 | 9.4% | 9.9% | +0.5 🟩 pp |
| Anuradhapura | 3.6% | 71,493 | 83,979 | +12,486 🟩 | 8.3% | 8.7% | +0.4 🟩 pp |
| Matara | 1.3% | 25,614 | 29,858 | +4,244 🟩 | 3.1% | 3.6% | +0.4 🟩 pp |
| Kilinochchi | 0.1% | 700 | 1,394 | +694 🟩 | 0.6% | 1.0% | +0.4 🟩 pp |
| Badulla | 2.3% | 47,192 | 53,563 | +6,371 🟩 | 5.8% | 6.1% | +0.4 🟩 pp |
| Jaffna | 0.2% | 2,363 | 4,352 | +1,989 🟩 | 0.4% | 0.7% | +0.3 🟩 pp |
| Monaragala | 0.5% | 9,809 | 12,262 | +2,453 🟩 | 2.2% | 2.3% | +0.1 🟩 pp |
| Hambantota | 0.8% | 15,204 | 17,947 | +2,743 🟩 | 2.5% | 2.7% | +0.1 🟩 pp |
| Ratnapura | 1.1% | 24,446 | 26,796 | +2,350 🟩 | 2.2% | 2.3% | +0.1 🟩 pp |
| Nuwara Eliya | 0.9% | 21,116 | 21,929 | +813 🟩 | 3.0% | 3.0% | +0.1 🟩 pp |

***Mannar** gained the most share at **+10.8pp**. **Nuwara Eliya** had the smallest share gain at **+0.1pp**. **Ampara** had the largest absolute increase (**+57,909**).*

### Roman Catholic

| District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Mullaitivu | 1.1% | 9,063 | 13,982 | +4,919 🟩 | 9.8% | 11.4% | +1.6 🟩 pp |
| Jaffna | 6.3% | 75,474 | 77,197 | +1,723 🟩 | 12.9% | 13.0% | +0.1 🟩 pp |
| Matara | 0.2% | 2,432 | 2,445 | +13 🟩 | 0.3% | 0.3% | 0.0 pp |
| Galle | 0.3% | 4,415 | 4,207 | -208 🟥 | 0.4% | 0.4% | 0.0 pp |
| Hambantota | 0.1% | 1,139 | 1,017 | -122 🟥 | 0.2% | 0.2% | 0.0 pp |
| Kilinochchi | 1.2% | 12,063 | 14,446 | +2,383 🟩 | 10.6% | 10.6% | -0.1 🟥 pp |
| Monaragala | 0.1% | 1,601 | 1,181 | -420 🟥 | 0.4% | 0.2% | -0.1 🟥 pp |
| Matale | 0.6% | 7,899 | 7,797 | -102 🟥 | 1.6% | 1.5% | -0.2 🟥 pp |
| Ampara | 0.6% | 7,588 | 7,351 | -237 🟥 | 1.2% | 1.0% | -0.2 🟥 pp |
| Anuradhapura | 0.5% | 6,747 | 5,760 | -987 🟥 | 0.8% | 0.6% | -0.2 🟥 pp |
| Kegalle | 0.6% | 8,777 | 7,292 | -1,485 🟥 | 1.0% | 0.8% | -0.2 🟥 pp |
| Polonnaruwa | 0.2% | 3,192 | 2,560 | -632 🟥 | 0.8% | 0.6% | -0.2 🟥 pp |
| Ratnapura | 0.7% | 10,844 | 8,607 | -2,237 🟥 | 1.0% | 0.8% | -0.2 🟥 pp |
| Batticaloa | 2.1% | 24,454 | 25,803 | +1,349 🟩 | 4.6% | 4.3% | -0.3 🟥 pp |
| Nuwara Eliya | 2.6% | 33,476 | 31,705 | -1,771 🟥 | 4.7% | 4.4% | -0.3 🟥 pp |
| Kandy | 1.5% | 22,379 | 18,623 | -3,756 🟥 | 1.6% | 1.3% | -0.4 🟥 pp |
| Badulla | 0.8% | 12,020 | 9,593 | -2,427 🟥 | 1.5% | 1.1% | -0.4 🟥 pp |
| Kurunegala | 3.3% | 43,707 | 40,273 | -3,434 🟥 | 2.7% | 2.3% | -0.4 🟥 pp |
| Kalutara | 3.0% | 39,774 | 36,510 | -3,264 🟥 | 3.3% | 2.8% | -0.5 🟥 pp |
| Trincomalee | 1.2% | 14,493 | 14,353 | -140 🟥 | 3.8% | 3.2% | -0.6 🟥 pp |
| Colombo | 11.4% | 162,260 | 139,882 | -22,378 🟥 | 7.0% | 5.9% | -1.1 🟥 pp |
| Gampaha | 36.1% | 449,398 | 442,291 | -7,107 🟥 | 19.5% | 18.2% | -1.3 🟥 pp |
| Vavuniya | 1.0% | 15,305 | 12,785 | -2,520 🟥 | 8.9% | 7.4% | -1.5 🟥 pp |
| Puttalam | 19.7% | 240,221 | 240,975 | +754 🟩 | 31.5% | 29.4% | -2.1 🟥 pp |
| Mannar | 4.7% | 52,415 | 57,713 | +5,298 🟩 | 52.6% | 46.6% | -6.0 🟥 pp |

***Mullaitivu** gained the most share at **+1.6pp**. **Mannar** saw the steepest share decline at **-6.0pp**. **Mannar** had the largest absolute increase (**+5,298**).*

### Other Christian

| District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Mullaitivu | 2.2% | 3,664 | 6,315 | +2,651 🟩 | 4.0% | 5.2% | +1.2 🟩 pp |
| Kilinochchi | 3.2% | 6,436 | 9,074 | +2,638 🟩 | 5.7% | 6.6% | +1.0 🟩 pp |
| Batticaloa | 9.8% | 22,833 | 27,728 | +4,895 🟩 | 4.3% | 4.7% | +0.3 🟩 pp |
| Vavuniya | 3.2% | 8,498 | 8,895 | +397 🟩 | 4.9% | 5.2% | +0.2 🟩 pp |
| Matara | 1.3% | 3,208 | 3,619 | +411 🟩 | 0.4% | 0.4% | 0.0 pp |
| Ampara | 2.3% | 5,541 | 6,486 | +945 🟩 | 0.9% | 0.9% | 0.0 pp |
| Jaffna | 7.4% | 20,511 | 20,857 | +346 🟩 | 3.5% | 3.5% | 0.0 pp |
| Galle | 1.9% | 5,315 | 5,377 | +62 🟩 | 0.5% | 0.5% | 0.0 pp |
| Anuradhapura | 1.3% | 3,660 | 3,656 | -4 🟥 | 0.4% | 0.4% | 0.0 pp |
| Nuwara Eliya | 5.5% | 15,508 | 15,474 | -34 🟥 | 2.2% | 2.1% | 0.0 pp |
| Monaragala | 0.3% | 859 | 713 | -146 🟥 | 0.2% | 0.1% | -0.1 🟥 pp |
| Polonnaruwa | 0.4% | 1,276 | 1,086 | -190 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Kurunegala | 3.3% | 9,926 | 9,413 | -513 🟥 | 0.6% | 0.5% | -0.1 🟥 pp |
| Hambantota | 0.4% | 1,692 | 1,247 | -445 🟥 | 0.3% | 0.2% | -0.1 🟥 pp |
| Matale | 0.7% | 2,342 | 2,026 | -316 🟥 | 0.5% | 0.4% | -0.1 🟥 pp |
| Ratnapura | 2.3% | 7,212 | 6,394 | -818 🟥 | 0.7% | 0.6% | -0.1 🟥 pp |
| Kalutara | 2.7% | 8,956 | 7,733 | -1,223 🟥 | 0.7% | 0.6% | -0.1 🟥 pp |
| Kegalle | 1.9% | 6,386 | 5,387 | -999 🟥 | 0.8% | 0.6% | -0.1 🟥 pp |
| Badulla | 2.0% | 6,615 | 5,729 | -886 🟥 | 0.8% | 0.7% | -0.2 🟥 pp |
| Gampaha | 15.8% | 46,080 | 44,540 | -1,540 🟥 | 2.0% | 1.8% | -0.2 🟥 pp |
| Kandy | 3.9% | 12,798 | 10,919 | -1,879 🟥 | 0.9% | 0.7% | -0.2 🟥 pp |
| Puttalam | 3.8% | 12,093 | 10,619 | -1,474 🟥 | 1.6% | 1.3% | -0.3 🟥 pp |
| Trincomalee | 2.7% | 7,774 | 7,714 | -60 🟥 | 2.0% | 1.7% | -0.3 🟥 pp |
| Mannar | 2.0% | 4,790 | 5,560 | +770 🟩 | 4.8% | 4.5% | -0.3 🟥 pp |
| Colombo | 19.7% | 66,947 | 55,624 | -11,323 🟥 | 2.9% | 2.3% | -0.5 🟥 pp |

***Mullaitivu** gained the most share at **+1.2pp**. **Colombo** saw the steepest share decline at **-0.5pp**. **Batticaloa** had the largest absolute increase (**+4,895**).*

### Other

| District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Polonnaruwa | 2.1% | 40 | 84 | +44 🟩 | 0.0% | 0.0% | 0.0 pp |
| Anuradhapura | 3.1% | 78 | 123 | +45 🟩 | 0.0% | 0.0% | 0.0 pp |
| Kandy | 5.7% | 165 | 227 | +62 🟩 | 0.0% | 0.0% | 0.0 pp |
| Ampara | 1.4% | 30 | 56 | +26 🟩 | 0.0% | 0.0% | 0.0 pp |
| Gampaha | 24.9% | 869 | 985 | +116 🟩 | 0.0% | 0.0% | 0.0 pp |
| Matale | 0.9% | 25 | 34 | +9 🟩 | 0.0% | 0.0% | 0.0 pp |
| Galle | 3.0% | 106 | 119 | +13 🟩 | 0.0% | 0.0% | 0.0 pp |
| Kegalle | 1.3% | 54 | 53 | -1 🟥 | 0.0% | 0.0% | 0.0 pp |
| Matara | 1.0% | 50 | 39 | -11 🟥 | 0.0% | 0.0% | 0.0 pp |
| Ratnapura | 1.5% | 79 | 61 | -18 🟥 | 0.0% | 0.0% | 0.0 pp |
| Monaragala | 0.5% | 30 | 19 | -11 🟥 | 0.0% | 0.0% | 0.0 pp |
| Kurunegala | 3.3% | 170 | 130 | -40 🟥 | 0.0% | 0.0% | 0.0 pp |
| Batticaloa | 0.8% | 52 | 33 | -19 🟥 | 0.0% | 0.0% | 0.0 pp |
| Kalutara | 3.7% | 212 | 145 | -67 🟥 | 0.0% | 0.0% | 0.0 pp |
| Nuwara Eliya | 2.0% | 127 | 78 | -49 🟥 | 0.0% | 0.0% | 0.0 pp |
| Trincomalee | 1.1% | 70 | 45 | -25 🟥 | 0.0% | 0.0% | 0.0 pp |
| Jaffna | 0.9% | 111 | 36 | -75 🟥 | 0.0% | 0.0% | 0.0 pp |
| Mannar | 0.1% | 17 | 4 | -13 🟥 | 0.0% | 0.0% | 0.0 pp |
| Vavuniya | 1.5% | 86 | 61 | -25 🟥 | 0.1% | 0.0% | 0.0 pp |
| Badulla | 1.4% | 171 | 54 | -117 🟥 | 0.0% | 0.0% | 0.0 pp |
| Hambantota | 1.8% | 302 | 70 | -232 🟥 | 0.1% | 0.0% | 0.0 pp |
| Kilinochchi | 0.1% | 50 | 5 | -45 🟥 | 0.0% | 0.0% | 0.0 pp |
| Colombo | 30.4% | 2,262 | 1,204 | -1,058 🟥 | 0.1% | 0.1% | 0.0 pp |
| Mullaitivu | 0.3% | 69 | 12 | -57 🟥 | 0.1% | 0.0% | -0.1 🟥 pp |
| Puttalam | 7.1% | 1,162 | 279 | -883 🟥 | 0.2% | 0.0% | -0.1 🟥 pp |

***Polonnaruwa** gained the most share at **0.0pp**. **Puttalam** saw the steepest share decline at **-0.1pp**. **Gampaha** had the largest absolute increase (**+116**).*

---

## A3. Largest Change in Religious Proportion

![A3 representative chart](analyses/a3_proportion_change/chart.png)

For each district, the religion whose share of the local population changed most between 2012 and 2024, showing only rows with absolute change > 1%.

### Hindu

| District | Share 2012 | Share 2024 | Change (pp) |
|---|---:|---:|---:|
| Kilinochchi | 81.9% | 80.7% | -1.3pp 🟥 |
| Mullaitivu | 75.3% | 72.4% | -2.9pp 🟥 |

### Islam

| District | Share 2012 | Share 2024 | Change (pp) |
|---|---:|---:|---:|
| Mannar | 16.6% | 27.4% | +10.8pp 🟩 |
| Trincomalee | 42.0% | 46.5% | +4.4pp 🟩 |
| Vavuniya | 7.0% | 10.3% | +3.4pp 🟩 |
| Ampara | 43.4% | 45.7% | +2.2pp 🟩 |
| Batticaloa | 25.5% | 27.1% | +1.6pp 🟩 |
| Kalutara | 9.4% | 10.6% | +1.2pp 🟩 |
| Kegalle | 7.3% | 8.3% | +1.1pp 🟩 |

### RomanCatholic

| District | Share 2012 | Share 2024 | Change (pp) |
|---|---:|---:|---:|
| Colombo | 7.0% | 5.9% | -1.1pp 🟥 |
| Gampaha | 19.5% | 18.2% | -1.3pp 🟥 |
| Puttalam | 31.5% | 29.4% | -2.1pp 🟥 |

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
| Kaduwela | Colombo | 90.4% | 92.3% | +1.9pp 🟩 |
| Gampaha | Gampaha | 87.6% | 88.8% | +1.2pp 🟩 |
| Maharagama | Colombo | 92.0% | 93.2% | +1.2pp 🟩 |

### Hindu

| DSD | District | Share 2012 | Share 2024 | Change (pp) |
|---|---|---:|---:|---:|
| Wattala | Gampaha | 13.0% | 16.9% | +3.9pp 🟩 |
| Vadamaradchi North (Point Pedro) | Jaffna | 83.9% | 86.4% | +2.5pp 🟩 |
| Thimbirigasyaya | Colombo | 22.5% | 24.4% | +1.9pp 🟩 |
| Colombo | Colombo | 22.7% | 24.6% | +1.9pp 🟩 |
| Manmunai South & Eruvil Pattu | Batticaloa | 93.9% | 95.4% | +1.4pp 🟩 |
| Karachchi | Kilinochchi | 83.1% | 81.4% | -1.7pp 🟥 |
| Vavuniya | Vavuniya | 78.3% | 75.8% | -2.5pp 🟥 |
| Nallur | Jaffna | 90.4% | 85.9% | -4.5pp 🟥 |
| Puthukkudiyiruppu | Mullaitivu | 84.8% | 78.6% | -6.2pp 🟥 |

### Islam

| DSD | District | Share 2012 | Share 2024 | Change (pp) |
|---|---|---:|---:|---:|
| Kolonnawa | Colombo | 23.1% | 31.3% | +8.3pp 🟩 |
| Dehiwala | Colombo | 22.6% | 30.4% | +7.8pp 🟩 |
| Galle 4 Gravets | Galle | 32.3% | 36.0% | +3.7pp 🟩 |
| Beruwala | Kalutara | 34.7% | 38.2% | +3.5pp 🟩 |
| Mundel | Puttalam | 38.6% | 41.9% | +3.3pp 🟩 |
| Akurana | Kandy | 64.9% | 67.9% | +3.0pp 🟩 |
| Negombo | Gampaha | 14.3% | 17.2% | +2.9pp 🟩 |
| Mawanella | Kegalle | 30.4% | 33.3% | +2.8pp 🟩 |
| Panadura | Kalutara | 14.4% | 17.2% | +2.8pp 🟩 |
| Puttalam | Puttalam | 64.2% | 66.6% | +2.4pp 🟩 |
| Attanagalla | Gampaha | 12.4% | 14.4% | +1.9pp 🟩 |
| Udunuwara | Kandy | 24.5% | 26.4% | +1.9pp 🟩 |
| Udapalatha | Kandy | 22.7% | 24.4% | +1.8pp 🟩 |
| Kuchchaweli | Trincomalee | 64.1% | 65.8% | +1.7pp 🟩 |
| Muthur | Trincomalee | 62.0% | 63.5% | +1.5pp 🟩 |
| Kinniya | Trincomalee | 95.8% | 97.1% | +1.4pp 🟩 |
| Koralai Pattu Central | Batticaloa | 97.2% | 0.3% | -96.9pp 🟥 |

### RomanCatholic

| DSD | District | Share 2012 | Share 2024 | Change (pp) |
|---|---|---:|---:|---:|
| Katana | Gampaha | 32.0% | 34.0% | +1.9pp 🟩 |
| Kalpitiya | Puttalam | 32.3% | 33.6% | +1.4pp 🟩 |
| Mahara | Gampaha | 8.8% | 7.6% | -1.2pp 🟥 |
| Chilaw | Puttalam | 45.7% | 44.4% | -1.3pp 🟥 |
| Mahawewa | Puttalam | 51.8% | 50.4% | -1.4pp 🟥 |
| Manmunai North | Batticaloa | 19.0% | 17.4% | -1.6pp 🟥 |
| Dankotuwa | Puttalam | 29.8% | 27.9% | -1.9pp 🟥 |
| Nanaddan | Mannar | 68.4% | 66.4% | -2.0pp 🟥 |
| Kelaniya | Gampaha | 9.8% | 7.7% | -2.1pp 🟥 |
| Jaffna | Jaffna | 52.9% | 50.6% | -2.3pp 🟥 |
| Nattandiya | Puttalam | 40.6% | 38.2% | -2.4pp 🟥 |
| Mannar Town | Mannar | 54.8% | 50.6% | -4.1pp 🟥 |

### OtherChristian

| DSD | District | Share 2012 | Share 2024 | Change (pp) |
|---|---|---:|---:|---:|
| Koralai Pattu North | Batticaloa | 12.1% | 13.5% | +1.4pp 🟩 |
| Sri Jayawardanapura Kotte | Colombo | 4.7% | 3.5% | -1.2pp 🟥 |

---

*Data from the 2012 and 2024 Sri Lanka Census, accessed via [lanka_data](https://pypi.org/project/lanka-data/). Raw data and derived tables live in the corresponding directories under [`analyses/`](analyses/).*
